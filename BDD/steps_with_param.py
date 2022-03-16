from behave import *


@given('A test case has "{nr_of_steps}" steps')
def step_impl(context, nr_of_steps):
    print(nr_of_steps)


@when('We implement "{nr_of_methods}" methods')
def step_impl(context, nr_of_methods):
    print(nr_of_methods)


@then('Cucumber helps with the execution of "{actual_nr_of_steps}"')
def step_impl(context, actual_nr_of_steps):
    print(actual_nr_of_steps)
