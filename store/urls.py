from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from .views import *

urlpatterns = [
    path('api/register', register, name='registering-api'),
    path('api/login', login, name='login'),
    path('api/getprofiledata/<int:id>', single_user_information, name='user-information-api'),
    path('api/deleteprofile/<int:id>', delete_profile, name='deleting-profile-api'),
    path('api/banners', banner_list, name='banner-api'),
    path('api/allcategories', category_list, name='all-category-api'),
    path('api/allproducts', product_list, name='all-products-api'),
    path('api/productsbycategory/<int:id>', products_by_category, name='products_by_category-api'),
    path('api/productsbyid/<int:id>', products_by_id, name='product-detail-api'),
    path('api/productsbyuser', products_by_user, name='user-products-api'),
    path('api/updateordeleteuserproduct/<int:id>', update_user_product, name='product-update-api'),
    path('api/addproduct', add_product, name='add-product-api'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}, name='serve-photos'),
    # urls for Dukan
    path('api/alldukanproducts', all_dukan_products, name='dukan-product-api'),
    path('api/dukanproductbyid/<int:id>', dukan_product_by_id, name='single-dukan-product')
]
