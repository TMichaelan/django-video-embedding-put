# Create your views here.
from django.shortcuts import render 
from .models import EmbeddedVideoItem
from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import IntegrityError
from django.views import View,generic


class VideoView(generic.DetailView):
    model = EmbeddedVideoItem
    template_name = 'video.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        video = self.get_object()        
        context['video'] = video
        return context


def index(request):
    videos = EmbeddedVideoItem.objects.all()
    return render(request, 'index.html', context={'videos': videos})