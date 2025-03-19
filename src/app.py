import os

from PySide6.QtWidgets import (QMainWindow, QDialog, QVBoxLayout, QLabel,
                               QPushButton, QFileDialog, QSpinBox)
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QSize
from typing import Tuple, Dict
from PIL import Image

from custom_exceptions.exceptions import WrongArrayShape, NotEnoughData
from ui.ui_map_generator import Ui_MainWindow
from map_gen import MapGenerator
from terrains_dict import TerrainDict
from noise_gen import PerlinNoiseGenerator


class SimpleInfoDialog(QDialog):
    """
    Class which builds simple QT Dialog
    """
    def __init__(self, message, title):
        super().__init__()
        self.title = title
        self.message = message
        self.setWindowTitle(self.title)
        self.resize(300, 150)

        layout = QVBoxLayout()

        label = QLabel(self.message)
        close_button = QPushButton("Okay")
        close_button.clicked.connect(self.close)

        layout.addWidget(label)
        layout.addWidget(close_button)

        self.setLayout(layout)


class TileMapWindow(QMainWindow):
    """
    Tile map generator UI class
    """
    def __init__(self, parent=None):
        super(TileMapWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Config variables
        self._max_image_height = 1000
        self._max_image_width = 1000
        self._image_save_path = "outputs"
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._image_save_path = os.path.join(base_dir, self._image_save_path)
        if not os.path.isdir(self._image_save_path):
            os.mkdir(self._image_save_path)

        # Connecting menu actions to functions
        self.ui.actionDefault_Mode.triggered.connect(self._switch_to_default_mode)
        self.ui.actionExpert_Mode.triggered.connect(self._switch_to_expert_mode)
        self.ui.actionHelp.triggered.connect(self._open_help_dialog)

        # Extracting UI elements
        # Default Page
        self.default_generate_button = self.ui.generate_button_def
        self.default_image_label = self.ui.generate_image_label_def
        self.default_seed_spin_box = self.ui.seed_spin_def
        self.default_shape_spin_box = self.ui.shape_spin_def
        # Expert Page
        self.expert_generate_button = self.ui.generate_button_exp
        self.expert_get_def_vals = self.ui.get_default_vals_button_exp
        self.expert_image_label = self.ui.generate_image_label_exp
        self.scale_slider = self.ui.scale_slider
        self.scale_spin_box = self.ui.scale_spin_box
        self.octaves_slider = self.ui.octaves_slider
        self.octaves_spin_box = self.ui.octaves_spin_box
        self.persistence_slider = self.ui.persistence_slider
        self.persistence_spin_box = self.ui.persistence_spin_box
        self.lacunarity_slider = self.ui.lacunarity_slider
        self.lacunarity_spin_box = self.ui.lacunarity_spin_box
        self.expert_shape_spin_box = self.ui.shape_spin_exp
        self.expert_seed_spin_box = self.ui.seed_spin_exp
        self.expert_fields_dict = {
            self.scale_slider: self.scale_spin_box,
            self.octaves_slider: self.octaves_spin_box,
            self.persistence_slider: self.persistence_spin_box,
            self.lacunarity_slider: self.lacunarity_spin_box,
        }
        self.terrains_json_button = self.ui.terrain_json_button
        self.terrains_json_line_edit = self.ui.terrain_json_line_edit
        self.terrain_info_button = self.ui.terrain_info

        # Connecting buttons to functions
        # Default Page
        self.default_generate_button.clicked.connect(self._generate_image_default_mode)
        # Expert Page
        self.expert_generate_button.clicked.connect(self._generate_image_expert_mode)
        self.expert_get_def_vals.clicked.connect(self._setup_expert_mode)
        self.terrains_json_button.clicked.connect(self._open_file_dialog)
        self.terrain_info_button.clicked.connect(self._open_terrains_info_dialog)

        self._connect_sliders_with_spin_boxes()

    def _generate_image_default_mode(self) -> None:
        """
        Generating map using default values
        """
        seed = self._get_seed_from_spin_box(self.default_seed_spin_box)
        # Getting default values for TerrainDict and PerlinNoiseGenerator
        terrain_dict = TerrainDict()
        perlin_noise_generator = PerlinNoiseGenerator(seed=seed)
        try:
            x_size, y_size = self._get_shape_from_spin_box(self.default_shape_spin_box)
            map_generator = MapGenerator(shape=(x_size, y_size), terrains=terrain_dict)
            image = map_generator.generate(perlin_noise_generator, save_path=self._image_save_path)
            pixmap = self._convert_image_to_pixmap(image)
            self.default_image_label.setPixmap(pixmap)
        except WrongArrayShape as e:
            error_dialog = SimpleInfoDialog(
                title="Error",
                message=str(e),
            )
            error_dialog.exec()

    def _generate_image_expert_mode(self) -> None:
        """
        Generating map using values provided by the user.
        """
        seed = self._get_seed_from_spin_box(self.expert_seed_spin_box)
        noise_parameters = self._get_noise_parameters_from_spin_boxes()
        terrain_json_path = self._get_json_config_path()
        try:
            terrain_dict = TerrainDict(json_path=terrain_json_path)
        except (ValueError, WrongArrayShape, NotEnoughData) as e:
            error_dialog = SimpleInfoDialog(
                title="Error",
                message=str(e),
            )
            error_dialog.exec()
            return  # Jumping out of function, since terrain dict is in a wrong format

        perlin_noise_generator = PerlinNoiseGenerator(
            seed=seed,
            scale=noise_parameters['scale'],
            octaves=noise_parameters['octaves'],
            persistence=noise_parameters['persistence'],
            lacunarity=noise_parameters['lacunarity'],
        )
        try:
            x_size, y_size = self._get_shape_from_spin_box(self.expert_shape_spin_box)
            map_generator = MapGenerator(shape=(x_size, y_size), terrains=terrain_dict)
            image = map_generator.generate(perlin_noise_generator, save_path=self._image_save_path)
            pixmap = self._convert_image_to_pixmap(image)
            self.expert_image_label.setPixmap(pixmap)
        except WrongArrayShape as e:
            error_dialog = SimpleInfoDialog(
                title="Error",
                message=str(e),
            )
            error_dialog.exec()

    def _get_json_config_path(self) -> str | None:
        """
        Getting terrain json config path
        """
        json_config_path = self.terrains_json_line_edit.text()
        if json_config_path == "":
            return None
        return json_config_path

    def _open_file_dialog(self) -> None:
        """
        Opening file dialog and putting json file path json line edit field.
        """
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Json Files (*.json);;Json Files (*.json)")
        if file_path:
            self.terrains_json_line_edit.setText(file_path)

    def _open_terrains_info_dialog(self) -> None:
        """
        Opening terrain info dialog
        """
        info_string = """
        Terrain Json file should look like this:
        {
        "terrain_name_1": [
        [255, 255, 255],
        0.5
        ],
        "terrain_name_2": [
        [125, 125, 125],
        0.6
        ],
        }
        Where first element in a terrain list is a list of RGB Color values and
        second is a threshold value for that terrain.
        """
        terrain_info_dialog = SimpleInfoDialog(
            title="Terrain Json Info",
            message=info_string,
        )
        terrain_info_dialog.exec()

    def _get_default_noise_values(self) -> Dict[str, float]:
        """
        Getting default noise parameters values
        """
        default_noise_generator = PerlinNoiseGenerator()
        default_noise_parameters = {
            "scale": default_noise_generator.scale,
            "octaves": default_noise_generator.octaves,
            "persistence": default_noise_generator.persistence,
            "lacunarity": default_noise_generator.lacunarity,
        }
        return default_noise_parameters

    def _setup_expert_mode(self) -> None:
        """
        Setting up expert mode, putting default noise parameters values into
        sliders and spin-boxes
        """
        default_noise_parameters = self._get_default_noise_values()
        self.scale_spin_box.setValue(default_noise_parameters['scale'])
        self.octaves_spin_box.setValue(default_noise_parameters['octaves'])
        self.persistence_spin_box.setValue(default_noise_parameters['persistence'])
        self.lacunarity_spin_box.setValue(default_noise_parameters['lacunarity'])

    def _get_noise_parameters_from_spin_boxes(self) -> Dict[str, float | int]:
        """
        Getting noise parameters from sliders and returning them.
        """
        scale = self.scale_spin_box.value()
        octaves = self.octaves_spin_box.value()
        persistence = self.persistence_spin_box.value()
        lacunarity = self.lacunarity_spin_box.value()
        noise_parameters = {
            "scale": scale,
            "octaves": octaves,
            "persistence": persistence,
            "lacunarity": lacunarity,
        }
        return noise_parameters

    def _convert_image_to_pixmap(self, image: Image.Image) -> QPixmap:
        """
        Converting image to a QPixmap and scale it if necessary
        """
        image_bytes = image.tobytes("raw", "RGB")
        q_image = QImage(image_bytes, image.width, image.height, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        if image.height > self._max_image_height or image.width > self._max_image_width:
            scaled_pixmap = pixmap.scaled(QSize(self._max_image_height, self._max_image_width))
            return scaled_pixmap
        else:
            return pixmap

    def _connect_sliders_with_spin_boxes(self) -> None:
        """
        Creating a two-way binding between slider-spin_box values
        """
        for slider, spin_box in self.expert_fields_dict.items():
            if slider == self.octaves_slider:
                # Octaves is an int value so we can't apply the same logic as for float fields
                self.octaves_slider.valueChanged.connect(self.octaves_spin_box.setValue)
                self.octaves_spin_box.valueChanged.connect(self.octaves_slider.setValue)
                continue
            # Scale, Persistence, Lacunarity are float fields, but QT slider works only on
            # int values, so we have to adjust that
            slider.valueChanged.connect(lambda value, s_box=spin_box: s_box.setValue(value / 100))
            spin_box.valueChanged.connect(lambda value, sldr=slider: sldr.setValue(int(value * 100)))

    def _get_shape_from_spin_box(self, spin_box: QSpinBox) -> Tuple[int, int]:
        """
        Getting shape values from spin-box
        Map should be square, so only one spin-box is needed
        """
        x = spin_box.value()
        y = spin_box.value()
        return x, y

    def _get_seed_from_spin_box(self, seed_spin_box: QSpinBox) -> int | None:
        """
        Getting seed value from spin box
        """
        seed = seed_spin_box.value()
        if seed == 0:
            return None
        else:
            return seed

    def _switch_to_expert_mode(self) -> None:
        """
        Switching to expert mode
        """
        expert_mode_page_nr = 1
        self._setup_expert_mode()
        self.ui.generator_stack.setCurrentIndex(expert_mode_page_nr)

    def _switch_to_default_mode(self) -> None:
        """
        Switching to default mode
        """
        default_mode_page_nr = 0
        self.ui.generator_stack.setCurrentIndex(default_mode_page_nr)

    def _open_help_dialog(self):
        """
        Opening help dialog
        """
        info_string = """
        If you want to generate map in default mode, just pass shape and optionally seed and click generate.
        * Map is always in squared shape
        
        If you want to customize your map, switch to expert mode. 
        
        Noise parameters in expert mode:
        Scale:
            Scale factor for the Perlin noise. Larger values 'zoom in', smaller values 'zoom out'
        octaves:
            Number of noise layers combined to create final noise
        persistence:
            Controls how much each layer contributes to the final image. When 0.5 - amplitude of noise
            is halved in each successive layer -> Each new layer contributes less than those before
        lacunarity:
            Controls how the size of the blobs changes with each layer. The higher the lacunarity, the more the blob
            size decreases with each new layer.
        seed:
            Seed for reproducibility
        """
        help_dialog = SimpleInfoDialog(
            title="Help",
            message=info_string,
        )
        help_dialog.exec()
