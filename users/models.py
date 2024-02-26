from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserAccoountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        email = email.lower()
        
        user = self.model(
            first_name =first_name,
            last_name=last_name,
            email=email,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, first_name, last_name, email, password=None):
        user = self.create_user(
            first_name,
            last_name,
            email,
            password=password,
        )
        
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user
    
class UserAccount(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile/images', null=True, blank=True)
    
    objects = UserAccoountManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", 'last_name']
    
    def __str__(self) -> str:
        return self.email
    
class Article(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Article by {self.user.email} - {self.date}"

class Comment(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.email} on {self.article}"