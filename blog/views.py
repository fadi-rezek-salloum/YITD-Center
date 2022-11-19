from django.views import generic
from django.contrib import messages
from django.shortcuts import redirect, get_list_or_404

from .models import Post, SubCategory
from .forms import CommentForm


def sub_categories_list(request):
    sub_categories = SubCategory.objects.all()

    return {
        'sub_categories': sub_categories
    }


class BlogList(generic.ListView):
    model = Post
    template_name = "blog/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        if 'languages' in self.kwargs['cat']:
            posts = Post.objects.filter(category__slug__icontains=str.lower(self.kwargs['cat']))
        else:
            posts = Post.objects.filter(sub_category__slug__icontains=str.lower(self.kwargs['cat']))

        return posts



class PostDetails(generic.DetailView):
    model = Post
    template_name = "blog/details.html"
    context_object_name = "post"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = CommentForm

        return context

    def post(self, request, *args, **kwargs):

        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your comment was sent successfully!")
        
        else:
            for field in form:
                for err in field.errors:
                    messages.error(request, err)
            
        return redirect(f"/blog/post/{kwargs['slug']}/")