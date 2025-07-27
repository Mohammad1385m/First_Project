from django.db import models

# Create your models here.

class Contact_Us_Model(models.Model):
    name = models.CharField()
    phone = models.CharField()
    email = models.EmailField()
    subject = models.CharField()
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    response = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.subject}"

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
