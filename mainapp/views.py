from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from mainapp.models import *

# Create your views here.
#dashboard
def dashboard(request):
    return render(request, 'dashboard.html')
#admin login page
def admin_login_page(request):
    return render(request,'admin_login.html')

#admin login
def admin_login(request):
    if request.method=='POST':#check request method
        username1=request.POST.get('username')
        password1=request.POST.get('password')
        if User.objects.filter(username__contains=username1).exists(): #check user exist or not

            user=authenticate(username=username1,password=password1) #authinticate user

            #session for the user.

            if user is not None:#check password
                login(request,user)
                request.session['username']=username1 #username as User admin
                request.session['password']=password1 #password as password in User admin
                return redirect(dashboard)#redirect to dashboard
            else:
                print("Invalid password") #invalid password
                return redirect(admin_login_page)
        else:#user does not exist
            print("User does not exist")
            return redirect(admin_login_page) #redirect to login page


#admin logout
def admin_logout(request):
    #delete session
    del request.session['username']
    del request.session['password']
    return redirect(admin_login_page) #redirect to login page


#add food type
def add_food_type_page(request):
    return render(request,'add_foodpage.html')
 #save food type        
def save_food_type(request):
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        foodimage=request.FILES.get('foodimage')
        foodtype=FoodType(name=name,description=description,foodimage=foodimage)
        foodtype.save()
        return redirect(add_food_type_page)
 #view food types   
def view_food_types(request):
    foodtypes=FoodType.objects.all()
    return render(request,'view_food_type.html',{'foodtypes':foodtypes})
#delete food type
def delete_food_type(request,food_id):
    foodtype=FoodType.objects.get(id=food_id)
    foodtype.delete()
    return redirect(view_food_types)


#edit food type
def edit_food_type(request,food_id):
    foodtype=FoodType.objects.get(id=food_id)
    return render(request,'edit_food_type.html',{'foodtype':foodtype})
#update food type
def update_food_type(request,food_id):
    if request.method=='POST':
        
        foodname=request.POST.get('name')
        description=request.POST.get('description')
        if  request.FILES.get('foodimage') :
            foodimage=request.FILES.get('foodimage')
        else:
            foodimage=FoodType.objects.get(id=food_id).foodimage
        obj=FoodType.objects.filter(id=food_id).update(name=foodname,description=description,foodimage=foodimage)
        # no need to  obj.save()
        return redirect(view_food_types)
    

#add restaurant page
def add_restaurant_page(request):
    return render(request,'add_rest.html')

