from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators import csrf
from cmdb.models import Usr
from Form import UsrForm,LoginForm

# from django.core.handlers.wsgi import WSGIRequest as request



# 加载指定页面

def login_view(request):
    """
    登录主界面
    """
    return render(request,'Login/login_view.html',{'form':LoginForm})

def find_view(request):
    """
    找回界面
    """
    return render(request,'Login/find_view.html',{'form':UsrForm})

def regist_view(request):
    """
    注册界面
    """
    return render(request,'Login/regist_view.html',{'form':UsrForm})




def login(request):
    
    '''
    提交登录表单
    '''
    request.session['is_login']=False
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect(reverse(request.session['stage']+'System:base'))

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            ID = login_form.cleaned_data.get('ID')
            password = login_form.cleaned_data.get('password')

            try:
                user = Usr.objects.get(ID=ID)
            except :
                message = '用户不存在！'
                return render(request, 'login/login_view.html', {"form":LoginForm,"message":message})

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.ID
                request.session['stage'] = user.stage
                return redirect(reverse(request.session['stage']+'System:base'))
            else:
                message = '密码不正确！'
                return render(request, 'login/login.html', {"form":LoginForm,"message":message})
        else:
            message = '填写格式不规范'
            return render(request, 'login/login.html', {"form":LoginForm,"message":message})

    login_form = UsrForm()
    return render(request, 'login/login.html', locals())

def logout(request):
    """
    在登录后进行退出登录 
    还没写路由什么的,只是定义了一个函数,具体退出需要在登录后的界面上安排
    """
    request.session['is_login']=False
    return render(request,'login/login_view.html',{"form":LoginForm})

def regist(request):
    """
    提交注册表单动作
    """
    regist_form = UsrForm(request.POST)
    if regist_form.is_valid():# 检验完整性
        if Usr.objects.filter(ID = regist_form.clean().get('ID')):# 检验是否重复ID
            message = "账号已存在"
            return render(request, 'login/regist_view.html',{"form":UsrForm,'message':message})
        else:
            tmp = regist_form.clean()
            Usr.objects.create(**tmp)
            return render(request,'login/login_view.html',{"form":LoginForm})

    elif regist_form.errors is not None:
        print(regist_form.errors)
        return HttpResponse(str(regist_form.errors))
