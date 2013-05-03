Feature: The test metrics should be available for a combination of arguments
    In order to see test recent testing efforts
    As a developer
    I want to see the percentage of my recent pushes containing tests

    Scenario: It should report the metrics for the user in question after a given date
        Given a repository with changesets
            | files | user | date |
            | codefile1 | A User       | 1980-10-02 |
            | codefile2 | Another user | 1980-10-04 |
            | testfile1 | A User       | 1980-10-04 |
            | codefile3 | A User       | 1980-10-04 |

        When I run the metrics tool with arguments
            | type        | arguments  |
            | --users     | A User     |
            | --afterDate | 1980-10-03 | 

        Then I should see the following output
            | output lines                     |
            | 50 percent of commits have tests |
