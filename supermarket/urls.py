from django.conf.urls import url

# Import views
from .views import (
    CatagoryList,
    CatagoryDetail,
    ProductList,
    ProductDetail,
)

app_name = 'supermarket'

# URL Maps
urlpatterns = [
    url(r'^catagories/$', CatagoryList.as_view(), name='catagory-list'),
    url(r'^catagory/(?P<pk>[0-9]+)/$', CatagoryDetail.as_view(), name='catagory-detail'),
    url(r'^products/$', ProductList.as_view(), name='product-list'),
    url(r'^product/(?P<pk>[0-9]+)/$', ProductDetail.as_view(), name='product-detail'),
]