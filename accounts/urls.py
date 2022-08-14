from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('success', views.success, name='success'),
    path('page_404', views.my_view, name='my_view')

]

