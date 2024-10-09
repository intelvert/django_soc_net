from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post_text=models.CharField(max_length=300)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.author.username}: {self.post_text}'
    
    
class Like(models.Model):
    post=models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together= ('post', 'user') #each like has unique user
        
    def __str__(self) -> str:
        return f'{self.user.username} likes Post {self.post.id}'