import cloudinary
from cloudinary.utils import cloudinary_url
from django.conf import settings
from decouple import config
CLOUDINARY_CLOUD_NAME=settings.CLOUDINARY_CLOUD_NAME
CLOUDINARY_SECRET_API_KEY=settings.CLOUDINARY_SECRET_API_KEY
CLOUDINARY_PUBLIC_API_KEY=settings.CLOUDINARY_PUBLIC_API_KEY
# Configuration       
def cloudinary_init():
    cloudinary.config( 
        cloud_name = CLOUDINARY_CLOUD_NAME, 
        api_key = CLOUDINARY_PUBLIC_API_KEY, 
        api_secret = CLOUDINARY_SECRET_API_KEY, # Click 'View API Keys' above to copy your API secret
        secure=True
    )


# # Upload an image
# upload_result = cloudinary.uploader.upload("https://res.cloudinary.com/demo/image/upload/getting-started/shoes.jpg",
#                                            public_id="shoes")
# print(upload_result["secure_url"])

# # Optimize delivery by resizing and applying auto-format and auto-quality
# optimize_url, _ = cloudinary_url("shoes", fetch_format="auto", quality="auto")
# print(optimize_url)

# # Transform the image: auto-crop to square aspect_ratio
# auto_crop_url, _ = cloudinary_url("shoes", width=500, height=500, crop="auto", gravity="auto")
# print(auto_crop_url)