from rest_framework import serializers
from . import models

# 채용공고 Serializer
class JobPostSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()
    skillset = serializers.SerializerMethodField()
    jobposition = serializers.SerializerMethodField()

    def get_company(self, obj):
        return obj.company.name

    def get_skillset(self, obj):
        skillset_list = obj.skillset.all()
        skillset_name_list = [ skillset.name for skillset in skillset_list ]
        return skillset_name_list

    def get_jobposition(self, obj):
        return obj.jobposition.name

    class Meta:
        model = models.JobPost
        fields = ('id', 'company', 'skillset', 'jobposition', 'salary', 'area', 'country')



# 채용공고 상세보기 Serializer
class JobPostDetailSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()
    skillset = serializers.SerializerMethodField()
    jobposition = serializers.SerializerMethodField()
    other_jobpost = serializers.SerializerMethodField()

    def get_company(self, obj):
        return obj.company.name

    def get_skillset(self, obj):
        skillset_list = obj.skillset.all()
        skillset_name_list = [ skillset.name for skillset in skillset_list ]
        return skillset_name_list

    def get_jobposition(self, obj):
        return obj.jobposition.name

    def get_other_jobpost(self, obj):
        jobpost_list = models.JobPost.objects.filter(company=obj.company)
        jobpost_id_list = [jobpost.id for jobpost in jobpost_list]
        return jobpost_id_list

    class Meta:
        model = models.JobPost
        fields = ('id', 'company', 'skillset', 'jobposition', 'salary', 'area', 'country', 'content', 'other_jobpost')