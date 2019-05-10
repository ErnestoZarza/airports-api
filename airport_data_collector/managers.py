from django.db.models import Q, QuerySet
from django.template.defaultfilters import slugify


class AirportSet(QuerySet):
    """QuerySet class in order to add
        filters to the Airports Model's queries
    """

    def search_by_name(self, pattern):
        slug_pattern = slugify(pattern)
        return self.filter(slug__icontains=slug_pattern).distinct()

    def search_by_iata(self, iata):
        return self.filter(iata=iata)
