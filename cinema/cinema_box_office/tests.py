from django.test import TestCase

# Create your tests here.
PTLam, [15.02.20 19:27]
У меня в модельке FilmSession есть метод для сверки даты новой сесси с датой самой сессии:

class FilmSession(models.Model):
     .....................

    def check_time_with_session_time(self, request, time_from, time_to):
        """
        :param time_from: start time of a new session
        :param time_to: end time of a new session
        :return: True if test was passed
        Test:
            1) (time_from < self.time_from and time_to < self.time_from) - ___new___|session_time|___ new session
            should be before existing session
                OR
            2) (time_from > self.time_to and time_to > self.time_to) - ____|session_time|___new___ new session should
            be after existing session
        """
        if (time_from < self.time_from and time_to < self.time_from) or (time_from > self.time_to and time_to > self.time_to):
            return True
        messages.add_message(request, messages.ERROR,
                             f'ERROR: The session was not created, as there is already a session during this time: {time_from}-{time_to}!')

PTLam, [15.02.20 19:28]
Потом я в view, которая создает объект новой сессии вызываю этот метод у всех существующих в БД сессии для сверки со временем с новой сессии.
Если нет совпадение, то я создаю объект, в противном случае вызываю ошибку.
class SessionCreateView(AdminTestMixin, CreateView):
    """
    Admin can create a new session.
    """
    model = FilmSession
    fields = ('film', 'hall', 'price', 'time_from', 'time_to', )
    template_name = 'filmsessions/sessions/create.html'

    def post(self, request, *args, **kwargs):
        film_obj = Film.objects.get(id=int(request.POST.get('film')))
        hall_id = int(request.POST.get('hall'))
        all_hall_sessions = FilmSession.objects.filter(hall__id=hall_id)

        # new session's naive datetime
        time_from_str = request.POST.get('time_from')
        time_to_str = request.POST.get('time_to')
        # transform the time to aware datetime 'Europe/Kiev'
        local = pytz.timezone('Europe/Kiev')
        time_from = local.localize(datetime.strptime(time_from_str, '%Y-%m-%d %H:%M'), is_dst=True)
        time_to = local.localize(datetime.strptime(time_to_str, '%Y-%m-%d %H:%M'), is_dst=True)

        # check if end time of new session > start time AND that session will be in the film's screening period
        if FilmSession.check_valid_sessiontime(request=request, time_from=time_from,
                                               time_to=time_to, film=film_obj):
            # check if new session will not be at the same time as another existing session in the hall
            if all(s.check_time_with_session_time(request=request,
                                                  time_from=time_from,
                                                  time_to=time_to) for s in all_hall_sessions):
                messages.add_message(request, messages.SUCCESS, f'The new session was created!')
                return super().post(request, *args, **kwargs)
        return redirect(self.request.META.get('HTTP_REFERER'))

    def get_success_url(self):
        return reverse_lazy('film-sessions:session-list')