Feature: The test metrics should be available for multiple users

    Scenario: It should be able to handle no changesets for any users
        Given a repository with changesets
            | files    | user         |
            | codefile | Another User |

        When I run the metrics tool with arguments
            | type    | arguments      |
            | --users | A User, B User |
            
        Then I should see the following output
            | output lines                                 |
            | There are no changesets meeting the criteria |

    Scenario: It should report the metrics for the users in question
        Given a repository with changesets
            | files     | user         |
            | codefile  | Another User |
            | testfile  | A User       |
            | codefile2 | B User       |

        When I run the metrics tool with arguments
            | type    | arguments      |
            | --users | A User, B User |

        Then I should see the following output
            | output lines                     |
            | 50 percent of commits have tests |
