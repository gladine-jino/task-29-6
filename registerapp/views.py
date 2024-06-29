from django.shortcuts import render
from .forms import RegisterForm,LoginForm
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,logout
from .models import User
from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required




# @login_required
def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)      
        if form.is_valid():  
            user=form.save()
            messages.success(request, 'Account created successfully') 
            access_code = User.generate_unique_code(user)
            user.code=access_code
            user.save()
            # User.objects.create(user_profile=user, code=access_code) 
            return render(request,'registerapp/login.html', {'access_code':access_code})         
          
            
        else:
            print(form.errors)
            return render(request,'registerapp/register.html', {'form':form})             
    else:        
        form=RegisterForm()
        return render(request, 'registerapp/register.html',{'form':form})

def login_view(request):
    if request.method=="POST":
        # print(request.data)
        username=request.POST.get('username')       
        
        form=LoginForm(data=request.POST)
        print(form.data)
        access_code=User.objects.filter(email=username).first() 
        if access_code:
            acc_code=access_code.code        
            if form.is_valid():
                username=request.POST.get('username') 
                print(username)           
                password=request.POST.get('password')
                print(password)            
                user=User.objects.filter(email=username,code=password).first()
                print(user)           
                if user:                
                        # auth_login(request,user)
                        messages.success(request, f'Welcome{username}') 
                        return HttpResponse("Success")                         
                else:
                    messages.error(request,'Please enter correct username and password')    
                    return render(request,'registerapp/login.html',{'form':form,'access_code':acc_code})  
            else:
                print(form.errors)
                messages.error(request,'Please enter correct username and password')  
                return render(request,'registerapp/login.html',{'form':form})        
        else:
            print(form.errors)
            messages.error(request,'Please enter correct username password') 
            return render(request,'registerapp/login.html',{'form':form})     
    else:      
        form=LoginForm()
        return render(request,'registerapp/login.html',{'form':form})
    

def user_logout(request):
    logout(request)
    messages.success(request, 'logout successfully') 
    return redirect('login_view')
