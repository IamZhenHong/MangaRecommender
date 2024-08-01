from django.shortcuts import render
import requests
from .services.prediction import predict
import csv
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .serializers import RecommendationSerializer
import json

def convert_single_to_double_quotes(image_data_str):
  """Converts single quotes to double quotes in the image data string.

  Args:
    image_data_str: The image data string containing single quotes.

  Returns:
    The image data string with double quotes.
  """

  return image_data_str.replace("'", '"')


class GetRecommendationsView(APIView):
  def post(self, request):
    title = request.data.get('manga_title')
    if not title:
      return Response({'error': 'Missing manga_title in request body'}, status=status.HTTP_400_BAD_REQUEST)

    # Call the predict function
    recommendations_df = predict(title)

    # Error handling (optional): handle potential errors from predict
    if recommendations_df is None:
      return Response({'error': 'Error generating recommendations'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Extract titles and image URLs
    recommendations = recommendations_df[['title', 'images']].to_dict('records')

    # Extract image_url directly during conversion (if 'jpg' key exists)
    for rec in recommendations:
        image_data_str = rec['images']
        image_data_str = convert_single_to_double_quotes(image_data_str)
        print(image_data_str)
        image_data = json.loads(image_data_str)
        image_url = image_data['jpg']['image_url']
        rec['image_url'] = image_url
        print(image_url)
    # Serialize data (if using a serializer)
    serializer = RecommendationSerializer(recommendations, many=True)
    serialized_data = serializer.data

    print(serialized_data)

    return Response(serialized_data)