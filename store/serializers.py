from rest_framework import serializers
from rest_framework.authtoken.views import Token
from .models import *

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    class Meta:
        model = Client
        fields = ('id', 'phone_number', 'password', 'token', 'is_staff')

        extra_kwargs = {'password':{
            'write_only': True
        }}
    
    def create(self, validated_data):
        user = Client.objects.create(phone_number=validated_data['phone_number'])
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user
    
    def get_token(self, obj):
        token = Token.objects.get(user=obj)
        return token.key

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'category_image', 'joined_date')

class ProductSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Product
        fields = ('id',
                 'product_adder',
                 'product_name',
                 'product_price',
                 'product_image',
                 'product_image2',
                 'product_image3',
                 'product_image4', 
                 'product_image5',
                 'product_image6',
                 'product_image7',
                 'product_image8', 
                 'product_address', 
                 'product_quantity', 
                 'product_description', 
                 'delivery', 
                 'credit', 
                 'is_vip', 
                 'is_active',
                 'joined_date', 
                 'product_category')
        extra_kwargs = {'product_adder': {'required': False}}
 
class DukanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dukan
        fields = '__all__'
