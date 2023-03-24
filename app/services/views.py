from django.shortcuts import render
from django.db.models import Prefetch

from rest_framework import generics

from .serializers import SubscriptionSerializer
from .models import Subscription
from clients.models import Client
# Create your views here.

class SubscriptionView(generics.ListAPIView):
    queryset = Subscription.objects.all().prefetch_related(
        Prefetch('client',queryset=Client.objects.all().select_related('user').only('company_name',
                                                             'user__email'))
    )
    serializer_class = SubscriptionSerializer

