import pytest
from unittest.mock import patch, MagicMock
from src.app import TileMapWindow


@pytest.fixture
def app_instance(qtbot):
    """Fixture for creating the TileMapWindow instance."""
    app = TileMapWindow()
    qtbot.addWidget(app)  # Manage the application's lifecycle
    return app


def test_switch_to_expert_mode(app_instance):
    """Test switching from default mode to expert mode."""
    app_instance._switch_to_expert_mode()

    assert app_instance.ui.generator_stack.currentIndex() == 1


def test_switch_to_default_mode(app_instance):
    """Test switching from expert mode to default mode."""
    app_instance._switch_to_default_mode()

    assert app_instance.ui.generator_stack.currentIndex() == 0


def test_open_file_dialog(app_instance):
    """Test the file dialog for terrain JSON files"""
    # Mocking QFileDialog behavior
    with patch("PySide6.QtWidgets.QFileDialog.getOpenFileName", return_value=("path/to/config.json", "")):
        app_instance._open_file_dialog()

        # Validate terrain JSON file path was set
        assert app_instance.terrains_json_line_edit.text() == "path/to/config.json"


def test_get_json_config_path_empty(app_instance):
    """Test getting the JSON configuration path when empty."""
    # Ensure the line edit is empty
    app_instance.terrains_json_line_edit.setText("")

    json_path = app_instance._get_json_config_path()

    # Validate that the result is None
    assert json_path is None


def test_get_json_config_path_valid(app_instance):
    """Test getting a valid JSON configuration path."""
    # Set the line edit text
    mock_path = "path/to/config.json"
    app_instance.terrains_json_line_edit.setText(mock_path)

    # Fetch the configuration path
    json_path = app_instance._get_json_config_path()

    # Validate the correct path is returned
    assert json_path == mock_path
