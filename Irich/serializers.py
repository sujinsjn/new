from statistics import mode
from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from authentication.models import Employee, Transactions, deals, payments,business_details,category, rewards
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import random
import string
#from rest_framework import nested
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class business_detailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = business_details 
        fields="__all__"

        
        

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields='__all__'
class transSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields='__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('id','username','email','phone')

class UseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('password','referl_code')



class EmployeesSerializer(serializers.ModelSerializer):
   user=UsersSerializer()
   class Meta:
        model = Employee
        fields=('phone')


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            
          'username',
          'password',
          'first_name',
          'last_name',
          'email',
          'phone'
        )

class EmployeeSerializer(serializers.ModelSerializer):
   #account = UserSerializer()

   class Meta:
        model = Employee
        fields=('user',)


class UserRegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=30)
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=100)
    last_name = serializers.CharField(max_length=15)
    password = serializers.CharField(style={'input_type': 'password'},write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'},write_only=True)
    

    class Meta:
        model = Employee
        fields = ['first_name','last_name', 'username', 'email', 'phone', 'password', 'password2','referral_code','postcode']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'error':'Password should be the same'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email id already exists'})
        
        if Employee.objects.filter(phone=self.validated_data['phone']).exists():
            raise serializers.ValidationError({'error':'This phone number is already been used'})

        if User.objects.filter(username=self.validated_data['username']):
            raise serializers.ValidationError({'error':'This username is already been taken'})

        user = User(
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            username = self.validated_data['username'],
            email = self.validated_data['email']
        )
        
        user.set_password(password)
        # account.is_rider = True
        user.save()
        
        employee = Employee(
            user = user,
            phone = self.validated_data['phone'],
            postcode = self.validated_data['postcode'],
            referral_code = self.validated_data['referral_code']
        )
        N=8
        referral = ''.join(random.choices(string.ascii_uppercase +
                                          string.digits, k=N))
        employee.referral = referral
        employee.save()

        return employee


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(UserTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({'user': self.user.username})
        data.update({'id': self.user.id})
        # and everything else you want to send in the response
        return data
        
class usersSerializer(serializers.ModelSerializer):
    user = UseSerializer()
    class Meta:
        model = Employee
        fields = (
          
        
          'user'
          
        )

    def create(self, validated_data):
        employee = validated_data.pop('employee')  
        employee = Employee.objects.create(**employee)
        user = User.objects.create(employee=employee, **validated_data)
        
        return user       
    
    
class walletpaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payments
        fields="__all__"


class paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payments
        exclude = ('irich_walletamount',)
        #fields=('amount','business', 'user_id')


class businessSerializer(serializers.ModelSerializer):
    class Meta:
        model = business_details
        fields=('categories',
    'bank_name',
    
    'business_name',
    'business_desc',
    'business_address',
    'email',
    'subcategory',
    'irich',    
    'Account_details',
    'account_number',
    'IFSC_code',
    'business_contact',
    'image1',)
class dealSerializer(serializers.ModelSerializer):
    class Meta:
        model = deals
        fields="__all__"

class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = rewards
        fields="__all__"

class RwardsSerialiser(serializers.ModelSerializer):
    class Meta:
        model = rewards
        fields = "__all__"

class UserdetailsSerializer(serializers.ModelSerializer):
    user=EmployeesSerializer()
    class Meta:
        model = User
        fields="__all__"


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = business_details
        fields = '__all__'