from django.urls import path
from .views import *

urlpatterns = [
    path('sendmail/', sendmail, name ="sendmail"),
    path('done/', done, name ="done"),
]