import pytest
from unittest.mock import MagicMock
from PIL import Image

from src.custom_exceptions.exceptions import WrongArrayShape
from src.map_gen import MapGenerator
from src.noise_gen import PerlinNoiseGenerator
from src.terrains_dict import TerrainDict
import numpy as np


@pytest.fixture
def sample_terrains():
    """Sample terrain dictionary for testing."""
    terrains = {
        "water": [(0, 0, 255), 0.3],  # blue
        "sand": [(194, 178, 128), 0.5],  # light brown
        "grass": [(0, 255, 0), 0.8],  # green
        "mountain": [(139, 128, 128), 1.0],  # grey
    }
    return TerrainDict(terrains)


@pytest.fixture
def sample_shape():
    """Sample shape for the map."""
    return 100, 100


@pytest.fixture
def perlin_noise_generator():
    """Mock PerlinNoiseGenerator."""
    noise_generator = MagicMock(spec=PerlinNoiseGenerator)
    noise_generator.generate_perlin_noise.return_value = np.random.random((100, 100))
    return noise_generator


@pytest.fixture
def map_generator(sample_shape, sample_terrains):
    """Map generator instance for testing."""
    return MapGenerator(shape=sample_shape, terrains=sample_terrains)


def test_init_valid_map_generator(sample_shape, sample_terrains):
    """Test successful initialization of MapGenerator."""
    generator = MapGenerator(shape=sample_shape, terrains=sample_terrains)
    assert generator.shape == sample_shape
    assert generator.terrains == sample_terrains.terrains


def test_init_invalid_map_generator(sample_terrains):
    """Test initializing MapGenerator with invalid shape."""
    with pytest.raises(Exception):
        MapGenerator(shape=(0, 100), terrains=sample_terrains)

    with pytest.raises(Exception):
        MapGenerator(shape=(-5, 50), terrains=sample_terrains)


def test_generate_map(map_generator, perlin_noise_generator):
    """Test generating a map without errors."""
    # Mocking save_path and generate_image
    save_path = None
    generated_image = map_generator.generate(
        noise_generator=perlin_noise_generator, save_path=save_path
    )
    assert isinstance(generated_image, Image.Image)


def test_apply_terrain(map_generator):
    """Test that terrain application correctly applies colors."""
    # Use an array matching the shape of the map generator
    sample_array = np.random.random(map_generator.shape)

    colored_array = map_generator._apply_terrain(sample_array)

    # Check the correctness of the returned array
    assert colored_array.shape == (*map_generator.shape, 3)
    assert all(
        tuple(value) in [(0, 0, 255), (194, 178, 128), (0, 255, 0), (139, 128, 128)]
        for value in colored_array.reshape(-1, 3)
    )


def test_update_map_generator_terrains(map_generator, sample_terrains):
    """Test updating terrains for MapGenerator."""
    new_terrains = {
        "water": [(0, 0, 155), 0.2],  # Different blue
        "forest": [(34, 139, 34), 0.6],  # Dark green
        "rock": [(128, 128, 128), 1.0],  # Grey
    }
    new_terrains_dict = TerrainDict(new_terrains)
    map_generator.terrains = new_terrains_dict

    assert map_generator.terrains == new_terrains_dict.terrains
    assert map_generator._terrains_dict == new_terrains_dict
    assert map_generator._terrains == new_terrains_dict.terrains


def test_shape_setter(map_generator):
    """Test setting a new shape for the map generator."""
    new_shape = (200, 200)
    map_generator.shape = new_shape
    assert map_generator.shape == new_shape
