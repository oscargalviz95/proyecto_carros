from django.shortcuts import render

lista = {
    'renoult' :{ 
        'Renoult 1','Renoult 2'
    },
    'chevrolet' :{ 
        'Chevrolet 1','Chevrolet 2'
    },
}

def inicio(request):

    context = { 'lista' : lista}

    return render(request,'inicio.html',context)

def list_carros(request, marca):

    context = { 'carros' : lista[marca] }

    return render(request,'list_carros.html',context)
