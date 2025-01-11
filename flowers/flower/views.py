from rest_framework import generics
from .models import Kingdom, Type, Species, Division, ClassName, Orders, Family, Genus, Subspecies, Sort, CharacteristicsKingdom
from .serializers import KingdomSerializer, TypeSerializer, SpeciesSerializer, DivisionSerializer, ClassNameSerializer, \
    OrdersSerializer, FamilySerializer, GenusSerializer, SubspeciesSerializer, SortSerializer, CharacteristicsKingdomSerializer, SubspeciesHomeSerializer, SortHomeSerializer, SpeciesHomeSerializer, GenusHomeSerializer, FamilyHomeSerializer, OrdersHomeSerializer, ClassNameHomeSerializer
from django.views.generic import TemplateView
from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class HomePageView(TemplateView):
    template_name = 'index.html'


class HomePageKingdomView(generics.ListAPIView):
    queryset = Kingdom.objects.all()
    serializer_class = KingdomSerializer

    def get(self, request, *args, **kwargs):
        print("Запрос к /api/Kingdom")
        return super().get(request, *args, **kwargs)

class ClassNameHomeView(generics.ListAPIView):
    queryset = ClassName.objects.all()
    serializer_class = ClassNameHomeSerializer

class OrdersHomeView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersHomeSerializer

class FamilyHomeView(generics.ListAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilyHomeSerializer

class GenusHomeView(generics.ListAPIView):
    queryset = Genus.objects.all()
    serializer_class = GenusHomeSerializer

class SpeciesHomeView(generics.ListAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesHomeSerializer

class SubspeciesHomeView(generics.ListAPIView):
    queryset = Subspecies.objects.all()
    serializer_class = SubspeciesHomeSerializer

class SortHomeView(generics.ListAPIView):
    queryset = Sort.objects.all()
    serializer_class = SortHomeSerializer

class DivisionHomeView(generics.ListAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class DivisionPageView(generics.RetrieveAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        print(f"Запрос к /api/kingdom/{kwargs['slug']}")
        return super().get(request, *args, **kwargs)


class ClassDetailView(generics.RetrieveAPIView):
    queryset = ClassName.objects.all()
    serializer_class = ClassNameSerializer

    def get_object(self):
        division_slug = self.kwargs['division_slug']
        class_name_slug = self.kwargs['class_name_slug']
        # Измените логику получения объекта на основе обоих slug
        return get_object_or_404(ClassName, division__slug=division_slug, slug=class_name_slug)

    def get(self, request, *args, **kwargs):
        division_slug = kwargs['division_slug']
        class_name_slug = kwargs['class_name_slug']
        print(f"Запрос к /api/kingdom/{division_slug}/{class_name_slug}")
        return super().get(request, *args, **kwargs)


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def get_object(self):
        division_slug = self.kwargs['division_slug']
        class_name_slug = self.kwargs['class_name_slug']
        order_slug = self.kwargs['order_slug']
        return get_object_or_404(Orders, division__slug=division_slug, className__slug=class_name_slug, slug=order_slug)

    def get(self, request, *args, **kwargs):
        division_slug = kwargs['division_slug']
        class_name_slug = kwargs['class_name_slug']
        order_slug = kwargs['order_slug']
        print(f"Запрос к /api/kingdom/{division_slug}/{class_name_slug}/{order_slug}")
        return super().get(request, *args, **kwargs)

class FamilyDetailView(generics.RetrieveAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

    def get_object(self):
        division_slug = self.kwargs['division_slug']
        class_name_slug = self.kwargs['class_name_slug']
        order_slug = self.kwargs['order_slug']
        family_slug = self.kwargs['family_slug']
        return get_object_or_404(Family, order__division__slug=division_slug, order__className__slug=class_name_slug, order__slug=order_slug, slug=family_slug)

    def get(self, request, *args, **kwargs):
        division_slug = kwargs['division_slug']
        class_name_slug = kwargs['class_name_slug']
        order_slug = kwargs['order_slug']
        family_slug = kwargs['family_slug']
        print(f"Запрос к /api/kingdom/{division_slug}/{class_name_slug}/{order_slug}/{family_slug}")
        return super().get(request, *args, **kwargs)


class GenusDetailView(generics.RetrieveAPIView):
    queryset = Genus.objects.all()
    serializer_class = GenusSerializer

    def get_object(self):
        division_slug = self.kwargs['division_slug']
        class_name_slug = self.kwargs['class_name_slug']
        order_slug = self.kwargs['order_slug']
        family_slug = self.kwargs['family_slug']
        genus_slug = self.kwargs['genus_slug']
        return get_object_or_404(Genus, family__order__division__slug=division_slug, family__order__className__slug=class_name_slug, family__order__slug=order_slug, family__slug=family_slug, slug=genus_slug)

    def get(self, request, *args, **kwargs):
        division_slug = kwargs['division_slug']
        class_name_slug = kwargs['class_name_slug']
        order_slug = kwargs['order_slug']
        family_slug = kwargs['family_slug']
        genus_slug = kwargs['genus_slug']
        print(f"Запрос к /api/kingdom/{division_slug}/{class_name_slug}/{order_slug}/{family_slug}/{genus_slug}")
        return super().get(request, *args, **kwargs)

class ClassNamePageView(generics.ListAPIView):
    queryset = ClassName.objects.all()
    serializer_class = ClassNameSerializer

class OrdersPageView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class FamilyPageView(generics.ListAPIView):
    queryset = Family.objects.all()
    serializer_class = FamilySerializer

class GenusPageView(generics.ListAPIView):
    queryset = Genus.objects.all()
    serializer_class = GenusSerializer

class SpeciesPageView(generics.ListAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer


class SubspeciesPageView(generics.ListAPIView):
    queryset = Subspecies.objects.all()
    serializer_class = SubspeciesSerializer


class SortPageView(generics.ListAPIView):
    queryset = Sort.objects.all()
    serializer_class = SortSerializer

class TypePageView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class SpeciesLastPageView(generics.ListAPIView):
    queryset = Species.objects.order_by('-created_at')[:4]
    serializer_class = SpeciesSerializer

class CharacteristicsKingdomPageView(generics.ListAPIView):
    queryset = CharacteristicsKingdom.objects.all()
    serializer_class = CharacteristicsKingdomSerializer

    def get(self, request, *args, **kwargs):
        print("Запрос к /api/characteristics")
        return super().get(request, *args, **kwargs)
