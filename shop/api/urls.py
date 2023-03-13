from django.urls import re_path, path
from .views import CategoryListView, DiscountListView, ProductItemListView, \
    ProducerListView, PromocodeListView, CategoryProductsView,\
    ProducerProductView, DiscountProductsView, RegistrationView, ActivateAccountView, \
    LoginView, BasketView, CreateOrderView, SingleProductItemView, GetStatisticView

urlpatterns = [
    re_path(r'^categories-all', CategoryListView.as_view(), name='categories-all'),
    re_path(r'^discounts-all', DiscountListView.as_view(), name='discounts-all'),
    re_path(r'^promocodes-all', PromocodeListView.as_view(), name='promocodes-all'),
    re_path(r'^products-all', ProductItemListView.as_view(), name='products-all'),
    re_path(r'^producers-all', ProducerListView.as_view(), name='producers-all'),
    path('category/<int:cat_id>/', CategoryProductsView.as_view()),
    path('producers/<int:producer_id>/', ProducerProductView.as_view()),
    path('discounts/<int:discount_id>/', DiscountProductsView.as_view()),
    path('product/<int:product_id>/', SingleProductItemView.as_view()),
    re_path(r'^register/', RegistrationView.as_view()),
    path('activate/<slug:uidb64>/<slug:token>/', ActivateAccountView.as_view(), name='activate'),
    re_path(r'^login/', LoginView.as_view()),
    re_path(r'^basket/', BasketView.as_view()),
    re_path(r'^create-order/', CreateOrderView.as_view()),
    re_path(r'^get-statistic/', GetStatisticView.as_view()),
]
