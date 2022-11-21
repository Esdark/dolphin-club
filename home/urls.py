from django.urls import path
from .views import ProductsView,HomePageView,GalleryPageView,CollectionView,ProductListView,ProductInfoView,ContactPageView,AboutPageView
app_name='home'
urlpatterns = [
    path('', HomePageView.as_view(),name="home"),
    path('products/', ProductsView.as_view(),name="products"),
    path('gallery/', GalleryPageView.as_view(),name="gallery"),
    path('collection/', CollectionView.as_view(),name="collection"),
    path('product-list/', ProductListView.as_view(),name="product-list"),
    path('product-info/', ProductInfoView.as_view(),name="product-info"),
    path('contact-us/', ContactPageView.as_view(),name="contact-us"),
    path('about/', AboutPageView.as_view(),name="about"),
]