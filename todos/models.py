from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.core import validators
from django.core.exceptions import ValidationError
from django.template.defaultfilters import filesizeformat
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from django.urls import reverse
User = get_user_model()


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-is_done', '-date']
        unique_together = ('user', 'title')

def profile_size(value):
    SIZE = 1024 * 1024 * 0.5
    if value.size > SIZE:
        raise ValidationError(f"Image size is {filesizeformat(value.size)} required {filesizeformat(SIZE)}")

def profile_name(instance, filename):
    return f"post/cover/{instance.__str__().lower()}.{filename.split('.')[-1]}"

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class UserPost(models.Model):
    title = models.CharField(_("Title"), max_length=250, help_text=_("the slug is auto genrated by the title."))
    body = RichTextField(config_name="my-custom-toolbar")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length = 250, unique=True, null=True, blank=True, editable=False)
    vote = models.PositiveIntegerField(default=0, editable=False)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    cover = models.FileField(
        upload_to=profile_name, verbose_name="Book cover",
        default="post/cover/image.png", blank=True,
        validators=[validators.FileExtensionValidator(
                allowed_extensions=validators.get_available_image_extensions(),
                message="Select valid Cover Image."), profile_size
        ],
    )

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title} by {self.user.get_full_name()}")
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        # Admin use only Lol :-)
        return reverse('userpost-detail', kwargs={'slug': self.slug})
    
class UserComment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
class UserLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} like {self.post}"
    
    class Meta:
        unique_together = ('user', 'post',)