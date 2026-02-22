from django.urls import path
from userapp import views

urlpatterns=[
    path('user_dashboard/',views.user_dashboard,name='user_dashboard'),
    path('sign_in_page/',views.sign_in_page,name='sign_in_page'),
    path('signUp_page/',views.signUp_page,name='signUp_page'),
    path('save_user/',views.save_user,name='save_user'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('view_cart/',views.view_cart,name='view_cart'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('save_contact/',views.save_contact,name='save_contact'),
    path('service_page/',views.service_page,name='service_page'),
    path('single_restaurant_page/<rst_name>/',views.single_restaurant_page,name='single_restaurant_page'),
    path('single_dish_page/<int:dish_id>/',views.single_dish_page,name='single_dish_page'),

]