from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import randint

app = Ursina()
window.fullscreen = True

player = FirstPersonController()
player.position = (-6, -3, 6)

def sol():
    global ground
    ground=Entity(
        model="plane",
        color = color.white,
        scale=(300, 1, 300),
        collider=("mesh"),
        position = (0, -4,0)
    )


############################# cube game #################################
def disable():
    destroy(cube)

def cube_g():
    global cube
    cube = Entity(
        model = 'cube',
        color = color.random_color(),
        collider='cube',
        sacle=1,
        on_click=disable,
        position=(randint(-30, 30) * .1, randint(-30, 30) * .1),
    )
        
def ball():
    global sphere
    sphere = Entity(
        model ='sphere',
        texture='grass',
        color = color.green,
        collider="sphere",
        scale = 2,
        rotation=45,
        on_click=cube_g,
        position =(-6, -2.5, 0),
        )

def couleur():
    sphere.color = color.random_color()


def cadre():
    P1 = Entity(model= 'cube', scale=(0.5, 11.5, 1.5), color = color.black, position = (-10, -1,0), collider="mesh")
    P2 = Entity(model= 'cube', scale=(2, 14, 1.5), color = color.black, position = (-3, 4, 0), collider="mesh")
    P2.rotation_y = 90
    P2.rotation_x = 90
    P3 = Entity(model= 'cube', scale=(0.5, 11.5, 1.5), color = color.black, position = (4, -1,0), collider="mesh")
    P4 = Entity(model= 'cube', scale=(0.5, 11.5, 14), color = color.black, position = (-3, -1,-1), collider="mesh")
    P4.rotation_y=90
    P5 = Entity(model= 'cube', scale=(2, 14, 1.5), color = color.black, position = (-3, -4.5, 0), collider="mesh")
    P5.rotation_y = 90
    P5.rotation_x = 90

def button():
    global boutton
    
    boutton=Entity(
        model = "cube",
        collider = "mesh",
        position = (-8, -3, 0),
        on_click = couleur,
        texture='Texture_Pack/change',
    )
sol()
ball()
button()
cadre()
############################# cube game #################################

app.run()