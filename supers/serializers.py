from rest_framework import serializers
from .models import Super

class Super_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Super
        fields = ['name','alter_ego','primary_ability','secondary_ability','catchphrase','super_type']