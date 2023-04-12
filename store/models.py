from django.db import models
from django.utils import timezone as tz
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model

class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError('Phone number must be set.')
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(phone_number, password, **extra_fields)

class Client(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=12, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.phone_number
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perm(self, app_label):
        return True
    
    class Meta:
        verbose_name_plural = 'Users'

class Banner(models.Model):
    image = models.ImageField(upload_to='banners', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Banners'


class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)
    category_image = models.ImageField(upload_to='category', blank=True, null=True)
    joined_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    product_adder = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='added_products', to_field='phone_number')
    product_name = models.CharField(max_length=70)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='product', blank = True, null=True)
    product_image2 = models.ImageField(upload_to='product', blank = True, null=True)
    product_image3 = models.ImageField(upload_to='product', blank = True, null=True)
    product_image4 = models.ImageField(upload_to='product', blank = True, null=True)
    product_image5 = models.ImageField(upload_to='product', blank = True, null=True)
    product_image6 = models.ImageField(upload_to='product', blank = True, null=True)
    product_image7 = models.ImageField(upload_to='product', blank = True, null=True)
    product_image8 = models.ImageField(upload_to='product', blank = True, null=True)
    product_address = models.CharField(max_length=100)
    product_quantity = models.CharField(max_length=8)
    product_description = models.TextField(blank=True)
    is_vip = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    delivery = models.BooleanField(default=False)
    credit = models.BooleanField(default=False)
    joined_date = models.DateField(auto_now_add=True)
    product_category = models.ForeignKey(Category, to_field='category_name', on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.product_name
        
    class Meta:
        verbose_name_plural = 'Products'

class Dukan(models.Model):
    product_name = models.CharField(max_length=70)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='DukanProductImages', blank = True, null=True)
    product_image2 = models.ImageField(upload_to='DukanProductImages', blank = True, null=True)
    product_image3 = models.ImageField(upload_to='DukanProductImages', blank = True, null=True)
    product_image4 = models.ImageField(upload_to='DukanProductImages', blank = True, null=True)
    product_image5 = models.ImageField(upload_to='DukanProductImages', blank = True, null=True)
    product_image6 = models.ImageField(upload_to='DukanProductImages', blank = True, null=True)
    product_image7 = models.ImageField(upload_to='DukanProductImages', blank = True, null=True)
    product_image8 = models.ImageField(upload_to='DukanProductImages', blank = True, null=True)
    product_address = models.CharField(max_length=100)
    product_quantity = models.CharField(max_length=8)
    product_description = models.TextField(blank=True)
    delivery = models.BooleanField(default=False)
    credit = models.BooleanField(default=False)
    joined_date = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return self.product_name
        
    class Meta:
        verbose_name_plural = 'Dukan'
        