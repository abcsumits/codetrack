from django.db import models

class profile(models.Model):
    user=models.CharField(max_length=100,default="Not Available")
    first_name=models.CharField(max_length=100,default="Not Available")
    last_name=models.CharField(max_length=100,default="Not Available")
    email=models.EmailField( max_length=254,default="example@email.com")
    codechef=models.CharField(max_length=100,default="Not Available")
    codeforces=models.CharField(max_length=100,default="Not Available")
    leetcode=models.CharField(max_length=100,default="Not Available")
    email_verified=models.BooleanField(default="False")
    leetcode_token=models.CharField(default="Not Available" ,max_length=100)
    codechef_token=models.CharField(default="Not Available" ,max_length=100)
    codeforces_token=models.CharField(default="Not Available" ,max_length=100)
    token=models.CharField(default="Not Available" ,max_length=100)
    leetcode_verified=models.BooleanField(default="False")
    codechef_verified=models.BooleanField(default="False")
    codeforces_verified=models.BooleanField(default="False")
    institute=models.CharField(max_length=100,default="@ Not Available")
    friends=models.JSONField(default=dict)
    followers=models.IntegerField(default=0)
    