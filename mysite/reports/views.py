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

    topWords_SQL = Keywords.objects.raw('SELECT *, SUM(word_count) as word_count2 FROM reports_keywords GROUP BY word ORDER BY word_count2 DESC LIMIT 10')

    topWords = []

    for topWord_SQL in topWords_SQL:
        row = {}
        word = topWord_SQL.word
        row['word'] = word

        week1_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 1', [word])
        for week1 in week1_SQL:
            row['week1'] = week1.word_count

        week2_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 2', [word])
        for week2 in week2_SQL:
            row['week2'] = week2.word_count

        week3_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 3', [word])
        for week3 in week3_SQL:
            row['week3'] = week3.word_count

        week4_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 4', [word])
        for week4 in week4_SQL:
            row['week4'] = week4.word_count

        topWords.append(row)



    return render(request, 'reports/index.html', {

        'topWords': topWords,

    })

def datatables(request):

    patents = Patent.objects.all()
    keywords = Keywords.objects.all()
    categories = Uspc.objects.all()

    return render(request, 'reports/datatables.html', {
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

def charts(request):

    topWords_SQL = Keywords.objects.raw('SELECT *, SUM(word_count) as word_count2 FROM reports_keywords GROUP BY word ORDER BY word_count2 DESC LIMIT 10')

    topWords = []

    for topWord_SQL in topWords_SQL:
        row = {}
        word = topWord_SQL.word
        row['word'] = word

        week1_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 1', [word])
        for week1 in week1_SQL:
            row['week1'] = week1.word_count

        week2_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 2', [word])
        for week2 in week2_SQL:
            row['week2'] = week2.word_count

        week3_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 3', [word])
        for week3 in week3_SQL:
            row['week3'] = week3.word_count

        week4_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 4', [word])
        for week4 in week4_SQL:
            row['week4'] = week4.word_count

        topWords.append(row)



    return render(request, 'reports/charts.html', {

        'topWords': topWords,

    })

def keywords(request):

    topWords_SQL = Keywords.objects.raw('SELECT *, SUM(word_count) as word_count2 FROM reports_keywords GROUP BY word ORDER BY word_count2 DESC LIMIT 10')

    topWords = []

    for topWord_SQL in topWords_SQL:
        row = {}
        word = topWord_SQL.word
        row['word'] = word

        week1_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 1', [word])
        for week1 in week1_SQL:
            row['week1'] = week1.word_count

        week2_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 2', [word])
        for week2 in week2_SQL:
            row['week2'] = week2.word_count

        week3_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 3', [word])
        for week3 in week3_SQL:
            row['week3'] = week3.word_count

        week4_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 4', [word])
        for week4 in week4_SQL:
            row['week4'] = week4.word_count

        topWords.append(row)



    return render(request, 'reports/keywords.html', {

        'topWords': topWords,

    })

def categories(request):

    topWords_SQL = Keywords.objects.raw('SELECT *, SUM(word_count) as word_count2 FROM reports_keywords GROUP BY word ORDER BY word_count2 DESC LIMIT 10')

    topWords = []

    for topWord_SQL in topWords_SQL:
        row = {}
        word = topWord_SQL.word
        row['word'] = word

        week1_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 1', [word])
        for week1 in week1_SQL:
            row['week1'] = week1.word_count

        week2_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 2', [word])
        for week2 in week2_SQL:
            row['week2'] = week2.word_count

        week3_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 3', [word])
        for week3 in week3_SQL:
            row['week3'] = week3.word_count

        week4_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 4', [word])
        for week4 in week4_SQL:
            row['week4'] = week4.word_count

        topWords.append(row)



    return render(request, 'reports/categories.html', {

        'topWords': topWords,

    })

def complex(request):

    topWords_SQL = Keywords.objects.raw('SELECT *, SUM(word_count) as word_count2 FROM reports_keywords GROUP BY word ORDER BY word_count2 DESC LIMIT 10')

    topWords = []

    for topWord_SQL in topWords_SQL:
        row = {}
        word = topWord_SQL.word
        row['word'] = word

        week1_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 1', [word])
        for week1 in week1_SQL:
            row['week1'] = week1.word_count

        week2_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 2', [word])
        for week2 in week2_SQL:
            row['week2'] = week2.word_count

        week3_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 3', [word])
        for week3 in week3_SQL:
            row['week3'] = week3.word_count

        week4_SQL = Keywords.objects.raw('SELECT * FROM reports_keywords WHERE word = %s AND week = 4', [word])
        for week4 in week4_SQL:
            row['week4'] = week4.word_count

        topWords.append(row)


    return render(request, 'reports/complex.html', {

        'topWords': topWords,

    })