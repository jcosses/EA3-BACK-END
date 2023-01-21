from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def datos(request):
    # contexto={"nombre":"JUAN CARLOS"}
    hijo=Class_Persona("Martin Cabrera","23")
    contexto={"nombre":"JUAN CARLOS","pariente":hijo}
    return render(request, 'datos.html',contexto)

class Class_Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()
        
