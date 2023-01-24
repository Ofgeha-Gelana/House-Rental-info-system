"""house_rental_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from system.views import admin_house_list, admin_msg, order_list, house_created, order_update, order_delete, msg_delete, newhouse
from accounts.views import (login_view, register_view, logout_view)
from payment.views import home, payment_with_cart, payment_with_express, success, cancel, ipn
from django.contrib.auth import views as auth_views
from system.views import  password_reset_request
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', admin_house_list, name='adminIndex'),
    url(r'^listOrder/$', order_list, name = "order_list"),
    url(r'^(?P<id>\d+)/editOrder/$', order_update, name = "order_edit"),
    url(r'^(?P<id>\d+)/deleteOrder/$', order_delete, name = "order_delete"),
    url(r'^create/$', house_created, name = "house_create"),
    url(r'^message/$', admin_msg, name='message'),
    url(r'^(?P<id>\d+)/deletemsg/$', msg_delete, name = "msg_delete"),
    url(r'^house/', include('system.urls')),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^register/', register_view, name='register'),
    url(r'^newhouse/$', newhouse, name = "newhouse"),

    url(r'^success/$', success, name = "success"),
    url(r'^cancel/$', cancel, name = "cancel"),
   # url(r'accounts/', include('django.contrib.auth.urls')),

    url(r'^reset_password/',
     auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
     name="reset_password"),

    url(r'^reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"), 
        name="password_reset_done"),

    url(r'^reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"), 
     name="password_reset_confirm"),

     url(r'^reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), 
        name="password_reset_complete"),
    # url(r'^$', include('payment.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)