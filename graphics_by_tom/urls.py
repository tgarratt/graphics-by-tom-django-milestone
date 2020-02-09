"""graphics_by_tom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from home.views import get_home
from purchasable.views import get_purchasable
from about_me.views import get_about_me
from order_work.views import get_order_work
from unpurchasable.views import get_unpurchasable
from admin_orders.views import get_admin_orders

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_home, name='home'),
    url(r'^purchasable$', get_purchasable, name='purchasable'),
    url(r'^about_me$', get_about_me, name='about_me'),
    url(r'^order_work$', get_order_work, name='order_work'),
    url(r'^unpurchasable$', get_unpurchasable, name='unpurchasable'),
    url(r'^admin_orders$', get_admin_orders, name='admin_orders'),
]
