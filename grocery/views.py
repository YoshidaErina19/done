from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .models import Grocery
from .forms import GroceryCreateForm, GroceryUpdateForm
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


# クラスベースビュー(checked,uncheckedの入力で買った物記録を新規登録できる)
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


# 関数ベースビュー(チェックしたものが買った物記録として新規作成される)
def grocery_create(request):
    initial_values = {"user": request.user}

    checkbox_1 = request.POST.getlist('checkbox_1')
    checkbox_2 = request.POST.getlist('checkbox_2')
    checkbox_3 = request.POST.getlist('checkbox_3')
    form = GroceryCreateForm(request.POST or initial_values)
    ctx = {"form": form}

    if request.method == 'GET':
        print(ctx)
        return render(request, 'grocery/grocery_create.html', ctx)

    if request.method == 'POST':
        if checkbox_1:
            checkbox_1 = 'checked'
        else:
            checkbox_1 = 'unchecked'

        if checkbox_2:
            checkbox_2 = 'checked'
        else:
            checkbox_2 = 'unchecked'

        if checkbox_3:
            checkbox_3 = 'checked'
        else:
            checkbox_3 = 'unchecked'

        object = Grocery.objects.create(
            user = request.user,
            checkbox_1 = checkbox_1,
            checkbox_2 = checkbox_2,
            checkbox_3 = checkbox_3,
            )

        object.save()
        messages.success(request, '買った物を登録しました。お疲れ様でした！')
        return redirect('grocery:grocery_list')

    return render(request, 'grocery/grocery_update.html', ctx)


def update(request, pk):
    obj = Grocery.objects.get(pk=pk)
    initial_values = {"user": obj.user}

    checkbox_1 = request.POST.getlist('checkbox_1')
    checkbox_2 = request.POST.getlist('checkbox_2')
    checkbox_3 = request.POST.getlist('checkbox_3')
    form = GroceryUpdateForm(request.POST or initial_values)
    ctx = {"form": form}

    if request.method == 'GET':
        ctx = {"checkbox_1": obj.checkbox_1,
               "checkbox_2": obj.checkbox_2,
               "checkbox_3": obj.checkbox_3,
               "checkbox_created_at": obj.checkbox_created_at,
               "pk": obj.pk,
               }
        return render(request, 'grocery/grocery_update.html', ctx)

    if request.method == 'POST':
        if checkbox_1:
            obj.checkbox_1 = 'checked'
        else:
            obj.checkbox_1 = 'unchecked'

        if checkbox_2:
            obj.checkbox_2 = 'checked'
        else:
            obj.checkbox_2 = 'unchecked'

        if checkbox_3:
            obj.checkbox_3 = 'checked'
        else:
            obj.checkbox_3 = 'unchecked'
        obj.save()
        messages.success(request, '買った物を登録しました。お疲れ様でした！')
        return redirect('grocery:grocery_list')

    return render(request, 'grocery/grocery_update.html', ctx)


class GroceryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Grocery
    template_name = 'grocery/grocery_delete.html'
    success_url = reverse_lazy('grocery:grocery_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "買った物記録を削除しました。")
        return super().delete(request, *args, **kwargs)
