Feature: The test metrics should be available for a specific user

    Scenario: It should be able to handle no changesets for the user
        Given a repository with changesets
            | files    | user         |
            | codefile | Another User |

        When I run the metrics tool with arguments
            | type    | arguments |
            | --users | A User    |

        Then I should see the following output
            | output lines           |
            | Filtering by...        |
            |     Users: A User      |
            |     On Branch: default |
            |                        |
            | Total Commits: 0       |

    Scenario: It should report the metrics for the user in question
        Given a repository with changesets
            | files     | user         |
            | codefile1 | A User       |
            | testfile1 | A User       |
            | codefile2 | Another User |

        When I run the metrics tool with arguments
            | type    | arguments |
            | --users | A User    |

        Then I should see the following output
            | output lines                   |
            | Filtering by...                |
            |     Users: A User              |
            |     On Branch: default         |
            |                                |
            | Total Commits: 2               |
            | Tested Commits: 1 - 50 percent |

