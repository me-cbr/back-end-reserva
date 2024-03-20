# from inspect import signature
from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_restaurant():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'name': fake.sentence(nb_words=6),
        'description': fake.sentence(nb_words=12),
        'classification': randint(1, 5),
        'opening_hours': fake.date_time(),
        'closing_hours': fake.date_time(),
        'details': fake.text(3000),
        'category_id': {
            'name': fake.word()
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/food,cook' % rand_ratio(),
        }
    }

if __name__ == '__main__':
    from pprint import pprint
    pprint(make_restaurant())