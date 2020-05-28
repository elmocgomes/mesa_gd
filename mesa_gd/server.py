from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter

from .gd_agents import Hunter, Turkey
from .model import GD_Hunter

color_dic = {10:"#808080",
             9: "#8c8c8c",
             8: "#999999",
             7: "#a6a6a6",
             6: "#b3b3b3",
             5: "#bfbfbf",
             4: "#cccccc",
             3: "#d9d9d9",
             2: "#e6e6e6",
             1: "#f2f2f2"}


def Interactor_portrayal(agent):
    if agent is None:
        return

    portrayal = {}

    if type(agent) is Hunter:
        portrayal["Shape"] = "mesa_gd/images/interactor.png"
        portrayal["scale"] = 0.9
        portrayal["Layer"] = 1

    elif type(agent) is Turkey:
        if agent.amount != 0:
            portrayal["Color"] = color_dic[agent.amount]
        else:
            portrayal["Color"] = "#ffffff"
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["Layer"] = 0
        portrayal["w"] = 1
        portrayal["h"] = 1

    return portrayal

canvas_element = CanvasGrid(Interactor_portrayal, 50, 50, 500, 500)
FrequencyChart_element = ChartModule([{"Label": "Frequency of Replicator", "Color": "Black"}])
InteractorChart_element = ChartModule([{"Label": "Population", "Color": "Gray"}])

# "Variable": UserSettableParameter('checkbox', 'Caption', True),

model_params = { "hunter_energy_consumption": UserSettableParameter('slider', 'Hunter Energy Consumption', 4, 1, 10),
                 "hunter_energy": UserSettableParameter('slider', 'Initial Hunter Energy', 10, 1, 20),
                 "initial_population": UserSettableParameter('slider', 'Initial Interactors Population', 100, 10, 300)}

server = ModularServer(GD_Hunter, [canvas_element, FrequencyChart_element, InteractorChart_element],
                       "GD Hunter Model", model_params)

server.port = int(os.environ.get("PORT", 5000))
server.launch()
