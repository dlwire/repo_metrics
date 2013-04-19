Feature: The test metrics should be available since a starting date
    In order to see test recent testing efforts
    As a developer
    I want to see the percentage of pushes containing tests since a date

    Scenario: It should be able to handle no changesets since the date
        Given a repository with changesets before the start date
        When I run the metrics tool with a start date
        Then I should see output indicating there have been no changes since the start date

    Scenario: It should report the metrics since the start date
        Given a repository with changesets before and after the start date
        When I run the metrics tool with a start date
        Then I should see output indicating the test commit percentage since the start date

