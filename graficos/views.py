from django.shortcuts import render
from django.views.generic import TemplateView
from .charts import BarChart


class IndexView(TemplateView):

    # template_name = 'index.html'

    def get(self, request, format=None):
        bar_char = BarChart()
        return render(request, 'index.html', {
            'bar_chart': bar_char,
        })
