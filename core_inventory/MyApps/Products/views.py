from django.shortcuts import render, redirect
from . models import Product
from django.views.generic.detail import DetailView

# Create your views here.
def vistaProducto(request):
    listaProductos = Product.objects.all()
    return render(request, "Productos/vistaProductos.html", {"productos":listaProductos})

def registrarProducto(request):
    nombreP = request.POST['txtName']
    descripcionP = request.POST['txtDescription']
    imagenP = request.FILES.get('fileImage')
    precioP = request.POST['txtPrice']
    cantidadP = request.POST['txtQuantity']
    estadoP = request.POST['inputState']
    
    producto = Product.objects.create(name=nombreP, descripction=descripcionP, price=precioP, image_product=imagenP, stock=cantidadP, status=estadoP)
    
    return redirect('/')

def productoAEditar(request, id):
    producto = Product.objects.get(id_product = id)
    return render(request, "Productos/editarProducto.html", {"prod":producto})


def editarProducto(request):
    codigoP = request.POST['txtCode']
    nombreP = request.POST['txtNameEdit']
    descripcionP = request.POST['txtDescriptionEdit']
    imagenP = request.FILES.get('fileImageEdit')
    precioP = request.POST['txtPriceEdit']
    
    print(precioP)
    producto = Product.objects.get(id_product = codigoP)
    producto.name = nombreP
    producto.descripction = descripcionP
    producto.price = precioP
    producto.image_product = imagenP
    producto.save()
    return redirect('/')

def eliminarProducto(request, id):
    producto = Product.objects.get(id_product = id)
    producto.delete()
    return redirect('/productos')

class productDetailView(DetailView):
    model = Product
    template_name = 'Carrito/productDetail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context