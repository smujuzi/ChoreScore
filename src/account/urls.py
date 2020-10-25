from django.urls import path
from .import views


from account.views import (


	register,
	logout,
	home_view,

)

urlpatterns = [
	
	
	
	path('register/', views.register, name="register"),
	path('login_view/', views.login_view, name="login_view"),
	path('logout/', views.logout_view, name="logout"),
	path('home/', views.home_view, name="home_view"),

	


]