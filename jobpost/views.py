from django.shortcuts import render
from django.db.models.query_utils import Q
from django.db.models import CharField

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status

from company.models import Company
from .models import JobPost, JobPosition, SkillSet, JobPostSkillSet
from .serializer import JobPostSerializer, JobPostDetailSerializer, ApplySerializer


# 채용공고 CRUD 기능
class JobPostView(APIView):
    # 채용공고 목록 조회
    def get(self, request):
        jobpost_list = JobPost.objects.all()
        return Response(JobPostSerializer(jobpost_list, many=True).data, status=status.HTTP_200_OK)

    # 채용공고 등록
    def post(self, request):
        company_id = request.data.pop("company_id", '')
        jobposition_name = request.data.pop("jobposition", '')
        skillset_list = request.data.pop("skillset", '').split()

        # 회사 오브젝트 탐색, 존재하지않으면 에러 return
        try:
            company_obj = Company.objects.get(id=company_id)
        except:
            return Response({"error": "회사가 존재하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

        # 채용포지션 오브젝트 탐색, 존재하지않으면 생성
        jobposition = JobPosition.objects.filter(name=jobposition_name)
        if len(jobposition) == 0:
            jobposition_obj = JobPosition.objects.create(name=jobposition_name)
        else:
            jobposition_obj = jobposition.first() 
        
        # 사용기슬 리스트 쿼리 객체 생성
        query = Q() 
        for skillset_name in skillset_list:
            query.add(Q(name=skillset_name), Q.OR)
        
        # 사용기술 쿼리셋 탐색
        skillset_queryset = SkillSet.objects.filter(query)

        jobpost_serializer = JobPostSerializer(data=request.data)
        if jobpost_serializer.is_valid():
            jobpost_serializer.save(company=company_obj, jobposition=jobposition_obj, skillset=skillset_queryset)
            return Response(jobpost_serializer.data, status=status.HTTP_200_OK)
        
        return Response(jobpost_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


    # 채용공고 수정
    def put(self, request):
        jobposition_name = request.data.pop("jobposition", '')
        skillset_list = request.data.pop("skillset", '').split()

        # 수정할 채용공고 오브젝트 탐색, 존재하지않으면 에러 return
        jobpost_id = request.data.pop('jobpost_id', '')
        try:
            jobpost_obj = JobPost.objects.get(id=jobpost_id)
        except:
            return Response({"error": "채용공고가 존재하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

        # 회사 id는 변경못하도록 변경 데이터에서 제외
        request.data.pop('company_id')

        # 수정할 채용포지션 오브젝트 탐색, 존재하지않으면 생성
        jobposition = JobPosition.objects.filter(name=jobposition_name)
        if len(jobposition) == 0:
            jobposition_obj = JobPosition.objects.create(name=jobposition_name)
        else:
            jobposition_obj = jobposition.first() 
        
        # 수정할 사용기슬 리스트 쿼리 객체 생성
        query = Q() 
        for skillset_name in skillset_list:
            query.add(Q(name=skillset_name), Q.OR)
        
        # 사용기술 쿼리셋 탐색
        skillset_queryset = SkillSet.objects.filter(query)

        jobpost_serializer = JobPostSerializer(jobpost_obj, data=request.data, partial=True)
        if jobpost_serializer.is_valid():
            jobpost_serializer.save(jobposition=jobposition_obj, skillset=skillset_queryset)
            return Response(jobpost_serializer.data, status=status.HTTP_200_OK)
        
        return Response(jobpost_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


    # 채용공고 삭제
    def delete(self, request):
        # 삭제할 채용공고 오브젝트 탐색, 존재하지않으면 에러 return
        jobpost_id = request.data.pop('jobpost_id', '')
        try:
            jobpost_obj = JobPost.objects.get(id=jobpost_id)
        except:
            return Response({"error": "채용공고가 존재하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

        jobpost_obj.delete()

        return Response({"success": "삭제 완료"}, status=status.HTTP_200_OK)

# 채용공고 상세보기 기능
class JobPostDetailView(APIView):
    # 채용공고 상세보기
    def get(self, request, id):
        # 상세보기할 채용공고 오브젝트 탐색, 존재하지않으면 에러 return
        jobpost_id = int(id)
        try:
            jobpost_obj = JobPost.objects.get(id=jobpost_id)
        except:
            return Response({"error": "채용공고가 존재하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(JobPostDetailSerializer(jobpost_obj).data, status=status.HTTP_200_OK)

# 채용공고 검색 기능
class JobPostSearchView(APIView):
    # 채용공고 검색
    def get(self, request):
        # 검색 단어
        search_word = request.GET.get('search', '')

        query = Q()
        query.add(Q(content__contains=search_word), Q.OR)
        query.add(Q(area__contains=search_word), Q.OR)
        query.add(Q(country__contains=search_word), Q.OR)
        query.add(Q(company__name__contains=search_word), Q.OR)
        query.add(Q(jobposition__name__contains=search_word), Q.OR)
        query.add(Q(skillset__name__contains=search_word), Q.OR)

        jobpost_search_list = JobPost.objects.filter(query)
        
        return Response(JobPostSerializer(jobpost_search_list, many=True).data, status=status.HTTP_200_OK)

# 채용공고 지원 기능
class ApplyView(APIView):
    # 채용공고 지원
    def post(self, request):
        apply_serializer = ApplySerializer(data=request.data)

        if apply_serializer.is_valid():
            apply_serializer.save()
            return Response(apply_serializer.data, status=status.HTTP_200_OK)

        return Response(apply_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

