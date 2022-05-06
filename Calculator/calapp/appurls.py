from django.urls import path
from . import views

urlpatterns = [
    path('value/', views.new),
    path('value1/<int:num1>/<int:num2>', views.add),
    path('value2/<int:num1>/<int:num2>', views.diff),
    path('value3/<int:num1>/<int:num2>', views.prod),
    path('value4/<int:num1>/<int:num2>', views.quo),
    path('value5/<int:num1>', views.calculate),
    path('hey/', views.message),
    path('',views.arithmentic,name='arith')
]
