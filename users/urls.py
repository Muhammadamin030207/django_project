from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('me/', views.MeView.as_view()),
    path('profile/', views.ProfileUpdateView.as_view()),
    path('my-profile/', views.MyProfileView.as_view()),
    
]
