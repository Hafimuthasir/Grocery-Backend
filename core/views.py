from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import GroceryItem
from .serializers import GroceryItemSerializer
from rest_framework import status

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class GroceryItemView(APIView):
    """
    API view for listing and creating grocery items.
    """
    pagination_class = CustomPageNumberPagination()

    def get(self, request, *args, **kwargs):
        """
        Get a paginated list of grocery items.

        :return: Paginated grocery item list.
        """
        page_number = self.request.query_params.get(self.pagination_class.page_query_param, 1)

        cache_key = f'grocery_item_list_page_{page_number}'
        cached_data = cache.get(cache_key)

        if cached_data is None:
            queryset = GroceryItem.objects.all().order_by('-id')
            page = self.pagination_class.paginate_queryset(queryset, request, view=self)

            if page is not None:
                serializer = GroceryItemSerializer(page, many=True)
                cached_data = self.pagination_class.get_paginated_response(serializer.data).data
                cache.set(cache_key, cached_data)

        return Response(cached_data)

    def post(self, request, *args, **kwargs):
        """
        Create a new grocery item.

        :return: Response with the created grocery item or validation errors.
        """
        serializer = GroceryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Invalidate the cache for the affected page
            self.invalidate_cache()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def invalidate_cache(self):
        """
        Invalidate the entire cache for grocery item lists.
        """
        cache.clear()



class GroceryItemDetailView(APIView):
    """
    API view for retrieving details of a specific grocery item.
    """
    def get(self, request, pk):
        """
        Get details of a specific grocery item.

        :param pk: Primary key of the grocery item.
        :return: Response with the grocery item details or a 404 error if not found.
        """

        cache_key = f'grocery_item_{pk}'
        item = cache.get(cache_key)

        if item is None:
            try:
                item = get_object_or_404(GroceryItem, pk=pk)
                cache.set(cache_key, item)
            except ObjectDoesNotExist:
                return Response({"error": "Grocery item not found."}, status=404)

        serializer = GroceryItemSerializer(item)
        return Response(serializer.data)
