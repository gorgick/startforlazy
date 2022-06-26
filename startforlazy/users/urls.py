from django.urls import path
from .views import LoginView, RegisterView, CartView, PersonalAreaView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('course/<str:slug>/<int:id>/', CartView.as_view(), name='owner'),
    path('personalarea/<int:id>/', PersonalAreaView.as_view(), name='personalarea')
]
