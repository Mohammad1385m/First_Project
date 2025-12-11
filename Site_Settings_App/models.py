from django.db import models

# Create your models here.

class SiteSettings(models.Model):
    title = models.CharField()
    logo = models.ImageField(upload_to="logo/")
    support_phone = models.CharField()
    email = models.EmailField()
    footer_logo = models.ImageField(upload_to="logo/")
    footer_description = models.TextField()
    post_code = models.CharField()
    address = models.TextField()
    business_time = models.CharField()
    instagram = models.URLField()
    telegram = models.URLField()
    whatsapp = models.URLField()
    eitaa = models.CharField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.id

class Sliders(models.Model):
    SLIDER_TYPE = (
        ("main_slider", "Main Slider"),
        ("most_sold_slider", "Most-Sold Slider"),
        ("categories_slider", "Categories Slider"),
        ("new_products_slider", "New-Products Slider"),
        ("brands_slider","Brands Slider"),
        ("blogs_slider", "Blogs Slider"),
        ("best_products_slider", "Best-Products Slider"),
        ("popular_products_slider", "Popular-Products Slider"),
    )
    slider_type = models.CharField(choices=SLIDER_TYPE)
    image = models.ImageField(upload_to="sliders/")
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.slider_type} - {self.id}"
