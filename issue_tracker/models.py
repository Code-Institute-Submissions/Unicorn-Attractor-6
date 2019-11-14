from django.db import models, IntegrityError
from django.utils import timezone
from django.contrib.auth.models import User

TASK_CHOICES = (
    ('to do','TODO'),
    ('doing','DOING'),
    ('done','DONE'),
)

class Bug(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=False)
    author = models.ForeignKey(User, related_name='features', on_delete=models.CASCADE, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    votes = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    status = models.CharField(max_length=6, choices=TASK_CHOICES, default='to do')
    
    def upvote(self, user):
        try:
            self.bug_votes.create(user=user, Bug=self, vote_type="up")
            self.votes += 1
            self.save()                
        except IntegrityError:
            return 'already_upvoted'
        return 'ok'
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    bug = models.ForeignKey(Bug, related_name='comments', null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    i_have_this_too = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    
    def __unicode__(self):
        return self.bug
