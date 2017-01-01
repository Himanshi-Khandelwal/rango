from django.conf.urls import patterns, include, url
from django.conf import settings
from tango import views



urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^add_category/$', views.add_category, name='add_category'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^restricted/', views.restricted, name='restricted'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),)
	

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}), )
