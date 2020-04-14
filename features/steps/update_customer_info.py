from behave import when


@when(u'"{name}" updates her name to "{new_name}"')
def update_customer_name(context, name, new_name):
    (first_name, surname) = new_name.split(' ', 2)

    response = context.web_client.put(
        f'/customers/{context.customer_id}',
        json={'firstName': first_name,
              'surname': surname,
              'cid': context.customer_id})
    assert response.status_code == 200, response.status_code


# @then('I should be able to fetch customer details for "{name}"')
# def fetch_customer_by_context_id(context, name):
#     response = context.web_client.get(f'/customers/{context.customer_id}')

#     assert response.status_code == 200, response.status_code
#     customer = response.get_json()
#     assert f"{customer['firstName']} {customer['surname']}" == name
