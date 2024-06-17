from django.contrib import admin
from django.urls import path
from .views import (
    student_list,
    student_create,
    student_edit,
    student_delete,
    student_detail
)

urlpatterns = [
    path('',student_list, name='student_list'),
    path('student_create',student_create,name='student_create'),
    path('student_edit/<int:pk>',student_edit,name='student_edit'),
    path('student_delete/<int:pk>',student_delete,name='student_delete'),
    path('student_detail/<int:pk>',student_detail,name='student_detail')
]