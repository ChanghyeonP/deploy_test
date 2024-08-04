from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Comment
from .forms import CommentForm
from decouple import config
import requests

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
        response.raise_for_status()
        data = response.json()
        item = data.get('response', {}).get('body', {}).get('items', {}).get('item', [])[0]
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
    except (IndexError, ValueError) as e:
        return JsonResponse({'error': 'No data found: ' + str(e)}, status=404)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.item_id = content_id
            comment.author = request.user
            comment.nickname = request.user.nickname
            comment.save()
            return redirect('tourist_attraction_detail', content_id=content_id)
    else:
        form = CommentForm()

    comments = Comment.objects.filter(item_id=content_id).order_by('-created_at')

    context = {
        'item': item,
        'kakao_api_key': kakao_api_key,
        'comments': comments,
        'form': form,
    }

    return render(request, 'detail.html', context)

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if comment.author == request.user:
        comment.delete()
    return redirect('tourist_attraction_detail', content_id=comment.item_id)
