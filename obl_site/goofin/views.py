from django.shortcuts import render
from django.http import Http404
from django.template import loader
from goofin.models import Goof_Table
# Create your views here.


def goof_list_view(request):
    published = Goof_Table.objects.exclude(published_date__exact=None)#query that retrieves data
    posts = published.order_by('-published_date') #order data
    context = {'posts': posts} #vlookup, kind of. More of 1:1 madlib
    return render(request, 'goofin/goof_list.html', context)
    # render(someone hit enter, HTML to inject it into, vlookup column)