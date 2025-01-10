from django.urls import path
from .views import HomePageKingdomView, HomePageView, TypePageView, SpeciesLastPageView, DivisionPageView, ClassNamePageView, OrdersPageView, FamilyPageView, GenusPageView, SpeciesPageView, SubspeciesPageView, SortPageView, CharacteristicsKingdomPageView, SubspeciesHomeView, SortHomeView, SpeciesHomeView, OrdersHomeView, ClassNameHomeView, FamilyHomeView, GenusHomeView, DivisionHomeView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('api/kingdom', HomePageKingdomView.as_view(), name='home_page_kingdom'),
    path('api/type', TypePageView.as_view(), name='type_page'),
    path('api/specieslast', SpeciesLastPageView.as_view(), name='specieslast'),
    path('api/kingdom/<slug:slug>', DivisionPageView.as_view(), name='division_page'),
    path('api/classname', ClassNamePageView.as_view(), name='classname_page'),
    path('api/orders', OrdersPageView.as_view(), name='orders_page'),
    path('api/family', FamilyPageView.as_view(), name='family_page'),
    path('api/genus', GenusPageView.as_view(), name='genus_page'),
    path('api/species', SpeciesPageView.as_view(), name='species_page'),
    path('api/subspecies', SubspeciesHomeView.as_view(), name='subspecies_page'),
    path('api/sort', SortPageView.as_view(), name='sort_page'),
    path('api/characteristics', CharacteristicsKingdomPageView.as_view(), name='characteristics_page'),
    path('api/divisionHome', DivisionHomeView.as_view(), name='divisionHome_page'),
    path('api/classNameHome', ClassNameHomeView.as_view(), name='classNameHome_page'),
    path('api/ordersHome', OrdersHomeView.as_view(), name='ordersHome_page'),
    path('api/familyHome', FamilyHomeView.as_view(), name='familyHome_page'),
    path('api/genusHome', GenusHomeView.as_view(), name='genusHome_page'),
    path('api/speciesHome', SpeciesHomeView.as_view(), name='species_home_page'),
    path('api/subspeciesHome', SubspeciesHomeView.as_view(), name='subspecies_home'),
    path('api/sortHome', SortHomeView.as_view(), name='sort_home'),
]