# Work in progress :) 


# Structure

- conversation.py: Includes simple classes for messages and dialogs

- agents.py: Includes AbstractAgent that defines interface for an agent

- tests.py: Includes two abstract classes for two different types of tests
    - AbstractTestCase: A test that is set up in a specific way with a specific evaluation
    - AsbtractDialogTest: Tests that can run on any dialog

- worlds.py: Include TestWorld that is set up to keep track of agents, dialogs and tests


# TODO: 
- Some tests will use transformer models. Needs to figure out some way of sharing same model between different test objects. Maybe this can be done with some class ModelXTestCase?
- Structure files into subdirectories