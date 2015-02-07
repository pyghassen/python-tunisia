"""
Events views module.
"""
from django.views.generic import ListView, DetailView
from events.models import Event


class ListEventsView(ListView):
    """
    List Events View class.
    """
    model = Event

    def get_context_data(self, **kwargs):
        """
        Gets the context data for ListEventsView.
        """
        context = super().get_context_data(**kwargs)
        context.update(
            future_events=Event.objects.future_events(),
            past_events=Event.objects.past_events()
        )
        return context

class EventDetailsView(DetailView):
    """
    Event Details View class.
    """
    model = Event

list_events_view = ListEventsView.as_view()
event_details_view = EventDetailsView.as_view()