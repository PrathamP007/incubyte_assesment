Feature: Login Functionality

  @smoke 
  Scenario: Verify Account Balance
    Given User is on the registration page
    When User clicks on register
    When User enters valid registration details
    When User clicks on register submit
    Then User should be able to see the balance afer clicking on overview