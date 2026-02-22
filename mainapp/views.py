from urllib import request
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

#save restaurant
def save_restaurant(request):
    if request.method=='POST':
        name=request.POST.get('name')
        address=request.POST.get('address')
        contact_number=request.POST.get('contact_number')
        restaurant_image=request.FILES.get('restaurant_image')
        obj=restaurantDb(name=name,address=address,contact_number=contact_number,restaurant_image=restaurant_image)
        obj.save()
        return redirect(add_restaurant_page)
    #view restaurants``
def view_restaurants(request):
    restaurants=restaurantDb.objects.all()
    return render(request,'view_rest.html',{'restaurants':restaurants})


#delete restaurant
def delete_restaurant(request,rest_id): 
    restaurant=restaurantDb.objects.get(id=rest_id)
    restaurant.delete() 
    return redirect(view_restaurants)

#edit restaurant
def edit_restaurant(request,rest_id):
    restaurant=restaurantDb.objects.get(id=rest_id)
    
    return render(request,'edit_rest.html',{'restaurant':restaurant})

#update restaurant
def update_restaurant(request,rest_id):
    if request.method=="POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        contact_number=request.POST.get('contact_number')
        if request.FILES.get('restaurant_image'):
            restaurant_image=request.FILES.get('restaurant_image')
        else:
            restaurant_image=restaurantDb.objects.get(id=rest_id).restaurant_image
        obj=restaurantDb.objects.filter(id=rest_id).update(name=name,address=address,contact_number=contact_number,restaurant_image=restaurant_image)
        return redirect(view_restaurants)
    
# add new dishes page
def add_dishes_page(request):
    provide_foodtypes=FoodType.objects.all()
    provide_restaurants=restaurantDb.objects.all()
    return render(request,'add_dishes.html',
                  {
        'food_types':provide_foodtypes,
        'restaurants':provide_restaurants
    }
    )
# save new dishes
def save_dishes(request):
    if request.method=='POST':
        name=request.POST.get('name')
        description=request.POST.get('description')
        price=request.POST.get('price')
        food_type=request.POST.get('food_type')
        restaurant=request.POST.get('restaurant')
        dish_image=request.FILES.get('dish_image')
        veg_nonveg=request.POST.get('veg_nonveg')

        
        obj=dishesDb(name=name,description=description,price=price,food_type=food_type,restaurant=restaurant,dish_image=dish_image,veg_nonveg=veg_nonveg)
        obj.save()
        return redirect(add_dishes_page)

#view dishes
def view_dishes(request):
    dishes=dishesDb.objects.all()
    return render(request,'view_dishes.html',{'dishes':dishes})

#delete dish
def delete_dish(request,dish_id): 
    dish=dishesDb.objects.get(id=dish_id) 
    dish.delete()
    return redirect(view_dishes)

#edit dishes
def edit_dish(request,dish_id):
    dish=dishesDb.objects.get(id=dish_id)
    restaurant=restaurantDb.objects.all()
    foodType=FoodType.objects.all()
    return render(request,'edit_dishes.html',{'dish':dish,
                                              "FoodType":foodType,  
                                              "restaurant":restaurant})

#service page
def add_service_page(request):
    return render(request,'add_service.html')


#update dishes
def update_dish(request,dish_id):
    name=request.POST.get('name')
    description=request.POST.get('description')
    price=request.POST.get('price')
    food_type=request.POST.get('food_type')
    restaurant=request.POST.get('restaurant')

    if request.FILES.get('dish_image'): 
        dish_image=request.FILES.get('dish_image')
    else:
        dish_image=dishesDb.objects.get(id=dish_id).dish_image
    veg_nonveg=request.POST.get('veg_nonveg')
    obj=dishesDb.objects.filter(id=dish_id).update(name=name,description=description,price=price,food_type=food_type,restaurant=restaurant,dish_image=dish_image,veg_nonveg=veg_nonveg)
    return redirect(view_dishes)

#save service
def save_service(request):
    if request.method=='POST':
        ServiceName=request.POST.get('ServiceName')
        Description=request.POST.get('Description')
        ServiceImage=request.FILES.get('ServiceImage')
        obj=serviceDb(ServiceName=ServiceName,Description=Description,ServiceImage=ServiceImage)
        obj.save()
        return redirect(add_service_page)

#view service
def view_service(request):
    services=serviceDb.objects.all()
    return render(request,'view_service.html',{'services':services})

# def delete_service(request,service_id):
#     service=serviceDb.objects.get(id=service_id)
#     service.delete()
#     return redirect(view_service)


#edit service page
def edit_service_page(request,service_id):
    service=serviceDb.objects.get(id=service_id)
    return render(request,'edit_service.html',{'service':service})

#update service
def update_service(request,service_id):
    if request.method=="POST":
        service_name=request.POST.get('ServiceName')
        Description=request.POST.get('Description')
        if request.FILES.get('ServiceImage'):
            ServiceImage=request.FILES.get('ServiceImage')
#             🔹 One and only one object → get()
# 🔹 Zero or many objects → filter()
        else:
            ServiceImage=serviceDb.objects.get(id=service_id).ServiceImage
        obj=serviceDb.objects.filter(id=service_id).update(ServiceName=service_name,Description=Description,ServiceImage=ServiceImage)
        return redirect(view_service)

#delete service
def delete_service(request,service_id):
    service=serviceDb.objects.get(id=service_id)
    service.delete()
    return redirect(view_service)


#contact us page
def contact_us_page(request):
    contact=contactDb.objects.all()
    return render(request,'contact.html',{'contact':contact})
    



