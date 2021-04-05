from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Faculty
from .forms import FacultyModelForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User

from django.views.generic import (
		CreateView,
		DetailView,
		ListView,
		UpdateView,
		DeleteView
	)
from .models import Faculty
from .forms import UserLoginForm, DepartmentForm

# Create your views here.
def navbar(req):
	context = {}
	return render(req, "includes/navbar.html", context)
class tempraryview(ListView):
	template_name = 'auth/index.html'
	queryset = Faculty.objects.all()

def login_view(request):
	form = UserLoginForm(request.POST or None)
	title = "Login"
	context = {}
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
#		if username == password and username.endswith("svecw.edu.in"):
		if user:
			login(request, user)
			return HttpResponseRedirect(reverse('faculty:home'))
		else:
			context = {
				"error" : "Provide valid credintials"
			}
			return render(request, "auth/login.html", context)
	else:
		return render(request, "auth/login.html", context)
		

class select_department(ListView):
	template_name = 'auth/select_department.html'
	queryset = Faculty.objects.all()
'''	
class home(ListView):
	template_name = 'auth/home.html'
	queryset = Faculty.objects.all()
	total = Faculty.objects.count()
'''

def home(request, *args, **kwargs):
	my_context = {
		"total" : Faculty.objects.count(),
		"cse" : Faculty.objects.filter(department="CSE").count(),
		"it" : Faculty.objects.filter(department="IT").count(),
		"ece" : Faculty.objects.filter(department="ECE").count(),
		"eee" : Faculty.objects.filter(department="EEE").count(),
		"mec" : Faculty.objects.filter(department="MEC").count(),
		"civ" : Faculty.objects.filter(department="CIV").count(),
		"bs" : Faculty.objects.filter(department="BS").count(),
		"mba" : Faculty.objects.filter(department="MBA").count(),
		
		"doctorates" : Faculty.objects.filter(designation="Doctorate").count(),
		"doctorates_eee" : Faculty.objects.filter(department="EEE").filter(designation="Doctorate").count(),
		"doctorates_ece" : Faculty.objects.filter(department="ECE").filter(designation="Doctorate").count(),
		"doctorates_it" : Faculty.objects.filter(department="IT").filter(designation="Doctorate").count(),
		"doctorates_mba" : Faculty.objects.filter(department="MBA").filter(designation="Doctorate").count(),
		"doctorates_cse" : Faculty.objects.filter(department="CSE").filter(designation="Doctorate").count(),
		"doctorates_bs" : Faculty.objects.filter(department="BS").filter(designation="Doctorate").count(),
		"doctorates_civ": Faculty.objects.filter(department="CIV").filter(designation="Doctorate").count(),
		"doctorates_mec" : Faculty.objects.filter(department="MEC").filter(designation="Doctorate").count(),

		"professors" : Faculty.objects.filter(designation="Professor").count(),
		"professors_ece" : Faculty.objects.filter(department="ECE").filter(designation="Professor").count(),
		"professors_cse" : Faculty.objects.filter(department="CSE").filter(designation="Professor").count(),
		"professors_it" : Faculty.objects.filter(department="IT").filter(designation="Professor").count(),
		"professors_eee" : Faculty.objects.filter(department="EEE").filter(designation="Professor").count(),
		"professors_mec" : Faculty.objects.filter(department="MEC").filter(designation="Professor").count(),
		"professors_civ" : Faculty.objects.filter(department="CIV").filter(designation="Professor").count(),
		"professors_bs" : Faculty.objects.filter(department="BS").filter(designation="Professor").count(),
		"professors_mba" : Faculty.objects.filter(department="MBA").filter(designation="Professor").count(),

		"associate" : Faculty.objects.filter(designation="Associate Professor").count(),
		"associate_eee" : Faculty.objects.filter(department="EEE").filter(designation="Associate Professor").count(),
		"associate_ece" : Faculty.objects.filter(department="ECE").filter(designation="Associate Professor").count(),
		"associate_cse" : Faculty.objects.filter(department="CSE").filter(designation="Associate Professor").count(),
		"associate_it" : Faculty.objects.filter(department="IT").filter(designation="Associate Professor").count(),
		"associate_mec" : Faculty.objects.filter(department="MEC").filter(designation="Associate Professor").count(),
		"associate_civ" : Faculty.objects.filter(department="CIV").filter(designation="Associate Professor").count(),
		"associate_bs" : Faculty.objects.filter(department="BS").filter(designation="Associate Professor").count(),
		"associate_mba" : Faculty.objects.filter(department="MBA").filter(designation="Associate Professor").count(),

		"assisstant" : Faculty.objects.filter(designation="Assisstant Professor").count(),
		"assisstant_eee" : Faculty.objects.filter(department="EEE").filter(designation="Assisstant Professor").count(),
		"assisstant_ece" : Faculty.objects.filter(department="ECE").filter(designation="Assisstant Professor").count(),
		"assisstant_mec" : Faculty.objects.filter(department="MEC").filter(designation="Assisstant Professor").count(),
		"assisstant_civ" : Faculty.objects.filter(department="CIV").filter(designation="Assisstant Professor").count(),
		"assisstant_it" : Faculty.objects.filter(department="IT").filter(designation="Assisstant Professor").count(),
		"assisstant_cse" : Faculty.objects.filter(department="CSE").filter(designation="Assisstant Professor").count(),
		"assisstant_bs" : Faculty.objects.filter(department="BS").filter(designation="Assisstant Professor").count(),
		"assisstant_mba" : Faculty.objects.filter(department="MBA").filter(designation="Assisstant Professor").count(),

		"ratified" : Faculty.objects.filter(ratified="Yes").count(),
		"ratified_cse" : Faculty.objects.filter(ratified="Yes").filter(department="CSE").count(),
		"ratified_it" : Faculty.objects.filter(ratified="Yes").filter(department="IT").count(),
		"ratified_ece" : Faculty.objects.filter(ratified="Yes").filter(department="ECE").count(),
		"ratified_eee" : Faculty.objects.filter(ratified="Yes").filter(department="EEE").count(),
		"ratified_civ" : Faculty.objects.filter(ratified="Yes").filter(department="CIV").count(),
		"ratified_mec" : Faculty.objects.filter(ratified="Yes").filter(department="MEC").count(),
		"ratified_bs" : Faculty.objects.filter(ratified="Yes").filter(department="BS").count(),
		"ratified_mba" : Faculty.objects.filter(ratified="Yes").filter(department="MBA").count(),

		"non_ratified" : Faculty.objects.filter(ratified="No").count(),
		"non_ratified_cse" : Faculty.objects.filter(ratified="No").filter(department="CSE").count(),
		"non_ratified_it" : Faculty.objects.filter(ratified="No").filter(department="IT").count(),
		"non_ratified_ece" : Faculty.objects.filter(ratified="No").filter(department="ECE").count(),
		"non_ratified_eee" : Faculty.objects.filter(ratified="No").filter(department="EEE").count(),
		"non_ratified_civ" : Faculty.objects.filter(ratified="No").filter(department="CIV").count(),
		"non_ratified_mec" : Faculty.objects.filter(ratified="No").filter(department="MEC").count(),
		"non_ratified_bs" : Faculty.objects.filter(ratified="No").filter(department="BS").count(),
		"non_ratified_mba" : Faculty.objects.filter(ratified="No").filter(department="MBA").count(),
	}
	return render(request, "auth/home.html", my_context)

class cse_view(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(department="CSE")


class it_view(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(department="IT")

class ece_view(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(department="ECE")

class eee_view(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(department="EEE")

class civ_view(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(department="CIV")

class mec_view(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(department="MEC")

class bs_view(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(department="BS")

class mba_view(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(department="MBA")

class doctorates_view(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Doctorate")

class doctorates_eee(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(department="EEE").filter(designation="Doctorate")

class doctorates_ece(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(department="ECE").filter(designation="Doctorate")

class doctorates_cse(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(department="EEE").filter(designation="Doctorate")

class doctorates_mec(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(department="MEC").filter(designation="Doctorate")

class doctorates_it(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(department="IT").filter(designation="Doctorate")

class doctorates_civ(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(department="CIV").filter(designation="Doctorate")

class doctorates_bs(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(department="BS").filter(designation="Doctorate")

class doctorates_mba(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(department="MBA").filter(designation="Doctorate")

class professors(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Professor")

class professors_eee(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Professor").filter(department="EEE")

class professors_cse(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Professor").filter(department="CSE")

class professors_it(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Professor").filter(department="IT")

class professors_ece(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Professor").filter(department="ECE")

class professors_mec(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Professor").filter(department="MEC")

class professors_civ(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Professor").filter(department="CIV")

class professors_bs(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Professor").filter(department="BS")

class professors_mba(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Professor").filter(department="MBA")

class associate(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Associate Professor")

class associate_eee(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Associate Professor").filter(department="EEE")

class associate_ece(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Associate Professor").filter(department="ECE")

class associate_cse(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Associate Professor").filter(department="CSE")

class associate_it(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Associate Professor").filter(department="IT")

class associate_mec(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Associate Professor").filter(department="MEC")

class associate_civ(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Associate Professor").filter(department="CIV")

class associate_bs(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Associate Professor").filter(department="BS")

class associate_mba(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Associate Professor").filter(department="MBA")

class assisstant(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Assisstant Professor")

class assisstant_eee(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Assisstant Professor").filter(department="EEE")

class assisstant_ece(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Assisstant Professor").filter(department="ECE")

class assisstant_cse(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Assisstant Professor").filter(department="CSE")

class assisstant_it(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Assisstant Professor").filter(department="IT")

class assisstant_civ(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Assisstant Professor").filter(department="CIV")

class assisstant_mec(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Assisstant Professor").filter(department="MEC")

class assisstant_bs(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Assisstant Professor").filter(department="BS")

class assisstant_mba(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(designation="Assisstant Professor").filter(department="MBA")

class ratified(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="Yes")

class ratified_cse(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="Yes").filter(department="CSE")

class ratified_it(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="Yes").filter(department="IT")

class ratified_ece(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="Yes").filter(department="ECE")

class ratified_eee(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="Yes").filter(department="EEE")

class ratified_civ(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="Yes").filter(department="CIV")

class ratified_mec(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="Yes").filter(department="MEC")

class ratified_bs(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="Yes").filter(department="BS")

class ratified_mba(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="Yes").filter(department="MBA")

class non_ratified(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="No")

class non_ratified_cse(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="No").filter(department="CSE")

class non_ratified_it(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="No").filter(department="IT")

class non_ratified_ece(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="No").filter(department="ECE")

class non_ratified_eee(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="No").filter(department="EEE")

class non_ratified_civ(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="No").filter(department="CIV")

class non_ratified_mec(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="No").filter(department="MEC")

class non_ratified_bs(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="No").filter(department="BS")

class non_ratified_mba(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.filter(ratified="No").filter(department="MBA")


def logout_view(request):
	if request.method == "POST":
		logout(request)
		return HttpResponseRedirect(reverse('user-login'))

class FacultyListView(ListView):
	template_name = 'faculty/faculty_list.html'
	queryset = Faculty.objects.all()

class FacultyDetailView(DetailView):
	template_name = 'faculty/faculty_details.html'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Faculty, id=id_)