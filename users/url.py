from django.urls import path  # Helper used to declare URL routes.
from . import views  # Import this app's API view functions.

urlpatterns = [
    # GET lists users; POST creates a user, optionally with a profile.
    path('users/', views.users_list, name='users-list'),
    # GET, PUT, or DELETE applies to a user identified by its integer ID.
    path('<int:pk>/', views.user_detail, name='user-detail'),
]
