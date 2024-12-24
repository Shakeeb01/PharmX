from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.Main,name='Main'),
    path('products',views.All_Products,name='All-Products'),
    path('create_product',views.creat_product,name='Creat-Product'),
    path('delete_product/<int:pk>/',views.delete_product,name='Delete-Product'),
    # Authentication Urls.
    path('register_user',views.register_user,name='Register-User'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)