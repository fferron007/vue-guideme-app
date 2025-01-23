from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Merchant
from .serializers import MerchantSerializer

@api_view(['GET'])
def filters(request):
    countries = Merchant.objects.values_list('country', flat=True).distinct()
    states = Merchant.objects.values_list('state', flat=True).distinct()
    categories = Merchant.objects.values_list('category', flat=True).distinct()
    response = {
        'Country': list(countries),
        'State': list(states),
        'Category': list(categories),
    }
    return Response(response)

@api_view(['GET'])
def merchants(request):
    queryset = Merchant.objects.all()
    country = request.GET.get('Country')
    state = request.GET.get('State')
    category = request.GET.get('Category')

    if country:
        queryset = queryset.filter(country=country)
    if state:
        queryset = queryset.filter(state=state)
    if category:
        queryset = queryset.filter(category=category)

    serializer = MerchantSerializer(queryset, many=True)
    return Response(serializer.data)

