
from bson.objectid import ObjectId
from pprint import pprint
from models import Category
from service import CategoryService


service = CategoryService()
while True:

    transactions = input('Plase type a process : ')

    match transactions:
        case 'create':
            name = input('Name :  ')
            description = input('Description :  ')
            category = Category(name=name, description=description)
            service.create(category.__dict__)


        case 'read all':
            service.get_all()


        case 'read by id':
            _id = input("ID: ")
            service.get_by_id(_id)


        case 'update':
            _id = input('id gir.')
            filter_value = {'_id': ObjectId(_id)}

            name = input('Name : ')
            description = input('Description : ')
            set_value = {
                    '_BaseEntity__status': 'Modifield',
                    'name': name,
                    'description': description
                }
            service.update(filter_value, set_value)


        case 'delete':
            _id = input('id gir.')
            filter_value = {'_id': ObjectId(_id)}

            set_value = {
                '_BaseEntity__status': 'Passive',
            }
            service.update(filter_value, set_value)
