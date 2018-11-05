from django.conf.urls import url, include
from .views import *


app_name = 'home'

urlpatterns = [
	url(r'^$', landing, name='landing'),
]
