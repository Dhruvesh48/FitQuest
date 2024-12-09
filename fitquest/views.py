from django.shortcuts import render
from .models import Plan

# Create your views here.
def plan_list(request):

    """Display all plans for the current user."""
    plans = Plan.objects.filter(is_active=False)
    context = {
        'plans': plans,
    }
    return render(request, 'fitquest/plan_list.html', context)