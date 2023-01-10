from pydantic import BaseModel
from PIL import Image


new_height = 720

def Resizing(image_path):
    image = Image.open(image_path)
    new_width = int(new_height / image.height *image.width)
    image.resize((new_width, new_height))
    return image



class Weapon(BaseModel):
    name: str
    attack_damage: int = 0
    magic_damage: int = 0
    attack_speed: int = 0
    ability_haste: int = 0
    


class Champion(BaseModel):
    name: str
    health: int
    mana: int
    health_regen: float
    mana_regen: float
    attack_damage: int
    magic_damage: int
    armor: float
    magic_resist: float
    critical_damage: int
    movement_speed: int
    attack_range: int
    weapon: Weapon
