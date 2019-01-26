
import sys
sys.path.append("..")
from . import views
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView



urlpatterns = [
    path('admin/', admin.site.urls),
    #  path('', include('payments.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('account/register/', views.register, name='register'),
    path('account/profile/', views.view_profile, name='profile'),
    path('account/edit_profile/', views.edit_profile, name='profile'),
    path('auth/', include('social_django.urls', namespace='social')),

   
]
