from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    desc = models.TextField(default="")
    def __str__(self):
        return self.name



job_choices = (
    ('Web Development', 'Web Development'),
    ('Backend Development', 'Backend Development'),
    ('Frontend Development', 'Frontend Development'),
    ('Content Writing', 'Content Writing'),
    ('Digital Marketing', 'Digital Marketing'),
    ('Android App Development', 'Android App Development'),
)

class Job(models.Model):
    comp = models.ForeignKey(Company, on_delete=models.CASCADE)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, choices=job_choices)
    skills = models.TextField()
    duration = models.PositiveIntegerField()
    activities = models.TextField()
    perks = models.CharField(max_length=300)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return self.title

courses = (
    ('B-TECH', 'B-TECH'),
    ('BBA', 'BBA'),
    ('M-TECH', 'M-TECH'),
    ('MCA', 'MCA'),

)


class Candidate(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    stud_name = models.CharField(max_length=350)
    address = models.TextField()
    mobile = models.PositiveIntegerField()
    class_12 = models.PositiveIntegerField()
    class_10 = models.PositiveIntegerField()
    persuing = models.CharField(max_length=25, choices=courses)
    pro_img = models.ImageField(upload_to='profile_img', blank=True, null=True)
    experience = models.TextField(blank=True)
    cv = models.FileField(upload_to='cv_all', blank=True, null=True)

    def __str__(self):
        return self.stud_name

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    cd = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    reason = models.TextField()
    objective = models.CharField(max_length=200)
    status1 = models.BooleanField(default=False)

    def __str__(self):
        return self.objective

class Accept(models.Model):
    apply = models.OneToOneField(Application, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

