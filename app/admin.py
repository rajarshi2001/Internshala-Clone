from django.contrib import admin
from .models import Candidate, Job, Company, Application, Accept



@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['id', 'user1', 'comp', 'title', 'skills', 'duration', 'activities', 'perks', 'amount' ]

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'stud_name', 'address', 'mobile', 'class_12', 'class_10', 'persuing', 'pro_img', 'experience', 'cv']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'job', 'cd', 'reason', 'objective', 'status1']

@admin.register(Accept)
class AcceptAdmin(admin.ModelAdmin):
    list_display = ['id', 'apply', 'done']

