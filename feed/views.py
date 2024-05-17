# This import only needed for function-based view
# from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, FormView
from django.contrib import messages
from .forms import PostForm
from .models import Post

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by("-date")
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = "detail.html"
    # use the following line of code, if there is more than one object(!) to refer to
    # context_object_name = "post"

class AddPostView(FormView):
    template_name = "new_post.html"
    form_class = PostForm
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        print(form.cleaned_data["text"])
        print(form.cleaned_data["image"])
        new_object = Post.objects.create(
            text=form.cleaned_data["text"],
            image=form.cleaned_data["image"],
            
        )
        messages.add_message(self.request, messages.SUCCESS, "Your post was successfully stored!")
        return super().form_valid(form)