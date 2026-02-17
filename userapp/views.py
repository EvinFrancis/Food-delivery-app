from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from mainapp.models import *
from userapp.models import *




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
def view_cart(request):
    return render(request,'cart_page.html')


