Feature: Autocomplete
  as a user
  I want to type letters
  so that an address to be suggested

  Scenario Outline: Check address field
    Given I go to autocomplete form
    When I type "<city>" in address field
    Then "<actual_city>" should be return
    Examples:
      | city | actual_city |
      | CJ | Cluj |
      | BU | Bucuresti |
      | TM | Timisoara |
