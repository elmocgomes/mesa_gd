import math
from mesa import Agent



class Interactor(Agent):
    def __init__(self, pos, model, replicators):
        super().__init__(pos, model) #inherit the agent class
        self.pos = pos # stores the location of the interactor in the environment
        self.replicators = replicators # list of replicators carried by the interactor


    def access_resources(self, pos):
        # Interact with the environment and access the resources in the location(pos)
        this_location = self.model.grid.get_cell_list_contents([pos]) #Get all entities/agents in that location
        for agent in this_location:
            if type(agent) is Resource: # looks for resources in the present location
                return agent #returns the resource

    def energize(self, replicators, replicators_list):
        for key in replicators:
            getattr(sys.modules[__name__], fieldname)()


    def replicate(self, interactor_agent):
        # Triggers the replication of the replicators into a new interactor
        self.model.grid.place_agent(interactor_agent, self.pos)
        self.model.schedule.add(interactor_agent)


    def expire(self):
        # Expires the interactor, removing it from the environment and from the schedule
        self.model.grid._remove_agent(self.pos, self)
        self.model.schedule.remove(self)



class Resource(Agent):
    # Class that defines the resources, or better said the source of resources
    def __init__(self, pos, model, max_resource):
        super().__init__(pos, model)
        self.amount = max_resource
        self.max_resource = max_resource
