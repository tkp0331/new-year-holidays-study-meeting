from django.views import generic

class SetView(generic.TemplateView):
    template_name = "set.htm"

class DriveView(generic.TemplateView):
    template_name = "drive.htm"