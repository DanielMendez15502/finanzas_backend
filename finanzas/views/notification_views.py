from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import Notification
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
import json

@login_required
@require_http_methods(["GET"])
def list_notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    data = [
        {
            "id": notif.id,
            "message": notif.message,
            "type": notif.type,
            "sent_at": notif.sent_at,
            "status": notif.status,
        } for notif in notifications
    ]
    return JsonResponse(data, safe=False)

@login_required
@require_http_methods(["POST"])
def create_notification(request):
    data = json.loads(request.body)
    notification = Notification.objects.create(
        user=request.user,
        message=data['message'],
        type=data['type'],
        status=data.get('status', 'no leído')
    )
    return JsonResponse({"id": notification.id})

@login_required
@require_http_methods(["DELETE"])
def delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.delete()
    return JsonResponse({"message": "Notificación eliminada correctamente"})
