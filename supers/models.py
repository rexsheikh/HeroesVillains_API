from django.db import models
from super_types.models import super_type

# Create your models here.
class Super(models.Model):
    name = models.CharField(max_length = 255)
    alter_ego = models.CharField(max_length = 255)
    primary_ability = models.CharField(max_length=255)
    secondary_ability = models.CharField(max_length = 255)
    catchphrase = models.CharField(max_length=255)
    super_type = models.ForeignKey(super_type,on_delete = models.CASCADE)