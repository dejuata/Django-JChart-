from jchart import Chart
from jchart.config import Axes, DataSet, rgba


class BarChart(Chart):
	"""
		Esta clase genera un grafico de barras
	"""
    chart_type = 'bar'

    def get_labels(self, **kwargs):
        return ["January", "February", "March", "April",
                "May", "June", "July"]

    def get_datasets(self, **kwargs):
        data = [10, 15, 29, 30, 5, 10, 22]
        colors = [
            rgba(255, 99, 132, 0.2),
            rgba(54, 162, 235, 0.2),
            rgba(255, 206, 86, 0.2),
            rgba(75, 192, 192, 0.2),
            rgba(153, 102, 255, 0.2),
            rgba(255, 159, 64, 0.2)
        ]

        return [DataSet(label='Bar Chart',
                        data=data,
                        borderWidth=1,
                        backgroundColor=colors,
                        borderColor=colors)]


class LineChart(Chart):
    chart_type = 'line'
    scales = {
        'xAxes': [Axes(type='time', position='bottom')],
    }

    def get_datasets(self, **kwargs):
        data = [{'y': 0, 'x': '2017-01-02T00:00:00'}, {'y': 1, 'x': '2017-01-03T00:00:00'}, {'y': 4, 'x': '2017-01-04T00:00:00'}, {'y': 9, 'x': '2017-01-05T00:00:00'}, {'y': 16, 'x': '2017-01-06T00:00:00'}, {'y': 25, 'x': '2017-01-07T00:00:00'}, {'y': 36, 'x': '2017-01-08T00:00:00'}, {'y': 49, 'x': '2017-01-09T00:00:00'}, {'y': 64, 'x': '2017-01-10T00:00:00'}, {'y': 81, 'x': '2017-01-11T00:00:00'}, {'y': 100, 'x': '2017-01-12T00:00:00'}, {'y': 121, 'x': '2017-01-13T00:00:00'}, {'y': 144, 'x': '2017-01-14T00:00:00'}, {'y': 169, 'x': '2017-01-15T00:00:00'}, {'y': 196, 'x': '2017-01-16T00:00:00'}, {'y': 225, 'x': '2017-01-17T00:00:00'}, {'y': 256, 'x': '2017-01-18T00:00:00'}, {'y': 289, 'x': '2017-01-19T00:00:00'}, {'y': 324, 'x': '2017-01-20T00:00:00'}, {'y': 361, 'x': '2017-01-21T00:00:00'}, {'y': 400, 'x': '2017-01-22T00:00:00'}, {'y': 441, 'x': '2017-01-23T00:00:00'}, {'y': 484, 'x': '2017-01-24T00:00:00'}, {'y': 529, 'x': '2017-01-25T00:00:00'}, {'y': 576, 'x': '2017-01-26T00:00:00'}, {'y': 625, 'x': '2017-01-27T00:00:00'}, {'y': 676, 'x': '2017-01-28T00:00:00'}, {'y': 729, 'x': '2017-01-29T00:00:00'}, {'y': 784, 'x': '2017-01-30T00:00:00'}, {'y': 841, 'x': '2017-01-31T00:00:00'}, {'y': 900, 'x': '2017-02-01T00:00:00'}]

        return [DataSet(
            type='line',
            label='Time Series',
            data=data,
        )]
