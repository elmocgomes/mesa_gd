import math
import sys, logging
from mesa import Agent



class Interactor(Agent):
    def __init__(self, pos, model, replicators, replicators_dictionary):
        super().__init__(pos, model) #inherit the agent class
        self.pos = pos # stores the location of the interactor in the environment
        self.replicators = replicators # list of replicators carried by the interactor
        self.replicators_dictionary = replicators_dictionary

    def access_resources(self, pos):
        # Interact with the environment and access the resources in the location(pos)
        this_location = self.model.grid.get_cell_list_contents([pos]) #Get all entities/agents in that location
        local_resources = []
        for agent in this_location:
            for base in agent.__class__.__bases__:
                if base.__name__ == 'Resource' : # looks for resources in the present location
                    local_resources.append(agent)
        return local_resources #returns the resource

    def energize(self):
        for key in self.replicators:
            selected_replicator= self.replicators_dictionary[key]
            selected_replicator(self)
            logging.info(selected_replicator)

    def replicate(self, interactor_agent):
        # Triggers the replication of the replicators into a new interactor
        self.model.grid.place_agent(interactor_agent, self.pos)
        self.model.schedule.add(interactor_agent)


    def expire(self):
        # Expires the interactor, removing it from the environment and from the schedule
        logging.info("self.pos")
        self.model.grid._remove_agent(self.pos, self)
        self.model.schedule.remove(self)



class Resource(Agent):
    # Class that defines the resources, or better said the source of resources
    def __init__(self, pos, model, max_resource):
        super().__init__(pos, model)
        self.amount = max_resource
        self.max_resource = max_resource
