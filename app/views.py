from django.shortcuts import render, HttpResponseRedirect
from .forms import Signupforms, loginForms, CandidateForms, CompanyForm, JobForm, ApplicationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Candidate, Company, Job, Application
from django.contrib.auth.models import User, Group
from .models import Accept

def signupView(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            forms = Signupforms(data=request.POST)
            if forms.is_valid():
                user = forms.save()
                if request.POST['postname'] == 'Participant':
                    group = Group.objects.get(name='participants')
                    user.groups.add(group)
                else:
                    group = Group.objects.get(name='Manager')
                    user.groups.add(group)
                messages.success(request, 'You are registered successfully !!')
        else:
            forms = Signupforms()
        return render(request, 'signup.html', {'forms': forms})
    else:
        return HttpResponseRedirect('/dashBoard/')

def loginView(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            forms = loginForms(data=request.POST)
            if forms.is_valid():
                u_name = forms.cleaned_data['username']
                pwd = forms.cleaned_data['password']
                user = authenticate(username=u_name, password=pwd)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/dashBoard/')
        else:
            forms = loginForms()
        return render(request, 'login.html', {'forms': forms})
    else:
        return HttpResponseRedirect('/dashboard/')

def logoutView(request):
    logout(request)
    return HttpResponseRedirect('/')

def profileView(request, name=None):
    if request.user.is_authenticated:
        name=name
        all = Candidate.objects.all()
        items = []
        for a in all:
            items.append(a.student)
        if name:
            ct = Candidate.objects.get(student__username=request.user.username)
            return render(request, 'userprofile.html', {'ct': ct, 'name': name})
        else:
            if request.user not in items:
                name1 = None
                if request.method == 'POST':
                    forms = CandidateForms(data=request.POST, files=request.FILES)
                    if forms.is_valid():
                        reg = forms.save(commit=False)
                        reg.student = request.user
                        reg.save()
                        messages.success(request, 'Your profile data has been saved successfully !!')
                        return HttpResponseRedirect('/dashBoard/')
                else:
                    forms = CandidateForms()
                return render(request, 'userprofile.html', {'forms': forms, 'name1': name1})
            else:
                ct = Candidate.objects.get(student__username=request.user.username)
                name1 = ct.stud_name
                if request.method == 'POST':
                    forms = CandidateForms(data=request.POST, files=request.FILES, instance=ct)
                    if forms.is_valid():
                        forms.save()
                        messages.success(request, 'Profile edited successfully !!')
                        return HttpResponseRedirect('/profile/edit/')
                else:
                    forms = CandidateForms(instance=ct)
                return render(request, 'userprofile.html', {'forms': forms, 'ct': ct, 'name1': name1})
    else:
        return HttpResponseRedirect('/')

def dashboardView(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name='Manager').exists():
            allCompany = Company.objects.all()
            allItems = []
            for item in allCompany:
                allItems.append(item.user)
            if request.user not in allItems:
                if request.method == 'POST':
                    forms = CompanyForm(data=request.POST)
                    if forms.is_valid():
                        reg = forms.save(commit=False)
                        reg.user = request.user
                        reg.save()
                        return HttpResponseRedirect('/dashBoard/')
                else:
                    forms = CompanyForm()
                return render(request, 'compDashboard.html', {'forms': forms})
            else:
                ct = Company.objects.get(user__username=request.user.username)
                if request.method == 'POST':
                    forms = CompanyForm(data=request.POST, instance=ct)
                    if forms.is_valid():
                        forms.save()
                        return HttpResponseRedirect('/dashBoard/')
                else:
                    forms = CompanyForm(instance=ct)
                return render(request, 'compDashboard.html', {'forms': forms, 'ct': ct})
        else:
            comp = Company.objects.all()
            cand =  Candidate.objects.all()
            cd = False
            for c in cand:
                if c.student == request.user:
                    cd = True
            return render(request, 'dashboard.html', {'comp': comp, 'cd':cd})
    else:
        return HttpResponseRedirect('/')

def companyProfileView(request, id):
    if request.user.is_authenticated:
        ct = Company.objects.get(pk=id)
        jb = Job.objects.filter(comp__id=id)
        if request.method == 'POST':
            forms = JobForm(data=request.POST)
            if forms.is_valid():
                reg = forms.save(commit=False)
                reg.user1 = request.user
                reg.comp = ct
                reg.save()
                return HttpResponseRedirect('/dashBoard/')
        else:
            forms = JobForm()
        return render(request, 'companyprofile.html', {'ct': ct, 'forms': forms, 'jb': jb})
    else:
        return HttpResponseRedirect('/')

def jobView(request, id):
    if request.user.is_authenticated:
        alljobs = Job.objects.filter(comp__id=id)
        return render(request, 'candidateJob.html', {'alljobs': alljobs})
    else:
        return HttpResponseRedirect('/')

def applyView(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            forms = ApplicationForm(data=request.POST)
            jb = Job.objects.get(pk=id)
            cp = Candidate.objects.get(student__username=request.user.username)
            if forms.is_valid():
                reg = forms.save(commit=False)
                reg.job = jb
                reg.cd = cp
                reg.save()
                messages.success(request, 'Your application has been submitted successfully !!')
                return HttpResponseRedirect(f'/jobs/view/{id}')
        else:
            forms = ApplicationForm()
        return render(request, 'candapplication.html', {'forms': forms})
    else:
        return HttpResponseRedirect('/')

def hrjobView(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Job.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashBoard/')
        else:
            jb1 = Job.objects.filter(comp__id=id)
            ap = Application.objects.filter(job__user1=request.user)
            return render(request, 'hrjob.html', {'jb1': jb1, 'ap': ap})
    else:
        return HttpResponseRedirect('/')

def statusView(request, id):
    if request.user.is_authenticated:
        ap = Application.objects.filter(job__id=id) 
        return render(request, 'status.html', {'ap': ap})
    else:
        return HttpResponseRedirect('/')

def editjobView(request, id):
    if request.user.is_authenticated:
        pt = Job.objects.get(pk=id)
        if request.method == 'POST':
            forms = JobForm(instance=pt, data=request.POST)
            if forms.is_valid():
                forms.save()
                return HttpResponseRedirect('/dashBoard/')
        else:
            forms = JobForm(instance=pt)
        return render(request, 'editJob.html', {'forms': forms})
    else:
        return HttpResponseRedirect('/')


def candjobView(request, id):
    if request.user.is_authenticated:
        myjob = Job.objects.get(pk=id)
        ap = Application.objects.filter(job=myjob).filter(cd__student=request.user)
        print(len(ap))
        if len(ap) != 0:
            ac = Accept.objects.all()
            ac1 = None
            for a in ac:
                if a.apply.id == ap[0].id:
                    cid  = a.apply.id
                    ac1 = Accept.objects.get(apply_id=cid)
                    break
            return render(request, 'job.html', {'myjob': myjob, 'ap': ap, 'ac1': ac1 })
        else:
            return render(request, 'job.html', {'myjob': myjob})
    else:
        return HttpResponseRedirect('/')

def statusrightView(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST['accepts'] == 'accepts':
                ap = Application.objects.get(pk=id)
                ap1 =Application(id=id, job=ap.job, cd=ap.cd, reason=ap.reason, objective=ap.objective, status1=True)
                ap1.save()
                ac = Accept(apply=ap1, done=True)
                ac.save()
                messages.success(request, 'Application sent succesfully !!')
                return HttpResponseRedirect('/dashBoard/')
        return render(request, 'acceptance.html')
    else:
        return HttpResponseRedirect('/')

def statuswrongView(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST['rejects'] == 'rejects':
                ap = Application.objects.get(pk=id)
                ap1 =Application(id=id, job=ap.job, cd=ap.cd, reason=ap.reason, objective=ap.objective, status1=True)
                ap1.save()
                ac = Accept(apply=ap1, done=False)
                ac.save()
                messages.success(request, 'Application sent succesfully !!')
                return HttpResponseRedirect('/dashBoard/')
        return render(request, 'rejection.html')
    else:
        return HttpResponseRedirect('/')
