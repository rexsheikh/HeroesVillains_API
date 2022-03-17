from rest_framework import serializers
from .models import Super_Types
# from .models import Product

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['id','title','description','price','inventory_quantity','image_link']

class Super_Types_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Super_Types
        fields = ['id','type']