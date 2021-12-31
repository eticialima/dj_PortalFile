from django.urls import path
from perfil.likes import ProfileAddLike
from perfil.views import EditPhotoProfile, ProfileView, ProfileEditView

app_name = "profile"
urlpatterns = [
    path('edit-profile', ProfileEditView.as_view(), name="edit-profile"), 
    path('<slug:username>', ProfileView.as_view(), name="user-profile"),  
    path('perfil/<int:pk>/like', ProfileAddLike.as_view(), name='like-profile'),  
    path('<int:pk>/photo/', EditPhotoProfile.as_view(), name='photo-profile'),
]
 