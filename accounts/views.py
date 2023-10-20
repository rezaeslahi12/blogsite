from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse






class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"
    
    
class MyLoginView(LoginView):
    redirect_authenticated_user = True
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    
        


def logoutView(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect("/blog/")
    
    

        
# Create your views here.











# @login_required(login_url="/accounts/login/")
# def my_view(request):
#     username = request.POST["username"]
#     password = request.POST["password"]
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#     if not request.user.is_authenticated:
#         return render(request, "myapp/login_error.html")
#     else:
#         ...