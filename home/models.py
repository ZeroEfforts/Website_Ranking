from django.db import models

# Create your models here.


class SearchHistory(models.Model):

    keyword = models.CharField(max_length=255, null=False)
    website = models.TextField(null=False)
    pause = models.IntegerField(null=False, default=2)

    class Meta:
        verbose_name = "SearchHistory"
        verbose_name_plural = "SearchHistorys"

    def __str__(self):
        return self.keyword +"|"+self.website

    def get_absolute_url(self):
        return reverse("SearchHistory_detail", kwargs={"pk": self.pk})

class SearchResult(models.Model):

    searchhistory=models.ForeignKey(SearchHistory, on_delete=models.CASCADE)
    totalwebsites=models.IntegerField()
    websiterank=models.IntegerField()

    class Meta:
        verbose_name = "SearchResult"
        verbose_name_plural = "SearchResults"

    def __str__(self):
        return self.websiterank+"/"+self.totalwebsites

    def get_absolute_url(self):
        return reverse("SearchResult_detail", kwargs={"pk": self.pk})
