from django.views.generic import ListView
from teststats.stats.models import Hit


class HitsView(ListView):
    model = Hit

    def get_queryset(self):
        qs = super(HitsView, self).get_queryset()
        user_id, page_id, date = map(self.request.GET.get, ['user_id', 'page_id', 'date'])
        if user_id:
            qs = qs.filter(user_id=user_id)
        if page_id:
            qs = qs.filter(page_id=page_id)
        if date:
            year, month, day = date.split('-')
            qs = qs.filter(time__year=year, time__month=month, time__day=day)
        return qs

    def get_context_data(self, **kwargs):
        context = super(HitsView, self).get_context_data(**kwargs)
        hits = Hit.objects.all()
        users = hits.values_list('user_id', flat=True).distinct()
        pages = hits.values_list('page_id', flat=True).distinct()
        dates = hits.datetimes('time', 'day')
        context.update({'users': users, 'pages': pages, 'dates': dates})
        return context
