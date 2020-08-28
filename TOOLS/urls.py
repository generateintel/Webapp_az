# import Views as Views
from django.conf.urls import url, include
from django.urls import path,include
from rest_framework import routers

from . import views
from .views import *

# urlpatterns = [

# ]

router=routers.DefaultRouter()
router.register(r'filter', Black_Box, 'filter')#User apis


urlpatterns=[
    path('', include(router.urls)),
]