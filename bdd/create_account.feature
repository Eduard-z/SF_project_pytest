Feature: create SF record
# in order to define a repeated step then use Background:
  Scenario Outline: create account record
    Given list view of Account object <object_name> <object_api_name>
    When I open New Account modal form for <record_type_name>
    And I populate <field_1> with <field_1_value>
    And I populate <field_2> with <field_2_value>
    And I populate <field_3> with <field_3_value>
    And I click "Save" button
    Then new Account record is created
    And having <field_1> equal to <field_1_value>
    And having <field_2> equal to <field_2_value>
    And having <field_3> equal to <field_3_value>

    Examples:
      | object_name | object_api_name | record_type_name | field_1 | field_1_value | field_2 | field_2_value | field_3 | field_3_value    |
      | Account     | Account         | Organization     | Account Name | A5       | Prospect Rating | Warm  | Has Support Plan | checked |
