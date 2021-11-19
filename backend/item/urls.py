from django.urls import path,include
from item import views
urlpatterns = [    
    path('itemlist/',views.itemlist.as_view()),    
]