from rest_framework import serializers
from .models import Student, Detail


class StudentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Student
		fields = '__all__'

class DetailSerializer(serializers.ModelSerializer):

	class Meta:
		model = Detail
		fields = '__all__'