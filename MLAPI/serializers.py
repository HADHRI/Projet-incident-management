from rest_framework import serializers
from .models import features

class featuresSerializers(serializers.ModelSerializer):
	class Meta:
		model=features
		fields='__all__'
		