from django.urls import path

from catalog.views import CategoryListView, ProductListView, ProductDetailView, CategoryDetailView, OrderCreateView

urlpatterns = [
    path("", CategoryListView.as_view(), name="category-list"),
    path("categorys/<int:pk>", CategoryDetailView.as_view(), name="category-detail"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("orders/", OrderCreateView.as_view(), name="order-create"),
    
]


app_name = "catalog"