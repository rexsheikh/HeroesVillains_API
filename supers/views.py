from unicodedata import name
from urllib import response
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

@api_view(['GET'])
def power_compare(request):
    custom_response_dict = {}
    powers = Power.objects.all()
    hero_param = request.query_params.get('hero')
    villain_param = request.query_params.get('villain')
    hero = get_object_or_404(Super,name = hero_param) 
    villain = get_object_or_404(Super,name = villain_param)
    hero_serializer = SuperSerializer(hero)
    villain_serializer = SuperSerializer(villain)
   

    if hero.super_type.type == villain.super_type.type:
        return Response('Enter a hero and villain')
    else:
        hero_power_count =  powers.filter(super__id = hero.id).count()
        villain_power_count = powers.filter(super__id = villain.id).count()
        if hero_power_count > villain_power_count:
            custom_response_dict['winner'] = hero_serializer.data
            custom_response_dict['loser'] = villain_serializer.data
            
        elif hero_power_count < villain_power_count:
            custom_response_dict['winner'] = villain_serializer.data
            custom_response_dict['loser'] = hero_serializer.data
        else:
            custom_response_dict['tie'] = villain_serializer.data,hero_serializer.data

    return Response(custom_response_dict)


    
#create an enpoint that allows you to pass in a hero name and villain as query params
#query for each of the submitted supers and compare their number of powers. 
#whoever has more powers listed is the winner 
#send back a custom object response that cotains a winner key containing the winner's info
#and a loser key containing the loser's infor, or a different message if it 
#is a tie.

#I retrieved the hero/villain objects and made sure they were of the appropriate type. 
#to perform the action requested in need to query the junction table and count how many times the 
#particular superid comes up. 
#retrieve id from the query param. use powers.filter(id).count() to compare and return the custom object 

#visit urls...unsure what to pass in as parameters here