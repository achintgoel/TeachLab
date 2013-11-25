from django.conf.urls import patterns, url
from repository import views
from django.contrib.auth.views import login
urlpatterns = patterns('',
    url(r'^my_courses/$', views.my_courses, name='my_courses'),
    url(r'^search_results/$', views.search_results, name='search_results'),
    url(r'^course_profile/$', views.course_profile, name='course_profile'),
    url(r'^course_profile_alternate/$', views.course_profile_alternate, name='course_profile_alternate'),
    url(r'^upload_file/$', views.upload_file, name='upload_file'),
)