from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import FinancialGoal
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
import json
from decimal import Decimal

@login_required
@require_http_methods(["GET"])
def list_goals(request):
    goals = FinancialGoal.objects.filter(user=request.user)
    data = [
        {
            "id": goal.id,
            "name": goal.name,
            "target_amount": goal.target_amount,
            "saved_amount": goal.saved_amount,
            "start_date": goal.start_date,
            "deadline": goal.deadline,
            "status": goal.status,
        } for goal in goals
    ]
    return JsonResponse(data, safe=False)

@login_required
@require_http_methods(["POST"])
def create_goal(request):
    data = json.loads(request.body)
    goal = FinancialGoal.objects.create(
        user=request.user,
        name=data['name'],
        target_amount=data['target_amount'],
        saved_amount=data.get('saved_amount', 0),
        start_date=data['start_date'],
        deadline=data['deadline'],
        status=data.get('status', 'en progreso')
    )
    return JsonResponse({"id": goal.id})

@login_required
@require_http_methods(["DELETE"])
def delete_goal(request, goal_id):
    goal = get_object_or_404(FinancialGoal, id=goal_id, user=request.user)
    goal.delete()
    return JsonResponse({"message": "Meta eliminada correctamente"})


@login_required
@require_http_methods(["POST"])
def abonar_meta(request, goal_id):
    goal = get_object_or_404(FinancialGoal, id=goal_id, user=request.user)
    
    data = json.loads(request.body)
    abono = Decimal(data['abono'])  # Convertir el abono a Decimal
    
    # Verificar si la suma de saved_amount y abono excede el target_amount
    if goal.saved_amount + abono > goal.target_amount:
        return JsonResponse({'status': 'error', 'message': 'El abono excede el monto objetivo'}, status=400)

    goal.saved_amount += abono  # Sumar el abono al monto ahorrado
    goal.save()

    return JsonResponse({'status': 'success', 'saved_amount': float(goal.saved_amount)})