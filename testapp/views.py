from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterForm,LoginForm,Project_Form
from django.contrib.auth import authenticate,login
from django.contrib import messages
from . models import Project_model

# Create your views here.


class home(View):

    def get(self,request):

        form = LoginForm()

        if request.user.is_authenticated is False:
            return render(request,'TestApp/home.html',{'form':form})
        else:
            return redirect('clients')

    def post(self,request):

        form = LoginForm(request.POST,data=request.POST)

        if form.is_valid():
            # print('form is valid')
            u_name=form.cleaned_data['username']
            u_pass=form.cleaned_data['password']
            # print(u_name,u_pass)

            user = authenticate(username=u_name,password=u_pass)
            if user is not None:
                login(request,user)
                messages.success(request,f'successfully user {u_name} login')
                return redirect('dashboard')
                
        messages.warning(request,'Something went wrong')       
        return render(request,'MyApp/home.html',{'form':form})

class register(View):

    def get(self,request):

        form = RegisterForm()

        return render(request,'TestApp/register.html',{'form':form})

    def post(self,request):

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()
            messages.success(request,'user registered successfully ')
            return redirect('home')


        return render(request,'TestApp/register.html',{'form':form})



class dashboard(View):

    def get(self,request):

        if request.user.is_authenticated:
            return render(request,'TestApp/dashboard.html')
        else:
            return redirect('home')
    def post(self,request):
        return render(request,'TestApp/dashboard.html')



class clients(View):
    def get(self,request):
        

        prj = Project_model.objects.all()

        context ={'prj': prj}

        return render(request,'TestApp/blogs.html' , context)


class add_pro(View):
    def get(self,request):
        form=Project_Form()
        return render(request,'MyApp/add_blog.html',{'form':form})

    def post(self,request):
        form=Project_Form(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Your Blog Added successfully ')
            return redirect('dashboard')
        return render(request,'TestApp/add_pro.html')



class see_blogs(View):
    def get(self,request):
        
        # context ={}

        # try:
        #     blog_objs = BlogModel.objects.filter(user=request.user)
        #     context['blog_objs'] = blog_objs
        # except Exception as e:
        #     print(e)

        # print(context)
        # return render(request, 'MyApp/see_blogs.html', context)

        prj1 = Project_model.objects.all()

        context ={'prj1': prj1}

        return render(request,'TestApp/see_blogs.html' , context)
