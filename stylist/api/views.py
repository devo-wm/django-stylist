from rest_framework import viewsets, mixins
from rest_framework.generics import CreateAPIView
from rest_framework.pagination import PageNumberPagination

from django.contrib.sites.models import Site
from django.shortcuts import redirect

from stylist.models import Style, Font
from stylist.api.serializers import StyleSerializer, FontSerializer


class StyleCreateAPIView(CreateAPIView):
     queryset = Style.objects.all()
     serializer_class = StyleSerializer

     def perform_create(self, serializer):
          if getattr(self.request, "site", None):
               site = self.request.site
          else:
               site = Site.objects.get_current()
          instance = serializer.save(site=site)
          instance.compile_attrs()

          if not Style.objects.filter(site=site, enabled=True):
               instance.enabled = True
               instance.save()

     def create(self, request, *args, **kwargs):
          response = super().create(request, *args, **kwargs)
          return redirect('stylist:stylist-index')


class StyleDuplicateAPIView(CreateAPIView):
     queryset = Style.objects.all()
     serializer_class = StyleSerializer

     def perform_create(self, serializer):
          previous = Style.objects.get(uuid=self.kwargs["uuid"])
          if getattr(self.request, "site", None):
               site = self.request.site
          else:
               site = Site.objects.get_current()
          new_name = previous.name + " copy"
          instance = serializer.save(site=site, attrs=previous.attrs, name=new_name)
          instance.compile_attrs()

          if not Style.objects.filter(site=site, enabled=True):
               instance.enabled = True
               instance.save()

     def create(self, request, *args, **kwargs):
          response = super().create(request, *args, **kwargs)
          return redirect('stylist:stylist-index')


class FontViewset(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Font.objects.all()
    serializer_class = FontSerializer
    pagination_class = PageNumberPagination
    page_size = 20