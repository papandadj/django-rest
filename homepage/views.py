from django.shortcuts import render
from .models import Product, CompanyIntro, HomeBanner, SuccessCase
from .serializers import ProductSerializer, CompanyIntroSerializer, HomeBannerSerializer, SuccessCaseSerializer
from rest_framework import generics

# Create your views here.

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CompanyIntroList(generics.ListCreateAPIView):
    queryset = CompanyIntro.objects.all()
    serializer_class = CompanyIntroSerializer


class CompanyIntroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyIntro.objects.all()
    serializer_class = CompanyIntroSerializer

class HomeBannerList(generics.ListCreateAPIView):
    queryset = HomeBanner.objects.all()
    serializer_class = HomeBannerSerializer


class HomeBannerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HomeBanner.objects.all()
    serializer_class = HomeBannerSerializer

class SuccessCaseList(generics.ListCreateAPIView):
    queryset = SuccessCase.objects.all()
    serializer_class = SuccessCaseSerializer


class SuccessCaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SuccessCase.objects.all()
    serializer_class = SuccessCaseSerializer