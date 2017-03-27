from django.conf.urls import url
from django.contrib import admin

from jchart.views import ChartView
from graficos.views import IndexView
from graficos.charts import LineChart

line_chart = LineChart()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view()),
    url(r'^charts/line_chart/$', ChartView.from_chart(line_chart), name='line_chart'),
]
