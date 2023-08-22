from rest_framework import pagination

class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 1
    page_query_description = 'count'
    max_page_size = 3
    page_query_param = 'p'
    print("ertyuiop[")