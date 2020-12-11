from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView, RedirectView
from rest_framework_simplejwt import views as jwt_views
from django.utils.translation import gettext as _, gettext_lazy


# Text to put at the end of each page's <title>.
admin.AdminSite.site_title = gettext_lazy('Todo')

# Text to put in each page's <h1>.
admin.AdminSite.site_header = gettext_lazy('Todo Vue Django')

# Text to put at the top of the admin index page.
admin.AdminSite.index_title = gettext_lazy('Admin')

# URL for the "View site" link at the top of each admin page.
admin.AdminSite.site_url = '/api/' # 'https://todovuedjango.herokuapp.com/'

admin.AdminSite.enable_nav_sidebar = False

admin.AdminSite.empty_value_display = '-'


urlpatterns = [
     path('api/', include('todos.urls')),
     path('auth/', include('rest_framework.urls', namespace='rest_framework')),
     path('admin/', admin.site.urls),
     re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
     re_path('^.*', TemplateView.as_view(template_name='todos/index.html'), name="index"), # to vue path
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)