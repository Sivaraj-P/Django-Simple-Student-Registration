from django.urls import path
from . import views

urlpatterns=[
    path('',views.add,name='add'),
    path('list/',views.list,name='list'),
    path('delete/',views.delete,name='delete')
]