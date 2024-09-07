from ursina import *
from ursina import Default, camera
from ursina.prefabs.first_person_controller import FirstPersonController

from numpy import floor
from perlin_noise import PerlinNoise

from ursina.shaders import basic_lighting_shader
import os

app = Ursina()
MAPSIZE = 10
BASE_DIR = os.getcwd()
IMG_DIR = os.path.join(BASE_DIR, 'assets/textures')
block_texture = []

file_list = os.listdir(IMG_DIR)
for image in file_list:
     textures = load_texture('assets/textures' + os.sep + image)
     textures.append(textures)

print(block_texture)


class Block(Button):
        id = 1


        def __init__(self, pos, **kwargs):
            super().__init__(
                parent=scene,
                model='cube',
                texture=textures[Block.id],
                scale=1,
                collider='box',
                position=pos,
                color=color.color(0,0, random.uniform(0.9, 1)),
                highlight_color=color.gray,
                shader=basic_lighting_shader,
                origin_y=-0.5,
                **kwargs)

                
        def input(self, key):
            if self.hovered:
                d = distance(player, self)
                if key == "left mouse down" and d<10:
                    destroy(self)
                if key == "right mouse down" and d<10:
                    block = Block(self.position + mouse.normal)
            if key == 'sroll up':
                Block.id+=1
                if Block.id<0:
                     Block.id = len(textures)-1


            



player = FirstPersonController()

sky = Sky(texture='sky_sunset')

light = DirectionalLight(shadows=True,)
light.look_at(Vec3(1,-1,1))


#scene.fog_density = (5, 50)   # sets linear density start and end

noise = PerlinNoise(octaves=2, seed=4522)

for x in range(-MAPSIZE, MAPSIZE):
        for z in range(-MAPSIZE, MAPSIZE):
            y = floor(noise([x/24, z/24])*6)
            block = Block((x,y,z))

window.fullscreen = True
app.run()
