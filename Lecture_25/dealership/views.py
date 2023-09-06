from django.shortcuts import render, redirect
from .models import Car, Brand, Dealer
from .forms import CarForm, BrandForm, DealerForm


def brand_list(request):
    brands = Brand.objects.all()
    context = {'brands': brands}
    return render(request, 'brand/brands.html', context=context)


def car_list(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'car/cars.html', context=context)


def dealer_list(request):
    dealers = Dealer.objects.all()
    context = {'dealers': dealers}
    return render(request, 'dealer/dealers.html', context=context)


def create_brand(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()

            return redirect('brand_list')
    form = BrandForm()
    return render(request, 'brand/create.html', {'form': form})


def create_dealer(request):
    if request.method == 'POST':
        form = DealerForm(request.POST)
        if form.is_valid():
            dealer = form.save(commit=False)
            dealer.save()

            return redirect('dealers_list')

    form = DealerForm()
    return render(request, 'dealer/create.html', {'form': form})


def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.save()
            return redirect('car_list')

    form = CarForm()
    return render(request, 'car/create.html', {'form': form})


def car_details(request, pk):
    car = Car.objects.get(pk=pk)
    dealers = Dealer.objects.filter(dealer_of=car.brand)
    context = {'car': car, 'dealers': dealers}
    return render(request, 'car/details.html', context=context)


def dealer_details(request, pk):
    dealer = Dealer.objects.get(pk=pk)
    dealer_of = Car.objects.filter(brand=dealer.dealer_of)

    context = {'dealer': dealer, 'products': dealer_of}
    return render(request, 'dealer/details.html', context=context)




