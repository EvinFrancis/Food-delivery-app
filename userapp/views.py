from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from mainapp.models import *
from userapp.models import *
from decimal import Decimal



# Create your views here.


#user dsahboard
def user_dashboard(request):
    restaurant=restaurantDb.objects.all()
    dishes=dishesDb.objects.all()
    latest_rest=restaurantDb.objects.first()
    return render(request,'index.html',{'restaurant':restaurant,
                                        'dishes':dishes,
                                        'latest_rest':latest_rest})  

#contact us page
def contact_us_page(request):
    return render(request,'contact.html') 
 
#dishes page
def dishes_page(request):
    dishes=dishesDb.objects.all()
    return render(request,'dishes.html',{'dishes':dishes})
#restaurant page
def restaurant_page(request):
    restaurant=restaurantDb.objects.all()
    return render(request,'restaurant.html',{'restaurant':restaurant})

#services page
def services_page(request):
    service=serviceDb.objects.all()
    return render(request,'services.html',{'service':service})




#contact us page
def contact_us(request):   
    return render(request,'contacts.html')

#savwe contact us data
def save_contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        subject=request.POST.get('subject')
        created_at=request.POST.get('created_at')
        obj=contactDb(name=name,email=email,message=message,subject=subject,created_at=created_at)
        obj.save()
        return redirect(contact_us)

def sign_in_page(request):
    return render(request,'sign_in.html')


def signUp_page(request):
    return render(request,'signUp.html')


#save user data
def save_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        obj=userDb(username=username,email=email,password=password)
        #check username and email already exist or not
        if userDb.objects.filter(username=username).exists():
            print("Username Already exists")
            return redirect(signUp_page)
        elif userDb.objects.filter(email=email).exists():
            print("Email Already exists")
            return redirect(signUp_page)
        else: 
           obj.save()
           return redirect(sign_in_page)

def user_login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        psw=request.POST.get('password')
        #check username and password exist or not
        if userDb.objects.filter(username=uname,password=psw).exists():
            request.session['username']=uname
            request.session['password']=psw
            return redirect(user_dashboard)
        else:
            print("Invalid username or password")
            return redirect(sign_in_page)
        
def user_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(user_dashboard)
            

#view cart page


#sevice page
def service_page(request):
    service=serviceDb.objects.all()
    return render (request,"service.html",{"service":service})

 #single restaurant page
def single_restaurant_page(request,rst_name):
    dishes=dishesDb.objects.filter(restaurant=rst_name)

    
    return render(request,'single_rest.html',{"dishes":dishes})

def single_dish_page(request,dish_id):
    dish=dishesDb.objects.get(id=dish_id)
    return render(request,'single_dishes.html',{"dish":dish})

def cart_saved(request):
    if request.method=='POST':
        username=request.session['username']
        dish_name=request.POST.get('dish_name')
        price=Decimal(request.POST.get('price'))
        quantity=request.POST.get('qty')
        total_price=Decimal(request.POST.get('total'))
        pro=dishesDb.objects.filter(name=dish_name).first()
        product_image=pro.dish_image if pro else None

        obj=cartdb(username=username,product_name=dish_name,price=price,quantity=quantity,total_price=total_price,product_image=product_image)
        obj.save()
        return redirect(view_cart)


def view_cart(request):
    data1=cartdb.objects.filter(username=request.session['username'])
    subtotal=0
    delivery=0
    grand_total=0
    for i in data1:
        subtotal+=i.total_price
        if subtotal>500:
            delivery=0
        else:
            delivery=50
        grand_total=subtotal+delivery   
    return render(request,'cart_page.html',{"data":data1,
                                            "subtotal":subtotal,
                                            "delivery":delivery,
                                            "grand_total":grand_total
                                            })


def checkout(request):
    return render(request,'check_out.html')