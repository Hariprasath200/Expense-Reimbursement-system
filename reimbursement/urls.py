from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name="Homepage"),
    path('Admin',views.Admin,name="Adminpage"),
    path('Manager',views.Manager, name="Managerpage"),
    path('Manager',views.update_status, name="manager_page"),
    path('Employee',views.Employee,name="Employeepage"),
    path('success', views.success_view, name='Successpage'),
    path('update_status', views.update_status, name='update_status'),
    path('admin_update_status', views.admin_update_status, name='admin_update_status'),
    

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)