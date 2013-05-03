Feature: The test metrics should be available for a specific user
    In order to see test recent testing efforts
    As a developer
    I want to see the percentage of my pushes containing tests

    Scenario: It should be able to handle no changesets for the user
        Given a repository with changesets
            | files    | user         |
            | codefile | Another User |

        When I run the metrics tool with arguments
            | type    | arguments |
            | --users | A User    |

        Then I should see the following output
            | output lines                                 |
            | There are no changesets meeting the criteria |

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
            | output lines                     |
            | 50 percent of commits have tests |

