# views.py

from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm

def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            menu_name = form.cleaned_data['menu_name']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            total_price = form.cleaned_data['total_price']
            order = Order(menu_name=menu_name, price=price, quantity=quantity, total_price=total_price)
            order.save()
            return redirect('success_page')  # 주문 완료 페이지로 리다이렉트
    else:
        form = OrderForm()

    return render(request, 'order.html', {'form': form})


def menu_view(request):
    # 프론트엔드의 메뉴 페이지를 렌더링하는 뷰
    return render(request, 'menu.html')

def pre_order_view(request):
    # 프론트엔드의 pre-order 페이지를 렌더링하는 뷰
    return render(request, 'pre-order.html')

def silver_bot_view(request):
    # 프론트엔드의 silver-bot 페이지를 렌더링하는 뷰
    return render(request, 'silverBot.html')

def recommend_view(request):
    # 프론트엔드의 recommend 페이지를 렌더링하는 뷰
    return render(request, 'recommend.html')


from django.shortcuts import render, redirect

from .models import Comment
from .forms import CommentForm

# Create your views here.
def index(request):
    comments = Comment.objects.order_by("-date_added")
    context = {'comments': comments}
    return render(request, 'guestbook/index.html', context)

def sign(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            return redirect('index')
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'guestbook/sign.html', context)







"""
from django.shortcuts import render,redirect

from .models import Comment
from .forms import CommentForm

# Create your views here.
def index(request):
    comments = Comment.objects.order_by("-date_added")

    context = {'comments' : comments}
    return render(request,'guestbook/index.html',context)

def sign(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(name=request.POST['name'],comment=request.POST['comment'])
            new_comment.save()
        return redirect('index')
    else:
        form = CommentForm()
    context = {'form' : form}
    return render(request,'guestbook/sign.html',context)
"""