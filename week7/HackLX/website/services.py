from .models import Offer

def get_categoty_names(Category):
    result_title_names = []
    query_set_tuples = Category.objects.values_list('name')

    for abs in query_set_tuples:
        result_title_names.insert(len(result_title_names), ''.join(abs))

    return result_title_names

def get_offer_status_pending(Offer):
    result_statuses_pending = []

    for e in Offer.objects.all():
        if e.status == 1:
            result_statuses_pending.insert(len(result_statuses_pending), e)

    return result_statuses_pending

def get_offer_status_approved_rejected(Offer):
    result = []

    for e in Offer.objects.all():
        if e.status == 2 or e.status == 3:
            result.insert(len(result), e)

    return result
