from django.contrib import admin
from .models import TransactionCategory, Transaction, Budget, FinancialGoal, Report, Notification, Savings, Debt, Investment, FinancialProfile

admin.site.register(TransactionCategory)
admin.site.register(Transaction)
admin.site.register(Budget)
admin.site.register(FinancialGoal)
admin.site.register(Report)
admin.site.register(Notification)
admin.site.register(Savings)
admin.site.register(Debt)
admin.site.register(Investment)
admin.site.register(FinancialProfile)
# Register your models here.
