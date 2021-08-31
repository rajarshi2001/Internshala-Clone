from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
   path('', views.loginView, name='userlogin'),
   path('logout/', views.logoutView, name='userlogout'),
   path('signup/', views.signupView, name='signup'),
   path('profile/', views.profileView, name='profile'),
   path('profile/edit/', views.profileView, name='editProfile'),
   path('profile/userview/<str:name>', views.profileView, name='viewProfile'),
   path('dashBoard/', views.dashboardView, name='user_dashboard'),
   path('dashBoard/view/<int:id>', views.companyProfileView, name='user_profile'),
   path('jobs/<int:id>', views.jobView, name='job'),
   path('dashBoard/view/job/<int:id>', views.hrjobView, name='hrJobs'),
   path('dashBoard/view/job/status/<int:id>', views.statusView, name='allstatus'),
   path('dashBoard/view/job/status/right/<int:id>', views.statusrightView, name="acceptance"),
   path('dashBoard/view/job/status/wrong/<int:id>', views.statuswrongView, name="rejection"),
   path('dashBoard/view/job/edit/<int:id>', views.editjobView, name='editjob'),
   path('jobs/view/<int:id>', views.candjobView, name='viewjob'),
   path('jobs/view/apply/<int:id>', views.applyView, name='applyjob'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
