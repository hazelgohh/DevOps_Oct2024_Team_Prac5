Feature: Checkout Process

  Scenario: Successfully complete a checkout
    Given I am logged into the website
    When I add a product to the cart
    And I proceed to checkout
    And I enter my shipping details
    And I confirm the purchase
    Then I should see a confirmation message
