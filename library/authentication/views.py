from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView

from order.models import Order
from .forms import CreateUser, UpdateUser, LoginUser, ResetPassword
from .models import CustomUser

# from book.models import Book
# from .forms import BookForm
from rest_framework import viewsets, generics, status
from .serializers import UserSerializer, UserOrdersListSerializer  # ,UserListSerializer


# for API
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserAllOrdersListView(generics.ListAPIView):
    serializer_class = UserOrdersListSerializer

    def get(self, request, *args, **kwargs):
        user_id = str(kwargs["user_id"]).split(",")
        # self.queryset = Order.objects.filter(user=kwargs['user_id'], )
        self.queryset = Order.objects.filter(user__in=user_id, )
        return self.list(request, *args, **kwargs)


class UserOrdersListView(generics.ListAPIView):
    serializer_class = UserOrdersListSerializer

    def get(self, request, *args, **kwargs):
        order_id = str(kwargs["order_id"]).split(",")
        self.queryset = Order.objects.filter(user=kwargs['user_id'], id__in=order_id)
        return self.list(request, *args, **kwargs)

    # def post(self, request, user_id, format=None):
    #     # serializer = CustomUserOrderSerializer(data=request.data)
    #     serializer_class = UserOrdersListSerializer(data=request.data)
    #
    #     if serializer_class.is_valid():
    #         serializer_class.save()
    #         return Response(serializer_class.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUES)


def user_item(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    context = {'first_name': user.first_name, 'middle_name': user.middle_name, 'last_name': user.last_name,
               'id': user.id, 'email': user.email, 'role': user.role, 'is_active': user.is_active,
               'orders': Order.objects.filter(user=user_id)}

    return render(request, 'authentication/user_details.html', context)


def delete_user(request, user_id):
    CustomUser.delete_by_id(user_id)
    return redirect('users')


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/book")


def create_user_new(request, user_id=None):
    if request.method == 'GET':
        if user_id:
            author = CustomUser.get_by_id(user_id)
            form = UpdateUser(instance=author)
            title = 'Update user'
        else:
            form = CreateUser()
            title = 'Create user'

        return render(request, 'authentication/register_new.html', {'form': form, 'title': title})
    else:
        if not user_id:
            form = CreateUser(request.POST)
            title = 'Create user'
        else:
            author = CustomUser.get_by_id(user_id)
            form = UpdateUser(request.POST, instance=author)
            title = 'Update user'
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.is_active = 1
            if 'password' in form.cleaned_data:
                new_user.set_password(form.cleaned_data['password'])
            new_user.save()
        else:
            return render(request, 'authentication/register_new.html', {'form': form, 'title': title})
        return redirect('users')


def users_new(request):
    users = CustomUser.get_all()
    title = 'Users'
    return render(request, 'authentication/user_list.html', {'users': users, 'title': title})


def login_(request):
    form = LoginUser()
    title = 'Login'
    if request.method == 'GET':

        return render(request, 'authentication/login_new.html', {'form': form, 'title': title})
    else:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {user.email}.")

            return redirect("/book")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'authentication/login_new.html', {'form': form, 'title': title})


def reset_passwd(request):
    form = ResetPassword()
    title = 'Reset password'
    if request.method == 'GET':

        return render(request, 'authentication/register_new.html', {'form': form, 'title': title})
    else:
        old_password = request.POST['old_password']
        user = CustomUser.get_by_id(request.user.id)
        passwd_check = user.check_password(old_password)
        if passwd_check:
            form = ResetPassword(request.POST)
            if form.is_valid():
                user.set_password(form.cleaned_data['new_password2'])
                user.save()
            else:
                return render(request, 'authentication/register_new.html', {'form': form, 'title': title})

        else:
            messages.info(request, f"The old password is not valid")
            return render(request, 'authentication/register_new.html', {'form': form, 'title': title})

        return redirect('users')
