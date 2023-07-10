from django.urls import path
from .views import MyTokenObtainPairView , UserList

urlpatterns = [
    path('token' , MyTokenObtainPairView.as_view() , name='token_obtain_pair'),
    path('' , UserList.as_view() , name='token_obtain_pair')
]
