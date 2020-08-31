from django.db import models

# Create your models here.


class SearchHistory(models.Model):

    keyword = models.CharField(max_length=255, null=False)
    wesite = models.CharField(null=False)
    pause = models.IntegerField(null=False, default=2)

    class Meta:
        verbose_name = "SearchHistory"
        verbose_name_plural = "SearchHistorys"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("SearchHistory_detail", kwargs={"pk": self.pk})
