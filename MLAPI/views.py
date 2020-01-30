from django.shortcuts import render
from .forms import MyForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import features
from .serializers import featuresSerializers
import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
import datetime 
import os
# Create your views here.
class FeaturesView(viewsets.ModelViewSet):
	queryset = features.objects.all()
	serializer_class = featuresSerializers

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filepath = os.path.join(BASE_DIR, 'MLAPI')
model_filename = filepath+ '/bestmodelrandom.pkl'

@api_view(["POST"])
def durationpredict(request):
	try:
		
		model_file = open(model_filename,"rb")
		model_imported = pickle.load(model_file)
		model_file.close()
		mydata=request.data
		unit=np.array(list(mydata.values()))
		unit=unit.reshape(1,-1)
		y_pred=model_imported .predict(unit)
		time = float(y_pred)*24
		time = str(datetime.timedelta(hours = time))
		#print(time)
		#y_pred=(y_pred>0.58)
		return JsonResponse('predicted duration is {}'.format(time), safe=False)
	except ValueError as e:
		return Response(e.args[0], status.HTTP_400_BAD_REQUEST)