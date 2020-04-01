import csv
import io
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse, HttpResponse, Http404
from django.views import View
from django.core.serializers.json import DjangoJSONEncoder
from django.core.paginator import _
from django.template.loader import get_template
from django.core import serializers
from django_filters.views import FilterView
import datetime
import json
import math
import os
from datetime import datetime, timedelta
from django.db.models import Count, Min, Sum, Avg, Max
from .models import TrendsRising
from django.views.generic import ListView
from django import forms
from django.core import serializers
from django.contrib.admin.options import get_content_type_for_model
from google_trends import settings
from apps.core.views_functions import *



# Create your views here.
class TrendsRisingList(ListView):
    ''' Database utilizado em settings.py '''
    DATABASE = 'google_trends_crawler'
    ''' Modelo do Django '''
    model = TrendsRising
    ''' Ordem das colunas  '''
    field_names_order = ['id', 'assunto', 'tendencia', 'estado', 'periodo']
    ''' Ordenação inicial:   
        Ordem Descrescente -> Sufixo '-'  +  Nome do campo   
        Ordem Crescente ->                   Nome do campo  
    '''
    order_by = "id"
    ''' Campo de Data: Nome do campo '''
    date_field = ''
    ''' Lista de Filtros: Nome dos campos que serão apresentados nos filtros '''
    filtered_fields = ['assunto','estado    ']
    ''' Número de registros por página '''
    rows_per_page = 10
    ''' Tipo de objeto que será preenchido pelo Queryset '''
    fillObject = 'table'  # 'table' or 'image'
    ''' Nome do Arquivo que será exportado '''
    filename = 'assuntos'

    # @classmethod
    # def export_csv(self):
    #     dados = PriceCrawler.objects.using('machines_crawler').all()
    #     response = HttpResponse(content_type='text/csv')
    #     response = create_csv(response, 'Histórico', dados)
    #     return response



    def get_queryset(self):
        return filter_queryset(self)

    def post(self, request, *args, **kwargs):

        # etapa_response = self.request.POST.get('etapa','')
        if self.request.POST.get('etapa','') == 'inicial':
            context_json = initial_post(self)
        else:
            context_json = ajax_post(self)

        return HttpResponse(context_json, content_type='application/json')

    def export_csv(self):
        cls = TrendsRisingList()
        dados = cls.model.objects.using(cls.DATABASE).all()
        response = HttpResponse(content_type='text/csv')
        response = create_csv(response, cls.filename, dados)
        return response


