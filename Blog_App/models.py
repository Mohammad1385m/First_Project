from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Blog_Model(models.Model):
    title = models.CharField()
    image = models.ImageField(upload_to="blogs/images/")
    short_description = models.TextField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE,null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, allow_unicode=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Block_Content_Model(models.Model):
    BLOCK_TYPES = (
        ("title_box", "Title Box"),
        ("start_box", "Start Box"),
        ("paragraph_box", "Paragraph Box"),
        ("quote_box", "Quote Box"),
        ("image_box", "Image Box"),
        ("alert_box", "Alert Box"),
        ("end_box", "End Box"),
    )
    blog = models.ForeignKey(to=Blog_Model, on_delete=models.CASCADE, related_name="contents")
    block_type = models.CharField(choices=BLOCK_TYPES)
    order = models.PositiveIntegerField()
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="blogs/images/extra/", null=True, blank=True)
    caption = models.CharField(null=True, blank=True)

    def __str__(self):
        return f"{self.blog} - {self.block_type} - {self.order}"

    class Meta:
        ordering = ["order"]