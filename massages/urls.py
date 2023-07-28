from django.urls import path, include
from . import views
from .routers import router


urlpatterns = [
    path('', include(router.urls)),
    path('get_massages/', views.all_massages, name="get-massages"),
    path('massage_unread/', views.massage_unread, name="get-unread-massages"),
    path('read_massage/', views.read_massage, name="read-massage"),
    path('delete_massage/<int:pk>/', views.delete_massage, name="delete-massage"),
    path('add_massage/', views.create_massage, name="add-massagee"),
    path('api-auth/', include('rest_framework.urls')),
]
