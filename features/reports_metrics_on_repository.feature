Feature: The test metrics should be available on the entire repository
    In order to understand the amount of testing being done
    As a developer
    I want to see the percentage of pushes containing tests

    Scenario: It should be able to handle no repository
        When I run the metrics tool
        Then I should see output indicating there is no repository

    Scenario: It should be able to handle empty repositories
        Given an empty repository
        When I run the metrics tool
        Then I should see output indicating the repository is empty

    Scenario: It should report the test commit percentage for the repository
        Given a repository with changesets
        When I run the metrics tool
        Then I should see output indicating the test commit percentage of the repository

    Scenario: It should report metrics only for the default branch
        Given a repository with changesets to multiple branches
        When I run the metrics tool
        Then I should see output indicating the test commit percentage of the default branch
