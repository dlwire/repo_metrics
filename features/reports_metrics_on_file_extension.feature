Feature: The test metrics should be available for commits touching specified file types

    Scenario: It should report the test commit percentage changesets touching specified extensions
        Given a repository with changesets
            | files                      |
            | codefile1.py               |
            | codefile2.cpp, testfile    |
            | codefile3.h, codefile3.cpp |

        When I run the metrics tool with arguments
            | type         | arguments |
            | --extensions | cpp       |

        Then I should see the following output
            | output lines                     |
            | Filtering by...                  |
            |     Extensions: cpp              |
            |                                  |
            | Total Commits: 2                 |
            | 50 percent of commits have tests |
