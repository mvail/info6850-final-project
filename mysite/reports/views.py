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

    keywords = Keywords.objects.all()

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
        'keywords': keywords,
        'topWords': topWords,

    })

def categories(request):

    top10_categories_week1 = Uspc.objects.filter(week=1).order_by('-patent_count')[:10]
    top10_categories_week2 = Uspc.objects.filter(week=2).order_by('-patent_count')[:10]
    top10_categories_week3 = Uspc.objects.filter(week=3).order_by('-patent_count')[:10]
    top10_categories_week4 = Uspc.objects.filter(week=4).order_by('-patent_count')[:10]

    topCategories_SQL = Uspc.objects.raw('SELECT *, SUM(patent_count) as patent_count2 FROM reports_uspc GROUP BY uspc ORDER BY patent_count2 DESC LIMIT 10')

    topCategories = []

    for topCategory_SQL in topCategories_SQL:
        row = {}
        uspc = topCategory_SQL.uspc
        row['uspc'] = uspc

        week1_SQL = Uspc.objects.raw('SELECT * FROM reports_uspc WHERE uspc = %s AND week = 1', [uspc])
        for week1 in week1_SQL:
            row['week1'] = week1.patent_count
        if 'week1' not in row:
            row['week1'] = 0

        week2_SQL = Uspc.objects.raw('SELECT * FROM reports_uspc WHERE uspc = %s AND week = 2', [uspc])
        for week2 in week2_SQL:
            row['week2'] = week2.patent_count
        if 'week2' not in row:
            row['week2'] = 0

        week3_SQL = Uspc.objects.raw('SELECT * FROM reports_uspc WHERE uspc = %s AND week = 3', [uspc])
        for week3 in week3_SQL:
            row['week3'] = week3.patent_count
        if 'week3' not in row:
            row['week3'] = 0

        week4_SQL = Uspc.objects.raw('SELECT * FROM reports_uspc WHERE uspc = %s AND week = 4', [uspc])
        for week4 in week4_SQL:
            row['week4'] = week4.patent_count
        if 'week4' not in row:
            row['week4'] = 0

        topCategories.append(row)

    categoriesChangedByTenPercent = []

    categories_SQL = Uspc.objects.raw('SELECT DISTINCT uspc, id FROM reports_uspc ORDER BY uspc ASC')

    for category_SQL in categories_SQL:
        row = {}
        uspc = category_SQL.uspc
        row['uspc'] = uspc

        week1_SQL = Uspc.objects.raw('SELECT * FROM reports_uspc WHERE uspc = %s AND week = 1', [uspc])
        for week1 in week1_SQL:
            row['week1'] = week1.patent_count
        if 'week1' not in row:
            row['week1'] = 0

        week2_SQL = Uspc.objects.raw('SELECT * FROM reports_uspc WHERE uspc = %s AND week = 2', [uspc])
        for week2 in week2_SQL:
            row['week2'] = week2.patent_count
        if 'week2' not in row:
            row['week2'] = 0

        week3_SQL = Uspc.objects.raw('SELECT * FROM reports_uspc WHERE uspc = %s AND week = 3', [uspc])
        for week3 in week3_SQL:
            row['week3'] = week3.patent_count
        if 'week3' not in row:
            row['week3'] = 0

        week4_SQL = Uspc.objects.raw('SELECT * FROM reports_uspc WHERE uspc = %s AND week = 4', [uspc])
        for week4 in week4_SQL:
            row['week4'] = week4.patent_count
        if 'week4' not in row:
            row['week4'] = 0

        values = []
        values.append(row['week1']);
        values.append(row['week2']);
        values.append(row['week3']);
        values.append(row['week4']);

        for a, b in zip(values[::1], values[1::1]):
            if a == 0:
                continue
            if 100 * (b - a) / a > 9:
                if row in categoriesChangedByTenPercent:
                    continue
                else:
                    categoriesChangedByTenPercent.append(row)
                continue

    return render(request, 'reports/categories.html', {
        'top10_categories_week1': top10_categories_week1,
        'top10_categories_week2': top10_categories_week2,
        'top10_categories_week3': top10_categories_week3,
        'top10_categories_week4': top10_categories_week4,
        'topCategories': topCategories,
        'categoriesChangedByTenPercent': categoriesChangedByTenPercent,
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