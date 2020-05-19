# mesa_gd
Generalized Darwinism package for the mesa ABM platform




## Installation

To install the dependencies use pip and the requirements.txt in this directory. e.g.

```
    $ pip install -r requirements.txt
```

## How to Run

To run the model interactively, run ``mesa runserver`` in this directory. e.g.

```
    $ mesa runserver
```

Then open your browser to [http://127.0.0.1:8521/](http://127.0.0.1:8521/) and press Reset, then Run.

## Files

* ``gd/agents.py``: Defines the Interactor, and Resource agent classes.
* ``gd/schedule.py``: This is exactly based on other schedule.py files like in sugarscape or wolfsheep models.
* ``gd/model.py``: Defines the GeneralizedDarwinism model itself
* ``gd/server.py``: Sets up the interactive visualization server
* ``run.py``: Launches a model visualization server.

## Further Reading

This model is based on the theoretical framework proposed by professors Geoffrey Hodgson and Thorbjorn Knudsen in
Darwin's Conjecture: The Search for General Principles of Social and Economic Evolution (2010)
