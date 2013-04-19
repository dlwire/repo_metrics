# -*- coding: utf-8 -*-
from lettuce import step, world
import os
from subprocess import check_output

@step(u'I run the metrics tool$')
def i_run_the_metrics_tool(step):
    world.output = check_output(['python', '../src/repo_metrics.py'], cwd=world.REPO_DIR).strip()

@step(u'I should see output indicating there is no repository')
def i_should_see_output_indicating_the_repository_is_empty(step):
    expected = 'There is no repository at %s' % os.getcwd() + '/repo'
    assert world.output == expected, 'Expected output: "%s"\nActual output: "%s"' % (expected, world.output)

@step(u'I should see output indicating the repository is empty')
def i_should_see_output_indicating_the_repository_is_empty(step):
    expected = 'The repository is empty'
    assert world.output == expected, 'Expected output: "%s"\nActual output: "%s"' % (expected, world.output)

@step(u'I should see output indicating the test commit percentage')
def i_should_see_output_indicating_the_test_commit_percentage_of_the_repository(step):
    expected = '%d percent of commits have tests' % 50
    assert world.output == expected, 'Expected output: "%s"\nActual output: "%s"' % (expected, world.output)

