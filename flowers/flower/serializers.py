from rest_framework import serializers
from .models import Kingdom, Division, ClassName, Orders, Species, Type, Example, Family, Genus, Subspecies, Sort, CharacteristicsKingdom, TypeRose


class KingdomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kingdom
        fields = '__all__'

class SortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sort
        fields = ['slug', 'name','description', 'descriptionBig', 'image']


class SubspeciesSerializer(serializers.ModelSerializer):
    sortSubspecies = SortSerializer(many=True, read_only=True, default=[])

    class Meta:
        model = Subspecies
        fields = ['slug', 'name','description', 'descriptionBig', 'image', 'sortSubspecies']


class SpeciesSerializer(serializers.ModelSerializer):
    subspecies = SubspeciesSerializer(many=True, read_only=True, default=[])
    sortSpecies = SortSerializer(many=True, read_only=True, default=[])

    class Meta:
        model = Species
        fields = ['slug', 'name','description', 'descriptionBig', 'image', 'speciesRose', 'subspecies', 'sortSpecies']

class TypeRoseSerializer(serializers.ModelSerializer):
    speciesRose = SpeciesSerializer(many=True, read_only=True, default=[])

    class Meta:
        model = TypeRose
        fields = ['name','description', 'image', 'genusRose', 'speciesRose']

class GenusSerializer(serializers.ModelSerializer):
    species = SpeciesSerializer(many=True, read_only=True, default=[])
    genusRose = TypeRoseSerializer(many=True, read_only=True, default=[])

    class Meta:
        model = Genus
        fields = ['slug', 'name','description', 'descriptionBig', 'image', 'species', 'genusRose']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['genusRose'] = list(instance.genusRoses.values())  # Получаем все связанные заказы
        return representation


class FamilySerializer(serializers.ModelSerializer):
    genus = GenusSerializer(many=True, read_only=True, default=[])

    class Meta:
        model = Family
        fields = ['slug', 'name','description', 'descriptionBig', 'image', 'genus']


class OrdersSerializer(serializers.ModelSerializer):
    family = FamilySerializer(many=True, read_only=True, default=[])

    class Meta:
        model = Orders
        fields = ['slug', 'name','description', 'descriptionBig', 'image', 'family']


class ClassNameSerializer(serializers.ModelSerializer):
    orderClass = OrdersSerializer(read_only=True, many=True, default=[])

    class Meta:
        model = ClassName
        fields = ['slug', 'name','description', 'descriptionBig', 'image', 'orderClass']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['orderClass'] = list(instance.orderClass.values())  # Получаем все связанные заказы
        return representation

class DivisionSerializer(serializers.ModelSerializer):
    classes = ClassNameSerializer(read_only=True, many=True)
    orders = OrdersSerializer(read_only=True, many=True)
    class Meta:
        model = Division
        fields = ['slug', 'name','description', 'descriptionBig', 'image', 'classes', 'orders']


class ClassNameHomeSerializer(serializers.ModelSerializer):
    division_slug = serializers.SlugRelatedField(source='division', slug_field='slug', queryset=Division.objects.all())
    class Meta:
        model = ClassName
        fields = ['slug', 'name','division_slug']


class OrdersHomeSerializer(serializers.ModelSerializer):
    class_name_slug = serializers.SlugRelatedField(source='className', slug_field='slug', queryset=ClassName.objects.all())
    division_slug = serializers.SlugRelatedField(source='className.division', slug_field='slug', queryset=Division.objects.all())

    class Meta:
        model = Orders
        fields = ['slug', 'name', 'class_name_slug', 'division_slug']


class FamilyHomeSerializer(serializers.ModelSerializer):
    order_slug = serializers.SlugRelatedField(source='order', slug_field='slug', queryset=Orders.objects.all())
    class_name_slug = serializers.SlugRelatedField(source='order.className', slug_field='slug', queryset=ClassName.objects.all())
    division_slug = serializers.SlugRelatedField(source='order.className.division', slug_field='slug', queryset=Division.objects.all())

    class Meta:
        model = Family
        fields = ['slug', 'name', 'order_slug', 'class_name_slug',
                  'division_slug']



class GenusHomeSerializer(serializers.ModelSerializer):
    family_slug = serializers.SlugRelatedField(source='family', slug_field='slug', queryset=Family.objects.all())
    order_slug = serializers.SlugRelatedField(source='family.order', slug_field='slug', queryset=Orders.objects.all())
    class_name_slug = serializers.SlugRelatedField(source='family.order.className', slug_field='slug', queryset=ClassName.objects.all())
    division_slug = serializers.SlugRelatedField(source='family.order.className.division', slug_field='slug', queryset=Division.objects.all())

    class Meta:
        model = Genus
        fields = ['slug', 'name',  'family_slug', 'order_slug', 'class_name_slug',
                  'division_slug']


class SpeciesHomeSerializer(serializers.ModelSerializer):
    genus_slug = serializers.SlugRelatedField(source='genus', slug_field='slug', queryset=Genus.objects.all())
    family_slug = serializers.SlugRelatedField(source='genus.family', slug_field='slug', queryset=Family.objects.all())
    order_slug = serializers.SlugRelatedField(source='genus.family.order', slug_field='slug', queryset=Orders.objects.all())
    class_name_slug = serializers.SlugRelatedField(source='genus.family.order.className', slug_field='slug', queryset=ClassName.objects.all())
    division_slug = serializers.SlugRelatedField(source='genus.family.order.className.division', slug_field='slug', queryset=Division.objects.all())

    class Meta:
        model = Species
        fields = ['slug', 'name', 'genus_slug', 'family_slug', 'order_slug', 'class_name_slug',
                  'division_slug']


class SubspeciesHomeSerializer(serializers.ModelSerializer):
    species_slug = serializers.SlugRelatedField(source='species', slug_field='slug', queryset=Species.objects.all())
    genus_slug = serializers.SlugRelatedField(source='species.genus', slug_field='slug', queryset=Genus.objects.all())
    family_slug = serializers.SlugRelatedField(source='species.genus.family', slug_field='slug', queryset=Family.objects.all())
    order_slug = serializers.SlugRelatedField(source='species.genus.family.order', slug_field='slug', queryset=Orders.objects.all())
    class_name_slug = serializers.SlugRelatedField(source='species.genus.family.order.className', slug_field='slug', queryset=ClassName.objects.all())
    division_slug = serializers.SlugRelatedField(source='species.genus.family.order.className.division', slug_field='slug', queryset=Division.objects.all())

    class Meta:
        model = Subspecies
        fields = ['slug', 'name', 'species_slug', 'genus_slug', 'family_slug', 'order_slug', 'class_name_slug',
                  'division_slug']


class SortHomeSerializer(serializers.ModelSerializer):
    subspecies_slug = serializers.SlugRelatedField(
        source='subspecies',
        slug_field='slug',
        queryset=Subspecies.objects.all(),
        allow_null=True  # Позволяет быть пустым
    )

    species_slug = serializers.SerializerMethodField()
    genus_slug = serializers.SerializerMethodField()
    family_slug = serializers.SerializerMethodField()
    order_slug = serializers.SerializerMethodField()
    class_name_slug = serializers.SerializerMethodField()
    division_slug = serializers.SerializerMethodField()


    class Meta:
        model = Sort
        fields = [
            'slug', 'name', 'subspecies_slug', 'species_slug',
            'genus_slug', 'family_slug', 'order_slug',
            'class_name_slug', 'division_slug'
        ]

    def get_species_slug(self, obj):
        if obj.subspecies:
            return obj.subspecies.species.slug
        return obj.species.slug if obj.species else None

    def get_genus_slug(self, obj):
        if obj.subspecies and obj.subspecies.species:
            return obj.subspecies.species.genus.slug
        return obj.species.genus.slug if obj.species else None

    def get_family_slug(self, obj):
        if obj.subspecies and obj.subspecies.species and obj.subspecies.species.genus:
            return obj.subspecies.species.genus.family.slug
        return obj.species.genus.family.slug if obj.species else None

    def get_order_slug(self, obj):
        if obj.subspecies and obj.subspecies.species and obj.subspecies.species.genus and obj.subspecies.species.genus.family:
            return obj.subspecies.species.genus.family.order.slug
        return obj.species.genus.family.order.slug if obj.species else None

    def get_class_name_slug(self, obj):
        if obj.subspecies and obj.subspecies.species and obj.subspecies.species.genus and obj.subspecies.species.genus.family and obj.subspecies.species.genus.family.order:
            return obj.subspecies.species.genus.family.order.className.slug
        return obj.species.genus.family.order.className.slug if obj.species else None

    def get_division_slug(self, obj):
        if obj.subspecies and obj.subspecies.species and obj.subspecies.species.genus and obj.subspecies.species.genus.family and obj.subspecies.species.genus.family.order and obj.subspecies.species.genus.family.order.className:
            return obj.subspecies.species.genus.family.order.className.division.slug
        return obj.species.genus.family.order.className.division.slug if obj.species else None


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ['id', 'name', 'image']


class TypeSerializer(serializers.ModelSerializer):
    examples = ExampleSerializer(many=True, read_only=True)  # Включаем примеры

    class Meta:
        model = Type
        fields = '__all__'

class CharacteristicsKingdomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacteristicsKingdom
        fields = '__all__'