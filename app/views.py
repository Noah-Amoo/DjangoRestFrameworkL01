from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Coupon
from .serializers import CouponSerializer

class CouponAPIView(APIView):
    def get(self, request):
        coupons = Coupon.objects.all()
        serializer = CouponSerializer(coupons, many=True)
        return Response({"coupons": serializer.data})
    
    def post(self, request):
        serializer = CouponSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)