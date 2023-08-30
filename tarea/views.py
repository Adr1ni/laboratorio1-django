from django.shortcuts import render

def sumar(request, num1, num2):
    resultado = num1 + num2
    return render(request, 'tarea/tarea.html', {
        'operacion': 'suma', 
        'num1': num1, 
        'num2': num2, 
        'resultado': resultado
    })

def restar(request, num1, num2):
    resultado = num1 - num2
    return render(request, 'tarea/tarea.html', {
        'operacion': 'resta', 
        'num1': num1, 
        'num2': num2, 
        'resultado': resultado
    })

def multiplicar(request, num1, num2):
    resultado = num1 * num2
    return render(request, 'tarea/tarea.html', {
        'operacion': 'multiplicación', 
        'num1': num1, 
        'num2': num2, 
        'resultado': resultado
    })

