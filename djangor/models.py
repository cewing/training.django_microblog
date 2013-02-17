from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Entry(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    author = models.ForeignKey(User)
    pub_date = models.DateTimeField()

    class Meta:
        ordering = ['-pub_date', ]
        verbose_name_plural = "entries"

    def __unicode__(self):
        return self.title

    def save(self):
        if not self.pk:
            # this object is new, set pub_date
            self.pub_date = timezone.now()
        super(Entry, self).save()
