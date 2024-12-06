from django.contrib import admin
from .models import Profile, Plan, Task, Progress, Friend, Activity

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)

class PlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'user', 'is_completed')
    list_filter = ('category', 'is_completed')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'plan', 'due_date', 'is_completed')
    list_filter = ('is_completed',)

class ProgressAdmin(admin.ModelAdmin):
    list_display = ('plan', 'date', 'tasks_completed', 'total_tasks')

class FriendAdmin(admin.ModelAdmin):
    list_display = ('user', 'friend', 'created_at')

class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'created_at')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Progress, ProgressAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(Activity, ActivityAdmin)