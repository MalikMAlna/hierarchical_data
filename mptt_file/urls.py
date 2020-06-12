from django.urls import path
from mptt_file import views

urlpatterns = [
    path('',
         views.index,
         name='homepage'
         ),
]
