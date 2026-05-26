"""
ScienceLabX: Ecosystem for Data People
Autor: Emmanuel Ascendra
Versión: 0.0.1
"""

__version__ = "0.0.1"
__author__ = ["Emmanuel Ascendra", "Dawin Jimenez", "Sebastian Garcia", "Isabel Paez", "Denzel Whashigton"]

# Importar las clases principales
from .datom_main import DAtom
from .data import Data
from .datasets import load_dataset
# from .analysis import *
# from .simulate import *
# from .model import *
# from .plots import *
# from .report import *
# from .utils import *
# from .app import *
# Definir qué se expone cuando se hace: from datom import *
__all__ = [
    "DAtom",
    "Data",
    "load_dataset"
]

def welcome():
    """Muestra información sobre la librería"""
    print(f"DAtom v{__version__}")
    print(f"Librería para Data People")
    print(f"Autores: \n  - {__author__[0]} \n  - {__author__[1]}")
    print(f"\nModulos disponibles:")
    print("  - Data: Carga y manipulación de datos")
    print("  - Analysis: Análisis estadístico")
    print("  - Datasets: Carga de Datasets")
    print("  - Simulate: Simulación de datos")
    print("  - Model: Modelos estadísticos")
    print("  - Plots: Gráficos estadísticos")
    print("  - Report: Generación de reportes")
    print("  - App: Aplicacion web")
    print(f"\nPara más información: help(datom)")