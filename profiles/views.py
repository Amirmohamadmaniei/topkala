from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from account.models import User
from order.models import Order
from product.models import Product
from profiles.forms import EditProfileForm
from profiles.models import Favorite


class ProfileView(LoginRequiredMixin, View):
    login_url = 'account:login'

    def get(self, request):
        product_favorites = Favorite.objects.filter(user=request.user)[0:2]
        orders = Order.objects.filter(user=request.user, is_paid=True)[0:3]
        return render(request, 'profiles/profile.html', {'product_favorites': product_favorites, 'orders': orders})


class ProfilePersonalView(View):
    def get(self, request):
        return render(request, 'profiles/profile_personal.html')


class ProfileEditView(View):
    form_class = EditProfileForm
    template_name = 'profiles/profile_edit.html'

    def setup(self, request, *args, **kwargs):
        self.user = get_object_or_404(User, pk=request.user.pk)
        super().setup(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class(instance=self.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, instance=self.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'اطلاعات شما با موفقیت بروزرسانی شد', extra_tags='alert alert-success')
            return redirect('profile:profile_personal')
        messages.error(request, 'اطلاعات شما با موفقیت بروزرسانی شد', extra_tags='alert alert-danger')
        return render(request, self.template_name, {'form': form})


class FavoriteDetailView(LoginRequiredMixin, View):
    login_url = 'account:login'

    def get(self, request):
        object_list = Favorite.objects.filter(user=request.user)
        return render(request, 'profiles/profile_favorites.html', {'object_list': object_list})


class FavoriteAddRemoveView(LoginRequiredMixin, View):
    login_url = 'account:login'

    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        try:
            Favorite.objects.get(user=request.user, product=product).delete()
        except:
            Favorite.objects.create(user=request.user, product=product)
        return redirect('product:detail', product_id, product.slug)


class FavoriteRemoveView(LoginRequiredMixin, View):
    login_url = 'account:login'

    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        Favorite.objects.get(user=request.user, product=product).delete()
        messages.success(request, 'محصول با موفقیت از مورد علاقه ها حذف شد', extra_tags='alert alert-success')
        return redirect('profile:favorites')


class OrderDetailView(LoginRequiredMixin, View):
    login_url = 'account:login'

    def get(self, request):
        orders = Order.objects.filter(user=request.user, is_paid=True)

        return render(request, 'profiles/profile_orders.html', {'orders': orders})
