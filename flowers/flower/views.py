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


from rest_framework import generics
from .models import Division, ClassName  # Импортируйте Ваши модели
from .serializers import DivisionSerializer, ClassNameSerializer  # Импортируйте Ваши сериализаторы


class ClassDetailView(generics.RetrieveAPIView):
    queryset = ClassName.objects.all()
    serializer_class = ClassNameSerializer
    # Удалите или измените lookup_field, так как у Вас два slug
    # lookup_field = 'slug'  # Убедитесь, что у Вас есть поле slug в модели ClassName

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
