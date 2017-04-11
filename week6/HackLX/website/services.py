from .models import Offer

def delete_offer(request, pk):
    offer = get_object_or_404(Offer, pk=int(pk))
    offer.delete()
    return redirect(reverse('website:index'))


def get_categoty_names(Category):
    result_title_names = []
    query_set_tuples = Category.objects.values_list('name')

    for abs in query_set_tuples:
        result_title_names.insert(len(result_title_names), ''.join(abs))

    # import ipdb; ipdb.set_trace()
    return result_title_names
