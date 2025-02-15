Feature: Search Functionality

  Scenario: Successfully search for a product
    Given I am on the homepage
    When I enter "Laptop" into the search bar
    And I click the search button
    Then I should see results related to "Laptop"

  Scenario: Search for an unavailable product
    Given I am on the homepage
    When I enter "XYZ123" into the search bar
    And I click the search button
    Then I should see a "No results found" message
