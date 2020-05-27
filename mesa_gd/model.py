'''
================================
Mesa_GD Model
================================
'''

from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from .gd_agents import Hunter, Turkey
from .schedule import RandomActivationByBreed
import logging

logging.basicConfig(filename="mesa_gd_hunter.log", level=logging.INFO)


#------------------------------------
# Replicator variations
#------------------------------------

def rv_moveany_directions(interactor):
    possible_directions = interactor.model.grid.get_neighborhood(
        interactor.pos,
        moore = False,
        include_center=False)
    logging.info("----------------------")
    logging.info("moveany")
    logging.info(possible_directions)
    logging.info("Last Pos:")
    logging.info(interactor.lastpos)
    logging.info("Pos:")
    logging.info(interactor.pos)
    new_position = interactor.random.choice(possible_directions)
    interactor.lastpos=interactor.pos # Updates last position visited as an information for the replicator
    logging.info("New Pos:")
    logging.info (new_position)
    interactor.model.grid.move_agent(interactor, new_position)

def rv_movefwd_directions(interactor):
    possible_directions = interactor.model.grid.get_neighborhood(
        interactor.pos, moore= False,
        include_center=False) # If moore is True allows movement in 8 directions, if it is False allows it only in 4 directions
    logging.info("----------------------")
    logging.info("movefwd")
    logging.info(possible_directions)
    logging.info("Last Pos:")
    logging.info(interactor.lastpos)
    logging.info("Pos:")
    logging.info(interactor.pos)
    if interactor.lastpos!=interactor.pos:
        possible_directions.remove(interactor.lastpos) # Excludes last position as a possible direction for the next move
    new_position = interactor.random.choice(possible_directions)
    interactor.lastpos=interactor.pos # Updates last position visited as an information for the replicator
    logging.info("New Pos:")
    logging.info (new_position)
    interactor.model.grid.move_agent(interactor, new_position)




#------------------------------------
# Metrics
#------------------------------------


def replicator_frequency (model):
    interactor_count=0
    replicator_count=0
    for i in model.schedule.agents:
        if type(i)== Hunter:
            interactor_count +=1
            if i.replicators[0]=="rv_movefwd_directions":
                replicator_count +=1
    if interactor_count==0:
        result=0
    else:
        result=replicator_count/interactor_count
    return result

#------------------------------------
# Models
#------------------------------------



class GD_Hunter(Model):

    def __init__(self, height, width, initial_population):

        # Height and Width of the environment grid
        self.height = height
        self.width = width
        self.initial_population = initial_population
        self.schedule = RandomActivationByBreed(self)
        self.grid = MultiGrid(self.height, self.width, torus=False)
        self.hunter_max_energy_consumption = 10

        # Create initial resource distribution in the environment
        # Create turkeys distribution
        for _, x, y in self.grid.coord_iter(): # For each cell, ignore its contents, gets position
            max_turkey = self.random.randrange(0,5) # Defines a maximum amount of turkey that each location will carry, before it is consumed
            turkey = Turkey((x, y), self, max_turkey) # Creates turkey groups with them maximum amount of turkeys defined for that location
            self.grid.place_agent(turkey, (x, y)) # Place the turkey
            self.schedule.add(turkey) # Add the turkeys to the schedule

        # Create interactor:
        for i in range(self.initial_population):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            hunter_energy = 10
            hunter_energy_consumption = 5
            replicators_list = ['rv_moveany_directions', 'rv_movefwd_directions']
            replicators=[]
            replicators.append (self.random.choice(replicators_list)) # Instruction to the researcher: List here the replicator variations as function names
            age = self.random.randint (0, 45) # Creates an initial population with an age distribution
            replicators_dictionary = {
                  "rv_moveany_directions": rv_moveany_directions,
                  "rv_movefwd_directions": rv_movefwd_directions
                }
            hunter = Hunter((x,y), self, hunter_energy, hunter_energy_consumption, age, replicators, replicators_dictionary) # Create the hunters self, pos, model, hunter_energy, hunter_energy_consumption, age
            self.grid.place_agent(hunter, (x, y)) # Place the hunters
            self.schedule.add(hunter) # Add the hunter to the schedule

        self.running = True
        self.datacollector = DataCollector({"Number of Hunters": lambda m: m.schedule.get_breed_count(Hunter), "Frequency of Replicator": replicator_frequency})
        self.datacollector.collect(self)

    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)

    def run_model(self, step_count=50):
        for i in range(step_count):
            self.step()
