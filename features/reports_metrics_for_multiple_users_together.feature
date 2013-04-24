Feature: The test metrics should be available for multiple users
    In order to see test recent testing efforts
    As a developer
    I want to see the percentage of my teams pushes containing tests

    Scenario: It should be able to handle no changesets for any users
        Given a repository with no changesets commited by the users
        When I run the metrics tool with multiple user names
        Then I should see output indicating there have been no changes by those users

    Scenario: It should report the metrics for the users in question
        Given a repository with changesets committed by the users
        When I run the metrics tool with multiple user names
        Then I should see output indicating the test commit percentage for those users

