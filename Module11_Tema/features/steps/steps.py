@given(u'I have a valid url page')
def step_impl(context):
    print(u'STEP: Given I have a valid url page')


@given(u'an expected title "The Internet"')
def step_impl(context):
    print(u'STEP: Given an expected title "The Internet"')


@when(u'I compare')
def step_impl(context):
    print(u'STEP: When I compare')


@then(u'the title from the url is equal with "The internet"')
def step_impl(context):
    print(u'STEP: Then the title from the url is equal with "The internet"')


@given(u'I have a valid user')
def step_impl(context):
    print(u'STEP: Given I have a valid user')


@given(u'a valid password')
def step_impl(context):
    print(u'STEP: Given a valid password')


@when(u'I click on login button')
def step_impl(context):
    print(u'STEP: When I click on login button')


@then(u'the new URL will be "https://the-internet.herokuapp.com/secure"')
def step_impl(context):
    print(u'STEP: Then the new URL will be "https://the-internet.herokuapp.com/secure"')


@given(u'I a valid XPATH = // h2')
def step_impl(context):
    print(u'STEP: Given I a valid XPATH = // h2')


@given(u'an expected text "Login Page"')
def step_impl(context):
    print(u'STEP: Given an expected text "Login Page"')


@when(u'I compare them')
def step_impl(context):
    print(u'STEP: When I compare them')


@then(u'the result is true')
def step_impl(context):
    print(u'STEP: Then the result is true')


@given(u'I have a valid url')
def step_impl(context):
    print(u'STEP: Given I have a valid url')


@given(u'a Login Page displayed')
def step_impl(context):
    print(u'STEP: Given a Login Page displayed')


@when(u'I search for the login button')
def step_impl(context):
    print(u'STEP: When I search for the login button')


@then(u'the login button is displayed')
def step_impl(context):
    print(u'STEP: Then the login button is displayed')


@given(u'I have no data for user')
def step_impl(context):
    print(u'STEP: Given I have no data for user')


@given(u'no data for password')
def step_impl(context):
    print(u'STEP: Given no data for password')


@when(u'I click login')
def step_impl(context):
    print(u'STEP: When I click login')


@then(u'an error is displayed')
def step_impl(context):
    print(u'STEP: Then an error is displayed')


@given(u'I enter an invalid login')
def step_impl(context):
    print(u'STEP: Given I enter an invalid login')


@given(u'an invalid password')
def step_impl(context):
    print(u'STEP: Given an invalid password')


@when(u'I send than to login form')
def step_impl(context):
    print(u'STEP: When I send than to login form')


@then(u'a correct error message will be displayed')
def step_impl(context):
    print(u'STEP: Then a correct error message will be displayed')


@then(u'the "x" button can be clicked')
def step_impl(context):
    print(u'STEP: Then the "x" button can be clicked')


@given(u'I search for all label')
def step_impl(context):
    print(u'STEP: Given I search for all label')


@given(u'the expected is "username" and "password"')
def step_impl(context):
    print(u'STEP: Given the expected is "username" and "password"')


@when(u'I compare the search result with the expected')
def step_impl(context):
    print(u'STEP: When I compare the search result with the expected')


@then(u'the result in True')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the result in True')


@then(u'elemst with "flash success" class is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then elemst with "flash success" class is displayed')


@when(u'than on logout button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When than on logout button')


@then(u'the new url is \'https://the-internet.herokuapp.com/login\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the new url is \'https://the-internet.herokuapp.com/login\'')


@given(u'I have link on the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have link on the login page')


@given(u'a href in elements')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a href in elements')


@then(u'the link \'Elemental Selenium\' is equal with the href')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the link \'Elemental Selenium\' is equal with the href')
