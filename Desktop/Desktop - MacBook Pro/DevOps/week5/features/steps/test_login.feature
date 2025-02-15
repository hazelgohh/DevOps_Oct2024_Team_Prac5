Feature: Login Functionality

  Scenario: Successful Login
    Given I open the login page
    When I enter a valid username and password
    And I click the login button
    Then I should be redirected to the homepage
