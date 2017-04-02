Feature: Collection of posts
  Background: init
    Given init API client
    Given init collection

  Scenario: Delete all items from post collection
    Given client has valid credentials
    When delete all items
    Then it does not have error
    Then it has no items

  Scenario: Get first item from post collection
    Given client has valid credentials
    When get first item
    Then it returns resource of post
