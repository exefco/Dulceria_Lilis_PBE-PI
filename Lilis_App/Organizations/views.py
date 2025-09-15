from django.shortcuts import render
from django.views import View

class dashboard(View):
    template_name = 'dashboard.html'
    def get(self,request):
        return render(request, "dashboard.html")

    def post(self,request):
        pass