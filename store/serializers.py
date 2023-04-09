from rest_framework import serializers
from rest_framework.authtoken.views import Token
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'phone_number', 'password')

        extra_kwargs = {'password':{
            'write_only': True
        }}
    
    def create(self, validated_data):
        user = Client.objects.create(phone_number=validated_data['phone_number'])
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name', 'category_image', 'joined_date')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id',
                 'product_name',
                 'product_price',
                 'product_image',
                 'product_image2',
                 'product_image3',
                 'product_image4', 
                 'product_image5', 
                 'phone_number', 
                 'product_address', 
                 'product_quantity', 
                 'about_product', 
                 'russian_product_name', 
                 'delivery', 
                 'credit', 
                 'is_vip', 
                 'joined_date', 
                 'product_category')
