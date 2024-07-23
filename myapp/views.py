from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from decouple import config
import requests

@login_required
def get_tourist_attractions(request):
    service_key = config('SERVICE_KEY')
    base_url = 'http://apis.data.go.kr/B551011/KorService1/locationBasedList1'

    # 현재 페이지 번호를 요청 파라미터에서 가져옴
    page_no = int(request.GET.get('page', 1))
    num_of_rows = 15  # 페이지 당 항목 수

    # 요청 파라미터에서 mapx와 mapy 값을 가져옴
    current_mapx = request.GET.get('mapx')
    current_mapy = request.GET.get('mapy')

    # 위치 정보가 없는 경우 기본 위치 사용
    if not current_mapx or not current_mapy:
        current_mapx = 126.9780  # 서울의 경도
        current_mapy = 37.5665   # 서울의 위도

    # 검색 쿼리 가져오기
    search_query = request.GET.get('search', '')

    params = {
        'serviceKey': service_key,
        'numOfRows': 1000,  # 서버 측에서 페이지네이션 처리하기 위해 많은 수의 결과 가져오기
        'pageNo': 1,
        'MobileOS': 'ETC',
        'MobileApp': 'AppTest',
        '_type': 'json',
        'listYN': 'Y',
        'arrange': 'S',  # 'E'를 사용하여 거리순으로 정렬
        'mapX': current_mapx,
        'mapY': current_mapy,
        'radius': 50000,
        'contentTypeId': 12
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # HTTP 에러 체크
        data = response.json()

        # 필요한 데이터 추출
        items = data.get('response', {}).get('body', {}).get('items', {}).get('item', [])
        
        # 검색 쿼리로 항목 필터링
        if search_query:
            items = [item for item in items if search_query.lower() in item.get('title', '').lower()]

        # 필터링된 항목에 대해 페이지네이션 구현
        paginator = Paginator(items, num_of_rows)
        paginated_items = paginator.get_page(page_no)

    except requests.exceptions.RequestException as e:
        # API 요청 에러 처리
        return JsonResponse({'error': str(e)}, status=500)

    except ValueError as e:
        # JSON 디코딩 에러 처리
        return JsonResponse({'error': 'JSON decode error: ' + str(e)}, status=500)

    context = {
        'items': paginated_items,  # 페이지네이션된 항목을 컨텍스트에 전달
        'current_page': page_no,
        'total_pages': paginator.num_pages,
        'search_query': search_query,
        'current_mapx': current_mapx,
        'current_mapy': current_mapy,
    }

    return render(request, 'index.html', context)
