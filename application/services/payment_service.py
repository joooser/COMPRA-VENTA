# payment_service.py

class PaymentService:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def process_payment(self, payment_info):
        # Logic to process payment through the payment gateway
        payment_result = self.payment_gateway.charge(payment_info)
        return payment_result

    # Additional methods as needed for payment management