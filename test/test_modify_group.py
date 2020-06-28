from model.group import Group


def test_modify_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="poka", header="poka", footer="poka")
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(Group(name="privet", header="privet", footer="privet"))
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    group = Group(name="New group1")
    group.id = old_groups[0].id
    if app.group.count() == 0:
        app.group.create(Group(name="privet", header="privet", footer="privet"))
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_header(app):
    old_groups = app.group.get_group_list()
    group = Group(header="New header")
    group.id = old_groups[0].id
    group.name = old_groups[0].name
    if app.group.count() == 0:
        app.group.create(Group(name="privet", header="privet", footer="privet"))
    app.group.modify_first_group(Group(header="New header"))
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_footer(app):
    old_groups = app.group.get_group_list()
    group = Group(footer="New footer")
    group.id = old_groups[0].id
    group.name = old_groups[0].name
    if app.group.count() == 0:
        app.group.create(Group(name="privet", header="privet", footer="privet"))
    app.group.modify_first_group(Group(footer="New footer"))
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)