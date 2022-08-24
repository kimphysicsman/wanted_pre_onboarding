from django.contrib import admin
from . import models

admin.site.register(models.SkillSet)
admin.site.register(models.JobPosition)
admin.site.register(models.JobPost)
admin.site.register(models.JobPostSkillSet)