# Basic Lib Import
from django.urls import path

from expense.views.add_category_views import CreateCategory
from expense.views.add_expense_views import CreateExpense
from expense.views.delete_expense_categories_views import DeleteExpenseCategories
from expense.views.delete_expense_views import DeleteExpense
from expense.views.download_expense_pdf import DownloadExpensePDF
from expense.views.expense_pdf_views import ViewExpensePDF
from expense.views.export_expense_csv_views import DownloadExpenseCSV
from expense.views.export_expense_excle_views import DownloadExpenseEXCLE
from expense.views.manage_expense_views import ExpenseCategory, ManageExpense
from expense.views.update_expense_categories_views import UpdateExpenseCategories
from expense.views.update_expense_views import UpdateExpense

# Routing Implement
urlpatterns = [
    # Expense
    path('list/', ManageExpense.as_view(), name='manage_expense'),
    path('add/', CreateExpense.as_view(), name='add_expense'),
    path('update/<pk>', UpdateExpense.as_view(), name='update_expense'),
    path('delete/<pk>', DeleteExpense, name='delete_expense'),

    # Categories
    path('category/', ExpenseCategory.as_view(), name='expense_category'),
    path('add/category/', CreateCategory.as_view(), name='add_category'),
    path('delete/category/<pk>', DeleteExpenseCategories, name='delete_expense_categories'),
    path('update/category/<pk>', UpdateExpenseCategories.as_view(), name='update_expense_categories'),

    # File management
    path('export/csv/', DownloadExpenseCSV.as_view(), name='download_expense_csv'),
    path('export/excle/', DownloadExpenseEXCLE.as_view(), name='download_expense_excle'),
    path('pdf/', ViewExpensePDF.as_view(), name='view_expense_pdf'),
    path('pdf/download/', DownloadExpensePDF.as_view(), name="pdf_expense_download")
]
