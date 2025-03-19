from numpy.typing import NDArray
import os
from PIL import Image
import datetime


def normalize_image_array(array: NDArray) -> NDArray:
    """
    Normalize array between 0 and 1

    Args:
        array (NDArray): Array to be normalized

    Returns:
        NDArray: Normalized array
    """
    if array.size == 1:
        return 0
    min_val = array.min()
    max_val = array.max()
    normalized_array = (array - min_val) / (max_val - min_val)
    return normalized_array


def generate_image(array: NDArray, save_path: str = None) -> Image:
    """
    Generates image from numpy array

    Args:
        array (NDArray): 3D RGB Array
        save_path (str, optional): Path to save the generated image. Defaults to None.
    Returns:
        image: PIL Image object
    """
    image = Image.fromarray(array)
    if save_path is not None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_name = f"/generated_map_{datetime.datetime.now().timestamp()}.png"
        save_path = os.path.join(base_dir, save_path) + image_name
        image.save(save_path)
    return image
