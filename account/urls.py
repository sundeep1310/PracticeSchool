from django.urls import path
from . import views
from project.views import projects
app_name='account'
urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('projects/',projects,name = "projects"),
    path('logout/', views.logout_view, name='logout'),
]
