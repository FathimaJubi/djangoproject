from django.core.mail import send_mail
from django.shortcuts import render,redirect
from app1.models import product_available,user_Model,cart_item,cartModel
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required

# def head(request):
#     return render(request,"home.html")

def registration(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        username=request.POST['usname']
        email=request.POST['names']
        # password=request.POST['password']
        address=request.POST['adress']
        birth=request.POST['age']
        mobile=request.POST['phone']
        gender=request.POST['gender']
        district=request.POST['district']
        
        
        
        if User.objects.filter(username=username).exists():
            print('username already exist')
            return render(request,'registration.html')
        else:
            password=request.POST['password']
            c_password=request.POST['cpassword']
            
            if password==c_password:
                if User.objects.filter(username=username):
                    return redirect('register')
                else:
                    
                    user1=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                    user1.save()
                    # print(firstname,lastname,username,email,password,address,birth,mobile,gender,district)
                    #log in the user
                    user1=authenticate(username=username,password=password)
                   
                    
                    
                    newuser=user_Model(user_birth=birth,user_address=address,user_number=mobile,user_gender=gender,user_district=district,user=user1)
                    newuser.save()
                    # print('success')
                    subject = 'Hello, django email'
                    message ='this is a test mail send from django'
                    from_email = 'fathima2336@gmail.com'
                    recipient_list = [user1.email]
                    send_mail(subject, message, from_email, recipient_list)
                    # return render(request,'home.html')
            
            if user1 is not None:
                login(request,user1)
                return redirect('list')
    else:
        return render(request,'registration.html')
    

def logins(request):
    # p=product_available.objects.all()
    # p.delete()
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['password']
        user2=authenticate(request,username=username,password=password)
        if user2 is not None:
            login(request,user2)
            products=product_available.objects.all()
            return render(request,'home.html',{'products':products})
        
        # print(username,password)
        # return render(request,'login2.html')
    else:
        return render(request,'loginpage.html')
    return render(request,'loginpage.html')

def userlogout(request):
    logout(request)
    return redirect('log')

def product_details(request):
    if request.method=='POST':
        p_name=request.POST['pname']
        p_price=request.POST['pprice']
        p_desc=request.POST['pdisc']
        p_image=request.FILES.get('image')
       
        new_product=product_available(pro_name=p_name,pro_price=p_price,pro_description=p_desc,pro_image=p_image)
        new_product.save()
        print('success')
       
        return render(request,'product.html')
    else:
         
         return render(request,'product.html')
     
@login_required(login_url='log')       
def product_list(request):
    products=product_available.objects.all()
    return render(request,'home.html',{'products':products})



def cart(request):
    current_user=request.user
    crt=cartModel.objects.get(user=current_user)
    cart_items=crt.items.all()
    return render(request,'cart.html',{'cart_items':cart_items})

def deletecart(request):
    current_user=request.user
    crt=cartModel.objects.get(user=current_user)
    
    crt.items.clear()
    crt.save()
    return redirect('items')

def remove(request,j):
    current_user=request.user
    user_cart=cartModel.objects.get(user=current_user)
    item=cart_item.objects.get(id=j)
    user_cart.items.remove(item)
    user_cart.save()
    return redirect('items')

def add_to_cart(request,i):
    current_user=request.user
    item=product_available.objects.get(id=i)
    qty=1
    price=item.pro_price
    try:
        user_cart=cartModel.objects.get(user=current_user)
        new_cart_item=cart_item(item=item,quantity=qty,price=price)
        new_cart_item.save()
        user_cart.items.add(new_cart_item)
        user_cart.save()
    except:
        user_cart=cartModel(user=current_user)
        user_cart.save()
        new_cart_item=cart_item(item=item,quantity=qty,price=price)
        new_cart_item.save()
        user_cart.items.add(new_cart_item)
        user_cart.save()
    return redirect('items')

 
# Create your views here.
