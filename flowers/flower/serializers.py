from rest_framework import serializers
from .models import Kingdom, Division, ClassName, Orders, Species, Type, Example, Family, Genus, Subspecies, Sort, CharacteristicsKingdom


class KingdomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kingdom
        fields = '__all__'




class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = ['slug', 'name','description', 'descriptionBig', 'image']



class ClassNameHomeSerializer(serializers.ModelSerializer):
    division_slug = serializers.SlugRelatedField(source='division', slug_field='slug', queryset=Division.objects.all())

    class Meta:
        model = ClassName
        fields = ['slug', 'name','division_slug']

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['slug', 'name']

class DivisionSerializer(serializers.ModelSerializer):
    classes = ClassNameSerializer(read_only=True, many=True)
    orders = OrdersSerializer(read_only=True, many=True)

    class Meta:
        model = Division
        fields = ['slug', 'name','description', 'descriptionBig', 'image', 'classes', 'orders']

class OrdersHomeSerializer(serializers.ModelSerializer):
    class_name_slug = serializers.SlugRelatedField(source='className', slug_field='slug', queryset=ClassName.objects.all())
    division_slug = serializers.SlugRelatedField(source='className.division', slug_field='slug', queryset=Division.objects.all())

    class Meta:
        model = Orders
        fields = ['slug', 'name', 'class_name_slug', 'division_slug']

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'

class FamilyHomeSerializer(serializers.ModelSerializer):
    order_slug = serializers.SlugRelatedField(source='order', slug_field='slug', queryset=Orders.objects.all())
    class_name_slug = serializers.SlugRelatedField(source='order.className', slug_field='slug', queryset=ClassName.objects.all())
    division_slug = serializers.SlugRelatedField(source='order.className.division', slug_field='slug', queryset=Division.objects.all())

    class Meta:
        model = Family
        fields = ['slug', 'name', 'order_slug', 'class_name_slug',
                  'division_slug']


class GenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genus
        fields = '__all__'

class GenusHomeSerializer(serializers.ModelSerializer):
    family_slug = serializers.SlugRelatedField(source='family', slug_field='slug', queryset=Family.objects.all())
    order_slug = serializers.SlugRelatedField(source='family.order', slug_field='slug', queryset=Orders.objects.all())
    class_name_slug = serializers.SlugRelatedField(source='family.order.className', slug_field='slug', queryset=ClassName.objects.all())
    division_slug = serializers.SlugRelatedField(source='family.order.className.division', slug_field='slug', queryset=Division.objects.all())

    class Meta:
        model = Genus
        fields = ['slug', 'name',  'family_slug', 'order_slug', 'class_name_slug',
                  'division_slug']


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = '__all__'

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

class SubspeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subspecies
        fields = '__all__'

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

class SortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sort
        fields = '__all__'


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