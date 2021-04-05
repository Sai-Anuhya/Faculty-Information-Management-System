from django.db import models
from django.urls import reverse

# Create your models here.


class Faculty(models.Model):
	Ratified = [
		('Yes', 'Yes'),
		('No', 'No')
	]

	PG = [
		('Yes', 'Yes'),
		('No', 'No')
	]

	Designation= [
    ('Doctorate', 'Doctorate'),
    ('Professor', 'Professor'),
    ('Associate Professor', 'Associate Professor'),
    ('Assistant Professor', 'Assistant Professor')
    ]

	Title= [
    ('Mr', 'Mr'),
    ('Ms', 'Ms'),
    ('Dr', 'Dr')
    ]

	Department= [
    ('CSE', 'CSE'),
    ('IT', 'IT'),
    ('EEE', 'EEE'),
    ('CIV', 'CIV'),
    ('ECE', 'ECE'),
    ('MEC', 'MEC'),
    ('BS', 'BS'),
    ('MBA', 'MBA')
    ]  
    
	
	#faculty_id = models.AutoField(primary_key=True)
	faculty_name = models.CharField(max_length=120)	
	department = models.CharField(max_length=100, choices=Department)
	dept_id = models.IntegerField()
	AICTE_id = models.CharField(max_length=200)
	title = models.CharField(max_length=50, choices=Title)
	mobile_No = models.IntegerField()
	email_id = models.EmailField(max_length=250)
	aadhar_No = models.CharField(max_length=50)
	pan_No = models.CharField(max_length=50)
	designation = models.CharField(max_length=50, choices=Designation)
	ug_percentage = models.IntegerField()
	ug_award_year = models.IntegerField()
	pg = models.CharField(max_length=10, choices=PG)
	pg_percentage = models.IntegerField(null=True, blank=True)
	pg_award_year = models.IntegerField(null=True, blank=True)
	phd_award_year = models.IntegerField()
	ratified = models.CharField(max_length=10, choices=Ratified)
	No_of_papers_published = models.IntegerField()
	No_of_books_published = models.IntegerField()
	No_of_paytents = models.IntegerField()
	No_of_rnd_projects = models.IntegerField()
	No_of_phd_guides = models.IntegerField()
	date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
	date_of_joining = models.DateField(auto_now=False, auto_now_add=False)
	date_of_relieving = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
	image = models.ImageField(upload_to='profile_image', blank=True)


	def get_absolute_url(self):
		return reverse("faculty:faculty_detail", kwargs = {"id":self.id})

	def get_absolute_url_dep(self):
		return reverse("faculty:faculty_detail", kwargs = {"id":self.id})
