from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('trainer', views.trainer, name='trainer'),
    path('contact', views.contact, name='contact'),
    path('why', views.why, name='why'),
   
  

]