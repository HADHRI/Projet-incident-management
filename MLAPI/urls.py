from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('MyAPI', views.FeaturesView)
urlpatterns = [
	#path('form/', views.myform, name='myform'),
    path('api/', include(router.urls)),
    path('predict/', views.durationpredict),
 ]