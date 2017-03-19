Feature: Posts

  Scenario: Make get request
    Given client has valid credentials
      When made get list request for posts
      Then client should return list of posts

    Given client has invalid credentials
      When made get list request for posts
      Then client should return error
