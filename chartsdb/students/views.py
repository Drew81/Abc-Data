from django.views import generic
from .models import Student, Detail, Score
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView

#Restframworks
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import StudentSerializer, DetailSerializer

#Json response(data)
from django.contrib.auth import get_user_model
from django.http import JsonResponse
#API views for charts data output
from django.db.models import Count, Avg, Sum

#views
class HomeView(TemplateView):
    template_name = 'students/home.html'

class StudentView(generic.ListView):
	template_name = 'students/student_list.html'
	context_object_name = 'all_students'
	def get_queryset(self):
		return Student.objects.all()

class AvgView(generic.ListView):
	template_name = 'students/home.html'
	context_object_name = 'avg_score'
	def get_queryset(self):
		return Score.objects.annotate(Sum('score'))

class DetailView(generic.DetailView):
	model = Student
	template_name = 'students/detail.html'




# Student forms
class StudentCreate(CreateView):
	model = Student
	fields = ['first_name', 'last_name', 'grade', 'gender', 'age', 'race']
	success_url = reverse_lazy('students:student_list')

class StudentUpdate(UpdateView):
	model = Student
	fields = ['first_name', 'last_name', 'grade', 'gender', 'age', 'race']
	success_url = reverse_lazy('students:student_list')

class StudentDelete(DeleteView):
	model = Student
	success_url = reverse_lazy('students:student_list')

class DetailCreate(CreateView):
	model = Detail
	fields = ['student', 'incident', 'incident_level', 'location', 'method', 'notes']
	success_url = reverse_lazy('students:student_list')

class DetailUpdate(UpdateView):
	model = Detail
	fields = ['student','incident', 'incident_level', 'location', 'method', 'notes']
	success_url = reverse_lazy('students:student_list')

class DetailDelete(DeleteView):
	model = Detail
	success_url = reverse_lazy('students:student_list')





#API views
class StudentList(generics.ListCreateAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Student.objects.all()
	serializer_class = StudentSerializer

class DetailList(generics.ListCreateAPIView):
	queryset = Detail.objects.all()
	serializer_class = DetailSerializer

class DetailsDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Detail.objects.all()
	serializer_class = DetailSerializer		



#API Score View for each student
class ScoreView(generic.ListView):
	template_name = 'students/score_list.html'
	context_object_name = 'all_scores'
	def get_queryset(self):
		return Score.objects.all()

class ScoreDetailView(generic.DetailView):
	model = Student
	template_name = 'students/score_list.html'


#Score
class ScoreCreate(CreateView):
	model = Score
	fields = ['student', 'math_score', 'reading_score']
	success_url = reverse_lazy('students:student_list')




#API to calculate for charts
class ChartsApi(APIView):
	def get(self, request, format=None):
		
		queryset = Student.objects.all().count()
		labels = ["id", "default"]
		default_items = [queryset]
		serializer = Student.objects.all()
		data = {

			"labels":labels,
			"default": default_items

		}
		return Response(data)

class DetailsApi(APIView):
	def get(self, request, format=None):
		qs_count = Detail.objects.all().count()
		values = Detail.objects.aggregate(Sum('incident_level'))
		serializer = Detail.objects.all()
		labels = [ "date", "incident_level"]
		default_items = [qs_count, values]
		data = {

			"labels":labels,
			"default": default_items,
			"incident_level_sum": values
			

		}
		return Response(data)

class ChartDetailApi(APIView):
	def get(self, request, format=None):
		qs_count = Detail.objects.all().count()
		values = Detail.objects.values_list('id', 'incident_level')
		serializer = Detail.objects.all()
		labels = ["id", "incident_level"]
		default_items = [values, "id"]
		data = {
			
			
			"labels":labels,
			"default": default_items,
			"incident_level": values

		}
		return Response(data)



class AvgApi(APIView):
	def get(self, request, format=None):
		queryset = Score.objects.all().count()
		values = Score.objects.annotate(Sum('math_score'))
		serializer = Score.objects.all()
		labels = ["avg_score" ]
		default_items = [queryset, values]
		data = {
			
			
			"labels":labels,
			"default": default_items,
			"avg_score": values
			
			
		}
		return Response(data)






