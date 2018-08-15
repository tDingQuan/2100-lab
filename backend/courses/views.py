from django.http import JsonResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Heroes, Course


def get_heroes(request):
    heroes = Heroes.objects.all()
    count = heroes.count()
    json_data = {
        'count': count,
        'content': []
    }
    for hero in heroes:
        json_data['content'].append(hero.as_dict())
    return JsonResponse(json_data)


def get_recent_courses(request):
    free_courses = Course.objects.filter(price='0.00').order_by('-modified_at')[:10]
    paid_courses = Course.objects.exclude(price='0.00').order_by('-modified_at')[:10]
    json_data = {
        'free_courses': [],
        'paid_courses': []
    }
    for free_course in free_courses:
        json_data['free_courses'].append(free_course.as_dict())
    for paid_course in paid_courses:
        json_data['paid_courses'].append(paid_course.as_dict())
    return JsonResponse(json_data)


def get_free_course_list(request):
    course_objects = Course.objects.filter(price='0.00').order_by('-modified_at')
    count = course_objects.count()

    page = request.GET.get('page', request.POST['page'])
    paginator = Paginator(course_objects, request.POST['page_limit'])

    try:
        course_page = paginator.page(page)
    except PageNotAnInteger:
        course_page = paginator.page(request.POST['page'])
    except EmptyPage:
        course_page = paginator.page(paginator.num_pages)

    course_list = list(
        map(lambda course_object: course_object.as_dict(), list(course_page))
    )
    return JsonResponse(
        {
            'count': count,
            'content': course_list
        },
        safe=False
    )


def get_paid_course_list(request):
    course_objects = Course.objects.exclude(price='0.00').order_by('-modified_at')
    count = course_objects.count()

    page = request.GET.get('page', request.POST['page'])
    paginator = Paginator(course_objects, request.POST['page_limit'])

    try:
        course_page = paginator.page(page)
    except PageNotAnInteger:
        course_page = paginator.page(request.POST['page'])
    except EmptyPage:
        course_page = paginator.page(paginator.num_pages)

    course_list = list(
        map(lambda course_object: course_object.as_dict(), list(course_page))
    )
    return JsonResponse(
        {
            'count': count,
            'content': course_list
        },
        safe=False
    )
