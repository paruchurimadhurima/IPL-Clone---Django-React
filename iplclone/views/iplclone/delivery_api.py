from rest_framework import permissions
from iplclone.serializers.delivery_serializer import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class DeliveriesList(APIView):
    """
    List all deliveries, or create a new delivery.
    """
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        deliveries = Delivery.objects.all()
        serializer =DeliverySerializer(deliveries, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DeliverySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeliveryDetail(APIView):
    """
    Retrieve, update or delete a delivery instance.
    """
    permission_classes = (permissions.AllowAny,)

    def get_object(self, pk):
        try:
            return Delivery.objects.filter(match_id=pk)
        except Delivery.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        delivery = self.get_object(pk)
        serializer = DeliverySerializer(delivery, many=True)
        return Response(serializer.data)

    def put(self, request, pk, dk, format=None):
        delivery = self.get_object(pk).filter(id=dk)
        serializer = DeliverySerializer(delivery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, dk, format=None):
        snippet = self.get_object(pk).filter(id=dk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


