# This import only needed for function-based view
# from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Post

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = "detail.html"
    # use the following line of code, if there is more than one object(!) to refer to
    # context_object_name = "post"