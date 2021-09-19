from django.db import models
from django.utils.translation import gettext_lazy as _


class Action(models.Model):

    class FrequencySelect(models.TextChoices):
        ONCE = 'O', _(" Once ")
        DAILY = 'D', _(" Daily ")
        WEEKLY = 'W', _(" Weekly ")
        MONTHLY = 'M', _(" Monthly ")
        YEARLY = 'Y', _(" Yearly ")

    title = models.CharField(max_length=255)
    unit = models.CharField(max_length=50, db_index=True, verbose_name="units")
    uamount = models.FloatField()
    frequency = models.CharField(
        max_length=1,
        choices=FrequencySelect.choices,
        default=FrequencySelect.DAILY
    )
    parent_pledge = models.ForeignKey('Pledge', on_delete=models.PROTECT, related_name="action", related_query_name="actions")
    created = models.DateField(auto_now_add=True)

    class Meta:
        app_label = "services"
