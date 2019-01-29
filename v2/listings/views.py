from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing

def listings(request):
    # Get Listing Model from DB name as listings
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    # Create Paginator variable with listing model and limit of 3 pages
    paginator = Paginator(listings, 3)
    # 'page' is url parameter we are looking for 
    page = request.GET.get('page') 
    # paged_listings created to hold page request --> Need to elaborate here and aboe
    paged_listings = paginator.get_page(page)

    context = {
        'listings':paged_listings
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')

#PAGINATOR
# 1. -> from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

#2. -> in the function/view: create variable paginator, page, paged_listing

    # paginator = Paginator(listings, 3)
    # page = request.GET.get('page')
    # paged_listings = paginator.get_page(page)
    # context = {
    #     'listings':paged_listings
    # }

#3 -> pass in variables [named as context in example]

#4 -> USE Bootstrap in HTML 



