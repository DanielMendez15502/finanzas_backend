from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import Transaction, TransactionCategory
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
import json

@login_required
@require_http_methods(["GET"])
def list_transactions(request):
    transactions = Transaction.objects.filter(user=request.user)
    data = [
        {
            "id": trans.id,
            "category": trans.category.name,
            "amount": trans.amount,
            "date": trans.date,
            "description": trans.description,
            "type": trans.type,
            "tag": trans.tag,
        } for trans in transactions
    ]
    return JsonResponse(data, safe=False)

@login_required
@require_http_methods(["POST"])
def create_transaction(request):
    data = json.loads(request.body)
    category = get_object_or_404(TransactionCategory, id=data['category'], user=request.user)
    transaction = Transaction.objects.create(
        user=request.user,
        category=category,
        amount=data['amount'],
        date=data['date'],
        description=data.get('description', ''),
        type=data['type'],
        tag=data.get('tag', '')
    )
    return JsonResponse({"id": transaction.id})

@login_required
@require_http_methods(["DELETE"])
def delete_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    transaction.delete()
    return JsonResponse({"message": "Transacción eliminada correctamente"})
