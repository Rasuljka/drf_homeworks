from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User, Payments
from users.serializers import UserSerializer, PaymentsSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny, )

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_lesson', 'paid_course', 'pay_transfer')
    ordering_fields = ['pay_date']

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        product = create_stripe_product(payment.paid_course)
        price = create_stripe_price(product=product, amount=payment.pay_sum)
        session_id, session_url = create_stripe_session(price)
        payment.session_id = session_id
        payment.payment_link = session_url
        payment.payment_status = check_status_stripe(payment.session_id)
        payment.save()

    @action(detail=True, methods=['get']) #доступно по адресу .../payments/<int:pk>/status/
    def status(self, request, pk=None):
        payment = self.get_object()
        payment_status = check_status_stripe(payment.session_id)
        return Response({"status": payment_status})