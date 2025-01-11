#from django.db import models
#from django.utils import timezone
#
#class Popularity_Name(models.Model):
#    name = models.CharField(max_length=300)
#
#    def __str__(self):
#        return self.name
#
#
#class Popularity_Sort(models.Model): #популярный сорт
#    name = models.CharField(max_length=300)
#    description = models.TextField()
#    popularity_name = models.ForeignKey(Popularity_Name, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.name
#
#class Name_Popularity_Sort(models.Model): #представители популярного сорта
#    name = models.CharField(max_length=300)
#    popularity_Sort = models.ForeignKey(Popularity_Sort, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.name
#
#
#class Popularity_Subspecies(models.Model): #популярный подвид
#    name = models.CharField(max_length=300)
#    description = models.TextField()
#    popularity_name = models.ForeignKey(Popularity_Name, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.name
#
#
#class Name_Popularity_Subspecies(models.Model): #представители популяроного подвида
#    name = models.CharField(max_length=300)
#    popularity_Sort = models.ForeignKey(Popularity_Subspecies, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.name
#
#class Popularity_Species(models.Model): #популярный вид
#    name = models.CharField(max_length=300)
#    description = models.TextField()
#    popularity_name = models.ForeignKey(Popularity_Name, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.name
#
#
#class Name_Popularity_Species(models.Model): #представители популярного вида
#    name = models.CharField(max_length=300)
#    popularity_Sort = models.ForeignKey(Popularity_Species, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.name
#
#
#class Popularity_Genus(models.Model): #популярный род
#    name = models.CharField(max_length=300)
#    description = models.TextField()
#    popularity_name = models.ForeignKey(Popularity_Name, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.name
#
#
#class Name_Popularity_Genus(models.Model): #представители популярного рада
#    name = models.CharField(max_length=300)
#    popularity_Sort = models.ForeignKey(Popularity_Genus, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.name
#
#class Popularity_Family(models.Model): #популярное семейство
#    name = models.CharField(max_length=300)
#    description = models.TextField()
#
#    def __str__(self):
#        return self.name
#
#
#class Name_Popularity_Family(models.Model): #представители популярного семейства
#    name = models.CharField(max_length=300)
#    popularity_Sort = models.ForeignKey(Popularity_Family, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.name
#
#class Popularity_Orders(models.Model): #популярный порядок
#    name = models.CharField(max_length=300)
#    description = models.TextField()
#    popularity_name = models.ForeignKey(Popularity_Name, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.name
#
#
#class Name_Popularity_Orders(models.Model): #представители популярного порядка
#    name = models.CharField(max_length=300)
#    popularity_Sort = models.ForeignKey(Popularity_Orders, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.name
#
#
#class Popularity_Division(models.Model): #популярный отдел
#    name = models.CharField(max_length=300)
#    description = models.TextField()
#    popularity_name = models.ForeignKey(Popularity_Name, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.name
#
#
#class Name_Popularity_Division(models.Model): #представители популярного отдела
#    name = models.CharField(max_length=300)
#    popularity_Sort = models.ForeignKey(Popularity_Division, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return self.name
#
#class Kingdom(models.Model): #Царство
#    name = models.CharField(max_length=300)
#    description = models.TextField()
#    popularity_division = models.ForeignKey(Popularity_Division, on_delete=models.CASCADE, null=True, default=1)
#    image = models.ImageField(upload_to='kingdoms/')
#
#    class Meta:
#        verbose_name = "Царство"
#        verbose_name_plural = "Царства"
#
#    def __str__(self):
#        return self.name
#
#class Division(models.Model): #Отдел
#    slug = models.SlugField(unique=True)
#    name = models.CharField(max_length=300)
#    description = models.TextField()
#    image = models.ImageField(upload_to='divisions/')
#    popularity = models.IntegerField(default=0)  # Популярность
#    popularity_orders = models.ForeignKey(Popularity_Orders, on_delete=models.CASCADE, null=True, default=1)
#    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
#    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Дата создания
#
#    def save(self, *args, **kwargs):
#        # Устанавливаем путь для изображения в зависимости от genus
#        self.image.field.upload_to = f'divisions/{self.kingdom.name}/'
#        super().save(*args, **kwargs)
#
#    class Meta:
#        verbose_name = "Отдел"
#        verbose_name_plural = "Отделы"
#
#    def __str__(self):
#        return self.name
#
#
#
#class Orders(models.Model): #Порядок
#    slug = models.SlugField(unique=True)
#    name = models.CharField(max_length=300)
#    description = models.TextField()
#    image = models.ImageField(upload_to='orders/')
#    popularity = models.IntegerField(default=0)  # Популярность
#    popularity_family = models.ForeignKey(Popularity_Family, on_delete=models.CASCADE, null=True,)
#    division = models.ForeignKey(Division, on_delete=models.CASCADE)
#    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Дата создания
#
#    def save(self, *args, **kwargs):
#        # Устанавливаем путь для изображения в зависимости от genus
#        self.image.field.upload_to = f'orders/{self.division.kingdom.name}/{self.division.name}/'
#        super().save(*args, **kwargs)
#
#    class Meta:
#        verbose_name = "Порядок"
#        verbose_name_plural = "Порядки"
#
#    def __str__(self):
#        return self.name
#
#
#
#class Family(models.Model): #Семейство
#    slug = models.SlugField(unique=True)
#    name = models.CharField(max_length=300)
#    description = models.TextField()
#    image = models.ImageField(upload_to='family/')
#    popularity = models.IntegerField(default=0)  # Популярность
#    popularity_genus = models.ForeignKey(Popularity_Genus, on_delete=models.CASCADE, null=True)
#    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
#    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Дата создания
#
#    def save(self, *args, **kwargs):
#        # Устанавливаем путь для изображения в зависимости от genus
#        self.image.field.upload_to = f'family/{self.order.division.kingdom.name}/{self.order.division.name}/{self.order.name}/'
#        super().save(*args, **kwargs)
#
#        class Meta:
#            verbose_name = "Семейство"
#            verbose_name_plural = "Семейства"
#
#    def __str__(self):
#        return self.name
#
#class Genus(models.Model): #Род
#    slug = models.SlugField(unique=True)
#    name = models.CharField(max_length=300)
#    description = models.TextField()
#    image = models.ImageField(upload_to='genus/')
#    popularity = models.IntegerField(default=0)  # Популярность
#    popularity_species = models.ForeignKey(Popularity_Species, on_delete=models.CASCADE, null=True)
#    family = models.ForeignKey(Family, on_delete=models.CASCADE)
#    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Дата создания
#
#    def save(self, *args, **kwargs):
#        # Устанавливаем путь для изображения в зависимости от genus
#        self.image.field.upload_to = f'genus/{self.family.order.division.kingdom.name}/{self.family.order.division.name}/{self.family.order.name}/{self.family.name}/'
#        super().save(*args, **kwargs)
#
#    class Meta:
#        verbose_name = "Род"
#        verbose_name_plural = "Роды"
#
#    def __str__(self):
#        return self.name
#
#class Species(models.Model): #Вид
#    slug = models.SlugField(unique=True)
#    name = models.CharField(max_length=300)
#    description = models.TextField()
#    image = models.ImageField(upload_to='species/')
#    popularity = models.IntegerField(default=0)  # Популярность
#    popularity_subspecies = models.ForeignKey(Popularity_Subspecies, on_delete=models.CASCADE, null=True)
#    genus = models.ForeignKey(Genus, on_delete=models.CASCADE)
#    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Дата создания
#
#    def save(self, *args, **kwargs):
#        # Устанавливаем путь для изображения в зависимости от genus
#        self.image.field.upload_to = f'species/{self.genus.family.order.division.kingdom.name}/{self.genus.family.order.division.name}/{self.genus.family.order.name}/{self.genus.family.name}/{self.genus.name}/'
#        super().save(*args, **kwargs)
#
#    class Meta:
#        verbose_name = "Вид"
#        verbose_name_plural = "Виды"
#
#    def __str__(self):
#        return self.name
#
#class Subspecies(models.Model): #Подвид
#    slug = models.SlugField(unique=True)
#    name = models.CharField(max_length=300)
#    description = models.TextField()
#    image = models.ImageField(upload_to='subspecies/')
#    popularity = models.IntegerField(default=0)  # Популярность
#    popularity_sort = models.ForeignKey(Popularity_Sort, on_delete=models.CASCADE, null=True)
#    species = models.ForeignKey(Species, on_delete=models.CASCADE)
#    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Дата создания
#
#    def save(self, *args, **kwargs):
#        # Устанавливаем путь загрузки изображения в зависимости от родительского элемента
#        self.image.field.upload_to = f'subspecies/{self.species.genus.family.order.division.kingdom.name}/{self.species.genus.family.order.division.name}/{self.species.genus.family.order.name}/{self.species.genus.family.name}/{self.species.genus.name}/{self.species.name}/'
#        super().save(*args, **kwargs)
#
#    class Meta:
#        verbose_name = "Подвид"
#        verbose_name_plural = "Подвиды"
#
#    def __str__(self):
#        return self.name
#
#class Sort(models.Model): #Сорт
#    slug = models.SlugField(unique=True)
#    name = models.CharField(max_length=300)
#    description = models.TextField()
#    image = models.ImageField(upload_to='sort/')
#    popularity = models.IntegerField(default=0)  # Популярность
#    subspecies = models.ForeignKey(Subspecies, on_delete=models.CASCADE)
#    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Дата создания
#
#    def save(self, *args, **kwargs):
#        # Устанавливаем путь загрузки изображения в зависимости от родительского элемента
#        self.image.field.upload_to = f'sorts/{self.subspecies.species.genus.family.order.division.kingdom.name}/{self.subspecies.species.genus.family.order.division.name}/{self.subspecies.species.genus.family.order.name}/{self.subspecies.species.genus.family.name}/{self.subspecies.species.genus.name}/{self.subspecies.species.name}/{self.subspecies.name}/'
#        super().save(*args, **kwargs)
#
#    class Meta:
#        verbose_name = "Сорт"
#        verbose_name_plural = "Сорта"
#
#    def __str__(self):
#        return self.name
#
#class Example(models.Model):  # Примеры растений
#    name = models.CharField(max_length=100)
#    image = models.ImageField(upload_to='example/')  # Фото примера
#
#    def __str__(self):
#        return self.name
#
#
#class Type(models.Model): # Типы растений
#    name = models.CharField(max_length=100)
#    description = models.TextField() #Описание
#    characteristics = models.TextField() #Характеристики
#    examples = models.ManyToManyField(Example, related_name='types')  # Связь с примерами
#
#    def __str__(self):
#        return self.name
#
#

from django.db import models
from django.utils import timezone


class Kingdom(models.Model):  # Царство
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='kingdom/')

    class Meta:
        verbose_name = "Царство"
        verbose_name_plural = "Царства"

    def __str__(self):
        return self.name


class Plantae(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    descriptionBig = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='', max_length=500)  # Путь будет установлен в дочерних классах
    popularity = models.IntegerField(default=0)  # Популярность
    created_at = models.DateTimeField(auto_now_add=True, null=True)  # Дата создания

    class Meta:
        abstract = True  # Указываем, что это абстрактная модель

    def save(self, *args, **kwargs):
        # Устанавливаем путь для изображения в зависимости от класса
        self.image.field.upload_to = self.get_upload_to()
        super().save(*args, **kwargs)

    def get_upload_to(self):
        raise NotImplementedError("Subclasses must implement get_upload_to method")


class Division(Plantae):  # Отдел
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    klass= models.BooleanField(default=False)  # Поле для указания наличия класса

    def get_upload_to(self):
        return f'kingdom/{self.slug}/'

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

    def __str__(self):
        return self.name


class PopularDivision(models.Model):  # популярный отдел
    name = models.CharField(max_length=300)
    description = models.TextField()
    kingdom = models.ForeignKey(Kingdom, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='popular_division/')

    class Meta:
        verbose_name = 'Популярный отдел'
        verbose_name_plural = 'Популярные отделы'

    def __str__(self):
        return self.name


class PopularDivisionName(models.Model):  # название представителя популярного отдела
    name = models.CharField(max_length=300)
    popular_division = models.ForeignKey(PopularDivision, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Название представителя популярного отдела'
        verbose_name_plural = 'Название представителей популярных отделов'

    def __str__(self):
        return self.name

class ClassName(Plantae): #Класс
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='classes')

    def get_upload_to(self):
        return f'kingdom/{self.division.slug}/{self.slug}/'

    class Meta:
        verbose_name = "Класс"
        verbose_name_plural = "Классы"

    def __str__(self):
        return self.name


class Orders(Plantae):  # Порядок
    division = models.ForeignKey(Division, on_delete=models.CASCADE, related_name='orders')
    className = models.ForeignKey(ClassName, on_delete=models.CASCADE, null=True, blank=True, related_name='orderClass')

    def get_upload_to(self):
        return f'kingdom/{self.division.slug}/{self.slug}/'

    class Meta:
        verbose_name = "Порядок"
        verbose_name_plural = "Порядки"

    def __str__(self):
        return self.name


class PopularOrders(models.Model):  # популярный порядок
    name = models.CharField(max_length=300)
    description = models.TextField()
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='popular_orders/')

    class Meta:
        verbose_name = 'Популярный порядок'
        verbose_name_plural = 'Популярные порядки'

    def __str__(self):
        return self.name


class PopularOrdersName(models.Model):  # название представителя популярного порядка
    name = models.CharField(max_length=300)
    popular_order = models.ForeignKey(PopularOrders, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Название представителя популярного порядка'
        verbose_name_plural = 'Название представителей популярных порядков'

    def __str__(self):
        return self.name


class Family(Plantae):  # Семейство
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='family')

    def get_upload_to(self):
        return f'kingdom/{self.order.division.slug}/{self.order.slug}/{self.slug}/'

    class Meta:
        verbose_name = "Семейство"
        verbose_name_plural = "Семейства"

    def __str__(self):
        return self.name


class PopularFamily(models.Model):  # популярное семейство
    name = models.CharField(max_length=300)
    description = models.TextField()
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='popular_family/')

    class Meta:
        verbose_name = 'Популярное семейство'
        verbose_name_plural = 'Популярные семейства'

    def __str__(self):
        return self.name


class PopularFamilyName(models.Model):  # название представителя популярного семейства
    name = models.CharField(max_length=300)
    popular_family = models.ForeignKey(PopularFamily, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Название представителя популярного семейства'
        verbose_name_plural = 'Название представителей популярных семейств'

    def __str__(self):
        return self.name


class Genus(Plantae):  # Род
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='genus')

    def get_upload_to(self):
        return f'kingdom/{self.family.order.division.slug}/{self.family.order.slug}/{self.family.slug}/{self.slug}/'

    class Meta:
        verbose_name = 'Род'
        verbose_name_plural = 'Роды'

    def __str__(self):
        return self.name


class PopularGenus(models.Model):  # популярный род
    name = models.CharField(max_length=300)
    description = models.TextField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='popular_genus/')

    class Meta:
        verbose_name = 'Популярный род'
        verbose_name_plural = 'Популярные роды'

    def __str__(self):
        return self.name


class PopularGenusName(models.Model):  # название представителя популярного рода
    name = models.CharField(max_length=300)
    popular_genus = models.ForeignKey(PopularGenus, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Название представителя популярного рода'
        verbose_name_plural = 'Название представителей популярных родов'

    def __str__(self):
        return self.name

class TypeRose(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='popular_rose/', null=True, blank=True)
    genusRose = models.ForeignKey(Genus, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='genusRoses')

    class Meta:
        verbose_name = 'Типы роз'
        verbose_name_plural = 'Типы роз'

    def __str__(self):
        return self.name

class Species(Plantae):  # Вид
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE, related_name='species')
    speciesRose = models.ForeignKey(TypeRose, on_delete=models.CASCADE, null=True, blank=True, related_name='speciesRose')

    def get_upload_to(self):
        return f'kingdom/{self.genus.family.order.division.slug}/{self.genus.family.order.slug}/{self.genus.family.slug}/{self.genus.slug}/{self.slug}/'

    class Meta:
        verbose_name = 'Вид'
        verbose_name_plural = 'Виды'

    def __str__(self):
        return self.name


class PopularSpecies(models.Model):  # популярный вид
    name = models.CharField(max_length=300)
    description = models.TextField()
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='popular_species/')

    class Meta:
        verbose_name = 'Популярный вид'
        verbose_name_plural = 'Популярные виды'

    def __str__(self):
        return self.name


class PopularSpeciesName(models.Model):  # название представителя популярного вида
    name = models.CharField(max_length=300)
    popular_species = models.ForeignKey(PopularSpecies, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Название представителя популярного вида'
        verbose_name_plural = 'Название представителей популярных видов'

    def __str__(self):
        return self.name


class Subspecies(Plantae):  # Подвид
    species = models.ForeignKey(Species, on_delete=models.CASCADE, related_name='subspecies')

    def get_upload_to(self):
        return f'kingdom/{self.species.genus.family.order.division.slug}/{self.species.genus.family.order.slug}/{self.species.genus.family.slug}/{self.species.genus.slug}/{self.species.slug}/{self.slug}/'

    class Meta:
        verbose_name = 'Подвид'
        verbose_name_plural = 'Подвиды'

    def __str__(self):
        return self.name


class PopularSubspecies(models.Model):  # популярный подвид
    name = models.CharField(max_length=300)
    description = models.TextField()
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='popular_subspecies/')

    class Meta:
        verbose_name = 'Популярный подвид'
        verbose_name_plural = 'Популярные подвиды'

    def __str__(self):
        return self.name


class PopularSubspeciesName(models.Model):  # название представителя популярного подвида
    name = models.CharField(max_length=300)
    popular_subspecies = models.ForeignKey(PopularSubspecies, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Название представителя популярного подвида'
        verbose_name_plural = 'Название представителей популярных подвидов'

    def __str__(self):
        return self.name


class Sort(Plantae):  # Сорт
    species = models.ForeignKey(Species, on_delete=models.CASCADE, null=True, blank=True, related_name='sortSpecies')
    subspecies = models.ForeignKey(Subspecies, on_delete=models.CASCADE, null=True, blank=True, related_name='sortSubspecies')

    def get_upload_to(self):
        return f'kingdom/{self.species.genus.family.order.division.slug}/{self.species.genus.family.order.slug}/{self.species.genus.family.slug}/{self.species.genus.slug}/{self.species.slug}/{self.slug}/'

    class Meta:
        verbose_name = 'Сорт'
        verbose_name_plural = 'Сорта'

    def __str__(self):
        return self.name


class PopularSort(models.Model):  # популярный сорт
    name = models.CharField(max_length=300)
    description = models.TextField()
    subspecies = models.ForeignKey(Subspecies, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='popular_sort/')

    class Meta:
        verbose_name = 'Популярный сорт'
        verbose_name_plural = 'Популярные сорта'

    def __str__(self):
        return self.name


class PopularSortName(models.Model):  # название представителя популярного сорта
    name = models.CharField(max_length=300)
    popular_sort = models.ForeignKey(PopularSort, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Название представителя популярного сорта'
        verbose_name_plural = 'Название представителей популярных сортов'

    def __str__(self):
        return self.name


class Example(models.Model):  # Примеры растений
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='example/')  # Фото примера

    class Meta:
        verbose_name = 'Пример типов растений'
        verbose_name_plural = 'Примеры типов растений'

    def __str__(self):
        return self.name


class Type(models.Model):  # Типы растений
    name = models.CharField(max_length=100)
    description = models.TextField()  # Описание
    characteristics = models.TextField()  # Характеристики
    examples = models.ManyToManyField(Example, related_name='types')  # Связь с примерами

    class Meta:
        verbose_name = 'Тип растений'
        verbose_name_plural = 'Типы растений'

    def __str__(self):
        return self.name


class CharacteristicsKingdom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Характеристика царства'
        verbose_name_plural = 'Характеристики царства'

    def __str__(self):
        return self.name