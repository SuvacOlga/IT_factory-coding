Feature: LogIn
  As a user
  I want to long in to facebook
  so that I can see stories

  @smoke
  Scenario: My credentials are valid
    Given My email address exists
    And My password is correct
    And I am not a robot
    When I enter my credentials
    And I click login
    Then Load my page

  @regression
  Scenario: Invalid credentials
    Given My email address exists
    And My password is correct
    And I am not a robot
    When I click login
    Then Please fill user and password

  @regression
  Scenario: Forgot password
    Given My email address exists
    And Password incorrect
    When I click login
    Then Please add a new password or click forgot password
