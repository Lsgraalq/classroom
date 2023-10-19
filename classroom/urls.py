from django.urls import path 
from .views import BoardMessageCreateView, index , by_subject

urlpatterns = [ 
    path('add/', BoardMessageCreateView.as_view(), name = 'add'),
    path('<int:subject_id>/', by_subject,name='by_subject'),
    path('', index, name='index'),
    
]