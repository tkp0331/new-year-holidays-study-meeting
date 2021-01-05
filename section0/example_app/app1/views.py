from django.views import generic


class Hello(generic.TemplateView):
    template_name = "hello.htm"


class World(generic.TemplateView):
    template_name = "world.htm"
