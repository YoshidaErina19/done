from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Grocery
from .forms import GroceryCreateForm
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.


class GroceryListView(LoginRequiredMixin, generic.ListView):
    model = Grocery
    template_name = 'grocery_list.html'

    def get_queryset(self):
        groceries = Grocery.objects.filter(user=self.request.user).order_by('-checkbox_created_at')
        return groceries


"""
# 関数ベースビューで記述したもの
def index(request):
    context = {
        'checkbox_list': CheckBox.objects.all(),
    }
    return render(request, 'grocery/grocery_list.html', context)
"""

class GroceryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Grocery
    template_name = 'grocery/grocery_create.html'
    form_class = GroceryCreateForm
    success_url = reverse_lazy('grocery:grocery_list')

    def form_valid(self, form):
        grocery = form.save(commit=False)
        grocery.user = self.request.user
        grocery.save()
        messages.success(self.request, '買った物を記録しました。お疲れ様でした！')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, '買った物の記録に失敗しました。')
        return super().form_invalid(form)
