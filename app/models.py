from django.db import models

class ContactSubmission(models.Model):
    full_name = models.CharField(max_length=150)
    email     = models.EmailField()
    phone     = models.CharField(max_length=20)
    city      = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Project(models.Model):
    image       = models.ImageField(upload_to='projects/')
    name        = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Client(models.Model):
    image       = models.ImageField(upload_to='clients/')
    name        = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class NewsletterSubscription(models.Model):
    email         = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email