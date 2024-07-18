from decouple import config
import requests
from django.shortcuts import render
from django.http import JsonResponse

def tourist_attraction_detail(request, content_id):
    service_key = config('SERVICE_KEY')
    kakao_api_key = config('KAKAO_API_KEY')
    base_url = 'http://apis.data.go.kr/B551011/KorService1/detailCommon1'

    params = {
        'serviceKey': service_key,
        'contentId': content_id,
        'MobileOS': 'ETC',
        'MobileApp': 'AppTest',
        '_type': 'json',
        'defaultYN': 'Y',
        'firstImageYN': 'Y',
        'areacodeYN': 'Y',
        'catcodeYN': 'Y',
        'addrinfoYN': 'Y',
        'mapinfoYN': 'Y',
        'overviewYN': 'Y',
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()

        # Extract necessary data
        item = data.get('response', {}).get('body', {}).get('items', {}).get('item', [])[0]

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    except (IndexError, ValueError) as e:
        return JsonResponse({'error': 'No data found: ' + str(e)}, status=404)

    context = {
        'item': item,
        'kakao_api_key': kakao_api_key,
    }

    return render(request, 'detail.html', context)
