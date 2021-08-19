from django.urls import path
from . import views

app_name = "leagues"
urlpatterns = [
	path('', views.index, name="index"),
	path('lvl1', views.lvl1, name="lvl1"),
	path('lvl2', views.lvl2, name="lvl2"),
	path('initialize', views.make_data, name="make_data"),
]
