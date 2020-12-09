from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views
from django.views.generic.base import RedirectView, TemplateView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
     path('api/', include('todos.urls')),
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
    path('favicon.ico',
         RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
    re_path('^.*', TemplateView.as_view(template_name='todos/index.html'), name="index"), # to vue path
]
