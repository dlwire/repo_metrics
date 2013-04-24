Feature: The test metrics should be available for a specific user
    In order to see test recent testing efforts
    As a developer
    I want to see the percentage of my pushes containing tests

    Scenario: It should be able to handle no changesets for the user
        Given a repository with no changesets commited by the user
        When I run the metrics tool with a user name
        Then I should see output indicating there have been no changes by that user

    Scenario: It should report the metrics for the user in question
        Given a repository with changesets committed by a user
        When I run the metrics tool with a user name
        Then I should see output indicating the test commit percentage for that user

