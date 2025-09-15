from django.shortcuts import render,redirect
from django.views import View
from Accounts.models import Usuario
from .models import Products
from Organizations.models import Organization
class Dashboard(View):
    login_url = '/login/'
    template_name = 'products/dashboard.html'
    def get(self,request):
        usuario = None
        usuario_id = request.session.get('usuario_id')
        if usuario_id:
            try:
                usuario = Usuario.objects.get(id=usuario_id)
            except:
                usuario = None
        if not usuario:
            return redirect(f'/login/?next={request.path}')

        return render(request, "products/dashboard.html", {"usuario": usuario})
    
    def post(self,request):
        pass

class Products_view(View):
    template_name = 'products/products.html'
    login_url = '/login'

    def get(self,request):
        try:
            id = request.session.get('usuario_id')
            usuario = Usuario.objects.get(id=id)
            if not usuario:
                print("no hay usuario\n")
                return redirect(f'/login/?next={request.path}')
            organization = Organization.objects.get(id=usuario.organization.id)
            products = Products.objects.filter(Organization=organization)
            return render(request, "products/products.html", {"products": products})
        except:
            print("nose\n")
            return redirect(f'/login/?next={request.path}')