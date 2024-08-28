from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import Budget, TransactionCategory
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
import json

@login_required
@require_http_methods(["GET"])
def list_budgets(request):
    budgets = Budget.objects.filter(user=request.user)
    data = [
        {
            "id": budget.id,
            "category": budget.category.name,
            "amount": budget.amount,
            "period": budget.period,
            "start_date": budget.start_date,
            "end_date": budget.end_date,
            "name": budget.name,
        } for budget in budgets
    ]
    return JsonResponse(data, safe=False)

@login_required
@require_http_methods(["POST"])
def create_budget(request):
    data = json.loads(request.body)
    category = get_object_or_404(TransactionCategory, id=data['category_id'], user=request.user)
    budget = Budget.objects.create(
        user=request.user,
        category=category,
        amount=data['amount'],
        period=data['period'],
        start_date=data['start_date'],
        end_date=data.get('end_date'),
        name=data.get('name', '')
    )
    return JsonResponse({"id": budget.id})

@login_required
@require_http_methods(["DELETE"])
def delete_budget(request, budget_id):
    budget = get_object_or_404(Budget, id=budget_id, user=request.user)
    budget.delete()
    return JsonResponse({"message": "Presupuesto eliminado correctamente"})
