from unicodedata import name
from django.urls import path
from . import views

app_name='my_app'

urlpatterns=[
    #path('simple/',views.simple_view, name='index'),
    #path('finance/', views.finance_view)
    # path('<str:topic>/', views.news_view, name='topic-page'),
    #path('<int:num1>/<int:num2>',views.add_view)
    # path('<int:num>',views.num_page_view)
    path('example/',views.example_view, name='example'),
    path('variable/', views.variable_view, name='variable'),
    path('patients/',views.list_patients),
    path('list/', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete')
]
