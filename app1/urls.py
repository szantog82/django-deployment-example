from django.conf.urls import url

from app1 import views 


app_name = 'app1'

urlpatterns = [
    url(r'^clients/', views.clients, name="clients"),
    url(r'^other/', views.other, name="other"),
    url(r'^special/', views.special, name="special"),
    url(r'^register/', views.register, name='register'),
    url(r'^user_login/', views.user_login, name='user_login'),
    ]
