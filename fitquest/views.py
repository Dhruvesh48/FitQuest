from django.shortcuts import render, get_object_or_404
from .models import Plan

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