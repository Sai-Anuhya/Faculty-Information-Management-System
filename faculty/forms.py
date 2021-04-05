from django import forms
from .models import Faculty

Depart= [
    ('CSE', 'CSE'),
    ('IT', 'IT'),
    ('EEE', 'EEE'),
    ('CIV', 'CIV'),
    ('ECE', 'ECE'),
    ('MEC', 'MEC'),
    ]

class DepartmentForm(forms.Form):
	
    select_dep = forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=Depart))

    class Meta:
    	fields = ['select_dep']


class FacultyModelForm(forms.ModelForm):

	class Meta:
		model = Faculty
		fields = [
	#		'faculty_id',
			'faculty_name',
			'department',
			'dept_id',
			'AICTE_id',
			'title',
			'mobile_No',
			'email_id',
			'aadhar_No',
			'pan_No',
			'designation',
			'ug_percentage',
			'ug_award_year',
			'pg',
			'pg_percentage',
			'phd_award_year',
			'pg_award_year',
			'ratified',
			'No_of_papers_published',
			'No_of_books_published',
			'No_of_paytents',
			'No_of_rnd_projects',
			'No_of_phd_guides',
			'date_of_birth',
			'date_of_joining',
			'date_of_relieving',
			'image'
		]


class UserLoginForm(forms.Form):
	username = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean_email(self, *args, **kwargs):
		email = self.cleaned_data.get("username")
		if not email.endswith("@svecw.edu.in"):
			raise forms.ValidationError("Not valid Email")
		return email
