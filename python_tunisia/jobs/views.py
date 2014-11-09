from request import get as http_get
from django.views.generic import TemplateView
from bs4 import BeautifulSoup

# Create your views here.
SEARCH_URL = (
    "http://tanitjobs.com/search-results-jobs/?action=search&listing_type%5B",
    "equal%5D=Job&keywords%5Ball_words%5D=python&JobCategory%5Bmulti_like%5",
    "D%5B%5D="
)

class JobView(TemplateView):
    """
    Job View Class.
    """

    def get_context_data(self, *args, **kwargs):
        super(JobView, self).get_context_data(*args, **kwargs)
        response = http_get(SEARCH_URL)
        soup = BeautifulSoup(response.text)
