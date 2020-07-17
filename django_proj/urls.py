from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

urlpatterns = [
    path('', include('todo.urls')),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password-change/',
         views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password-change/done/',
         views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('password-reset/',
         views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password-reset/done/',
         views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/',
         views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('admin/', admin.site.urls),
]
