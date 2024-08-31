from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from ..models import *
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
import json
import datetime

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


def generate_report(request, report_id):
    try:
        report = get_object_or_404(Report, id=report_id, user=request.user)
        print(f"Generando reporte: {report.name}, Tipo: {report.report_type}")
        
        if report.report_type == 'transacciones':
            data = generate_transaction_report(report)
        elif report.report_type == 'presupuestos':
            data = generate_budget_report(report)
        elif report.report_type == 'metas':
            data = generate_goal_report(report)
        else:
            return JsonResponse({'error': 'Tipo de reporte no válido'}, status=400)
        
        return JsonResponse({'data': data})
    except Exception as e:
        print(f"Error al generar el reporte: {str(e)}")
        return JsonResponse({'error': f'Error interno del servidor: {str(e)}'}, status=500)


def generate_transaction_report(report):
    period_start, period_end = get_period_dates(report.report_period)
    transactions = Transaction.objects.filter(user=report.user, date__range=[period_start, period_end])
    
    report_data = {
        'report_name': report.name,
        'report_type': report.report_type,
        'transactions': list(transactions.values()),
    }
    return report_data

def generate_budget_report(report):
    period_start, period_end = get_period_dates(report.report_period)
    budgets = Budget.objects.filter(user=report.user, start_date__lte=period_end, end_date__gte=period_start)
    
    report_data = {
        'report_name': report.name,
        'report_type': report.report_type,
        'budgets': list(budgets.values()),
    }
    return report_data

def generate_goal_report(report):
    period_start, period_end = get_period_dates(report.report_period)
    goals = FinancialGoal.objects.filter(user=report.user, start_date__lte=period_end, end_date__gte=period_start)
    
    report_data = {
        'report_name': report.name,
        'report_type': report.report_type,
        'goals': list(goals.values()),
    }
    return report_data

def get_period_dates(period_type):
    today = datetime.date.today()
    if period_type == 'diario':
        start_date = today
        end_date = today
    elif period_type == 'mensual':
        start_date = today.replace(day=1)
        end_date = today.replace(day=28) + datetime.timedelta(days=4)
        end_date = end_date - datetime.timedelta(days=end_date.day)
    elif period_type == 'anual':
        start_date = today.replace(month=1, day=1)
        end_date = today.replace(month=12, day=31)
    else:
        raise ValueError('Tipo de período no válido')
    
    return start_date, end_date