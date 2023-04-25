from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:num>', views.calc_tax, name="calc_rate"),
    path('taxrate/', views.tax_rate, name='tax_rate'),
]