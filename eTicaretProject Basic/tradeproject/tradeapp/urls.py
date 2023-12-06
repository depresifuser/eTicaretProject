from django.urls import path
from . import views

app_name = 'tradeapp'

urlpatterns = [
    path('',views.mainpage,name='mainpage'),
    path('clothes/',views.clothes,name='clothes'),
    path('sweater/',views.sweater,name='sweater'),
    path('tshirt/',views.tshirt,name='tshirt'),
    path('pants/',views.pants,name='pants'),
    path('shopbag/',views.shopbag,name='shopbag'),
    path('signup/',views.SignUpView.as_view(),name="signup")
]
