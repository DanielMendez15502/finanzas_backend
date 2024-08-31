from django.urls import path
from ..views import register, login, procesosGenerales
from ..views import (
    list_categories, create_category, delete_category,
    list_transactions, create_transaction, delete_transaction,
    list_budgets, create_budget, delete_budget,
    list_goals, create_goal, delete_goal,
    list_reports, create_report, delete_report,
    list_notifications, create_notification, delete_notification, SavingsListCreateView, SavingsRetrieveUpdateDestroyView,
    DebtListCreateView, DebtRetrieveUpdateDestroyView,
    InvestmentListCreateView, InvestmentRetrieveUpdateDestroyView,
    FinancialProfileListCreateView, FinancialProfileRetrieveUpdateDestroyView,guardar_informacion_general,obtener_informacion_por_id,
    obtener_flujo_caja,abonar_meta,obtener_distribucion_gastos,get_user_info,generate_report
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    # Añade más rutas según las funcionalidades
    # Categorías de Transacciones
    path('categories/', list_categories, name='list_categories'),
    path('categories/create/', create_category, name='create_category'),
    path('categories/delete/<int:category_id>/', delete_category, name='delete_category'),

    # Transacciones
    path('transactions/', list_transactions, name='list_transactions'),
    path('transactions/create/', create_transaction, name='create_transaction'),
    path('transactions/delete/<int:transaction_id>/', delete_transaction, name='delete_transaction'),

    # Presupuestos
    path('budgets/', list_budgets, name='list_budgets'),
    path('budgets/create/', create_budget, name='create_budget'),
    path('budgets/delete/<int:budget_id>/', delete_budget, name='delete_budget'),

    # Metas Financieras
    path('goals/', list_goals, name='list_goals'),
    path('goals/create/', create_goal, name='create_goal'),
    path('goals/delete/<int:goal_id>/', delete_goal, name='delete_goal'),
    path('goals/abono/<int:goal_id>/', abonar_meta, name='abonar_meta'),

    # Reportes
    path('reports/', list_reports, name='list_reports'),
    path('reports/create/', create_report, name='create_report'),
    path('reports/delete/<int:report_id>/', delete_report, name='delete_report'),
    path('reports/create/', create_report, name='create_report'),
    path('reports/<int:report_id>/', generate_report, name='generate_report'),

    # Notificaciones
    path('notifications/', list_notifications, name='list_notifications'),
    path('notifications/create/', create_notification, name='create_notification'),
    path('notifications/delete/<int:notification_id>/', delete_notification, name='delete_notification'),
    # Savings URLs
    path('savings/', SavingsListCreateView.as_view(), name='savings-list-create'),
    path('savings/<int:pk>/', SavingsRetrieveUpdateDestroyView.as_view(), name='savings-detail'),

    # Debt URLs
    path('debts/', DebtListCreateView.as_view(), name='debt-list-create'),
    path('debts/<int:pk>/', DebtRetrieveUpdateDestroyView.as_view(), name='debt-detail'),

    # Investment URLs
    path('investments/', InvestmentListCreateView.as_view(), name='investment-list-create'),
    path('investments/<int:pk>/', InvestmentRetrieveUpdateDestroyView.as_view(), name='investment-detail'),

    # Financial Profile URLs
    path('financial-profiles/', FinancialProfileListCreateView.as_view(), name='financial-profile-list-create'),
    path('financial-profiles/<int:pk>/', FinancialProfileRetrieveUpdateDestroyView.as_view(), name='financial-profile-detail'),

    #Procesos generales
    path('guardar-informacion-general/', guardar_informacion_general, name='guardar_informacion_general'),
    path('obtener-informacion-general/<int:id>/', obtener_informacion_por_id, name='obtener_informacion_por_id'),
    path('obtener-transacciones-recientes/', procesosGenerales.obtener_transacciones_recientes, name='obtener_transacciones_recientes'),
    path('obtener-flujo-caja/<int:user_id>/', obtener_flujo_caja, name='obtener_flujo_caja'),
    path('distribucion-gastos/', obtener_distribucion_gastos, name='obtener_distribucion_gastos'),


    #Ususarios
     path('users/<int:id>/profile/', get_user_info, name='get_user_info'),
]
