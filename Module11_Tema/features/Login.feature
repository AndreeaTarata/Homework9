Feature: Login into the page 'https://the-internet.herokuapp.com/'
  As a user
  I want to login to "https://the-internet.herokuapp.com/login"
  So I can enter and exit my account safely

  Scenario: test new URL after login
    Given I have a valid url page
    And an expected title "The Internet"
    When I compare
    Then the title from the url is equal with "The internet"

  Scenario: test page title
    Given I have a valid user
    And a valid password
    When I click on login button
    Then the new URL will be "https://the-internet.herokuapp.com/secure"


  Scenario: test the text from XPATH = // h2
    Given I a valid XPATH = // h2
    And an expected text "Login Page"
    When I compare them
    Then the result is true

  Scenario: test if login button is displayed
    Given I have a valid url
    And a Login Page displayed
    When I search for the login button
    Then the login button is displayed

  Scenario: new URL
    Given I have a valid user
    And a valid password
    When I click on login button
    Then the new URL will be "https://the-internet.herokuapp.com/secure"

  Scenario: test error after no value are entered in login area
    Given I have no data for user
    And no data for password
    When I click login
    Then an error is displayed

  Scenario: test invalid login
    Given I enter an invalid login
    And an invalid password
    When I send than to login form
    Then a correct error message will be displayed

  Scenario: test "x" that can be clicked when invalid login
    Given I have no data for user
    And no data for password
    When I click login
    Then an error is displayed
    And the "x" button can be clicked

  Scenario: test text on //label elements
    Given I search for all label
    And the expected is "username" and "password"
    When I compare the search result with the expected
    Then the result in True

  Scenario: test new URL is correct after valid logindc
    Given I have a valid user
    And a valid password
    When I click on login button
    Then the new URL will be "https://the-internet.herokuapp.com/secure"
    And elemst with "flash success" class is displayed

  Scenario: test logout url
    Given I have a valid user
    And a valid password
    When I click on login button
    And than on logout button
    Then the new url is 'https://the-internet.herokuapp.com/login'



