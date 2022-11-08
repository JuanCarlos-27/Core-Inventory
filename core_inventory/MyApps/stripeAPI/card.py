from .import stripe

def create_card(user, token):
    source = stripe.Customer.create_source(
        user.customer_id,
        source=token
    )
    return source


def delete_card(user,card_id):
    source=stripe.Customer.delete_source(
        user.customer_id,
        source=card_id
    )
    return source