from enum import Enum


class Filter(Enum):
    page = 1
    limit = 2
    name = 3
    Sort = 4


class UserEntry(Enum):
    id = 101
    first_name = 102
    last_name = 103
    company_name = 104
    city = 105
    state = 106
    zip = 107
    email = 108
    web = 109
    age = 110


class CollectionName(Enum):
    users = 201
