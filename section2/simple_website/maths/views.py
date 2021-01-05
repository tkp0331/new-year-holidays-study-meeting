from django.views import generic

class BarView(generic.TemplateView):
    template_name = "bar.htm"

class WaveView(generic.TemplateView):
    template_name = "wave.htm"

class TableView(generic.TemplateView):
    template_name = "table.htm"