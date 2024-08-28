from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from ..models import UserProfile, Debt, Investment, TransactionCategory,Transaction
import json
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def guardar_informacion_general(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            ingresos_mensuales = data.get('ingresosMensuales')
            gastos_mensuales = data.get('gastosMensuales')

            if not ingresos_mensuales or not gastos_mensuales:
                return JsonResponse({'error': 'Los campos de Ingresos Mensuales y Gastos Mensuales son obligatorios.'}, status=400)

            ahorra_regularmente = data.get('ahorraRegularmente')
            porcentaje_ahorro = data.get('porcentajeAhorro', None)

            # Obtener o crear el perfil del usuario autenticado
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)

            # Actualizar los campos del perfil del usuario
            user_profile.ingresos_mensuales = ingresos_mensuales
            user_profile.gastos_mensuales = gastos_mensuales
            user_profile.ahorra_regularmente = ahorra_regularmente == 'si'
            if ahorra_regularmente == 'si' and porcentaje_ahorro:
                user_profile.porcentaje_ahorro = porcentaje_ahorro

            # Guardar los cambios en la base de datos para el perfil
            user_profile.save()

            # Puedes agregar lógica para las otras entidades aquí

            return JsonResponse({'message': 'Información general guardada correctamente'}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Datos JSON inválidos'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obtener_informacion_por_id(request, id):
    try:
        # Obtener el perfil del usuario por ID
        user_profile = UserProfile.objects.get(id=id)

        # Preparar los datos para la respuesta
        data = {
            'user_id': user_profile.user.id,
            'ingresosMensuales': user_profile.ingresos_mensuales,
            'gastosMensuales': user_profile.gastos_mensuales,
            'ahorraRegularmente': 'si' if user_profile.ahorra_regularmente else 'no',
            'porcentajeAhorro': user_profile.porcentaje_ahorro,
            # Puedes agregar más campos aquí si es necesario
        }

        return JsonResponse(data, status=200)

    except UserProfile.DoesNotExist:
        return JsonResponse({'error': 'Perfil de usuario no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    

@csrf_exempt
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obtener_transacciones_recientes(request):
    user = request.user
    transacciones = Transaction.objects.filter(user=user).order_by('-date')[:10]  # Últimas 10 transacciones

    ingresos = []
    gastos = []

    for transaccion in transacciones:
        if transaccion.type == 'ingreso':
            ingresos.append({
                'fecha': transaccion.date,
                'ingresos': float(transaccion.amount),
                'gastos': 0
            })
        else:
            gastos.append({
                'fecha': transaccion.date,
                'ingresos': 0,
                'gastos': float(transaccion.amount)
            })

    data = {
        'ingresos': ingresos,
        'gastos': gastos,
    }

    return JsonResponse(data, safe=False)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obtener_flujo_caja(request, user_id):
    # Obtener todas las transacciones del usuario
    transactions = Transaction.objects.filter(user_id=user_id).order_by('date')
    
    flujo_caja = []
    saldo_acumulado = 0

    for transaction in transactions:
        if transaction.type == 'ingreso':
            saldo_acumulado += transaction.amount
        else:
            saldo_acumulado -= transaction.amount
        flujo_caja.append({
            'fecha': transaction.date,
            'cantidad': saldo_acumulado,
        })
    
    return JsonResponse(flujo_caja, safe=False,status=200)


@login_required
def obtener_distribucion_gastos(request):
    gastos_por_categoria = Transaction.objects.filter(user=request.user, type='gasto')\
        .values('category__name')\
        .annotate(total=Sum('amount'))\
        .order_by('-total')
    
    data = [{'categoria': gasto['category__name'], 'monto': gasto['total']} for gasto in gastos_por_categoria]
    
    return JsonResponse(data, safe=False)