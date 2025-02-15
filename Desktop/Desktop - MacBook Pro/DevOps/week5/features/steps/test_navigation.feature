Feature: Website Navigation

  Scenario: Navigate through different pages
    Given I am on the homepage
    When I click on the "Products" page
    Then I should be redirected to the products page

  Scenario: Navigate to the login page
    Given I am on the homepage
    When I click on the "Login" button
    Then I should be redirected to the login page
