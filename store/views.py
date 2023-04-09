from rest_framework.decorators import api_view, permission_classes, authentication_classes, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password
from rest_framework import status
from .serializers import *

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        if request.data['phone_number'][:5] != '+9936' or int(request.data['phone_number'][4:6]) > 65 or int(request.data['phone_number'][4:6]) < 61:
            return Response({'ERROR': 'This phone_number is NOT valid. Please type correct number.'}, status=status.HTTP_400_BAD_REQUEST)
        if request.data['phone_number'][1:].isdigit() == False or ' ' in request.data['phone_number']:
            return Response({'ERROR': 'A phone number can NOT contain letters or spaces.'}, status=status.HTTP_400_BAD_REQUEST)
        if len(request.data['phone_number']) < 12:
            return Response({'ERROR': 'The length of phone number can NOT be less than 12 characters.'}, status=status.HTTP_400_BAD_REQUEST)
        if len(request.data['phone_number']) > 12:
            return Response({'ERROR': 'The length of phone number can NOT exceed 12 characters.'}, status=status.HTTP_400_BAD_REQUEST)
        if len(request.data['password']) < 6:
            return Response({'ERROR': 'This password is NOT valid. Minimum length of password must be 6.'}, status=status.HTTP_400_BAD_REQUEST)
        if len(request.data['password'])  > 20:
            return Response({'ERROR': 'This password is NOT valid. Maximum length of password must be 20.'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        phone_number = request.data['phone_number']
        password = request.data['password']
        try:
            user = Client.objects.get(phone_number=phone_number)
        except Client.DoesNotExist:
            return Response({'ERROR': f'phone number: {phone_number} is unauthorized.'}, status=status.HTTP_401_UNAUTHORIZED)
        if check_password(password, user.password) == True:
            try:
                Token.objects.create(user=user)
                return Response({'SUCCESS': 'You have been logged in.'}, status=status.HTTP_201_CREATED)
            except:
                token = user.auth_token.key
                return Response({'ERROR': f'phone number {phone_number} is already logged in.'}, status=status.HTTP_400_BAD_REQUEST)
        elif check_password(password, user.password) == False:
            return Response({'ERROR': 'Invalid password'}, status=status.HTTP_417_EXPECTATION_FAILED)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    if request.method == 'POST':
        token= Token.objects.get(user=request.user)
        token.delete()
        return Response({'SUCCESS': 'You have been logged out.'})

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_profile(request, id):
    if request.method == 'DELETE':
        try:
            user = Client.objects.get(id=id)
            user.delete()
            return Response({'SUCCESS': f'profile {user} deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Client.DoesNotExist:
            return Response({'ERROR': 'user does not exist.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def single_user_information(request, id):
    if request.method == 'GET':
        try:
            user = Client.objects.get(id=id)
            serializer = UserSerializer(user, context={'requsest': request})
            return Response(serializer.data)
        except Client.DoesNotExist:
            return Response({'ERROR': 'user does not exist.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def banner_list(request):
    if request.method == 'GET':
        data = Banner.objects.all()
        serializer = BannerSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def category_list(request):
    if request.method == 'GET':
        data = Category.objects.all()
        serializer = CategorySerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 20
        data = Product.objects.filter(is_active=True).order_by('-id')
        result_data = paginator.paginate_queryset(data, request)
        serializer = ProductSerializer(result_data, context={'request': request}, many=True)
        return paginator.get_paginated_response(serializer.data)

@api_view(['GET'])
def products_by_category(request, id):
    if request.method == 'GET':
        try:
            category = Category.objects.get(id=id)
            paginator = PageNumberPagination()
            paginator.page_size = 20
            data = category.products.filter(is_active=True).order_by('-id')
            result_data = paginator.paginate_queryset(data, request)
            serializer = ProductSerializer(result_data, context={'request': request}, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Category.DoesNotExist:
            return Response({'ERROR': 'Category does NOT exists'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def products_by_id(request, id):
    try:
        item = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({'ERROR': 'Product does NOT exists'}, status=status.HTTP_204_NO_CONTENT)
    if request.method == 'GET':
        serializer = ProductSerializer(item, context={'request': request})
        return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@parser_classes([JSONParser, MultiPartParser, FormParser])
def add_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product_adder=request.user)
            return Response({'SUCCESS': 'product added successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def products_by_user(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 20
        data = request.user.added_products.filter(is_active=True).order_by('-id')
        result_data = paginator.paginate_queryset(data, request)
        serializer = ProductSerializer(result_data, context={'request': request}, many=True)
        return paginator.get_paginated_response(serializer.data)

@api_view(['PATCH', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_user_product(request, id):
    try:
        product = Product.objects.get(id=id, is_active=True)
    except Product.DoesNotExist:
        return Response({'NOT FOUND': 'product does not exists'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PATCH':
        serializer = ProductSerializer(instance=product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'SUCCESS': 'product updated successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        product.delete()
        return Response({'SUCCESS': 'product deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        