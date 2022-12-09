from rest_framework import serializers
from listings.models import Listing,Poi
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point

class ListingSerializer(serializers.ModelSerializer):
    seller_username = serializers.SerializerMethodField()
    seller_agency_name = serializers.SerializerMethodField()
    listing_pois_within_10km = serializers.SerializerMethodField()
    # listing_pois = serializers.SerializerMethodField()
    """ def get_listing_pois(self,obj):
        query = Poi.objects.all()
        query_serialized = PoiSerializer(query,many = True)
        return query_serialized.data """

    def get_listing_pois_within_10km(self,obj):
        listing_location = Point(obj.latitude,obj.longitude,srid=4326)
        query = Poi.objects.filter(location__distance_lte=(listing_location,D(km=10)))
        query_serialized = PoiSerializer(query, many = True)
        return query_serialized.data 

    def get_seller_username(self, obj):
        return obj.seller.username

    def get_seller_agency_name(self, obj):
        return obj.seller.profile.agency_name    
    class Meta:
        model = Listing
        fields = '__all__'

class PoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poi
        fields = '__all__'
