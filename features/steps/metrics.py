# -*- coding: utf-8 -*-
from lettuce import step, world
import os
from subprocess import check_output

@step(u'I run the metrics tool$')
def i_run_the_metrics_tool(step):
    world.output = check_output(['python', '../src/run_metrics.py'], cwd=world.REPO_DIR).strip()

@step(u'I run the metrics tool with arguments$')
def i_run_the_metrics_tool_with_arguments(step):
    command = ['python', '../src/run_metrics.py']
    for arg_dict in step.hashes:
        command += [arg_dict['type']] 
        command += [arg.strip() for arg in arg_dict['arguments'].split(',')]

    world.output = check_output(command, cwd=world.REPO_DIR).strip()

@step(u'I should see output indicating there is no repository')
def i_should_see_output_indicating_the_repository_is_empty(step):
    expected = 'There is no repository at %s' % os.getcwd() + '/repo'
    assert world.output == expected, 'Expected output: "%s"\nActual output: "%s"' % (expected, world.output)

@step(u'I should see the following output')
def i_should_see_the_following_output(step):
    actuals = world.output.split('\n')
    for i, line in enumerate(step.hashes):
        expected = line['output lines'].strip()
        actual = actuals[i].strip()
        
        assert actual == expected, 'Line %d:\n    Expected output: "%s"\n    Actual output: "%s"' % (i, expected, actual)
