from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Feed,SavedURL


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
         model = Feed
         fields = ["id","name","feed","Category"]

class FeedSubscriber(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ["id"]
        read_only_field = ["name","feed","Category"]

class URLSerializers(serializers.ModelSerializer):
    class Meta:
         model = SavedURL
         fields = ["id","url"]

class URLRemoveSerializers(serializers.ModelSerializer):
    class Meta:
         model = SavedURL
         fields = ["id"]
         read_only_field = ["url"]