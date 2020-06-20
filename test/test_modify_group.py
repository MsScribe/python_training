from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="privet", header="privet", footer="privet"))
    app.group.modify_first_group(Group(name="poka", header="poka", footer="poka"))


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="privet", header="privet", footer="privet"))
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="privet", header="privet", footer="privet"))
    app.group.modify_first_group(Group(header="New header"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="privet", header="privet", footer="privet"))
    app.group.modify_first_group(Group(footer="New footer"))