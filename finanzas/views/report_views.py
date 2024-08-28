from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import Report
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
import json

@login_required
@require_http_methods(["GET"])
def list_reports(request):
    reports = Report.objects.filter(user=request.user)
    data = [
        {
            "id": report.id,
            "name": report.name,
            "created_at": report.created_at,
            "report_type": report.report_type,
            "report_period": report.report_period,
        } for report in reports
    ]
    return JsonResponse(data, safe=False)

@login_required
@require_http_methods(["POST"])
def create_report(request):
    data = json.loads(request.body)
    report = Report.objects.create(
        user=request.user,
        name=data['name'],
        report_type=data['report_type'],
        report_period=data['report_period']
    )
    return JsonResponse({"id": report.id})

@login_required
@require_http_methods(["DELETE"])
def delete_report(request, report_id):
    report = get_object_or_404(Report, id=report_id, user=request.user)
    report.delete()
    return JsonResponse({"message": "Reporte eliminado correctamente"})
