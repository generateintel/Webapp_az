from django.contrib.auth.models import User
from rest_framework import serializers

from .models import User_Profile, Contact_Us


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=User_Profile
        fields=['user','profile_picture', 'gender','age','interest','mobile','location']



class ProfilePostSerializer(serializers.ModelSerializer):
    class Meta:
        model=User_Profile
        fields=['user','profile_picture', 'gender','age','interest','mobile','location','verfication_status','activation_Key']
#


class Contact_Us_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Contact_Us
        fields=['name','email','phone','message','created_date','modified_date']
