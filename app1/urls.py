from django.urls import path
from .import views

urlpatterns =[
    # path('index',views.head,name='index'),
    path('reg',views.registration,name='register'),
    path('',views.logins,name='log'),
    path('product',views.product_details,name='product'),
    path('list',views.product_list,name='list'),
    path('items',views.cart,name='items'),
    path('cart/<int:i>',views.add_to_cart,name='cart'),
    path('remove',views.deletecart,name='remove'),
    path('rmv/<int:j>',views.remove,name='rmv'),
    path('userlogout',views.userlogout,name='userlogout')
    ]