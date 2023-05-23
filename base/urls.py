from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('login/', views.loginPage, name ="login"),
    path('logout/', views.logoutUser, name ="logout"),
    path('register/', views.registerPage, name ="register"),
    path('infos/', views.infos, name ="infos"),


    path('', views.home, name='home' ),
    path('service/<str:pk>/', views.service, name='service'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),


    path('create-service/', views.createService, name = "create-service"),
    path('update-service/<str:pk>/', views.updateService, name = "update-service"),
    path('delete-service/<str:pk>/', views.deleteService, name = "delete-service"),
    path('map_view/', views.map_view, name='map_view'),
    path('service/<str:pk>/message/', views.messagerie, name='message'),
     path('service/<int:pk>/map/', views.service_map_view, name='service_map_view')
]

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)