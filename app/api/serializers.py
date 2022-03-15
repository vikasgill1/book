from ..models import *
from rest_framework.serializers import *

class UserSerializer(ModelSerializer):
    email=EmailField(error_messages={'required':'email key is required','blank':'email is required'})
    password=CharField(write_only=True,error_messages={'required':'password key is required','blank':'password is required'})
    username=CharField(write_only=True,error_messages={'required':'username key is required','blank':'username is required'})
    first_name=CharField(write_only=True,error_messages={'required':'username key is required','blank':'username is required'})
    last_name=CharField(write_only=True,error_messages={'required':'username key is required','blank':'username is required'})
    class Meta:
        model=User
        fields=("__all__")
        
    def validate(self,data):
        username=data.get('username')
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise ValidationError("Username already exists")
        return data
    
class EmployeUserSerializer(Serializer):
    email=EmailField(error_messages={'required':'email key is required','blank':'email is required'})
    password=CharField(error_messages={'required':'password key is required','blank':'password is required'})
    username=CharField(error_messages={'required':'username key is required','blank':'username is required'})
    first_name=CharField(error_messages={'required':'username key is required','blank':'username is required'})
    last_name=CharField(error_messages={'required':'username key is required','blank':'username is required'})
        
    def validate(self,data):
        username=data.get('username')
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise ValidationError("Username already exists")
        return data
    def create(self, validated_data):
        first_name=validated_data.get('first_name')
        last_name=validated_data.get('last_name')
        email=validated_data.get('email')
        username=validated_data.get('username')
        password=validated_data.get('password')
        
        user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,is_staff=True,user_type=1)
        user.set_password(password)
        user.save()
        return validated_data
    
class Noteserializer(Serializer):
    note_name=CharField(error_messages={'required':'email key is required','blank':'email is required'})
    note_describe=CharField(error_messages={'required':'email key is required','blank':'email is required'})
    def create(self,data):
        Note.objects.create(user=self.context.get('user'),note_name=data.get('note_name'),note_describe=data.get('note_describe')).save()
        return data
    def update(self,instance,validated_data):
        instance.note_name=validated_data.get('note_name')
        instance.note_describe=validated_data.get('note_describe')
        instance.save()
        return validated_data