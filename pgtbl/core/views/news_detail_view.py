from django.views.generic import DetailView
from core.models import News


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/details.html'
