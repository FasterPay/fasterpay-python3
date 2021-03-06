from fasterpay.gateway import Gateway
from random import randint


if __name__ == "__main__":

    gateway = Gateway("<Your Private key>", "<Your Public key>",True)

    parameters = {
        "payload": {
            "description": "Golden Ticket",
            "amount": "10",
            "currency": "EUR",
            "merchant_order_id": randint(1000, 9999),
            "success_url": "http://localhost:12345/success.php",
            "recurring_name": "Test FP Recurring",
            "recurring_sku_id": "fp_test_recurring",
            "recurring_period": "10d",
            "recurring_trial_amount": "1",
            "recurring_trial_period": "3d",
            "recurring_duration": 0
        },
        "auto_submit_form": True
    }

    paymentForm = gateway.payment_form().build_form(parameters)

    print(paymentForm)
