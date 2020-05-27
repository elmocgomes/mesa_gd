# Generalized Darwinism Economic Behaviour model

## Summary

This model is based on the Generalized Darwininsm Framework proposed by Geoffrey Hodgson and Thorbjorn Knudsen in the book "Darwin's Conjectures" (2010)

The model consist of communities of entities and resources(energy and material) in a given environment, living under the following rules:

- Entities need resources to continue alive, and spend resources in order to obtain resources. Without resources they degrade until they die. As entities interact with the environment, they are interactors.
- Resources are locally and immediately scarce, being only available for a certain time, in a certain place and in a certain quantity. Therefore, on individual perspective, the probability of resource availability is always less than one.
- Some adaptive solutions to local and immediate scarcity problem are retained through time and can be passed to others. Those solutions are stored in replicators. Replicators are material structures that retain information of adaptive solutions that is used by the interactors.
- An explanation of the evolution of such system must involve: variation, inheritance and selection.








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
