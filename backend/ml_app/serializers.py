from rest_framework import serializers

class RecommendationSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    image_url = serializers.URLField()
    score = serializers.DecimalField(max_digits = 10, decimal_places = 2)