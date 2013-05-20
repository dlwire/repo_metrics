Feature: The test metrics should be available by month over the life of the repository

   Scenario: It should report monthly metrics for the repository
        Given a repository with changesets
            | files                | date       |
            | codefile1            | 1980-9-02  |
            | testfile1            | 1980-10-03 |
            | codefile2            | 1980-10-03 |
            | codefile3, testfile2 | 1980-11-30 |

        When I run the metrics tool with arguments
            | type      | arguments  |
            | --byMonth |            |

        Then I should see the following output
            | output lines                                     |
            | Filtering by...                                  |
            |     On Branch: default                           |
            |                                                  |
            | YYYY-MM, Total Commits, Tested Commits, % Tested |
            | 1980-09, 1, 0, 0                                 |
            | 1980-10, 2, 1, 50                                |
            | 1980-11, 1, 1, 100                               |

   Scenario: It should handle months with no changes
        Given a repository with changesets
            | files                | date       |
            | codefile1            | 1980-9-02  |
            | codefile3, testfile2 | 1980-11-30 |

        When I run the metrics tool with arguments
            | type      | arguments  |
            | --byMonth |            |

        Then I should see the following output
            | output lines                                     |
            | Filtering by...                                  |
            |     On Branch: default                           |
            |                                                  |
            | YYYY-MM, Total Commits, Tested Commits, % Tested |
            | 1980-09, 1, 0, 0                                 |
            | 1980-11, 1, 1, 100                               |


