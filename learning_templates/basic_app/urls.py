from django.urls import path
from basic_app import views
# from . import views


# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path(r'relative/', views.relative, name='relative'),
    path(r'other/', views.other, name='other'),
]
