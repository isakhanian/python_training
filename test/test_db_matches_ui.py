from model.group import Group
from timeit import timeit

def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1)) #выводим на печать время,  за которое получаем список по юай
    def clean(group):
        return Group(id=group.id, name=group.name.strip())
    print(timeit(lambda: map(clean, db.get_group_list()), number=1000)) #выводим на печать время,  за которое получаем список из бд
    assert False #sorted(ui_list, key = Group.id_or_max) == sorted(db_list, key = Group.id_or_max)
