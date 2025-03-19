from noise_gen import PerlinNoiseGenerator
from numpy.typing import NDArray
import numpy as np
from PIL import Image
from typing import Tuple
from terrains_dict import TerrainDict
from helper_functions import (generate_image)
from custom_exceptions.exceptions import WrongArrayShape



class MapGenerator:
    """
    A class to generate a tile map using perlin noise

    Attributes:
    -----------
        shape: (int, int)
            Shape of the generated map
        terrains: TerrainDict
            Instance of TerrainDict object.

    Methods:
    --------
        generate():
            Generates a tile map of self.size and with self.terrain parameters using perlin noise
        _apply_terrain():
            Applies colors to numpy perlin noise array based on self.terrain parameters
    """

    def __init__(self, shape: Tuple[int, int],
                 terrains: TerrainDict):
        self._terrains_dict = terrains
        self._terrains = terrains.terrains
        x, y = shape
        if x <= 0 or y <= 0:
            raise WrongArrayShape("Map Shape dimensions should be > 0")
        self._shape = (int(x), int(y))

    @property
    def shape(self):
        return self._shape

    @property
    def terrains(self):
        return self._terrains

    @shape.setter
    def shape(self, new_shape: Tuple[int, int, int]):
        self._shape = new_shape

    @terrains.setter
    def terrains(self, new_terrains_dict: TerrainDict):
        self._terrains_dict = new_terrains_dict
        self._terrains = new_terrains_dict.terrains

    def generate(self, noise_generator: PerlinNoiseGenerator, save_path: str = None) -> Image.Image:
        """
        Generate tile map of self.size using PerlinNoiseGenerator

        Args:
            noise_generator (PerlinNoiseGenerator): PerlinNoiseGenerator instance
            save_path (str): String where map image should be saved, if None, map won't be saved

        Returns:
            map_image (NDArray): Tile map image
        """
        noise_array = noise_generator.generate_perlin_noise(self._shape)
        noise_array_terrain_applied = self._apply_terrain(noise_array)
        map_image = generate_image(noise_array_terrain_applied, save_path)
        return map_image

    def _apply_terrain(self, array: NDArray) -> NDArray:
        """
        Apply terrain color map to the numpy array, based on threshold and colors from self.terrains.
        This function treats perlin noise array like 'heightmap', so for example:
            When specific value in given array is 0.3, threshold for water is 0.5 and color for water is
             (176, 224, 230) -> blue, this function will apply that color on before created 3D matrix
             at the corresponding index. It returns 3 dimensional array since we are creating an rgb image.

        Args:
            array (NDArray): Array with perlin noise applied

        Returns:
            array (NDArray): Array of shape (self.shape, 3).
        """
        highest_terrain = next(reversed(self._terrains.items()))
        x_size, y_size = self.shape
        terrain_matrix = np.zeros((x_size, y_size, 3), dtype=np.uint8)
        array_copy = array.copy()
        thresholds = np.array([value[1] for value in self._terrains.values()])
        colors = np.array([value[0] for value in self._terrains.values()])
        # Applying colors for all terrains, except the highest one
        for i in range(len(thresholds)):
            mask = array_copy < thresholds[i]
            terrain_matrix[mask] = colors[i]
            array_copy[mask] = np.inf

        # Applying color of the highest terrain
        replacement_values = np.array((highest_terrain[1][0]))
        zero_mask = np.all(terrain_matrix == 0, axis=-1)
        terrain_matrix[zero_mask] = replacement_values

        return terrain_matrix
