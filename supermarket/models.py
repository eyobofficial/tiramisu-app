from django.db import models
from django.urls import reverse


class Catagory(models.Model):
    """
    Abstracts catagory of products
    Example: Electronics, Juice, Beverage, Snacks etc...
    """
    title = models.CharField('Catagory Title', max_length=60,)
    description = models.TextField(null=True, blank=True,)

    class Meta:
        ordering = ['title', ]
        verbose_name = 'Product Catagory'
        verbose_name_plural = 'Product Catagories'

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('supermarket:catagory-detail', args=[str(self.pk)])


class Brand(models.Model):
    """
    Abstracts product brands
    Example: Mac-coffee, Nestle, Genesis Farm, Coca-cola, Sony etc...
    """
    title = models.CharField('Brand Title', max_length=60)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['title', ]
        verbose_name = 'Product Brand'
        verbose_name_plural = 'Product Brands'

    def __str__(self):
        return self.title

    def get_absolute_url(self, *args, **kwargs):
        return reverse('supermarket:brand-detail', args=[str(self.pk)])


class Tag(models.Model):
    """
    Abstracts a Tag to identify a product
    Example:
    Sony, Electronics, LED, Entertainment
    """
    title = models.CharField('Tag Name', max_length=30)


class Product(models.Model):
    """
    Abstracts a particular Product item
    Example: Mango Juice, 42' Sony LED TV, etc...
    """
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField('Product Name', max_length=100)
    description = models.TextField(
        'Product Description',
        null=True,
        blank=True
    )
    price = models.DecimalField(max_digits=8, decimal_places=2)
    thumbnail = models.ImageField(
        upload_to='thumbnails/',
        null=True, blank=True
    )
    expiration_date = models.DateField(
        'Product Expiration Date',
        null=True,
        blank=True,
    )
    on_sale = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title', 'price', ]

    def get_absolute_url(self, *args, **kwargs):
        return reverse('supermarket:product-detail', args=[str(self.pk)])

    def __str__(self):
        return self.title


class Section(models.Model):
    """
    Abstract (section)location of a product in the Supermarket
    Example: Fruits Section, Snack Section, Beverage Section etc..
    """
    FLOOR_OPTIONS = (
        ('first', 'First Floor'),
        ('second', 'Second Floor'),
        ('third', 'Third Floor'),
    )
    title = models.CharField('Floor Section Title', max_length=60)
    floor = models.CharField(max_length=60, choices=FLOOR_OPTIONS)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['floor', 'title', ]

    def get_absolute_url(self, *args, **kwargs):
        return reverse('supermarket:section-detail', args=[str(self.pk)])

    def __str__(self):
        return self.title


class Inventory(models.Model):
    """
    Abstracts Product Inventory
    """
    section = models.ForeignKey(Section, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.IntegerField(blank=True, null=True, default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['product', ]

    def get_absolute_url(self, *args, **kwargs):
        return reverse('supermarket:Inventory-detail', args=[str(self.pk)])

    def __str__(self):
        return self.product

