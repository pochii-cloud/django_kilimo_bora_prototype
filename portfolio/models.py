from django.db import models


# Create your models here.
class Query(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=500)
    response = models.CharField(max_length=500, default='Question not yet answered.check later')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Queries'
        ordering = ['-id']
