from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class features(models.Model):
	reassignment_count=models.IntegerField(default=0)
	sys_mod_count=models.IntegerField(default=0)
	caller_id=models.IntegerField(default=0)
	opened_by=models.IntegerField(default=0)
	location=models.IntegerField(default=0)
	category=models.IntegerField(default=0)
	subcategory=models.IntegerField(default=0)
	assignment_group=models.IntegerField(default=0)
	assigned_to=models.IntegerField(default=0)
	
	opened_at_day=models.IntegerField(default=1,
		validators=[
            MaxValueValidator(31),
            MinValueValidator(1)
        ])
	opened_at_month=models.IntegerField(default=1,
		validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ])
	opened_at_minute=models.IntegerField()
	sys_updated_day=models.IntegerField(default=1,
		validators=[
            MaxValueValidator(31),
            MinValueValidator(1)
        ])
	sys_updated_month=models.IntegerField(
		default=1,
		validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ])
	

	def __str__(self):
		return str(self.caller_id)
	
	
	
	
	


