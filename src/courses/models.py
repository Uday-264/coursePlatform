import helpers
from django.db import models
from cloudinary.models import CloudinaryField
helpers.cloudinary_init() 
class AccessRequirement(models.TextChoices):
    ANYONE="any","Anyone"
    EMAIL_REQUIRED="email_required","Email Required"

class publicStatus(models.TextChoices):
    PUBLISHED="publish","Published"
    COMMING_SOON="soon","Comming Soon"
    DRAFT="draft","Draft"

def handle_upload(instance,filename):
    return f"{filename}"
# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField(blank=True,null=True)
    # image=models.ImageField(upload_to=handle_upload,blank=True,null=True)
    image=CloudinaryField("image",null=True)
    access=models.CharField(max_length=15,
                            choices=AccessRequirement.choices,
                            default=AccessRequirement.EMAIL_REQUIRED
                            )
    status=models.CharField(max_length=10,
                            choices=publicStatus.choices,
                            default=publicStatus.DRAFT
                            )
    @property
    def is_published(self):
        return self.status==publicStatus.PUBLISHED
    @property
    def image_admin_url(self):
        if not self.image:
            return ''
        image_options={
            "width":200
        }
        url=self.image.build_url(**image_options)
        return url
    
    def get_image_thumbnail(self,as_html=False,width=500):
        if not self.image:
            return ''
        image_options={
            "width":width
        }
        if as_html:
            return self.image.image(**image_options)
            # it is like above CloudinaryImage(cloudinary_id).image(width=500)
        url=self.image.build_url(**image_options)
        # CloudinaryImage(cloudinary_id).build_url(width=500)
        return url