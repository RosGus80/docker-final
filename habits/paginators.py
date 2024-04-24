from rest_framework.pagination import PageNumberPagination


class HabitListPaginator(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_no'
