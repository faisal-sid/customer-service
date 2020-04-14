from customer_service.model.customer import Customer


def get_customer(customer_id, customer_repository):
    return customer_repository.fetch_by_id(customer_id)


def create_customer(first_name, surname, customer_repository):
    customer = Customer(first_name=first_name, surname=surname)
    customer_repository.store(customer)

    return customer.customer_id


def update_customer(first_name, surname, cid, customer_repository):
    customer = customer_repository.fetch_by_id(cid)
    customer.first_name = first_name
    customer.surname = surname
    customer_repository.store(customer)
    return customer
