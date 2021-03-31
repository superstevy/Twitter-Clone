from django.shortcuts import render, redirect
from .models import Tweet
from .forms import TweetForm
from cloudinary.forms import cl_init_js_callbacks


# Create your views here.

def index(request):
    tweets = Tweet.objects.all()
    ctx = {'tweets': tweets}
    return render(request, 'twitter/index.html', ctx)


def loadTweet(request):
    if request.POST:
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TweetForm()
    ctx = {'form': form}
    return render(request, 'twitter/load.html', ctx)


def updateTweet(request, id):
    tweet = Tweet.objects.get(pk=id) 
    if request.POST:              
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TweetForm(instance=tweet)
    ctx = {'form': form}
    return render(request, 'twitter/update.html', ctx)
