from django.urls import path

from .views import *

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('getSubcategory/', get_subcategory, name="get_subcategory")
]