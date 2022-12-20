from fastapi import FastAPI
from pydantic import BaseModel
from backdir.models import Champion, Weapon, Resizing

app = FastAPI()

essence_reaver= Weapon(
    attack_damage=45, 
    ability_haste=20)

masteryi = Champion(
    name="master-yi", 
    health=654, 
    mana=349 , 
    health_regen=3.75, 
    mana_regen=8.18 , 
    attack_damage=60 , 
    magic_damage=0,
    armor=28, 
    magic_resist=30, 
    critical_damage=175, 
    movement_speed=335, 
    attack_range=500, 
    weapon=essence_reaver)

Champions_List = []
Champions_List.append(masteryi)

Champions_Info = {
    "champions": Champions_List,
    "number_of_champions": len(Champions_List)
}

@app.get("/")
def home():
    return {"Welcome ":"This is The Default Page"}

@app.get("/about")
def about():
    return {"Data":"About"}


@app.get("/v1/view-champions")
def Display_Champions_Info():
    return Champions_Info

@app.get("/v1/champions/masteryi")
def Zed():
    return masteryi

@app.post("/v1/champions/add-champion")
def Add_Champion(champion: Champion):
    return {"SUCCESS":"You Added a Champion !"}

@app.get("/v1/weapons/essence_reaver")
def Essence_Reaver():
    return essence_reaver

