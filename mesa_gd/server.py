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
InteractorChart_element = ChartModule([{"Label": "Frequency of Replicator", "Color": "#gg0000"}]) #{"Label": "Number of Hunters", "Color": "#AA0000"},

# "Variable": UserSettableParameter('checkbox', 'Caption', True),

model_params = { "width": UserSettableParameter('slider', 'Grid width', 50, 10, 100),
                 "height": UserSettableParameter('slider', 'Grid Height', 50, 10, 100),
                 "initial_population": UserSettableParameter('slider', 'Initial Interactors Population', 100, 10, 300)}

server = ModularServer(GD_Hunter, [canvas_element, InteractorChart_element],
                       "GD Hunter Model", model_params)
# server.launch()
