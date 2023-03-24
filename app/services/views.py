from django.shortcuts import render
from rest_framework import generics

from .serializers import SubscriptionSerializer
from .models import Subscription
# Create your views here.

class SubscriptionView(generics.ListAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

