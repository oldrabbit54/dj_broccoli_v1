from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home-page'),
    path('gallery/', include('gallery.urls')),
    path('thoughts/', include('thoughts.urls')),
    path('events/', include('events.urls')),
    path('register', views.RegisterUserView.as_view(),name='register'),
    path('login', views.LoginUserView.as_view(),name='user-login'),
    path('vk_auth', views.VKAuth, name='vk-login'),
    path('vk_thru_auth', views.VK_through_auth),
    path('help', views.HelpPageView.as_view(), name='help-page'),
    path('logout', views.log_user_out, name='user-logout'),
    path('send_email', views.EmailSendView.as_view(), name='send-email-test'),
    path('activate/<str:uidb64>/<str:token>/', views.activate, name='activate'),
    path('my_profile/', include('my_profile.urls'))
]
