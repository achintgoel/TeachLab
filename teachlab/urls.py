from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teachlab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^$', RedirectView.as_view(url='/accounts/profile')),
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    url(r'^repository/', include('repository.urls', namespace="repository")),
    url(r'^admin/', include(admin.site.urls)),
)
