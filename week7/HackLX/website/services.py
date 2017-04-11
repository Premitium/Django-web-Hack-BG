from .models import Offer

def get_categoty_names(Category):
    result_title_names = []
    query_set_tuples = Category.objects.values_list('name')

    for abs in query_set_tuples:
        result_title_names.insert(len(result_title_names), ''.join(abs))

    return result_title_names
