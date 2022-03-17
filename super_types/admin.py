from django.contrib import admin
from super_types.models import Super_Type
from supers.models import Super

# Register your models here.
admin.site.register(Super_Type)
admin.site.register(Super)
