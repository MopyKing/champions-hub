from fastapi import FastAPI
from backdir.models import Weapon, Champion
import mysql
import mysql.connector
from backdir.dbmain import db_champion, insert_champion, db_weapon, insert_weapon, db_update_champion, db_update_weapon


app = FastAPI()

essence_reaver= Weapon(
    name="essence-reaver",
    attack_damage=45, 
    ability_haste=20)

everfrost=Weapon(
    name="everfrost",
    magic_damage=70,
    ability_haste=20
)

masteryi = Champion(
    name="masteryi", 
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

poppy = Champion(
    name="poppy", 
    health=589, 
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

karthus = Champion(
    name="karthus", 
    health=630, 
    mana=520 , 
    health_regen=3, 
    mana_regen=8.2, 
    attack_damage=46 , 
    magic_damage=0,
    armor=30, 
    magic_resist=50, 
    critical_damage=175, 
    movement_speed=335, 
    attack_range=450, 
    weapon=essence_reaver)

Champions_List = [masteryi,karthus,poppy]
Weapons_List = [essence_reaver, everfrost]

Champions_Info = {
    "champions": Champions_List,
    "number_of_champions": len(Champions_List)
}

Weapons_Info = {
    "weapons":Weapons_List,
    "number_of_weapons":len(Weapons_List)
}

insert_weapon(essence_reaver)
insert_weapon(everfrost)
insert_champion(karthus,everfrost)
insert_champion(masteryi,essence_reaver)
insert_champion(poppy,essence_reaver)


@app.get("/")
def home():
    return {"Welcome ":"This is The Default Page"}

@app.get("/v1/view-champions")
def Display_Champions_Info():
    return Champions_Info

@app.get("/v1/champions/masteryi")
def Masteryi():
    champ_name="masteryi"
    return db_champion(champ_name)

@app.get("/v1/champions/poppy")
def Poppy():
    champ_name="poppy"
    return db_champion(champ_name)

@app.get("/v1/champions/karthus")
def Karthus():
    champ_name="karthus"
    return db_champion(champ_name)

@app.get("/v1/champions/get-champion-by-name")
def get_champion(champion_name : str):
    for champ in Champions_Info["champions"]:
        if champ.name == champion_name:
            return db_champion(champ.name)
    return {"Exception": "No Such Champion"}

@app.get("/v1/weapons/get-weapon-by-name")
def get_weapon(weapon_name : str):
    for weap in Weapons_Info["weapons"]:
        if weap.name == weapon_name:
            return db_weapon(weap.name)
    return {"Exception": "No Such Weapon"}

@app.put("/v1/champions/update-champion")
def update_champion(champion: Champion):
    db_update_champion(champion)

@app.put("/v1/weapons/update-weapon")
def update_weapon(weapon: Weapon):
    db_update_weapon(weapon)

@app.get("/v1/weapons/essence_reaver")
def Essence_Reaver():
    return essence_reaver


# sending the image as UTF-8 String : 
'''
data_uri = base64.b64encode(open('/app/backdir/league-of-legends/poppy.png', 'rb').read()).decode('utf-8')
img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)
return {"image": img_tag, "champion": poppy}

FRONT-END SIDE : 
st.markdown(json_obj["image"], unsafe_allow_html=True)
'''


### DATABASE CONFIGS ###

# db = mysql.connector.connect(
#     host="mydb",
#     user="root",
#     passwd="123456",
#     database="eass"
# )

# create_champions_table_query = """
# CREATE TABLE champions(
#     name VARCHAR(100) PRIMARY KEY, 
#     health INT, 
#     mana INT, 
#     health_regen float(10,7), 
#     mana_regen float(10,7), 
#     attack_damage INT, 
#     magic_damage INT,
#     armor INT, 
#     magic_resist INT, 
#     critical_damage INT, 
#     movement_speed INT, 
#     attack_range INT, 
#     weapon VARCHAR(100) FOREIGN KEY REFERENCE weapons(name)
# )
# """

# create_weapons_table_query = """
# CREATE TABLE champions(
#     name VARCHAR(100) PRIMARY KEY, 
#     health INT, 
#     mana INT, 
#     health_regen float(10,7), 
#     mana_regen float(10,7), 
#     attack_damage INT, 
#     magic_damage INT,
#     armor INT, 
#     magic_resist INT, 
#     critical_damage INT, 
#     movement_speed INT, 
#     attack_range INT, 
#     weapon VARCHAR(100)
# )
# """
# with db.cursor() as cursor:
#     cursor.execute(create_weapons_table_query)
#     db.commit()
