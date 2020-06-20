from model.group import Group


def test_modify_group(app):
    app.group.modify_first_group(Group(name="poka", header="poka", footer="poka"))


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="New group"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="New header"))


def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footer="New footer"))