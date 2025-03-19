import pytest
import json
from src.terrains_dict import TerrainDict


def test_default_initialization():
    """Test the initialization with default terrains."""
    terrain_dict = TerrainDict()
    assert terrain_dict.terrains is not None
    assert isinstance(terrain_dict.terrains, dict)
    assert len(terrain_dict.terrains) > 0  # Default terrains must exist


def test_custom_terrains_initialization():
    """Test initialization with custom terrains."""
    custom_terrains = {
        "ocean": [(0, 0, 255), 0.5],
        "plains": [(34, 139, 34), 0.7]
    }
    terrain_dict = TerrainDict(terrains=custom_terrains)
    assert terrain_dict.terrains == custom_terrains


def test_invalid_terrains_initialization():
    """Test validation error for incorrect terrains format."""
    invalid_terrains = {
        "ocean": [(0, 0), 0.5],  # Invalid color size
        "plains": [(34, 139, 34), 0.7]
    }
    with pytest.raises(Exception):
        TerrainDict(terrains=invalid_terrains)


def test_non_unique_thresholds():
    """Test validation error for non-unique threshold values."""
    invalid_terrains = {
        "ocean": [(0, 0, 255), 0.5],
        "plains": [(34, 139, 34), 0.5]  # Duplicate threshold value
    }
    with pytest.raises(ValueError, match="Every threshold value must be unique!"):
        TerrainDict(terrains=invalid_terrains)


def test_load_terrains_from_json(tmp_path):
    """Test loading terrains from a JSON file."""
    terrains_json = {
        "ocean": [[0, 0, 255], 0.5],
        "plains": [[34, 139, 34], 0.7]
    }
    json_path = tmp_path / "terrains.json"
    with open(json_path, "w") as f:
        json.dump(terrains_json, f)

    terrain_dict = TerrainDict(json_path=str(json_path))
    assert terrain_dict.terrains == terrains_json


def test_write_terrains_to_json(tmp_path):
    """Test writing terrains to a JSON file."""
    custom_terrains = {
        "ocean": [[0, 0, 255], 0.5],
        "plains": [[34, 139, 34], 0.7]
    }
    json_path = tmp_path / "terrains.json"

    terrain_dict = TerrainDict(terrains=custom_terrains)
    terrain_dict.write_terrains_to_json(write_json_path=str(json_path))

    with open(json_path, "r") as f:
        loaded_terrains = json.load(f)

    assert loaded_terrains == custom_terrains


def test_sorted_terrains():
    """Test that terrains are sorted by threshold values after initialization."""
    unsorted_terrains = {
        "plains": [(34, 139, 34), 0.7],
        "ocean": [(0, 0, 255), 0.5]
    }
    terrain_dict = TerrainDict(terrains=unsorted_terrains)
    sorted_keys = list(terrain_dict.terrains.keys())
    assert sorted_keys == ["ocean", "plains"]  # Expected sorted order
