from django.shortcuts import render,redirect
from django.views import View
from .forms import UsuarioForm
from .models import Usuario,Rol
import bcrypt

class Registrarse(View):
    template_name = 'accounts/register.html'
    def get(self,request):
        form = UsuarioForm()
        return render(request, "accounts/register.html", {"form": form})
    
    def post(self,request):
        form = UsuarioForm( request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return render(request, self.template_name, {"form": form})

class Login(View):
    template_name = 'accounts/login.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):        
        next_url = request.POST.get('next') or request.GET.get('next')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return render(request, self.template_name, {"error": "Email o contraseña incorrectos."})

        if bcrypt.checkpw(password.encode('utf-8'), usuario.password.encode('utf-8')):
            request.session['usuario_id'] = usuario.id
            if next_url:
                return redirect(next_url)
            return redirect('products_dashboard')

        return render(request, self.template_name, {"error": "Email o contraseña incorrectos."})
    
class Password_reset(View):
    template_name = 'accounts/password_reset.html'

    def get(self,request):
        usuario_id = request.session.get('usuario_id')
        if not usuario_id:
            return redirect('/login/?next=/password_reset/')
        return render(request, self.template_name)

    def post(self,request):
        usuario_id = request.session.get('usuario_id')
        if not usuario_id:
            return redirect('/login/?next=/password_reset/')
        actual_password = request.POST.get('actual_password')
        nueva_password = request.POST.get('new_password')
        nueva_password2 = request.POST.get('new_password2')
        try:
            usuario = Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            return redirect('/login/')
        if not bcrypt.checkpw(actual_password.encode('utf-8'), usuario.password.encode('utf-8')):
            return redirect('/password_reset/')
        if nueva_password != nueva_password2:
            return redirect('/password_reset/')
        usuario.password = bcrypt.hashpw(nueva_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        usuario.save()
        return redirect('products_dashboard')


    

def Logout(request):
    request.session.flush()
    return redirect("login")