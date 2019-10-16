"""CarApplication URL Configuration

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
from django.contrib import admin
from django.urls import path

from car_sales import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('sale_record/', views.SaleRecord.as_view(), name='sale_records'),
    path('customer/', views.CustomerRecord.as_view(), name='customer'),
    path('update_sale_record/', views.UpdateSaleRecord.as_view(), name='update_record'),
    path('delete_record/', views.DeleteSaleRecord.as_view(), name='delete_record'),
    path('get_graph_records/', views.GraphRecords.as_view(), name='delete_record'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
