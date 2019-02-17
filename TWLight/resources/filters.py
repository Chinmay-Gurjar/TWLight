import django_filters

from .models import Language,Partner

# The combination of taggit and filters caused a bootstrapping problem.
# This code can run before the taggit migrations have run, meaning the tables
# don't yet exist;, so it needs to be a function.
def get_partner_tags():
    try:
        return Partner.tags.all()
    except:
        pass

class PartnerFilter(django_filters.FilterSet):
    tags = django_filters.ModelChoiceFilter(queryset=get_partner_tags())
    languages = django_filters.ModelChoiceFilter(queryset=Language.objects.all())
<<<<<<< HEAD
    company_name = django_filters.CharFilter(lookup_expr = 'icontains')
=======
    company_name = django_filters.CharFilter(lookup_expr='icontains')
>>>>>>> b71a7e352d6857106cae15486538b688a993eba4
    class Meta:
        model = Partner
        fields = ['languages', 'tags', 'company_name']

<<<<<<< HEAD
=======

>>>>>>> b71a7e352d6857106cae15486538b688a993eba4
PartnerFilter.base_filters['company_name'].label = 'Company Name'
