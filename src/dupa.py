terrains = {
                "water": [(31, 69, 252), 0.55],
                "shallow_water": [(133, 216, 229), 0.58],
                "sand": [(242, 232, 211), 0.60],
                "land": [(34, 139, 34), 0.75],
                "mountains": [(255, 255, 255), 0.90],
                "higher_mountains": [(123, 123, 123), 0.91]
            }

from map_gen import MapGenerator
from noise_gen import PerlinNoiseGenerator
from terrains_dict import TerrainDict

# test = dict(sorted(terrains.items(), key=lambda item: item[1][1]))
# print(next(reversed(test.items())))
# for key, value in test.items():
#     print(value)
td = TerrainDict(terrains=terrains)


for i in range(10):
    mg = MapGenerator(shape=(512, 512), terrains=td)
    png = PerlinNoiseGenerator(
        scale=0.5,
    )
    mg.generate(png)
