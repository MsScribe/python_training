from model.group import Group
from random import randrange


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="privet", header="privet", footer="privet"))
    old_groups = app.group.get_group_list()
    group = Group(name="poka", header="poka", footer="poka")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="privet", header="privet", footer="privet"))
    old_groups = app.group.get_group_list()
    group = Group(name="New group1")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="privet", header="privet", footer="privet"))
    old_groups = app.group.get_group_list()
    group = Group(header="New header")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    group.name = old_groups[index].name
    app.group.modify_group_by_index(index, Group(header="New header"))
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="privet", header="privet", footer="privet"))
    old_groups = app.group.get_group_list()
    group = Group(footer="New footer")
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    group.name = old_groups[index].name
    app.group.modify_group_by_index(index, Group(footer="New footer"))
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)