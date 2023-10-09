from django.views import generic
from .models import Post
from django.views.generic.base import TemplateView

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = Post.objects.filter(status=1).order_by('-created_on')[:3]
        return context

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['recent_posts'] = Post.objects.filter(status=1).order_by('-created_on')[:3]
            return context

class ContactView(TemplateView):
    template_name = 'contact.html' 

class AboutView(TemplateView):
    template_name = 'about.html' 
