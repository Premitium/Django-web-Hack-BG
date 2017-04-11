from .models import Offer

def delete_offer(request, pk):
    offer = get_object_or_404(Offer, pk=int(pk))
    offer.delete()
    return redirect(reverse('website:index'))
