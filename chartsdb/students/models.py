from django.db import models

# Create your models here.
class Student(models.Model):
	GENDER_CHOICE = (
		('1', 'Male'),
		('2', 'Female'),
		('3', 'Transgender')
	)

	ETHNIC_CHOICE = (
		('1', 'African American'),
		('2', 'Spanish/Latin'),
		('3', 'White'),
		('4', 'African'),
		('5', 'European'),
		('6', 'Aboriginal')
	)
	
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	grade = models.IntegerField()
	gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
	race = models.CharField(max_length=1, choices=ETHNIC_CHOICE)
	age = models.IntegerField(null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)


	def get_absolute_url(self):
		return reverse('students:detail', kwargs={'pk':self.pk})

	def __str__(self):
		return self.first_name

class Detail(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	LEVEL_CHOICE = (
		('1', 'Low'),
		('2', 'Moderate'),
		('3', 'high')
	)

	incident = models.TextField(max_length=10000)
	incident_level = models.CharField(max_length=1, choices=LEVEL_CHOICE)
	location = models.CharField(max_length=50)
	method = models.TextField(max_length=1000)
	notes = models.TextField(max_length=1000)
	date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __unicode__(self):
		return self.incident_level

class Score(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	math_score = models.IntegerField()
	reading_score = models.IntegerField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.math_score 

class Classroom(models.Model):
	student = models.ForeignKey(Student ,on_delete=models.CASCADE, blank=True)
	detail = models.ManyToManyField(Detail)
	score = models.ManyToManyField(Score)





















