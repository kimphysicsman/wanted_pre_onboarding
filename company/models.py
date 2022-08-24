from django.db import models
from user.models import User

# 채용공고를 올릴 회사 모델
class Company(models.Model):
    name = models.CharField("회사명", max_length=100)

    def __str__(self):
        return self.name