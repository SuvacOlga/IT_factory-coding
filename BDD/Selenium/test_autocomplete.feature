Feature: Autocomplete
  as a user
  I want to type letters
  so that an address to be suggested

  Scenario: Check address field
    Given I go to autocomplete form
    When I type CJ in address field
    Then Cluj should be return
    And Postal code

