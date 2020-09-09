from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.HomeView, name="home"),
    url(r'^record/$', views.RecordView, name="record"),
    url(r'^lost-person/$', views.LostPerson, name='lost-person'),
    url(r'^details/(?P<pk>\d+)/$', views.DetailView, name='details'),
    url(r'^my-entries/$', views.MyEntries, name='my-entries'),
    url(r'^found-people/$', views.FoundPeople, name='found-people'),
    url(r'^delete/(?P<pk>\d+)/$', views.DelReport, name='delete'),
    url(r'^report-found/(?P<pk>\d+)/$', views.ReportFound, name='report-found'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)