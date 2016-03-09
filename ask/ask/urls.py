from django.conf.urls import include, url
from django.contrib import admin
from ask.views import test

urlpatterns = [
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'ask.views.test', name='index'),
    url(r'^login/', 'ask.views.test', name='login'),
    url(r'^signup/', 'ask.views.test', name='signup'),
    url(r'^question/(?P<id>[0-9]+)/$', 'ask.views.test', name='question'),
    url(r'^ask/', 'ask.views.test', name='ask'),
    url(r'^popular/', 'ask.views.test', name='popular'),
    url(r'^new/', 'ask.views.test', name='new'),
    url(r'^admin/', include('admin.site.urls')),
]
