from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def test(request):
    lista=["Lazaña","Charquican","Porotos Granados"]
    hijo=Class_Persona("Fernando Rivera","23")
    contexto = {"nombre":"Juan Carlos Osses","comidas":lista,"hijo":hijo}
    return render(request, 'core/datos.html', contexto)

class Class_Persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()