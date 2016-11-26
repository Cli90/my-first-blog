#stai attenta all'allineamento#
from django.db import models
from django.utils import timezone

#definiamo le classi#
class Post(models.Model):  #la classe post eredita le proprietà di models#
    author = models.ForeignKey('auth.User') #def proprietà, la chiave attribuisce la proprietà e l'accesso all'utente#
    title = models.CharField(max_length=200) 
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    
    def publish(self): #definisci la pubblicazione è un'azione#
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self): #il self fa riferimento a tutto il blocco#
        return self.title