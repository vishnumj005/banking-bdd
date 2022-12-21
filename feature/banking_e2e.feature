@banking
Feature: Validating the Banking feature

  @add-customer
  Scenario: Attempt to add customer to Bank
    Given url is loaded
    When I click on bank manager login button
    And I verify the page url
    And I click on add customer button
    And I fill the customer information and click add customer button
    And I click on open account tab
    And I select customer name and currency
    And I click process button
    Then verify the account created pop up message
