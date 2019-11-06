from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('',views.index,name='index'),
  path('syllabus/',views.syllabus,name='syllabus'),
  path('carrier/',views.carrier,name='carrier'),
  path('about_us/',views.about_us,name='about_us'),
  path('login/',views.login,name='login'),
  path('logout/',views.logout,name='logout'),
  path('team/',views.team,name='team'),
  path('teacher_profile/',views.teacher_profile,name='teacher_profile'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)