from django.conf.urls import patterns, include, url
from django.contrib import admin
from javaseer import views

urlpatterns = patterns('',
	
	url(r'^javaseer/$', views.javaseer ),
	url(r'^setup/$', views.setup ),

    url(r'^admin/', include(admin.site.urls)),
)
