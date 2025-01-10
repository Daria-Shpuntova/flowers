# admin.py
from django.contrib import admin
from .models import (Kingdom, Division, Orders, ClassName, Family, Genus, Species, Subspecies, Sort, Type,
                     PopularDivision, \
                     PopularDivisionName, PopularOrders, PopularOrdersName, PopularFamily, PopularFamilyName,
                     PopularGenus, PopularGenusName,
                     PopularSpecies, PopularSpeciesName, PopularSubspecies, PopularSubspeciesName, PopularSort,
                     PopularSortName, Example, TypeRose, CharacteristicsKingdom)

admin.site.register(Kingdom)
admin.site.register(Division)
admin.site.register(PopularDivision)
admin.site.register(PopularDivisionName)
admin.site.register(Orders)
admin.site.register(PopularOrders)
admin.site.register(PopularOrdersName)
admin.site.register(ClassName)
admin.site.register(Family)
admin.site.register(PopularFamily)
admin.site.register(PopularFamilyName)
admin.site.register(Genus)
admin.site.register(PopularGenus)
admin.site.register(PopularGenusName)
admin.site.register(Species)
admin.site.register(PopularSpecies)
admin.site.register(PopularSpeciesName)
admin.site.register(Subspecies)
admin.site.register(PopularSubspecies)
admin.site.register(PopularSubspeciesName)
admin.site.register(Sort)
admin.site.register(PopularSort)
admin.site.register(PopularSortName)
admin.site.register(Type)
admin.site.register(Example)
admin.site.register(TypeRose)
admin.site.register(CharacteristicsKingdom)
