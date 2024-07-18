import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from decouple import config

def get_tourist_attractions(request):
    service_key = config('SERVICE_KEY')    
    base_url = 'http://apis.data.go.kr/B551011/KorService1/locationBasedList1'

    # Get the current page number from the request parameters
    page_no = int(request.GET.get('page', 1))
    num_of_rows = 15  # Number of items per page

    # 기본 위치 설정
    current_mapx = float(request.GET.get('mapx', 129.004202))
    current_mapy = float(request.GET.get('mapy', 36.0197789))

    # Get search query
    search_query = request.GET.get('search', '')

    params = {
        'serviceKey': service_key,
        'numOfRows': 1000,  # Fetch a large number of results to handle pagination on server side
        'pageNo': 1,
        'MobileOS': 'ETC',
        'MobileApp': 'AppTest',
        '_type': 'json',
        'listYN': 'Y',
        'arrange': 'S',  # Use 'E' to arrange by distance
        'mapX': current_mapx,
        'mapY': current_mapy,
        'radius': 50000,
        'contentTypeId': 12
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()

        # Extract necessary data
        items = data.get('response', {}).get('body', {}).get('items', {}).get('item', [])
        
        # Filter items by search query
        if search_query:
            items = [item for item in items if search_query.lower() in item.get('title', '').lower()]

        # Implement pagination for filtered items
        paginator = Paginator(items, num_of_rows)
        paginated_items = paginator.get_page(page_no)

    except requests.exceptions.RequestException as e:
        # Handle API request errors
        return JsonResponse({'error': str(e)}, status=500)

    except ValueError as e:
        # Handle JSON decoding errors
        return JsonResponse({'error': 'JSON decode error: ' + str(e)}, status=500)

    context = {
        'items': paginated_items,  # Pass the paginated items to the context
        'current_page': page_no,
        'total_pages': paginator.num_pages,
        'search_query': search_query,
        'current_mapx': current_mapx,
        'current_mapy': current_mapy,
    }

    return render(request, 'index.html', context)
