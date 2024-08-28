from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import TransactionCategory
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
import json

@login_required
@require_http_methods(["GET"])
def list_categories(request):
    categories = TransactionCategory.objects.filter(user=request.user)
    data = [{"id": cat.id, "name": cat.name, "type": cat.type} for cat in categories]
    return JsonResponse(data, safe=False)

@login_required
@require_http_methods(["POST"])
def create_category(request):
    data = json.loads(request.body)
    category = TransactionCategory.objects.create(
        user=request.user,
        name=data['name'],
        type=data['type']
    )
    return JsonResponse({"id": category.id, "name": category.name, "type": category.type})

@login_required
@require_http_methods(["DELETE"])
def delete_category(request, category_id):
    category = get_object_or_404(TransactionCategory, id=category_id, user=request.user)
    category.delete()
    return JsonResponse({"message": "Categoría eliminada correctamente"})
