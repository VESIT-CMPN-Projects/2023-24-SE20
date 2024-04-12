from django.shortcuts import render
from django.http import HttpResponse
import requests
from .forms import registration
from .models import user,UserInteraction
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required





@login_required
def index(request):
    username = request.user.username  # Assuming the username is needed
    url = "https://newsapi.org/v2/everything?q=global-sports&apiKey=b128b1dd24cd471e934182c7d3eeaf35"
    news = requests.get(url).json()

    a = news['articles']
    link = []
    disc = []
    title = []
    img = []

    if request.method == 'POST':
        fm = registration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            msg = fm.cleaned_data['message']
            reg = user(name=name, email=email, message=msg)
            reg.save()
    else:
        fm = registration()

    sorted_articles = sort_articles_based_on_user_interactions(request.user, a)

    for f in sorted_articles:
        link.append(f['url'])
        title.append(f['title'])
        disc.append(f['description'])
        img.append(f['urlToImage'])

    mylist = zip(title, disc, img, link)
    context = {'mylist': mylist, 'form': fm, 'user_name': username}
    return render(request, 'index.html', context)

def sort_articles_based_on_user_interactions(user, articles):
  sorted_articles = []
  for article in articles:
    interaction = UserInteraction.objects.filter(user=user, article_url=article['url']).first()
    if interaction:
      interaction.count += 1  # Update interaction count
      interaction.save()
      if interaction.count >= 2:
        sorted_articles.insert(0, article)
      else:
        sorted_articles.append(article)
    else:
      # Handle case where no interaction exists (create new interaction)
      sorted_articles.append(article)
  return sorted_articles


from django.http import JsonResponse
import requests
import json

def get_ipl_countries(request):
  """Fetches country data from CricAPI and returns a JSON response."""

  api_key = "61a0ed8e-2a0e-4c85-a06c-f1c830a050db"  # Replace with your CricAPI key
  offset = 0
  max_offset = 1
  country_data = []

  while offset < max_offset:
    url = f"https://api.cricapi.com/v1/countries?apikey={api_key}&offset={offset}"
    response = requests.get(url)

    if response.status_code != 200:
      return JsonResponse({"error": "Failed to retrieve data from CricAPI"}, status=500)

    data = json.loads(response.text)

    if data["status"] != "success":
      return JsonResponse({"error": f"API returned error: {data['status']}"})

    max_offset = data["info"]["totalRows"]
    offset += len(data["data"])
    country_data.extend(data["data"])

  return JsonResponse(country_data, safe=False)

from django.http import JsonResponse
import requests
import json

def fetch_from_offset(offset):
  """
  Fetches IPL series data from CricAPI for a given offset and returns it as a list.

  Args:
      offset: The offset value for pagination (starts from 0).

  Returns:
      A list containing the fetched IPL series data or an empty list if no data found.
  """

  api_key = "61a0ed8e-2a0e-4c85-a06c-f1c830a050db"  # Replace with your CricAPI key
  url = f"https://api.cricapi.com/v1/match_info?apikey={api_key}&offset={offset}&search=IPL"

  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for non-200 status codes
  except requests.exceptions.RequestException as e:
    print(f"Error fetching data from CricAPI: {e}")
    return []

  data = json.loads(response.text)

  if data["status"] != "success":
    print(f"API returned error: {data['status']}")
    return []

  series_data = data["data"]
  if not series_data:
    return []

  if offset >= data["info"]["totalRows"]:
    return series_data
  else:
    # Make recursive calls synchronously within the view (avoiding coroutines)
    next_data = fetch_from_offset(offset + 25)
    return series_data + next_data

def get_ipl_series(request):
  """
  View function to trigger IPL series data retrieval and return JSON response.

  Args:
      request: The Django HTTP request object.

  Returns:
      A Django JsonResponse containing the fetched IPL series data or an error message.
  """

  offset = 0
  series_data = fetch_from_offset(offset)

  if not series_data:
    return JsonResponse({"error": "No IPL series data found"}, status=404)

  return JsonResponse(series_data, safe=False)





def search(request):
    url = "https://newsapi.org/v2/everything?q=espn-sports&apiKey=b128b1dd24cd471e934182c7d3eeaf35"
    news = requests.get(url).json()

    a = news['articles']
    link = []
    disc = []
    title = []
    img = []

    if request.method == 'POST':
        fm = registration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            msg = fm.cleaned_data['message']
            reg = user(name=name, email=email, message=msg)
            reg.save()
    else:
        fm = registration()

    query = request.GET.get('query', '')  # Get the query parameter from request

    for i in range(len(a)):
        f = a[i]
        link.append(f['url'])
        title.append(f['title'])
        disc.append(f['description'])
        img.append(f['urlToImage'])

    mylist = zip(title, disc, img, link)

    if query:
        # Filter mylist based on query using list comprehension
        mylist = [item for item in mylist if query.lower() in item[0].lower()]

    context = {'mylist': mylist, 'form': fm}
    return render(request, 'search.html', context)







def fetch_news(request, category, api_url):
    news = requests.get(api_url).json()
    articles = news.get('articles', [])
    
    if request.method == 'POST':
        form = registration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            msg = form.cleaned_data['message']
            user = user(name=name, email=email, message=msg)
            user.save()
    else:
        form = registration()

    mylist = [(article['title'], article['description'], article['urlToImage'], article['url']) for article in articles]
    context = {'mylist': mylist, 'form': form}
    return render(request, 'result.html', context)

def cricket(request):
    url = "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=b128b1dd24cd471e934182c7d3eeaf35"
    return fetch_news(request, "cricket", url)

def football(request):
    url = "https://newsapi.org/v2/everything?q=football&apiKey=b128b1dd24cd471e934182c7d3eeaf35"
    return fetch_news(request, "football", url)

def baseball(request):
    url = "https://newsapi.org/v2/everything?q=baseball&apiKey=b128b1dd24cd471e934182c7d3eeaf35"
    return fetch_news(request, "baseball", url)

def tennis(request):
    url = "https://newsapi.org/v2/everything?q=tennis&apiKey=b128b1dd24cd471e934182c7d3eeaf35"
    return fetch_news(request, "tennis", url)

def golf(request):
    url = "https://newsapi.org/v2/everything?q=golf&apiKey=b128b1dd24cd471e934182c7d3eeaf35"
    return fetch_news(request, "golf", url)

def badminton(request):
    url = "https://newsapi.org/v2/everything?q=badminton&apiKey=b128b1dd24cd471e934182c7d3eeaf35"
    return fetch_news(request, "badminton", url)

def kabadii(request):
    url = "https://newsapi.org/v2/everything?q=kabaddi-india&apiKey=b128b1dd24cd471e934182c7d3eeaf35"
    return fetch_news(request, "kabadii", url)

def boxing(request):
    url = "https://newsapi.org/v2/everything?q=boxing&apiKey=b128b1dd24cd471e934182c7d3eeaf35"
    return fetch_news(request, "boxing", url)

def athletics(request):
    url = "https://newsapi.org/v2/everything?q=athletics&apiKey=b128b1dd24cd471e934182c7d3eeaf35"
    return fetch_news(request, "athletics", url)

def chess(request):
    url = "https://newsapi.org/v2/everything?q=chess&apiKey=b128b1dd24cd471e934182c7d3eeaf35"
    return fetch_news(request, "chess", url)

def swimming(request):
    url = "https://newsapi.org/v2/everything?q=swimming-sports&apiKey=b128b1dd24cd471e934182c7d3eeaf35"
    return fetch_news(request, "swimming", url)

def shooting(request):
    url = "https://newsapi.org/v2/everything?q=shooting-sport&apiKey=b128b1dd24cd471e934182c7d3eeaf35"
    return fetch_news(request, "shooting", url)

def wrestling(request):
    url = "https://newsapi.org/v2/everything?q=wrestling&apiKey=b128b1dd24cd471e934182c7d3eeaf35"
    return fetch_news(request, "wrestling", url)

def tabletennis(request):
    url = "https://newsapi.org/v2/everything?q=table-tennis&apiKey=b128b1dd24cd471e934182c7d3eeaf35"
    return fetch_news(request, "tabletennis", url)

def other(request):
    url = "https://newsapi.org/v2/everything?q=indian-sports&apiKey=b128b1dd24cd471e934182c7d3eeaf35"
    return fetch_news(request, "other", url)