from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from apps.blogs.models import Blog,Departments,About,Gallery,Contact
from apps.blogs.forms import BlogCreateForm, BlogUpdateForm, BlogDeleteForm


class BlogCreateView(generic.CreateView):
    model = Blog
    form_class = BlogCreateForm
    template_name = 'blogs/blog_create.html'
    success_url = reverse_lazy('blogs:list')


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog-default.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogCreateForm()
        return context


class BlogLargeView(generic.ListView):
    model = Blog
    template_name = 'blog-large.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogCreateForm()
        return context


class BlogSingleView(generic.ListView):
    model = Blog
    template_name = 'blog-single.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BlogCreateForm()
        return context


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog-detail.html'
    context_object_name = 'detail'
    pk_url_kwarg = 'pk'


class BlogUpdateView(generic.UpdateView):
    model = Blog
    form_class = BlogUpdateForm
    template_name = 'blogs/blog_update.html'
    success_url = reverse_lazy('blogs:list')


class BlogDeleteView(generic.DeleteView):
    model = Blog
    form_class = BlogDeleteForm
    template_name =  'blogs/blog_delete.html'
    context_object_name = 'blog'
    success_url = reverse_lazy('blogs:list')


class DepartmentsListView(generic.ListView):
    model = Departments
    template_name = 'departments.html'


class AboutUsView(generic.TemplateView):
    model = About
    template_name = 'about.html'


class GalleryListView(generic.ListView):
    model = Gallery
    template_name = 'project.html'
    context_object_name = 'blogs'


class GallerySingleView(generic.ListView):
    model = Gallery
    template_name = 'project-single.html'
    context_object_name = 'blogs'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ContactListView(generic.ListView):
    model = Contact
    template_name = 'contact.html'
