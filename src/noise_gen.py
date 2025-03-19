import random
import noise
from numpy.typing import NDArray
import numpy as np
from helper_functions import normalize_image_array



class PerlinNoiseGenerator:
    """
    A class to generate perlin noise array.

    Attributes:
    ----------
        scale (float) Defaults: 0.5:
            Scale factor for the Perlin noise. Larger values 'zoom in', smaller values 'zoom out'
        octaves (int) Defaults: 4:
            Number of noise layers combined to create final noise
        persistence (float) Defaults: 0.5:
            Controls how much each layer contributes to the final image. When 0.5 - amplitude of noise
            is halved in each successive layer -> Each new layer contributes less than those before
        lacunarity (float) Defaults: 2.0:
            Controls how the size of the blobs changes with each layer. The higher the lacunarity, the more the blob
            size decreases with each new layer.
        seed (int) Defaults: randint(0, 10000):
            Seed for reproducibility

    Methods:
    --------
        generate_perlin_noise():
                Generates a random perlin noise 2D ,normalized between 0 and 1, array
    """

    def __init__(self, scale: float = 0.5,
                 octaves: int = 8,
                persistence: float = 0.5,
                 lacunarity: float = 2.0,
                 seed: int | None = None):
        if scale <= 0:
            raise ValueError("Scale must be positive")
        self._scale = scale
        self._octaves = octaves
        self._persistence = persistence
        self._lacunarity = lacunarity
        if seed:
            self._seed = seed
        else:
            self._seed = random.randint(0, 10000)

    def generate_perlin_noise(self, shape: (int, int)) -> NDArray:
        """
        Generates perlin noise to 2D array
        Args:
            shape (int, int): 2D array to apply perlin noise to
        Returns:
            perlin_array (NDArray): 2D array with perlin noise applied, normalized between [0,1]
        """
        # Noise array is being generated with transposed
        # shape so we have to swap coordinates here
        x_idx = np.linspace(0, 1, shape[1])
        y_idx = np.linspace(0, 1, shape[0])
        world_x, world_y = np.meshgrid(x_idx, y_idx)
        random.seed(self._seed)
        # Since seed is not implemented in perlin noise
        # Generating random offsets for x, y coordinates
        x_offset = random.uniform(0, 1000)
        y_offset = random.uniform(0, 1000)
        noise_array = np.vectorize(noise.pnoise2)(world_x / self._scale + x_offset,
                                                  world_y / self._scale + y_offset,
                                                  octaves=self._octaves,
                                                  persistence=self._persistence,
                                                  lacunarity=self._lacunarity,
                                                  )

        return normalize_image_array(noise_array)

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, new_scale):
        self._scale = new_scale

    @property
    def octaves(self):
        return self._octaves

    @octaves.setter
    def octaves(self, new_octaves):
        self._octaves = new_octaves

    @property
    def persistence(self):
        return self._persistence

    @persistence.setter
    def persistence(self, new_persistence):
        self._persistence = new_persistence

    @property
    def lacunarity(self):
        return self._lacunarity

    @lacunarity.setter
    def lacunarity(self, new_lacunarity):
        self._lacunarity = new_lacunarity

    @property
    def seed(self):
        return self._seed

    @seed.setter
    def seed(self, new_seed):
        self._seed = new_seed
