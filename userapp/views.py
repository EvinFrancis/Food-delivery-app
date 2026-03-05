from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from mainapp.models import *
from userapp.models import *
from decimal import Decimal
from django.contrib import messages
import razorpay



# Create your views here.


#user dsahboard
def user_dashboard(request):
    uname = request.session.get('username')
    cart_total=0

    if uname:
    
            cart_total=cartdb.objects.filter(username=uname).count()
    restaurant=restaurantDb.objects.all()
    dishes=dishesDb.objects.all()
    latest_rest=restaurantDb.objects.first()
    second_latest = restaurantDb.objects.order_by('-id')[1]

    return render(request,'index.html',{'restaurant':restaurant,
                                        'dishes':dishes,
                                        'latest_rest':latest_rest,
                                        'second_latest':second_latest,
                                        "cart_total":cart_total})  

#contact us page
def contact_us_page(request):
    uname = request.session.get('username')
    cart_total=0

    if uname:
    
            cart_total=cartdb.objects.filter(username=uname).count()
    return render(request,'contact.html',{"cart_total":cart_total}) 
 
#dishes page
def dishes_page(request):
    uname = request.session.get('username')
    cart_total=0

    if uname:
    
            cart_total=cartdb.objects.filter(username=uname).count()
    dishes=dishesDb.objects.all()
    return render(request,'dishes.html',{'dishes':dishes,"cart_total":cart_total})
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
            




#sevice page
def service_page(request):
    service=serviceDb.objects.all()
    return render (request,"service.html",{"service":service})

 #single restaurant page
def single_restaurant_page(request,rst_name):
    uname = request.session.get('username')
    cart_total=0

    if uname:
    
            cart_total=cartdb.objects.filter(username=uname).count()
    dishes=dishesDb.objects.filter(restaurant=rst_name)

    
    return render(request,'single_rest.html',{"dishes":dishes,
                                              "cart_total":cart_total})

def single_dish_page(request,dish_id):
    uname = request.session.get('username')
    cart_total=0

    if uname:
    
            cart_total=cartdb.objects.filter(username=uname).count()
    dish=dishesDb.objects.get(id=dish_id)
    return render(request,'single_dishes.html',{"dish":dish,
                                                "cart_total":cart_total})

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


#view cart page

def view_cart(request):
    uname = request.session.get('username')
    cart_total=0

    if uname:
    
            cart_total=cartdb.objects.filter(username=uname).count()
    username = request.session.get('username')

    if not username:
       return redirect(sign_in_page)
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
                                            "grand_total":grand_total,"cart_total":cart_total
                                            })


def checkout(request):
    username = request.session.get('username')

    if not username:
       return redirect(sign_in_page)

    data1 = cartdb.objects.filter(username=username)


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
    return render(request,'check_out.html',{"data":data1,
                                            "subtotal":subtotal,
                                            "delivery":delivery,
                                            "grand_total":grand_total
                                            })

#delet cart
def delete_cart(request,cart_id):
    
    cartdb.objects.filter(id=cart_id).delete()
    messages.error(request,"Product deleted successfully")
    return redirect(view_cart)


#save chcout page
def checkout_save(request):
     if request.method=="POST":
        firstname=request.POST.get("first_name")
        lastname=request.POST.get("last_name") 
        country=request.POST.get("country")
        address=request.POST.get("address")
        city=request.POST.get("city")
        state=request.POST.get("state")
        pincode=request.POST.get("pincode")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        totalprice=request.POST.get("grand_total")
        obj=chechoutdb(firstname=firstname,lastname=lastname,country=country,address=address,city=city,pin=pincode,email=email,mobile=phone,totalprice=totalprice)
        obj.save()
        return redirect(paytment_page)
     
def  paytment_page(request):
    username = request.session.get('username')

    if not username:
            return redirect(sign_in_page)


    
    uname = request.session.get('username')
    cart_total=0
    if uname:
    
            cart_total=cartdb.objects.filter(username=uname).count()
    customer=chechoutdb.objects.order_by('-id').first()
    payy=customer.totalprice
    amount=int(payy*100)
    payy_str=str(amount)
    
    if request.method=="POST":
         order_currency="INR"
         client=razorpay.Client(auth=("rzp_test_0ib0jPwwZ7I1lT", "VjHNO5zKeKxz8PYe7VnzwxMR"))
         payment=client.order.create({'amount':amount,'currency':order_currency})
         
    
    return render(request,'paymentpage.html',{"cart_total":cart_total,
         "payy_str":payy_str
    })

#update_quantity_cart acrtion form
def update_quantity_cart(request,cart_id):
     if request.method=="POST":
        action=request.POST.get("action")
        
        cart=cartdb.objects.get(id=cart_id)
        if action=="plus":
             cart.quantity+=1
        elif action=="minus":
             if cart.quantity>1:
                 cart.quantity-=1
        
        cart.total_price=cart.quantity*cart.price
        cart.save()    
        return redirect(view_cart)
     
          
