from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('new-arrival/', views.new_arrival, name="new-arrival"),
    path('get-products/<product_category>', views.get_products, name="getProducts"),
    path('product/<product_id>/', views.product_detail)
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)