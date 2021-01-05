from django.urls.base import reverse_lazy
from univ.forms import EntryForm
from django.views import generic
from .models import Faculty
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "index.html"


class EntryView(generic.FormView):
    template_name = "entry.html"
    form_class = EntryForm


class FacultyListView(generic.ListView):
    template_name = "faculty.html"
    model = Faculty

    def get_queryset(self):
        faculties = Faculty.objects.filter(id__gt=3)
        return faculties
