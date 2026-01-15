from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, View
from .models import AppModel

class AppViews(ListView):
    model = AppModel
    template_name = "app/app_home.html"
    context_object_name = "apps"


class AppPageViews(DetailView):
    model = AppModel
    template_name = "app/app.html"
    context_object_name = "app"
    slug_field ="slug"# campo del modelo
    slug_url_kwarg ="slug"# nombre en la URL de urls.py

    

class AppDownloadView(View):

    def get(self, request, id):
        app = get_object_or_404(AppModel, id=id)

        return FileResponse(
            app.file.open(),
            as_attachment=True,
            filename=app.file.name
        )