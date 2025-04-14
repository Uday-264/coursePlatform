from django.db import models

class AccessRequirement(models.TextChoices):
    ANYONE="any","Anyone"
    EMAIL_REQUIRED="email","Email Required"

class publicStatus(models.TextChoices):
    PUBLISHED="publish","Published"
    COMMING_SOON="soon","Comming Soon"
    DRAFT="draft","Draft"

# Create your models here.
class Course(models.Model):
    title=models.CharField()
    description=models.TextField(blank=True,null=True)
    # image
    access=models.CharField(max_length=10,choices=AccessRequirement.choices)
    status=models.CharField(max_length=10,
                            choices=publicStatus.choices,
                            default=publicStatus.DRAFT
                            )
    @property
    def is_published(self):
        return self.status==publicStatus.PUBLISHED
    