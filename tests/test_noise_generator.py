import pytest
import numpy as np
from src.noise_gen import PerlinNoiseGenerator


def test_default_initialization():
    """Test the default initialization of PerlinNoiseGenerator."""
    generator = PerlinNoiseGenerator()
    assert generator.scale == 0.5
    assert generator.octaves == 8
    assert generator.persistence == 0.5
    assert generator.lacunarity == 2.0
    assert isinstance(generator.seed, int)


def test_custom_initialization():
    """Test the initialization with custom parameters."""
    generator = PerlinNoiseGenerator(scale=1.0, octaves=6, persistence=0.8, lacunarity=3.0, seed=42)
    assert generator.scale == 1.0
    assert generator.octaves == 6
    assert generator.persistence == 0.8
    assert generator.lacunarity == 3.0
    assert generator.seed == 42


def test_negative_scale_initialization():
    """Test that a ValueError is raised for negative scale."""
    with pytest.raises(ValueError, match="Scale must be positive"):
        PerlinNoiseGenerator(scale=-1.0)


def test_generate_perlin_noise_shape():
    """Test that the generated noise has the expected shape."""
    generator = PerlinNoiseGenerator(seed=42)
    shape = (100, 200)
    noise_array = generator.generate_perlin_noise(shape)
    assert noise_array.shape == shape


def test_generate_perlin_noise_normalized():
    """Test that the generated noise is normalized between 0 and 1."""
    generator = PerlinNoiseGenerator(seed=42)
    shape = (50, 50)
    noise_array = generator.generate_perlin_noise(shape)
    assert noise_array.min() >= 0.0
    assert noise_array.max() <= 1.0


def test_setters():
    """Test the setter methods for all attributes."""
    generator = PerlinNoiseGenerator()

    generator.scale = 1.2
    assert generator.scale == 1.2

    generator.octaves = 6
    assert generator.octaves == 6

    generator.persistence = 0.6
    assert generator.persistence == 0.6

    generator.lacunarity = 3.5
    assert generator.lacunarity == 3.5

    generator.seed = 1234
    assert generator.seed == 1234


def test_consistent_seed():
    """Test that the same seed generates the same noise."""
    generator1 = PerlinNoiseGenerator(seed=42)
    generator2 = PerlinNoiseGenerator(seed=42)

    shape = (30, 30)
    noise_array1 = generator1.generate_perlin_noise(shape)
    noise_array2 = generator2.generate_perlin_noise(shape)

    assert np.array_equal(noise_array1, noise_array2)


def test_different_seed():
    """Test that different seeds generate different noise arrays."""
    generator1 = PerlinNoiseGenerator(seed=1)
    generator2 = PerlinNoiseGenerator(seed=2)

    shape = (30, 30)
    noise_array1 = generator1.generate_perlin_noise(shape)
    noise_array2 = generator2.generate_perlin_noise(shape)

    assert not np.array_equal(noise_array1, noise_array2)
