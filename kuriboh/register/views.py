from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from datetime import datetime

from .models import User
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

def HomeView(request):
	#model = User
	#template_name = 'register/home.html'
	return render(request, 'register/home.html')

class LoginView(generic.FormView):
	template_name = 'register/login.html'
	form_class = LoginForm
	success_url = '/register/'

	def form_valid(self, form):
		#form.login_account()
		usrname = form.cleaned_data['name']
		pwd = form.cleaned_data['passwd']
		usr = User(username=usrname, password=pwd, register_date=datetime.now())
		usr.save()
		return super().form_valid(form)
	#return render(request, 'register/login.html')


class LogoutView(generic.FormView):
	model = User
	template_name = 'register/logout.html'


class SignUpView(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'register/signup.html'

