from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from . models import Site


class IndexView(TemplateView):
    template_name = 'home/home.html'
    model = Site
    context_object_name = 'sites'
    paginate_by = 10
    queryset = Site.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)
        return context

    def dispatch(self, request, msg=None, *args, **kwargs):
        if msg is not None:
            messages.set_level(request, messages.ERROR)
            messages.add_message(self.request, messages.ERROR, 'Login failed')

        return super(IndexView, self).dispatch(request, *args, **kwargs)


class SiteView(LoginRequiredMixin, TemplateView):
    template_name = 'home/sites.html'
    model = Site
    context_object_name = 'sites'
    paginate_by = 10
    queryset = Site.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(SiteView, self).get_context_data(*args, **kwargs)


class CategoryView(LoginRequiredMixin, TemplateView):
    template_name = 'home/sites.html'
    model = Site
    context_object_name = 'categories'
    paginate_by = 10
    queryset = Site.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryView, self).get_context_data(*args, **kwargs)


class LoginView(RedirectView):
    url = '/'

    def post(self, request, *args, **kwargs):
        username = self.request.POST['username']
        password = self.request.POST['passwd']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('sites:home'))
        else:
            return redirect(reverse('sites:home'))
        return super(LoginView, self).get(request, *args, **kwargs)


    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse('users:dashboard'))
        return super(LoginView, self).dispatch(request, *args, **kwargs)


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *arg, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *arg, **kwargs)
