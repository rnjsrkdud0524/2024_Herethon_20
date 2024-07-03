from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']  # 이메일을 입력 폼에서 받아옴
        password = request.POST['password']
        repeat_password = request.POST['repeat']

        if password == repeat_password and len(password) >= 8:
            # 이메일을 사용하여 새로운 사용자 생성
            new_user = User.objects.create_user(username=email, email=email, password=password)
            messages.success(request, '회원가입 성공')
            return redirect('main')
        else:
            if len(password) < 8:
                messages.error(request, '비밀번호는 8자리 이상이어야 합니다.')
            else:
                messages.error(request, '비밀번호가 일치하지 않습니다.')

    return render(request, 'signup.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user is not None:
            auth_login(request, user)
            print('로그인 성공')
            return redirect('main')
        else: 
            error_message = "아이디 또는 비밀번호가 잘못되었습니다."  # 에러 메시지 설정
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    

def logout(request):
    return redirect('main')