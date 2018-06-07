from .models import Product, CompanyIntro, HomeBanner, SuccessCase
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'desc', 'pic')

class CompanyIntroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CompanyIntro
        fields = ('desc', 'pic1', 'pic2')

class HomeBannerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HomeBanner
        fields = ('pic1')

class SuccessCaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SuccessCase
        fields = ('title', 'desc', 'pic')