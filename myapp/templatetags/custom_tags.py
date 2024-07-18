from django import template

register = template.Library()

@register.simple_tag
def get_range(total_pages, current_page):
    try:
        current_page = int(current_page)
    except (ValueError, TypeError):
        current_page = 1  # 기본값 설정

    try:
        total_pages = int(total_pages)
    except (ValueError, TypeError):
        total_pages = 1  # 기본값 설정

    start_page = max(current_page - 5, 1)
    end_page = min(current_page + 5, total_pages)
    return range(start_page, end_page + 1)
