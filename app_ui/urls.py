from . import views
# from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, re_path

app_name = 'app_ui'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
]
