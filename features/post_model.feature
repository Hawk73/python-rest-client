Feature: Post model
  Background: init
    Given init API client
    Given init post model

  # Get all resources

  Scenario: Get lists with valid credentials
    Given client has valid credentials
    When make get all request for posts
    Then it does not have error
    Then it returns collection of posts

  Scenario: Get lists with invalid credentials
    Given client has invalid credentials
    When make get all request for posts
    Then it throws unauthorized error


  # Get resource

  Scenario: Get resource with valid credentials
    Given client has valid credentials
    When make get resource request for posts
    Then it does not have error
    Then it returns resource of post

  Scenario: Get nonexistent resource with valid credentials
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
    Then it returns resource of post

  Scenario: Create resource with invalid credentials
    Given client has invalid credentials
    When make create resource request for posts
    Then it throws unauthorized error


  # Update resource

  Scenario: Update resource with valid credentials
    Given client has valid credentials
    When make update resource request for posts
    Then it does not have error
    Then it returns True

  Scenario: Update nonexistent resource with valid credentials
    Given client has invalid credentials
    Given resource does not exist
    When make update resource request for posts
    Then it throws not found error

  Scenario: Update resource with invalid credentials
    Given client has invalid credentials
    When make update resource request for posts
    Then it throws unauthorized error


  # Delete resource by ID

  Scenario: Delete resource by ID with valid credentials
    Given client has valid credentials
    When make delete resource by ID request for posts
    Then it does not have error
    Then it returns True

  Scenario: Delete nonexistent resource by ID with valid credentials
    Given client has valid credentials
    Given resource does not exist
    When make delete resource by ID request for posts
    Then it throws not found error

  Scenario: Delete resource by ID with invalid credentials
    Given client has invalid credentials
    When make delete resource by ID request for posts
    Then it throws unauthorized error

  # Delete resource

  Scenario: Delete resource with valid credentials
    Given client has valid credentials
    When make delete resource request for posts
    Then it does not have error
    Then it returns True

  Scenario: Delete nonexistent resource with valid credentials
    Given client has valid credentials
    Given resource does not exist
    When make delete resource request for posts
    Then it throws not found error

  Scenario: Delete resource with invalid credentials
    Given client has invalid credentials
    When make delete resource request for posts
    Then it throws unauthorized error
