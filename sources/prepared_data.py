import faker
fake = faker.Faker()


data = {
    'userId': fake.random_int(min=1, max=10),
    'title': fake.word(),
    'body': fake.text(max_nb_chars=100)
}
big_data = {
    'userId': fake.random_int(min=99999999999, max=9999999999999),
    'title': fake.text(max_nb_chars=999999),
    'body': fake.text(max_nb_chars=9999999)
}
max_data = {
    'userId': fake.random_int(min=9999, max=999999),
    'title': fake.word(),
    'body': fake.text(max_nb_chars=9999999)
}
max_data_for_update = {
    'userId': fake.random_int(min=9999, max=999999),
    'title': fake.word(),
    'body': fake.text(max_nb_chars=9999)
}
