from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


class NewsListView(ListView):
    model = models.News
    template_name = 'news_list.html'


class NewsDetailView(DetailView):
    model = models.News
    template_name = 'news_detail.html'


class NewsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = models.News
    fields = ('category', 'title', 'slug', 'body', 'image')
    template_name = 'news_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class NewsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.News
    fields = ('category', 'title', 'slug', 'body', 'image')
    template_name = 'news_update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class NewsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.News
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news-list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class CommitCreateView(CreateView, LoginRequiredMixin):
    model = models.Commit
    fields = "__all__"
    template_name = ('news_detail.html')

    # def form_valid(self, form):
    #     form.instance.news = self.request.news
    #     return super().form_valid(form)