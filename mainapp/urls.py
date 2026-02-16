from django.urls import path
from mainapp import views
urlpatterns = [
    path('dashboard/',views.dashboard, name='dashboard'),
    path('admin_login/',views.admin_login_page,name='admin_login_page'),
    path('admin_login_submit/',views.admin_login,name='admin_login'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),
    path('add_food_type_page/',views.add_food_type_page,name='add_food_type_page'),
    path('save_food_type/',views.save_food_type,name='save_food_type'),
    path('view_food_types/',views.view_food_types,name='view_food_types'),
    path('delete_food_type/<int:food_id>/',views.delete_food_type,name='delete_food_type'),
    path('edit_food_type/<int:food_id>/',views.edit_food_type,name='edit_food_type'),
    path('update_food_type/<int:food_id>/',views.update_food_type,name='update_food_type'),
    path('add_restaurant_page/',views.add_restaurant_page,name='add_restaurant_page'),
    path('save_restaurant/',views.save_restaurant,name='save_restaurant'),
    path('view_restaurants/',views.view_restaurants,name='view_restaurants'),
    path('delete_restaurant/<int:rest_id>/',views.delete_restaurant,name='delete_restaurant'),
    path('edit_restaurant/<int:rest_id>/',views.edit_restaurant,name='edit_restaurant'),
    path('update_restaurant/<int:rest_id>/',views.update_restaurant,name='update_restaurant'),
    path('add_dishes_page/',views.add_dishes_page,name='add_dishes_page'),
    path('save_dishes/',views.save_dishes,name='save_dishes'),
    path('view_dishes/',views.view_dishes,name='view_dishes'), 
    path('delete_dish/<int:dish_id>/',views.delete_dish,name='delete_dish'), 
    path('add_service_page/',views.add_service_page,name='add_service_page'), 
    path('save_service/',views.save_service,name='save_service'),
    path('view_service/',views.view_service,name='view_service'),
    path('contact_us_page/',views.contact_us_page,name='contact_us_page'),
    path('edit_service_page/<int:service_id>/',views.edit_service_page,name='edit_service_page'),
    path('update_service/<int:service_id>/',views.update_service,name='update_service'),
    path('update_service/<int:service_id>/',views.update_service,name='update_service'),
    path('delete_service/<int:service_id>/',views.delete_service,name='delete_service'),
 

    
  

]
