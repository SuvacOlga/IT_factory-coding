Feature: BDD supports multiple parameters
  As a tester
  I want to see how many parameters supports BDD
  so that I will avoid duplication

  @smoke
  Scenario Outline: BDD with data driven approach
    Given A test case has "<nr_of_steps>" steps
    When We implement "<nr_of_methods>" methods
    Then Cucumber helps with the execution of "<actual_nr_of_steps>"
    Examples:
      | nr_of_steps | nr_of_methods | actual_nr_of_steps |
      | 1           | 4             | 3                  |
      | 2           | 7             | 2                  |
      | 3           | 2             | 2                  |
      | 3           | 2             | 2                  |
      | 3           | 2             | 2                  |
      | 3           | 2             | 2                  |
      | 3           | 2             | 2                  |
      | 3           | 2             | 2                  |
      | 3           | 2             | 2                  |
      | 3           | 2             | 2                  |
      | 3           | 2             | 2                  |
      | 3           | 2             | 2                  |
      | 3           | 2             | 2                  |
      | 3           | 2             | 2                  |
      | 3           | 2             | 2                  |
      | 3           | 2             | 2                  |
      | 3           | 2             | 2                  |
