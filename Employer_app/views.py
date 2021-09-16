from django.shortcuts import render, redirect
from .formulaire import EmployeeForm

from rest_framework.decorators import api_view

from rest_framework.permissions import SAFE_METHODS,AllowAny,IsAuthenticated, BasePermission,IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Employee




# Create your views here.
def index(request):
	if request.method == "POST":
		form = EmployeeForm(request.POST).save()
		
	else:
	    form = EmployeeForm()

	return render(request, 'index.html', {'form': form, 'dataEmployee':Employee.objects.all()})


