from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.CustomUserList.as_view(), name="users"),
    path("users/customers/", views.CustomerList.as_view(), name="customers"),
    path("users/vendors/", views.VendorList.as_view(), name="vendors"),
    path("users/<str:user_id>/", views.CustomUserDetail.as_view(), name="user"),
    path("users/<str:user_id>/transactions/", views.UserTransactionList.as_view(), name="user_transactions"),
    path("users/<str:user_id>/vendors/", views.CustomerVendorList.as_view(), name="customer_vendor"),
    path("transactions/", views.TransactionList.as_view(), name="transactions"),
    path("transactions/<str:transaction_id>/", views.TransactionDetail.as_view(), name="transaction"),
]
