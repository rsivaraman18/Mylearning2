
from django.urls import path
from . import views

urlpatterns = [
    path('greet/', views.greet),
    path('index/', views.index_page),
    path('index2/', views.index_page2),
    path('studentregister/', views.student_register),
    path('studentviewall/', views.Student_viewall ,name='viewallpage'),
    path('studentdelete/<int:id>/', views.Student_delete , name='StDelete'),
    path('studentupdate/<int:id>/', views.Student_Update, name='StUpdate'),
]
