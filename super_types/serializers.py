from rest_framework import serializers
from .models import Super_Type
# from .models import Product

# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ['id','title','description','price','inventory_quantity','image_link']

class Super_Type_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Super_Type
        fields = ['id','type']