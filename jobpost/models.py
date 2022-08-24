from django.db import models
import jobpost
from user.models import User
from company.models import Company

# 사용기술
class SkillSet(models.Model):
    name = models.CharField("사용기술", max_length=20)

    def __str__(self):
        return self.name

# 채용포지션
class JobPosition(models.Model):
    name = models.CharField("채용포지션", max_length=128)

    def __str__(self):
        return self.name

# 채용공고 모델
class JobPost(models.Model):
    company = models.ForeignKey(Company, verbose_name="회사", on_delete=models.SET_NULL, null=True)
    jobposition = models.ForeignKey(JobPosition, verbose_name="채용포지션", on_delete=models.SET_NULL, null=True)
    skillset = models.ManyToManyField(SkillSet, verbose_name="사용기술",  through='JobPostSkillSet')

    content = models.TextField("채용내용")
    salary = models.IntegerField("채용보상금")
    area = models.CharField("지역", max_length=128)
    country = models.CharField("국가", max_length=128)

    def __str__(self):
        return f"채용공고 - {self.id}"
    

# JopPost - SkillSet 중간 테이블
class JobPostSkillSet(models.Model):
    skillset = models.ForeignKey(SkillSet, on_delete=models.SET_NULL, null=True)
    jobpost = models.ForeignKey(JobPost, on_delete=models.SET_NULL, null=True)


# 채용공고 지원 모델
class Apply(models.Model):
    user = models.OneToOneField(User, verbose_name="지원자", on_delete=models.SET_NULL, null=True)
    jobpost = models.OneToOneField(JobPost, verbose_name="채용공고", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField("지원 시간", auto_now_add=True)