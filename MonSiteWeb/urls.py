from django.conf.urls import url,include
from django.contrib import admin
from MonSiteWeb import views

urlpatterns = [
    url(r'^article/(?P<id>\d+)-(?P<slug>.+)$',views.post),
    url(r'^$',views.index,name='url_index'),
    url(r'^(?P<page>\d+)$', views.index,name='url_index'),
    url(r'^contact$',views.contact),
    url(r'^about$',views.about),
    url(r'^admin/', include(admin.site.urls)),
]