from django.conf.urls import url

# Import views
from .views import (
    IndexView,
    CatagoryList,
    CatagoryDetail,
    ProductList,
    ProductDetail,
)

# App namespace
app_name = 'supermarket'

# URL Maps
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^catagories/$', CatagoryList.as_view(), name='catagory-list'),
    url(r'^catagory/(?P<pk>[0-9]+)/$', CatagoryDetail.as_view(), name='catagory-detail'),
    url(r'^products/$', ProductList.as_view(), name='product-list'),
    url(r'^product/(?P<pk>[0-9]+)/$', ProductDetail.as_view(), name='product-detail'),
]