from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
	class Meta:
		model = Employee
		fields = ['prenom', 'nom', 'mail', 'tel', 'date_embauche']
		