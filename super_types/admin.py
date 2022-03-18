from django.contrib import admin
from super_types.models import Super_Type
from supers.models import Super
from supers.models import Power

# Register your models here.
admin.site.register(Super_Type)
admin.site.register(Super)
admin.site.register(Power)
