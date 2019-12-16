
from django.urls import path

from app1.views import EmailList

urlpatterns = [
    path('email/', EmailList.as_view(), name='emailview'),
]
