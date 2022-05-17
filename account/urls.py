from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')), # substitui as urls de login e logout, mudar e resetar senha
    # Django autenticação de usuário
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Urls para Mudar senha
    #path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    #path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),  name='password_change_done'),

    # Urls para resetar senha
    #path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]