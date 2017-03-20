Feature: Posts

  Scenario: Get lists with valid credentials
    Given client has valid credentials
      When made get list request for posts
      Then it returns not empty list

  Scenario: Get lists with invalid credentials
    Given client has invalid credentials
      When made get list request for posts
      Then it throws 403 error
