Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <middlename>, <lastname>, <nickname>, <title>, <company>, <homeaddress>, <homephone>, <mobilephone>, <workphone>, <faxphone>, <email>, <email2>, <email3>, <homepage>, <bday>, <bmonth>, <byear>, <aday>, <amonth>, <ayear>, <address2>, <phone2> and <notes>
  When I add the contact to the list
  Then the new contact list is equal to the old contact list with the added contact

  Examples:
  | firstname  | middlename  | lastname  | nickname  | title  | company  | homeaddress    | homephone | mobilephone  | workphone | faxphone | email             | email2           | email3           | homepage      | bday | bmonth | byear | aday | amonth   | ayear | address2 | phone2     | notes  |
  | firstname1 | middlename1 | lastname1 | nickname1 | title1 | company1 | streetaddress1 | +76703299 | +79998765533 | +25386    | +173     | emailcuxz@mail.ru | email@mail.ru    | email@mail.ru    | https://5Hgk  | 1    | July   | 1990  | 3    | November | 1999  | address1 | +440495557 | notes1 |
  | firstname2 | middlename2 | lastname2 | nickname2 | title2 | company2 | streetaddress2 | +71234267 | +79876543210 | +25386    | +173     | email8@mail.ru    | emailFXJ@mail.ru | emailPqg@mail.ru | https://dgsdf | 2    | July   | 1997  | 4    | November | 2001  | address2 | +45155122  | notes2 |


Scenario: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I modify the contact from the list
  Then the contact has been replaced in the contact list


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old contact list without the deleted contact