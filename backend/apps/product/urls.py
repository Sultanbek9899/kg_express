from django.urls import path

from .views import *

urlpatterns = [
    path('getSubcategory/', get_subcategory, name="get_subcategory")
]