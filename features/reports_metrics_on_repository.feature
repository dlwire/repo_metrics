Feature: The test metrics should be available on the entire repository

    Scenario: It should be able to handle no repository
        When I run the metrics tool
        Then I should see output indicating there is no repository

    Scenario: It should be able to handle empty repositories
        Given an empty repository
        When I run the metrics tool
        Then I should see the following output
            | output lines            |
            | The repository is empty |

    Scenario: It should report the test commit percentage for the repository
        Given a repository with changesets
            | files               |
            | codefile1, testfile | 
            | codefile2           |
        When I run the metrics tool
        Then I should see the following output
            | output lines                     |
            | 50 percent of commits have tests |

    Scenario: It should report metrics only for the default branch
        Given a repository with changesets
            | files               | branch     |
            | codefile1, testfile | default    |
            | codefile2           | default    |
            | codefile3           | Don't Care |
        When I run the metrics tool
        Then I should see the following output
            | output lines                     |
            | 50 percent of commits have tests |
