import os
import sass

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.models import Site
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.shortcuts import reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, UpdateView, DeleteView

from tempfile import gettempdir

from .forms import StyleForm, StyleEditForm, ActiveStyleForm
from .models import Style, css_file_path

class StylistIndexView(LoginRequiredMixin, ListView):
    """
    List of styles available for editing
    """
    template_name = "stylist/index.html"
    model = Style

    def get_queryset(self):
        site_id = settings.SITE_ID
        if hasattr(self.request, 'site'):
            site_id = self.request.site.id
        return Style.objects.filter(site=site_id)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context["form"] = StyleForm
        context["active_form"] = ActiveStyleForm
        site_id = settings.SITE_ID
        if hasattr(self.request, 'site'):
            site_id = self.request.site.id
        try:
            context["active_theme"] = Style.objects.filter(site=site_id).get(enabled=True)
        except:
            pass
        return context
    

# Stylist Preview Link - Autogenerated CSS from SASS/SCSS
class StylistPreviewView(LoginRequiredMixin, FormView):
    form_class = StyleEditForm
    template_name = "stylist/style_form.html"
    success_url = reverse_lazy("stylist:stylist-index")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context["object"] = Style.objects.get(uuid=self.kwargs["uuid"])
        return context

    def form_valid(self, form):
        with open(gettempdir() + "/custom_vars.scss", "w+") as custom_vars:
            string = ""
            google_fonts = "@import url('https://fonts.googleapis.com/css2?family="
            num_fonts = 0
            for key in form.cleaned_data:
                if key != "name":
                    string += "$" + key + ": " + form.cleaned_data[key] + ";\n"
                    if settings.STYLE_SCHEMA[key]["type"] == "font":
                        if num_fonts > 0:
                            google_fonts += "&family="
                        google_fonts += form.cleaned_data[key].replace(" ", "+")
                        google_fonts += ":wght@100;200;300;400;500;600;700;800;900"
                        num_fonts += 1
            if num_fonts > 0:
                google_fonts += "&display=swap');\n"
                string = google_fonts + string
            custom_vars.write(string)
            custom_vars.seek(0)

            instance = Style.objects.get(uuid=self.kwargs["uuid"])

            filename = css_file_path(instance, instance.name + "_preview.css")
            if default_storage.exists(filename):
                default_storage.delete(filename)
            content = sass.compile(filename=settings.STYLIST_SCSS_TEMPLATE, include_paths=[gettempdir()])
            preview = default_storage.save(filename, ContentFile(content.encode()))
            
            self.request.session["preview_css"] = default_storage.url(preview)
            self.request.session["preview_path"] = preview
            os.remove(custom_vars.name)
        return redirect(self.get_success_url())


# Stylist Edit Page
class StylistUpdateView(LoginRequiredMixin, UpdateView):
    model = Style
    form_class = StyleEditForm

    def get_object(self, *args, **kwargs):
        return Style.objects.get(uuid=self.kwargs.get("uuid"))


# Change which Style is currently active for the site
class StylistActiveView(LoginRequiredMixin, FormView):
    form_class = ActiveStyleForm
    template_name = "stylist/active_form.html"

    def form_valid(self, form):
        instance = form.cleaned_data["active"]
        instance.enabled = True
        instance.save()
        return redirect('stylist:stylist-index')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        site_id = settings.SITE_ID
        if hasattr(self.request, 'site'):
            site_id = self.request.site.id
        try:
            context["active_theme"] = Style.objects.filter(site=site_id).get(enabled=True)
        except:
            pass
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


# Stylist Detail Page


class StylistDeleteView(LoginRequiredMixin, DeleteView):
    model = Style
    template_name = 'stylist/style_delete.html'

    def get_object(self, queryset=None):
        return Style.objects.get(uuid=self.kwargs.get("uuid"))

    def get_success_url(self):
        return reverse('stylist:stylist-index')


# Ends preview mode
@login_required
def end_preview(request):
    preview = request.session.pop("preview_css", None)
    preview_path = request.session.pop("preview_path", None)
    if preview_path:
        default_storage.delete(preview_path)
    return redirect(request.META.get('HTTP_REFERER'))
