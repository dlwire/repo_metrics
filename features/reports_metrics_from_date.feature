Feature: The test metrics should be available since a starting date

    Scenario: It should be able to handle no changesets since the date
        Given a repository with changesets
            | files              | date       |
            | codefile, testfile | 1980-10-02 |

        When I run the metrics tool with arguments
            | type        | arguments  |
            | --afterDate | 1980-10-02 |

        Then I should see the following output
            | output lines                                 |
            | Filtering by...                              |
            |     After Date: 1980-10-02                   |
            |                                              |
            | There are no changesets meeting the criteria |

    Scenario: It should report the metrics since the start date
        Given a repository with changesets
            | files                | date       |
            | codefile1, testfile1 | 1980-10-02 |
            | testfile2            | 1980-10-03 |
            | codefile2            | 1980-10-03 |

        When I run the metrics tool with arguments
            | type        | arguments  |
            | --afterDate | 1980-10-02 |

        Then I should see the following output
            | output lines                   |
            | Filtering by...                |
            |     After Date: 1980-10-02     |
            |                                |
            | Total Commits: 2               |
            | Tested Commits: 1 - 50 percent |
