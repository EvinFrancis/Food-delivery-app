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
]
