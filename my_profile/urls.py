from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProfileView.as_view(), name='my_profile'),
    path('edit', views.ProfileEditView.as_view(), name='my_profile_edit')
]
