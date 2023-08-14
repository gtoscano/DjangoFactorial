from django.urls import path
from .views import FactorialView

urlpatterns = [
    path('factorial/<int:number>', FactorialView.as_view(), name='factorial'),
]
