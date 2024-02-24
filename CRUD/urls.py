from django.urls import path
from .views import *
urlpatterns=[

    path('tv/',Todo_view),
    path('dv/',display,name='display_url'),
    path('uv/<int:pk>/',update_view,name='update_url'),
    path('dv/<int:pk>/',delete_view,name='delete_url'),
    #path('hv/',home_view,name='home_view')

]