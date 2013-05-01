Feature: The test metrics should be available for commits touching specified file types

    Scenario: It should report the test commit percentage changesets touching specified extensions
        Given a repository with changesets with extensions
        When I run the metrics tool with specified extensions
        Then I should see output indicating the test commit percentage
