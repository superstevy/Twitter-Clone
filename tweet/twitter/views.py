from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from .models import Tweet
from .forms import TweetForm
from cloudinary.forms import cl_init_js_callbacks


# Create your views here.

def index(request):
    tweets = Tweet.objects.all()
    stuff = get_object_or_404(Tweet, id = self.kwargs['pk'])
    total_likes = stuff.total_likes()
    ctx = {'tweets': tweets,
           'total_likes': total_likes
           }
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
        form = TweetForm(request.POST, request.FILES, instance = tweet)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TweetForm(instance = tweet)
    ctx = {'form': form}
    return render(request, 'twitter/update.html', ctx)


def deleteTweet(request, id):
    tweet = get_object_or_404(Tweet, id = id)
    if request.POST:
        tweet.delete()
        return redirect('index')
    ctx = {
        'tweet': tweet
        }
    return render(request, 'twitter/delete.html', ctx)


def likePost(request, pk):
    tweet = get_object_or_404(Tweet, id = request.POST.get('tweet_id'))
    tweet.like_count.add(request.user)
    return HttpResponseRedirect(reverse('index', args = [str(pk)]))
