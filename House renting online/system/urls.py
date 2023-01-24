from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),

    url(r'^houselist/$', views.house_list, name = "house_list"),
    url(r'^createOrder/$', views.order_created, name = "order_create"),

    url(r'^(?P<id>\d+)/edit/$', views.house_update, name = "house_edit"),


    url(r'^(?P<id>\d+)/$', views.house_detail, name = "house_detail"),
    url(r'^detail/(?P<id>\d+)/$', views.order_detail, name = "order_detail"),

    url(r'^(?P<id>\d+)/delete/$', views.house_delete, name = "house_delete"),
    url(r'^(?P<id>\d+)/deleteOrder/$', views.order_delete, name = "order_delete"),
    url(r'^contact/$', views.contact, name = "contact"),
    url(r'^newhouse/$', views.newhouse, name = "newhouse"),
    url(r'^(?P<id>\d+)/like/$', views.like_update, name = "like"),
    url(r'^popularhouse/$', views.popular_house, name = "popularhouse"),
    url(r'^payment_with_express/$', views.payment_with_express, name = "payment_with_express"),
    url(r'^payment_with_cart/$', views.payment_with_cart, name = "payment_with_cart"),
    url(r'^success/$', views.success, name = "success"),
    url(r'^cancel/$', views.cancel, name = "cancel"),
    url(r'^ipn/$', views.ipn, name = "ipn"),
    url(r'^noweasy/$', views.noweasy, name = "noweasy"),
     url(r'^password_reset/', auth_views.PasswordResetView.as_view(), name="password_reset")

]
