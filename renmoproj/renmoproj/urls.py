
import sys
sys.path.append("..")
from . import views
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',views.home, name='home'),
    path('account/register/', views.register, name='register'),
    path('account/profile/', views.view_profile, name='profile'),
    path('account/edit_profile/', views.edit_profile, name='edit_profile'),
    path('send_tokens', views.transfer_token, name='transfer_token'),
    path('account/token/', views.add_token, name='add_token'),
    path('charge/', views.charge, name='charge'),
    path('auth/', include('social_django.urls', namespace='social')),

   
]
