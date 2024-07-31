from django.shortcuts import render
import requests
from .services.prediction import predict
# Create your views here.



def get_recommendations(request):
    if request.method == "POST":
        # Get the text from the form
        title = request.POST.get("manga_title")
        # Call the predict function
        print("works fine")
        recommendations_df = predict(title)
        # Extract titles from the DataFrame
        print("here")
        recommendations = recommendations_df['title'].tolist()

        return render(request, "ml_app/recommendations.html", {"recommendations": recommendations})
    return render(request, "ml_app/get_recommendations.html")