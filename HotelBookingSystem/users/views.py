from django.shortcuts import render
from django.views.generic import FormView, TemplateView,CreateView
from .forms import CustomLoginForm, SignUpForm
from django.contrib.auth import authenticate, login

from django.shortcuts import redirect
from django.urls import reverse_lazy

# Create your views here.

class CustomLoginView(TemplateView):
    form_class = CustomLoginForm
    template_name = 'users/login.html'

    def post(self, *args, **kwargs):
        data = self.request.POST
        phone_email = data.get('phone_email')
        password = data.get('password')
        
        # for local numbers 
        if phone_email.startswith('0'):
            phone_email = '+26' + phone_email

        user = authenticate(self.request, username=phone_email, password=password)
        if user:
            login(self.request, user)
            return redirect('landing-page')
        else:
            return render(self.request, self.template_name, {'error_message': 'invalid credentials', 'form': self.form_class()})
        
   
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login') 

    
   


