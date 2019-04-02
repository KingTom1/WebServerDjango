from django.conf.urls import url
from WebServerDjangoApp import views
urlpatterns = [
    url(r'^show_user/', views.show_user),
    url(r'^addUser/', views.add_user),
]