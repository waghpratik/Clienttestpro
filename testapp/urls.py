from django.urls import path
from . import views


urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('register/',views.register.as_view(),name='register'),
    path('dashboard/',views.dashboard.as_view(),name='dashboard'),
    
    # path('clients/',views.clients.as_view(),name='client'),
    # path('add_pro/',views.add_pro.as_view(),name='add_pro'),
    
    # path('blog_delete/<int:id>',views.blog_delete.as_view(), name="blog_delete"),

]