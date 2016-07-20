from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'infoscheme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^administrator/', 'administrator.views.home', name='home'),
    url(r'^login/', 'administrator.views.admin_login', name='admin_login'),
    url(r'^users/', 'users.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
]
