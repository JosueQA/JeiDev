from django.views.generic import ListView, DetailView
from .models import AppModel

class AppViews(ListView):
    template_name = "app/app_home.html"
    context_object_name = "app_home"

    def get_queryset(self):
        return []
    
class AppPageViews(DetailView):
    template_name = "app/app.html"
    context_object_name = "app"
    slug_field ="slug"# campo del modelo
    slug_url_kwarg ="slug"# nombre en la URL
    
    def get_object(self):
        app = self.kwargs.get('app')
        
        return {"app": app}