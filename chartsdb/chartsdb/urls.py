"""chartsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from students import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^students/', include('students.urls')),
    #api students
    url(r'^api/students/$', views.StudentList.as_view()),
    url(r'^api/students/(?P<pk>\d+)/$', views.StudentDetail.as_view()),
    #api details
    url(r'^api/details/$', views.DetailList.as_view()),
    url(r'^api/details/(?P<pk>\d+)/$', views.DetailsDetail.as_view()),
    #api charts students and details
    url(r'^api/charts/', views.ChartsApi.as_view()),
    url(r'^api/student/details', views.DetailsApi.as_view()),

    url(r'^api/chart/detail/', views.ChartDetailApi.as_view()),
    url(r'^api/chart/avg/', views.AvgApi.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)






