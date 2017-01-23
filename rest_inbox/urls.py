from __future__ import unicode_literals, absolute_import

from django.conf.urls import url
from rest_inbox import views


urlpatterns = [
    url(r'^get-user/', views.get_user),
    url(r'^get-mails/', views.get_mails),
    url(r'^logout/', views.logout),
]