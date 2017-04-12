# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Patent
from .models import Keywords
from .models import Uspc


def index(request):

    patents = Patent.objects.all()
    keywords = Keywords.objects.all()
    categories = Uspc.objects.all()

    return render(request, 'reports/index.html', {
        'patents': patents,
        'keywords': keywords,
        'categories': categories,
    })

def detail(request, pid):
    try:
        patent = Patent.objects.get(pk=pid)
    except Patent.DoesNotExist:
        raise Http404("Patent does not exist")
    return render(request, 'reports/detail.html', {'patent': patent})

def patent_list(request):
    patent_list = Patent.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(patent_list, 10)
    try:
        patents = paginator.page(page)
    except PageNotAnInteger:
        patents = paginator.page(1)
    except EmptyPage:
        patents = paginator.page(paginator.num_pages)

    return render(request, 'reports/patent_list.html', { 'patents': patents })