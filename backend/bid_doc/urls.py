from django.urls import path,include
from bid_doc import views 


urlpatterns = [
    path('biddoc/',views.biddoc_list.as_view()),          
]