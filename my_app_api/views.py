from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import userModel
from .serializers import userModelSerializer
# Create your views here.

@api_view(['GET'])
def testPoint(request):
    data=request.data
    print(data)
    print(request.query_params.get("hela"))
    
    res= Response(data,201)
    res.set_cookie("token","1st cookie",max_age=15)
    return res


@api_view(['POST'])
def addUser(request):
    # get name and email from request body
    data=request.data
   
    name=data.get("name")
    email=data.get("email")
    # if name or emal does'nt exists return
    if(name==None or email==None): return Response(data={"sucess":False,"data":[],"message":"insufficient details"})
    # check if user already exists or not
    check=userModel.objects.filter(email=email)
  
    if(check): return Response(data={"sucess":False,"data":[],"message":"user alreayd exists"})
    # create a new user
    data=userModel.objects.create(name=name,email=email)
    #  while creating if any error occurs
    if data is None:  return Response({"sucess":False,"data":[],"message":"error occured . try again"})
    # serialize the data
    data=userModelSerializer(data,many=False)
    # return response
    return Response(data={"success":True,"data":data.data,"message":"user created successfull"},status=201)



#api to get all data
@api_view(['GET'])
def getAllUSers(request):
    data=userModel.objects.all()
    serialize_data=userModelSerializer(data,many=True)
    return Response(data={"success":True,"data":serialize_data.data,"message":"successfull retrived all data"},status=201)


#request to update the user
@api_view(["PUT"])
def updateUser(request):
    params=request.query_params
    id=params.get("id")
    body_data=request.data
    email=body_data.get("email")
    name=body_data.get("name")
    # if not of email
    if(email is None and name is None):  return Response(data={"sucess":False,"data":[],"message":"insufficient details"})
     
    # find the user
    user=userModel.objects.filter(id=id)
    print(user)
    # if user doesn't exist
    if(len(user)==0):  return Response(data={"sucess":False,"data":[],"message":"user doesn't exist"})
    user=userModel.objects.get(id=id)
    if(name):user.name=name
    if(email):user.email=email
    user.save()
    serialized_data=userModelSerializer(user,many=False)
    return Response(data={"success":True,"data":serialized_data.data,"message":"user created successfull"},status=201)

    

@api_view(["DELETE"])
def deleteUserByid(request):
    id=request.query_params.get("id")
    if(id is None): return Response(data={"sucess":False,"data":[],"message":"insufficient details"})

    # find user with id    
    user=userModel.objects.filter(id=id).first()
    print(user)
    if(user is None): return Response(data={"sucess":False,"data":[],"message":"user doesn't exists"})
    print(user.email)
    user.delete()
    return  Response(data={"sucess":True,"data":[],"message":"deleted sucessfully"})
    