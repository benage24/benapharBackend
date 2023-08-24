from rest_framework import pagination
from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):

    page_size = 10  # Number of items per page
    page_size_query_param = 'limit'  # Parameter for specifying page size in URL
    max_page_size = 100  # Maximum page size allowed

    # Override get_paginated_response method to include page_size in response
    def get_paginated_response(self, data):
        # Call the parent class's method to get the standard paginated response
        response = super().get_paginated_response(data)

        # Add the page_size field to the response data
        response.data['page_size'] = self.page_size

        return response
