from django.shortcuts import render, get_object_or_404, redirect
from .models import Plan, Task, Progress

# Create your views here.
def plan_list(request):

    """Display all plans for the current user."""
    plans = Plan.objects.filter(is_active=False)
    context = {
        'plans': plans,
    }
    return render(request, 'fitquest/plan_list.html', context)

def plan_detail(request, plan_id):
    """
    View to display the details of a specific plan.
    """
    plan = get_object_or_404(Plan, id=plan_id)
    context = {
        'plan': plan,
    }
    return render(request, 'fitquest/plan_detail.html', context)

def view_tasks(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    tasks = Task.objects.filter(plan=plan).order_by('due_date')
    progress, created = Progress.objects.get_or_create(user=request.user, plan=plan)
    
    context = {
        'plan': plan,
        'tasks': tasks,
        'progress': progress,
    }
    return render(request, 'fitquest/view_tasks.html', context)

def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = not task.is_completed
    task.save()

    progress = Progress.objects.get(user=request.user, plan=task.plan)
    completed_tasks = Task.objects.filter(plan=task.plan, is_completed=True).count()
    total_tasks = Task.objects.filter(plan=task.plan).count()
    progress.tasks_completed = completed_tasks
    progress.total_tasks = total_tasks
    progress.save()

    return redirect('view_tasks', plan_id=task.plan.id)