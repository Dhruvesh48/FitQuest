from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    BODY_TYPE_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('toned', 'Toned and Lean'),
        ('general_fitness', 'General Fitness'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    body_type = models.CharField(
        max_length=50,
        choices=BODY_TYPE_CHOICES,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class Plan(models.Model):
    BODY_TYPE_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('toned', 'Toned and Lean'),
        ('general_fitness', 'General Fitness'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    training_plan = models.TextField(default='Training plan')
    body_type = models.CharField(
        max_length=50,
        choices=BODY_TYPE_CHOICES,
        blank=True,
        null=True
    )
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def duration(self):
        """Calculate the duration of the plan in days."""
        return (self.end_date - self.start_date).days
    
class NutritionalPlan(models.Model):
    BODY_TYPE_CHOICES = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('toned', 'Toned and Lean'),
        ('general_fitness', 'General Fitness'),
    ]

    body_type = models.CharField(max_length=50, choices=BODY_TYPE_CHOICES)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='nutritional_plans')
    meal_name = models.CharField(max_length=255)
    description = models.TextField()
    calories = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.body_type.title()} - {self.meal_name}"
    
class Task(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({'Completed' if self.is_completed else 'Pending'})"
    
class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='progress')
    date = models.DateField(auto_now_add=True)
    tasks_completed = models.IntegerField(default=0)
    total_tasks = models.IntegerField(default=0)

    def calculate_completion_rate(self):
        if self.total_tasks > 0:
            return (self.tasks_completed / self.total_tasks) * 100
        return 0

    def __str__(self):
        return f"Progress for {self.plan.title} on {self.date}"
    
class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.friend.username}"
    
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='activities', null=True, blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='activities', null=True, blank=True)
    activity_type = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.activity_type}"