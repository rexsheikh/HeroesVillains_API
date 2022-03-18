from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Super,Power
from super_types.models import Super_Type
from .serializers import SuperSerializer,PowerSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET','POST'])
def super_list(request):
    custom_response_dict = {}
    supers = Super.objects.all()
    super_types = Super_Type.objects.all()

    if request.method == 'GET':
        super_param = request.query_params.get('type')
        if super_param:
            if super_param == 'hero':
                supers = supers.filter(super_type__type = 'Hero')
            elif super_param == 'villain':
                supers = supers.filter(super_type__type = 'Villain')
        else:
            for super_type in super_types:
                supers = Super.objects.all()
                supers = supers.filter(super_type__type = super_type.type)
                serializer = SuperSerializer(supers,many = True)
                custom_response_dict[super_type.type] = serializer.data
            return Response(custom_response_dict)
        serializer = SuperSerializer(supers,many=True)
        return Response(serializer.data)

        
        #anything with hero type gets added to hero key in customdict
        #anything with villain type gets added to villain key in customdict 

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def super_detail(request,pk):
    super = get_object_or_404(Super,pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['PATCH'])
def power_patch(request,pk,id):
    super = get_object_or_404(Super,pk = pk) #access particular super by pk
    power = get_object_or_404(Power,id = id) #access particular power by id
    super.powers.add(power)
    serializer = SuperSerializer(super,data=request.data,partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
#power model has name property. it is registered with seeded values. primary and secondary ability have 
#been replaced with a powers manytomanyfield 
#create a patch endpoint -> urls now has path('<int:pk>/power/',views.power_patch)
#http://127.0.0.1:8000/supers/1/telekinesis
#what does pk = pk do even? 
#how does the serializer change? do i need to change the fields to be displayed?
#