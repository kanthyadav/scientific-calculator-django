from django.shortcuts import render
import math

def home(request):
    return render(request, 'calculator/index.html')

def calculate(request):
    result = None
    if request.method == 'POST':
        expression = request.POST.get('expression')

        try:
            # Safe dictionary for allowed functions
            allowed = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            result = eval(expression, {"__builtins__": None}, allowed)
        except Exception:
            result = "Invalid Expression"

    return render(request, 'calculator/index.html', {'result': result})
