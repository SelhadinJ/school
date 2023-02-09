from django.urls import reverse_lazy
from django.views import generic
from . import models


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'index.html'


class SchoolListView(generic.ListView):
    model = models.School


class SchoolDetailView(generic.DetailView):
    model = models.School


class SchoolCreateView(generic.CreateView):
    model = models.School
    fields = '__all__'


class SchoolUpdateView(generic.UpdateView):
    model = models.School
    fields = ('name', 'principal')


class SchoolDeleteView(generic.DeleteView):
    model = models.School
    success_url = reverse_lazy('school_app:list')


class StudentUpdateView(generic.UpdateView):
    model = models.Student
    fields = ('name', 'major', 'school')


class StudentDeleteView(generic.DeleteView):
    model = models.Student
    success_url = reverse_lazy('school_app:list')
