Interactors
========================
According to GH&TK(2010), an interactor is the general form of entity that directly interacts with the environment as a cohesive whole,
to be found in complex population systems in nature and human society.


In the platform, the interactor is built upon the Class Interactor, which has the following attributes(variables):

* replicators: a list of replicators hosted in the interactor instance.
* replicators_dictionary: a dictionary that relates the name of the replicator and the function that contains it as a procedure or disposition.
* pos: the location where the interactor is in the grid(environment)

And it has the following methods(functions of the class):

* access_resources(pos): access the resources in a sector or location of the environment, indicated by pos.
* energize(): energizes all replicators hosted by the interactor instance. This method calls the function found in the replicators_dictionary related to each replicator in the replicators list.
* replicate(interactor_agent): replicates all of the replicators and other desired characteristics of the interactor into a new interactor.
* expire(): trigger the expiration (death or termination) of the interactor instance.

The type of interactor used in the model can have its own attributes and methods in addition to the ones from the Interactor class.
For example, in the Hunter model, the Hunter is an interactor which also has methods to track its energy variances, age, last pos, etc.
Here is the beggining of its code:

.. code-block:: python

    class Hunter(Interactor):
        def __init__(self, pos, model, hunter_energy, hunter_energy_consumption, age, replicators, replicators_dictionary):
            super().__init__(pos, model, replicators, replicators_dictionary)
            self.replicators=replicators
            self.replicators_dictionary=replicators_dictionary
            self.lastpos=pos
            self.hunter_energy=hunter_energy
            self.hunter_energy_consumption=hunter_energy_consumption
            self.age = age
