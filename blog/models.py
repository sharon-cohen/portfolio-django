from django.db import models
from django.contrib.auth.models import User


# create a tuple for the status of each post
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)
TYPE_PROJ=(
    ('0','c'),
    ('1','c++'),
    ('2','flutter'),
    ('3','web'),
)

# each field in this class represents a column in the database table
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    url=models.URLField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    type_proj = models.CharField(max_length=1,choices=TYPE_PROJ, default='C')

    # this class contains metadata and uses the created_on field from the model to sort out data which sorts
    # in descending order by default
    
    class Meta:
        ordering = ['-created_on']

    
    # this method is the default human-readable representation of the object. Django will use it in many places
    # such as the admin panel
    def __str__(self):
        return self.title