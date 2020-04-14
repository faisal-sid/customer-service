Feature: Update customer info

  Scenario: An existante customer changes lastname
    Given customer "Gene Kim" with ID "12345" exists
    When "Gene Kim" updates her name to "Gene Sid"
    Then I should be able to fetch customer details for "Gene Sid"
