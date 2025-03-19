import pytest
import numpy as np
from PIL import Image
from src.helper_functions import normalize_image_array, generate_image
import os


def test_normalize_image_array():
    # Test 1: Simple 2D numpy array
    array = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
    normalized = normalize_image_array(array)
    expected = (array - 1) / (6 - 1)
    assert np.allclose(normalized, expected), "Normalization failed for 2D numpy array"

    # Test 2: Check with a single value array
    single_value_array = np.array([[3]])
    normalized = normalize_image_array(single_value_array)
    assert np.allclose(normalized, 0), "Normalization failed for single-value array"

    # Test 3: Check negative values
    array = np.array([[-3, -2, -1], [0, 1, 2]])
    normalized = normalize_image_array(array)
    expected = (array - (-3)) / (2 - (-3))
    assert np.allclose(normalized, expected), "Normalization failed for array with negative values"

    # Test 4: Check already normalized array
    array = np.array([[0, 0.5, 1]])
    normalized = normalize_image_array(array)
    assert np.allclose(normalized, array), "Normalization failed for already normalized array"


def test_generate_image(tmp_path):
    # Test 1: Generate an image and return it without saving
    array = (np.random.rand(100, 100, 3) * 255).astype(np.uint8)  # Random RGB image
    image = generate_image(array)
    assert isinstance(image, Image.Image), "Generated image is not a PIL Image object"
    assert image.size == (100, 100), "Generated image has incorrect dimensions"

    # Test 2: Save the image to a temporary location
    save_dir = tmp_path / "images"
    save_dir.mkdir()
    save_path = str(save_dir)
    image = generate_image(array, save_path=save_path)

    # Check if the image file exists
    generated_images = [f for f in os.listdir(save_dir) if f.startswith("generated_map_") and f.endswith(".png")]
    assert len(generated_images) == 1, "Image was not saved with the correct name"
    image_path = save_dir / generated_images[0]
    assert image_path.exists(), "Image file does not exist in the save path"
    assert Image.open(image_path).size == (100, 100), "Saved image has incorrect dimensions"
