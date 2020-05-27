import sys, logging
from .mesa_gd_agents import Interactor, Resource





#------------------------------------
# Interactors
#------------------------------------


class Hunter(Interactor):
    def __init__(self, pos, model, hunter_energy, hunter_energy_consumption, age, replicators, replicators_dictionary):
        super().__init__(pos, model, replicators, replicators_dictionary)
        self.replicators=replicators
        self.replicators_dictionary=replicators_dictionary
        self.lastpos=pos
        self.hunter_energy=hunter_energy
        self.hunter_energy_consumption=hunter_energy_consumption
        self.age = age

    def absorb_energy(self):
        resource_patch = self.access_resources(self.pos) # Access resources in the location
        resource_energy_value = {'Turkey' : 3} # Defines the energy value of each unit for each type of resource
        for resource in resource_patch:
            resource_energy = resource.amount * resource_energy_value [resource.__class__.__name__]

            logging.info("Resource Energy")
            logging.info(resource_energy)
            logging.info("Resource Energy Consumption")
            logging.info(self.hunter_energy_consumption)
            #if resource.amount != 0:
            self.hunter_energy = self.hunter_energy - self.hunter_energy_consumption + resource_energy
            resource.amount = 0 # Consume all resources in that location


    def step(self): #defines what happens in each new period in the life of the hunter

        logging.info("------------------")
        logging.info("Hunter")
        logging.info(self.unique_id)
        logging.info("Pos:")
        logging.info(self.pos)

        self.energize() # The hunter energizes its replicator, which in his case is its prey searching habit

        logging.info("Hunter Energy")
        logging.info(self.hunter_energy)

        self.absorb_energy() # The hunter absorbs energy from the resources in its sector of  the environment
        logging.info("Hunter Energy")
        logging.info(self.hunter_energy)

        logging.info("Hunter Age")
        logging.info(self.age)

        if self.age == 180: # Checks if the hunter is at the age of expiration
            self.expire()
            logging.info("Hunter Expired")
        else:

            # If the hunter starves than he expires
            if self.hunter_energy <= 0:
                self.expire()
                logging.info("Hunter Expired")

            else:
                if self.hunter_energy >60:
                    self.hunter_energy=60
                    logging.info("Hunter Energy Capped")

                if self.age == 60 or self.age==80: # Checks if the hunter is in reproduction age
                    hunter_energy = 10
                    hunter_energy_consumption = 4
                    replicators = self.replicators # Copy the replicators in the interactor triggering
                    age = 0
                    hunter = Hunter(self.pos, self.model, hunter_energy, hunter_energy_consumption, age, self.replicators, self.replicators_dictionary)
                    self.replicate(hunter)
                    logging.info("Hunter Replicated")

                # Hunter ages one step
                self.age += 1



#------------------------------------
# Resources
#------------------------------------


class Turkey(Resource):

    def __init__(self, pos, model, max_resource):
        super().__init__(pos, model, max_resource)
        self.amount = max_resource
        self.max_resource=max_resource

    def renew(self):
        self.amount = self.max_resource

    def step(self):
        if self.amount == 0: #If resource is equal to zero then there is a probability that it will be renewed
            if self.random.randint(0,4) == 1: # There is 1 chance in 5 that the location is replenished with the maximum amount of turkeys
                self.renew()
