from django.conf.urls import url
from students import views


app_name = 'students'

urlpatterns = [
	url(r'^home/$', views.HomeView.as_view(), name='home'),
	url(r'^list/$', views.StudentView.as_view(), name='student_list'),
	url(r'^detail/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^add/$', views.StudentCreate.as_view(), name='new_student'),
	#url(r'^score/add/$', views.ScoreCreate.as_view(), name='new_score'),
	#url(r'^scores/$', views.ScoreView.as_view(), name='score_list'),
	#url(r'^scorelist/(?P<pk>\d+)/$', views.ScoreDetailView.as_view(), name='score_detail'),
	url(r'^student/(?P<pk>\d+)/$', views.StudentUpdate.as_view(), name='student_update'),
	url(r'^student/(?P<pk>\d+)/delete/$', views.StudentDelete.as_view(), name='student_delete'),
	url(r'^detail/add/$', views.DetailCreate.as_view(), name='new_detail'),
	url(r'^detail/(?P<pk>\d+)/$', views.DetailUpdate.as_view(), name='detail_update'),
	url(r'^student/(?P<pk>\d+)/delete/$', views.DetailDelete.as_view(), name='detail_delete')

	
]