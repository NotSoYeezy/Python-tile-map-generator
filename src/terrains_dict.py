from typing import Dict, Tuple, List, Union
from custom_exceptions.exceptions import WrongArrayShape, NotEnoughData
import json
import os


class TerrainDict:
    """
    A class to represent a terrain map

    Attributes:
    ----------
        terrains: dict, defaults to None
            Dictionary describing the terrain map, must consist of key - terrain name,
            list of 2 elements - 3 element color array and int - terrain threshold value
        json_path: str, defaults to None
            String representing the path to the json file with terrain config. It will be used
            to save the current config and load it.

    Methods:
    -------
        _set_up_default_terrains():
            Sets default, hardcoded terrain.
        _load_terrains_from_json():
            Loads terrain map from json config file, uses json_path.
        write_terrains_to_json():
            Writes current terrain map to json config file - uses json_path.
        _validate_terrains()::
            Checks if terrain dictionary is in a correct format.
    """
    def __init__(self,
                 terrains: Dict[str, List[Union[Tuple[float, float, float], float]]] | None = None,
                 json_path: str = None, ):
        self._terrains = terrains
        if json_path:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            self._json_path = os.path.join(base_dir, json_path)
            self._load_terrains_from_json()
        if self._terrains is None and json_path is None:
            self._set_up_default_terrains()
        self._validate_terrains()
        # Sorting terrain based on threshold value
        self._terrains = dict(sorted(self._terrains.items(), key=lambda item: item[1][1]))

    @property
    def terrains(self) -> Dict[str, List[Union[Tuple[float, float, float], float]]]:
        return self._terrains

    @terrains.setter
    def terrains(self, new_terrains: Dict[str, List[Union[Tuple[float, float, float], float]]]):
        self._terrains = new_terrains

    def _set_up_default_terrains(self):
        """
        Method responsible for setting up the default terrains.
        """
        self._terrains = {
            "water": [(31, 69, 252), 0.46],
            "shallow_water": [(133, 216, 229), 0.53],
            "sand": [(242, 232, 211), 0.59],
            "land": [(34, 139, 34), 0.73],
            "dark_forest": [(6, 64, 43), 0.89],
            "mountains": [(255, 255, 255), 0.92],
            "higher_mountains": [(123, 123, 123), 0.94]
        }

    def _load_terrains_from_json(self):
        """
        Method responsible for loading terrains_dict from json
        """
        with open(self._json_path, 'r') as f:
            self._terrains = json.load(f)

    def write_terrains_to_json(self, write_json_path: str = None):
        """
        Method responsible for writing terrains_dict to json
        """
        base_dir = os.path.dirname(os.path.abspath(__file__))
        write_json_path = os.path.join(base_dir, write_json_path)
        with open(write_json_path, "w") as f:
            json.dump(self._terrains, f, indent=2)

    def _validate_terrains(self):
        """
         Method responsible for validating terrains dictionary.
         It checks if all threshold values are unique -> This indicates that
         there must be a maximum value, which then will be considered as the highest terrain.
         It also checks if shapes of colors arrays are correct.
        """
        threshold_values = []
        correct_array_size = 3
        try:
            for colors_array, threshold_value in self._terrains.values():
                threshold_values.append(threshold_value)
                if len(colors_array) != correct_array_size:
                    raise WrongArrayShape(f"Colors array should be of size: {correct_array_size}")
        except ValueError:
            raise NotEnoughData("Every terrain should have colors array and threshold value")
        if len(list(set(threshold_values))) != len(self._terrains):
            raise ValueError("Every threshold value must be unique!")
