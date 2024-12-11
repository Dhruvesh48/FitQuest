from django.contrib import admin
from .models import Profile, Plan, NutritionalPlan, Task, Progress, Friend, Activity
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

class PlanAdmin(SummernoteModelAdmin):
    list_display = ('title', 'body_type', 'is_completed')
    list_filter = ('body_type', 'is_completed')
    summernote_field = ('training_plan',)

class NutritionalPlanAdmin(SummernoteModelAdmin):
    list_display = ('body_type', 'meal_name', 'plan', 'calories', 'created_at', 'updated_at')
    list_filter = ('body_type', 'plan')
    summernote_field = ('description',)

class TaskAdmin(SummernoteModelAdmin):
    list_display = ('title', 'plan', 'due_date', 'is_completed')
    list_filter = ('is_completed',)
    summernote_field = ('description',)

class ProgressAdmin(admin.ModelAdmin):
    list_display = ('plan', 'date', 'tasks_completed', 'total_tasks')

class FriendAdmin(admin.ModelAdmin):
    list_display = ('user', 'friend', 'created_at')

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'created_at')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(NutritionalPlan, NutritionalPlanAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Progress, ProgressAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(Activity, ActivityAdmin)