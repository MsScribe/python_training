from model.group import Group
import random
import allure


def test_modify_group(app, db, check_ui):
    with allure.step("Given a non-empty group list"):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="privet", header="privet", footer="privet"))
        old_groups = db.get_group_list()
    with allure.step("Given a random group from the list"):
        group_random = random.choice(old_groups)
    group = Group(name="poka6", header="poka1", footer="poka1")
    with allure.step("When I modify the group from the list"):
        app.group.modify_group_by_id(group_random.id, group)
        old_groups[old_groups.index(group_random)].name = group.name
        old_groups[old_groups.index(group_random)].header = group.header
        old_groups[old_groups.index(group_random)].footer = group.footer
    with allure.step("Then the group has been replaced in the group list"):
        new_groups = db.get_group_list()
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="privet", header="privet", footer="privet"))
    old_groups = db.get_group_list()
    group_random = random.choice(old_groups)
    group = Group(name="New group1")
    app.group.modify_group_by_id(group_random.id, group)
    old_groups[old_groups.index(group_random)].name = group.name
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_group_header(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="privet", header="privet", footer="privet"))
    old_groups = db.get_group_list()
    group_random = random.choice(old_groups)
    group = Group(header="New header")
    app.group.modify_group_by_id(group_random.id, group)
    old_groups[old_groups.index(group_random)].header = group.header
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_group_footer(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="privet", header="privet", footer="privet"))
    old_groups = db.get_group_list()
    group_random = random.choice(old_groups)
    group = Group(footer="New footer")
    app.group.modify_group_by_id(group_random.id, group)
    new_groups = db.get_group_list()
    old_groups[old_groups.index(group_random)].footer = group.footer
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)