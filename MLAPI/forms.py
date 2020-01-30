from django.forms import ModelForm
from .models import features

class MyForm(ModelForm):
	class Meta:
		model=features
		fields = '__all__'