from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q

from .choices import CourseChoices, SocietyChoices, InterestChoices, GenderChoices, LibraryFloorChoices

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GenderChoices.get_choices())
    bio = models.TextField(max_length=300)
    year_in = models.IntegerField()
    location = models.CharField(max_length=30)
    library_floor = models.CharField(max_length=20, choices=LibraryFloorChoices.get_choices())
    looking_for = models.CharField(max_length=1, choices=GenderChoices.get_choices())   # Allow to pick one, not multiple

    # TODO: deal with media files 
    image1 = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    image2 = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    image3 = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    image4 = models.ImageField(upload_to='profile_pics', blank=True, null=True)
    image5 = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    course = models.ForeignKey("Course", on_delete=models.SET_NULL, null=True)
    interests = models.ManyToManyField("Interest")
    societies = models.ManyToManyField("Society")

    def get_matches(self):
        return Match.objects.filter(Q(profile1=self) | Q(profile2=self))

    def __str__(self):
        return self.user.username

class Like(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="likes")
    profile_liked = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="liked")
    is_liked = models.BooleanField()  # if false - represents a dislike, if true - like

    def __str__(self):
        if is_liked: 
            return self.profile + " liked " + self.profile_liked
        elif not is_liked:
            return self.profile + " disliked " + self.profile_liked

class Match(models.Model):
    profile1 = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="matches")
    profile2 = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="matched")
    time_matched = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Match between " + self.profile1 + " and " + self.profile2

    class Meta:
        verbose_name_plural = "Matches"

class Message(models.Model):
    sender = models.OneToOneField(Profile, on_delete=models.SET_NULL, null=True, related_name="sender")
    receiver = models.OneToOneField(Profile, on_delete=models.SET_NULL, null=True, related_name="receiver")
    msg_content = models.TextField(max_length=500)
    time_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.msg_content

class Society(models.Model):
    society = models.CharField(max_length=50, choices=SocietyChoices.get_choices())

    def __str__(self):
        return self.society

    class Meta:
        verbose_name_plural = 'Societies'

class Course(models.Model):
    course = models.CharField(max_length=50, choices=CourseChoices.get_choices())

    def __str__(self):
        return self.course

class Interest(models.Model):
    interest = models.CharField(max_length=30, choices=InterestChoices.get_choices())

    def __str__(self):
        return self.interest