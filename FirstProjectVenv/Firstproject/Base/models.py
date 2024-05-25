from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post_img=models.ImageField(upload_to='',blank=True,null=True)
    def __str__(self) :
        return self.title
  
  



# step 1:
#     create a model post
# step 2:
#     media settings:https://djangocentral.com/managing-media-files-in-django/
# step 3:
        # run migrations
# step 4
#       register model at admin.py
step 5:
    # create a view to show post
# step 6:
    # create a template to show post
    
# step 7:
#    add a card from bootstrap to show post  :https://getbootstrap.com/docs/5.3/components/card/
    