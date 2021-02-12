app_name = 'userprofile'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.user_login, name='login'),
	url(r'^logout/', views.user_logout, name='logout'),
	url(r'^register/', views.user_register, name='register'),
	url(r'^delete/(?P<id>[0-9]+)/', views.user_delete, name='delete'),
	url(r'^edit/(?P<id>[0-9]+)/', views.profile_edit, name='edit'),
]