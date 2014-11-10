from requests import get as http_get
from django.views.generic import TemplateView
from bs4 import BeautifulSoup


SEARCH_URL = "".join(
    [
    "http://tanitjobs.com/search-results-jobs/?action=search&listing_type%5B",
    "equal%5D=Job&keywords%5Ball_words%5D=python&JobCategory%5Bmulti_like%5",
    "D%5B%5D="
    ]
)


class JobView(TemplateView):
    """
    Job View Class.
    """

    def get_context_data(self, *args, **kwargs):
        context = super(JobView, self).get_context_data(*args, **kwargs)
        response = http_get(SEARCH_URL)
        soup = BeautifulSoup(response.text)
        jobs_info = soup.find_all("div", attrs={"class":"detail"})
        jobs = []
        for job_info in jobs_info:
            jobs.append(
                dict(
                    title=job_info.a.text,
                    link=job_info.a["href"]
                )
            )
        context.update(jobs=jobs)
        return context
