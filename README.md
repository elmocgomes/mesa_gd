# mesa_gd

Agent-Based Modelling package for Generalized Darwinism Models based on MESA

## Installation

To install the package, use pip install and reference to the Github repository

```
    $ pip install https://github.com/elmocgomes/mesa_gd
```

## How to Run

To run the model interactively, run ``mesa runserver`` in this directory. e.g.

```
    $ mesa runserver
```

Then open your browser to [http://127.0.0.1:8521/](http://127.0.0.1:8521/) and press Reset, then Run.

## Files

* ``run.py``: Launches a model visualization server.

The below files are not expected to be changed by the user
* ``mesa_gd/mesa_gd_agents.py``: Defines the Interactor, and Resource agent classes.
* ``mesa_gd/agents.py``: Defines the Interactor, and Resource agent classes.
* ``mesa_gd/schedule.py``: This is exactly based on other schedule.py using mesa, and coordinates the simulation steps.

The below files need to be customized for the specific model. Currently they have the Turkey Hunter model as an example
* ``mesa_gd/model.py``: Defines the GeneralizedDarwinism model itself
* ``mesa_gd/gd_agents.py``: Defines specific interactors and resources studied in the model and uses the mesa_gd_agents classes as a base.
* ``mesa_gd/server.py``: Sets up the interactive visualization server


## Further Reading
Please refer to the full documentation at http://mesa_gd.reathedocs.io
This model is based on the theoretical framework proposed by professors Geoffrey Hodgson and Thorbjorn Knudsen in
the book "Darwin's Conjecture: The Search for General Principles of Social and Economic Evolution (2010)"
