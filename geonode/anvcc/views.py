from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
import requests
from django.conf import settings

# Create your views here.


class ClassifyCSSView(APIView):
    def get(self, request):
        title = request.query_params.get('title')
        dataset = request.query_params.get('dataset')
        attribute = request.query_params.get('attribute', None)
        classes = request.query_params.getlist('classes', None)
        start_color = request.query_params.get('start_color', '#fef0d9')
        mid_color = request.query_params.get('mid_color', '#fd8d3c')
        end_color = request.query_params.get('end_color', '#b30000')
        intervals = request.query_params.get('intervals', 3)
        method = request.query_params.get('method')

        if classes:
            classes = [x.strip() for x in classes.split(',')]
        url = f"/geonode/gs/rest/sldservice/{dataset}/classify.json?intervals={len(classes)}&method={method}&attribute={attribute}&ramp=CUSTOM&startColor={start_color.replace('#', '0x')}&midColor={mid_color.replace('#', '0x')}&endColor={end_color.replace('#', '0x')}"
        rules = requests.get(url, auth=(settings.GEOSERVER_USER, settings.GEOSERVER_PASSWORD))
        rules = dict(rules.json())['Rules']['Rule']

        if len(classes) == len(rules):
            for rule, label in zip(rules, classes):
                rule['label'] = label

        context = {"rules": rules, "title": dataset, "attribute": attribute, "classes": classes}

        template_name = 'classify.css'
        res = render(request, template_name, context)

        return HttpResponse(res, content_type='text/css')
