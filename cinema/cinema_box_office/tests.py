# class BuyTicketView(CreateView, LoginRequiredMixin):
#     template_name = 'cinema/buy_ticket.html'
#     # model = Ticket
#     http_method_names = ['get', 'post']
#     login_url = 'authentication/login/'
#     success_url = '/'
#     form_class = AmountForm
#     session = None

#     def get(self, request, *args, **kwargs):
#         if request.user.is_superuser:
#             raise PermissionDenied()
#         else:
#             return super().get(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         if request.user.is_superuser:
#             raise PermissionDenied()
#         else:
#             self.session = MovieSession.objects.get(id=kwargs.get("session_id"))
#             return super().post(request, *args, **kwargs)

#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.buyer = self.request.user
#         obj.session = self.session
#         obj.summ = int(self.request.POST.get('amount')) * obj.session.price
#         if obj.buyer.bonuses < obj.summ:
#             messages.error(self.request, "Sorry. Not enough bonuses")
#             return HttpResponseRedirect(reverse('session-list'))
#         if obj.session.hall.seats < int(self.request.POST.get('amount')):
#             messages.error(self.request, "tickets are not enough in stock")
#             return HttpResponseRedirect(reverse('session-list'))
#         obj.buy(price=self.session.price, quantity=self.request.POST.get('amount'), session=self.session)
#         obj.save()
#         messages.info(self.request, "You've successfully bought staff")
#         return HttpResponseRedirect(self.success_url)





# class Ticket(models.Model):
#     session = models.ForeignKey(MovieSession, related_name='tickets', on_delete=models.CASCADE)
#     buyer = models.ForeignKey(User, related_name='tickets', on_delete=models.CASCADE)
#     amount = models.PositiveIntegerField(default=1)
#     created_on = models.DateTimeField(auto_now_add=True)

#     def get_cost(self):
#         return self.session.price * self.amount

#     def buy(self, price, quantity, session):
#         # buy and add to total_bonuses
#         self.buyer.bonuses -= price * int(quantity)
#         self.buyer.save()
#         self.session.available_seats -= int(quantity)
#         self.session.save()
#         self.buyer.total_bonuses += price * int(quantity)
#         self.buyer.save()

#     def __str__(self):
#         return f"Ticket of film '{self.session.film.name}' at {self.session.time_from}"


# class AmountForm(forms.ModelForm):
#     class Meta:
#         model = Ticket
#         fields = ['amount', ]

# <form action="{% url 'buy_ticket' session.id %}" method="post">
#                 {% csrf_token  %}
#                 {{ amount }}
#                 <input type="submit" value="buy">

#                 </form>