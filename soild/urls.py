"""
soild URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from paypal.standard.ipn import urls
from django.contrib import admin
from django.urls import path , include
from web.views import views as web_views
from web.views.user_views import register , log_out ,login_page
from web.views.paypal_view import PaypalCancelView , PaypalReturnView
from django.conf.urls.static import static
from soild import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',web_views.index,name="index"),
    ######################################################
    path('login/',login_page,name="login"),
    path('logout/',log_out,name="logot"),
    path('register/',register,name="register"),
    #######################################################
    path('upload/',web_views.upload,name="upload"),
    path('list/',web_views.list_uploads,name="list"),
    path('details/<int:oid>', web_views.view_download,name='view_download'),
    path('download/<str:filename>', web_views.download_file,name='download_file'),
    #######################################################
    path('paypal/', include("paypal.standard.ipn.urls")),
    path('payment/',web_views.upgrade,name="payment"),
    path('paypal-cancel/', PaypalCancelView.as_view(), name='paypal-cancel'),
    path('paypal-return/', PaypalReturnView.as_view(), name='paypal-return'),
    #######################################################
]+static('s/',document_root=settings.MEDIA_ROOT)
