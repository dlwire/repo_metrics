Feature: The test metrics should be available for a combination of arguments
    In order to see test recent testing efforts
    As a developer
    I want to see the percentage of my recent pushes containing tests

    Scenario: It should report the metrics for the user in question after a given date
        Given a repository with changesets committed by a user before and after a date
        When I run the metrics tool with a user name and start date
        Then I should see output indicating the test commit percentage

