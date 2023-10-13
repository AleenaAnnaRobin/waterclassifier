from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="register_user")

class QualityAnalysis(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="quality_user")
    register=models.ForeignKey(Register,on_delete=models.CASCADE)
    sample_id=models.CharField(max_length=10,null=True)
    pH = models.FloatField()
    dissolved_oxygen = models.FloatField()
    temperature = models.FloatField()
    conductivity = models.FloatField()
    turbidity = models.FloatField()
    tds = models.FloatField()
    chlorine = models.FloatField()
    

class QualityResult(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="result_user")
    quality_analysis=models.ForeignKey(QualityAnalysis,on_delete=models.CASCADE)
    result = models.CharField(max_length=20)
    created_on=models.DateTimeField(null=True)