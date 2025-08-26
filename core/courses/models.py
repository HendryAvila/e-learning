from django.contrib.auth.models import User
from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="courses_created"
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="courses"
    )
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ["title"]

    def __str__(self):
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Module"
        verbose_name_plural = "Modules"
        ordering = ["title"]

    def __str__(self):
        return self.title
