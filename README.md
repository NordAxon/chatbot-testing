# Work in progress :) 


# How it works:
- dialogs are created in the testcases
- dialogs are passed around to dialogtests that add metrics to the dialog.metrics attribute


# Howto
TODO: Write instructions

## Implement your own TestCase


## Implement your own DialogTest


## Implement your own Agent


# Structure

- conversation.py: Includes simple classes for messages and dialogs

- agents.py: Includes AbstractAgent that defines interface for an agent

- tests.py: Includes two abstract classes for two different types of tests
    - AbstractTestCase: A test that is set up in a specific way with a specific evaluation
    - AsbtractDialogTest: Tests that can run on any dialog

- worlds.py: Include AbstractTestWorld that is set up to keep track of agents, dialogs and tests

# Structure
agents
tests
worlds


# Interfaces:

## Agents


## Tests

There are two types of test:
1. TestCase
2. DialogTest

A TestCase is a specific test where the dialog is somehow modified, or steered

### TestCases


### DialogTest


# TODO: 
- Some tests will use transformer models. Needs to figure out some way of sharing same model between different test objects. Maybe this can be done with some class ModelXTestCase?
- Structure files into subdirectories