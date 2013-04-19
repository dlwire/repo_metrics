from lettuce import *
import os
from shutil import rmtree
from sys import path

@before.each_scenario
def setup(scenario):
    path.append(os.getcwd() + '../src')
    world.REPO_DIR = 'repo'
    os.mkdir(world.REPO_DIR)
   
@after.each_scenario
def teardown(scenario):
    rmtree(world.REPO_DIR)
