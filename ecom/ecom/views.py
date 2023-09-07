from django.shortcuts import render
from products.models import Product
from django.http import JsonResponse, HttpResponse
import json
from django.core import serializers
from django.utils import timezone


# defining home view 
def home(request):
    return render(request, 'home.html')


def new_arrival(request):
    return render(request, 'new-arrival.html')


# Api creation at the end point domain.com/get_products/<type>
def get_products(request, product_category):
    if request.method == "GET":
        if product_category == "new-arrival":
            two_days_ago = timezone.now() - timezone.timedelta(days=2)
            print(two_days_ago)
            data = Product.objects.filter(pub_date__gte=two_days_ago)
            json_data = serializers.serialize('json', data)
            return JsonResponse(json_data, safe=False)
        else:
            data = Product.objects.filter(category=product_category)
            json_data = serializers.serialize('json', data)
            return JsonResponse(json_data, safe=False)


# Detail page of product url = domain.com/product/<id>
def product_detail(request, product_id):
    data = Product.objects.get(pk = product_id)
    return render(request, 'product_detail_page.html', {"data": data})


