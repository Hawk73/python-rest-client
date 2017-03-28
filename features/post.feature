Feature: Posts

  # Get resources

  Scenario: Get lists with valid credentials
    Given client has valid credentials
    When make get list request for posts
    Then it does not have error
    Then it returns not empty list

  Scenario: Get lists with invalid credentials
    Given client has invalid credentials
    When make get list request for posts
    Then it throws unauthorized error


  # Get resource

  Scenario: Get resource with valid credentials
    Given client has valid credentials
    When make get resource request for posts
    Then it does not have error
    Then it returns resource

  Scenario: Get resource with valid credentials
    Given client has valid credentials
    Given resource does not exist
    When make get resource request for posts
    Then it throws not found error

  Scenario: Get resource with invalid credentials
    Given client has invalid credentials
    When make get resource request for posts
    Then it throws unauthorized error


  # Create resource

  Scenario: Create resource with valid credentials
    Given client has valid credentials
    When make create resource request for posts
    Then it does not have error
    Then it returns ID

    Scenario: Create resource with invalid credentials
    Given client has invalid credentials
    When make create resource request for posts
    Then it throws unauthorized error
