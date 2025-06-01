from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('coupons/', views.CouponAPIView.as_view()),
]
