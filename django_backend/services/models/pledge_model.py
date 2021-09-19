from django.db import models 

class Pledge(models.Model):
    statement = models.TextField()
    mission = models.TextField()
    impact = models.TextField()
    author = models.ForeignKey(
        'accounts.User',
        related_name='author_of',
        on_delete=models.PROTECT,
    )
    signers = models.ManyToManyField(
        'accounts.User',
        related_name="signed",
        blank=True
    )
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        app_label = "services"