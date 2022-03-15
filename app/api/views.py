
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from app.api.serializers import EmployeUserSerializer,Noteserializer, UserSerializer
from ..models import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
# Create your views here.
'''

         ===============>              SIMPLE USER PROFILE CODE        <======================

'''

class UserRegister(APIView):
    permission_classes = (AllowAny,)
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():              
            serializer.save()
            return Response({'account': 'create successfully',"data":serializer.data},status=HTTP_201_CREATED)
        return Response(serializer.errors)

class UserProfile(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        stu=User.objects.get(id=request.user.id)
        serializer=UserSerializer(stu)
        return Response({'data':serializer.data},status=HTTP_200_OK)
    def put(self,request):
        stu=User.objects.get(id=request.user.id)
        serializer=UserSerializer(instance=stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'account': 'create successfully',"data":serializer.data},status=HTTP_201_CREATED)
        return Response(serializer.errors)
    def delete(self,request):
        try:
            stu=User.objects.get(id=request.user.id)
            stu.delete()
        except Exception as e:
            return Response({'error':e},status=HTTP_400_BAD_REQUEST)
        
        
        
        
class NoteView(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request):
        stu=Note.objects.filter(user=request.user)
        serializer=Noteserializer(stu,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=Noteserializer(data=request.data,context={'user':request.user})
        if serializer.is_valid():
            serializer.save()
            return Response({'Note': 'Update successfully',"data":serializer.data},status=HTTP_201_CREATED)
        return Response({"error":serializer.errors},status=HTTP_400_BAD_REQUEST) 
    
    def put(self,request):
        stu=Note.objects.get(id=request.data.get('id'))
        serializer=Noteserializer(instance=stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Note': 'Update successfully',"data":serializer.data},status=HTTP_201_CREATED)
        return Response({"error":serializer.errors},status=HTTP_400_BAD_REQUEST)
    
    
    def delete(self,request):
        try:
            stu=Note.objects.get(user=request.user,id=request.data.get('id'))
            stu.delete()
            return Response({'delete': 'successfully delete'},status=HTTP_200_OK)
        except Exception as e:
            return Response({'error':e})
    
    
        
        
        
        '''
                   +++++++++++++     ADMIN  PANEL    ++++++++++++++++
               
        '''
        

class AdminUserRegister(APIView):
    permission_classes = (IsAdminUser,)
    def post(self,request):
        serializer=EmployeUserSerializer(data=request.data)       
        if serializer.is_valid():        
            serializer.save()
            return Response({'account': 'create successfully',"data":serializer.data},status=HTTP_201_CREATED)
        return Response(serializer.errors)
    
    
class UserAdminEdit(APIView):
    permission_classes = (IsAdminUser,)
    
    def get(self,request):
            if User.objects.get(id=request.data.get('id')).exists():
                stu=User.objects.filter(id=request.data.get('id'))
                serializer=UserSerializer(stu,many=True)
                return Response({'data':serializer.data},status=HTTP_200_OK)
            else:
                stu=User.objects.all()
                serializer=UserSerializer(stu,many=True)
                return Response({'data':serializer.data},status=HTTP_200_OK)
    def  post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():              
            serializer.save()
            return Response({'account': 'create successfully',"data":serializer.data},status=HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def put(self,request):
        stu=User.objects.get(id=request.data.get('id'))
        serializer=UserSerializer(instance=stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'account': 'create successfully',"data":serializer.data},status=HTTP_201_CREATED)
        return Response(serializer.errors)
    def delete(self,request):
        try:
            stu=User.objects.get(id=request.data.get('id'))
            stu.delete()
        except Exception as e:
            return Response({'error': e},status=HTTP_400_BAD_REQUEST)
        
        
        
class NoteAdmin(APIView):
    permission_classes=(IsAdminUser,)
    def get(self,request):
        if Note.objects.filter(user=request.data.get('user'),id=request.data.get('id')):
            stu=Note.objects.filter(user=request.data.get('user'),id=request.data.get('id'))
            serializer=Noteserializer(stu,many=True)
            return Response({'data':serializer.data},status=HTTP_200_OK)
        elif Note.objects.filter(id=request.data.get('id')):
            stu=Note.objects.filter(id=request.data.get('id'))
            serializer=Noteserializer(stu,many=True)
            return Response({'data':serializer.data},status=HTTP_200_OK)
        elif Note.objects.filter(user=request.data.get('user')):
            stu=Note.objects.filter(user=request.data.get('user'))
            serializer=Noteserializer(stu,many=True)
            return Response({'data':serializer.data},status=HTTP_200_OK)
        else:
            stu=Note.objects.all()
            serializer=Noteserializer(stu,many=True)
            return Response({'data':serializer.data},status=HTTP_200_OK)
   
    
    def put(self,request):
        if Note.objects.get(user=request.data.get('user'),id=request.get('id')).exists():
            stu=Note.objects.get(user=request.data.get('user'),id=request.get('id'))
            serializer=Noteserializer(instance=stu,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Note': 'Update successfully',"data":serializer.data},status=HTTP_201_CREATED)
            return Response({"error":serializer.errors},status=HTTP_400_BAD_REQUEST)
        elif Note.objects.get(id=request.get('id')).exists():
            stu=Note.objects.get(id=request.get('id'))
            serializer=Noteserializer(instance=stu,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Note': 'Update successfully',"data":serializer.data},status=HTTP_201_CREATED)
            return Response({"error":serializer.errors},status=HTTP_400_BAD_REQUEST)
        else:
            return Response({"data":"invalid id"},status=HTTP_404_NOT_FOUND)
    
    def delete(self,request):        
        if Note.objects.filter(user=request.data.get('user'),id=request.data.get('id')).exists():  
            Note.objects.filter(user=request.data.get('user'),id=request.data.get('id')).delete()
            return Response({'delete': 'successfully delete'},status=HTTP_200_OK)
        elif Note.objects.filter(id=request.data.get('id')).exists():  
            Note.objects.filter(id=request.data.get('id')).delete()
            return Response({'delete': 'successfully delete'},status=HTTP_200_OK)
        else:
            return Response({'error','id is not exit'},status=HTTP_400_BAD_REQUEST)
     
    