# Tile Map Generator Documentation

## Project goal and description

The project is a straightforward tile map generator implemented in Python. It features a GUI built with PySide6,
enabling users to visualize the generated maps and adjust settings for varying results. By
leveraging [Perlin Noise](https://en.wikipedia.org/wiki/Perlin_noise), the program creates terrain that appears "
natural." Users can further refine the terrain by modifying color values and tweaking the threshold (height) at which
these values are applied.

## Implementation details

#### Core Classes

1. `PerlinNoiseGenerator`

- Generates Perlin noise 2D array, using noise library

2. `MapGenerator`

- Generates full tile map, by applying terrains colors on noise array

3. `TerrainDict`

- Represents Terrain map
- Validates terrain map provided by user
- Accepts terrain map as json

4. `SimpleInfoDialog`

- Custom PySide6 dialog

5. `TileMapWindow`

- Handles whole UI

#### Helper Functions

1. `normalize_image_array`

- Normalizes array values between 0 and 1

2. `generate_image`

- Generates image from numpy array
- Saves image to a file

## Dependencies

- Python > 3.10
- Modules:

```
colorama==0.4.6
exceptiongroup==1.2.2
iniconfig==2.0.0
noise==1.2.2
numpy==2.1.3
packaging==24.2
pillow==11.0.0
pluggy==1.5.0
PySide6==6.8.1
PySide6_Addons==6.8.1
PySide6_Essentials==6.8.1
pytest==8.3.4
shiboken6==6.8.1
tomli==2.2.1
```

## Run Locally

Clone the project

```bash
  git clone https://gitlab-stud.elka.pw.edu.pl/mwojdals/tile-map-generator-pipr-projekt.git
```

Go to the project directory

```bash
  cd tile-map-generator-pipr-projekt
```

Create venv

```bash
  python -m venv .venv
```

Activate venv

- Linux

```bash
  source .venv/bin/activate
```

- Windows

```bash
  .venv/Scripts/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the program

```bash
  python src/main.py
```

## Json terrain config structure

When you want to input custom terrains config, your json file must look like this:

```json
{
  "water": [[31, 69, 252], 0.56],
  "shallow_water": [[133, 216, 229], 0.615],
  "sand": [[242, 232, 211], 0.65]
}
```

First element is a list of RGB values and second is a height threshold.
In config folder there is a default json file, which can be used to play with custom terrains,
but you should not forget to use that in expert mode.

## Limitations

- Map can only be a square, this implementation does not allow rectangular shapes
- For shapes higher than 1000x1000 program tends to slow down
- Generation runs in the same thread as GUI, because of that app can freeze for few seconds when generation process
  starts (especially for bigger shapes).

## Reflection

The project took approximately 10-15 hours to complete. During development, the concept evolved multiple times. One of
the initial challenges was selecting the appropriate noise library, as the available documentation was often incomplete,
making it difficult to determine the best option. Initially, I considered implementing multithreading in the GUI to
handle the time-consuming map generation process, but I ultimately decided it was too complex for this task. Instead, I
focused on optimizing the methods as much as possible. In the end, I achieved full functionality, including additional
features like an Expert mode and the ability for users to input custom terrains.
