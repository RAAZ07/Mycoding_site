from django.urls import path
from . import views

app_name = 'mycompiler'
urlpatterns = [
    # /mycompiler/
    path('login', views.user_login, name='user_login'),
    # /mycompiler/home
    path('home', views.home, name='home'),
    # /mycompiler/problem/id
    path('problem/<int:problem_id>', views.submission, name='submission'),
    # /mycompiler/signup
    path('signup', views.signup, name='signup'),
    # /mycompiler/logout
    path('logout', views.user_logout, name='logout')
]
