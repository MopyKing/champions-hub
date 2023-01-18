import mysql
import mysql.connector
from models import Champion, Weapon

essence_reaver= Weapon(
    name="essence reaver",
    attack_damage=45, 
    ability_haste=20)

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

db = mysql.connector.connect(
    host="mydb",
    user="root",
    passwd="123456",
    database="eass",
    auth_plugin='mysql_native_password'
)

create_weapons_table_query = """
CREATE TABLE IF NOT EXISTS weapons(
    name VARCHAR(100) PRIMARY KEY, 
    attack_damage INT, 
    magic_damage INT,
    attack_speed INT, 
    ability_haste INT
    )
"""

with db.cursor() as cursor:
    cursor.execute(create_weapons_table_query)
    db.commit()

create_champions_table_query = """
CREATE TABLE IF NOT EXISTS champions(
    name VARCHAR(100) PRIMARY KEY, 
    health INT, 
    mana INT, 
    health_regen float(10,7), 
    mana_regen float(10,7), 
    attack_damage INT, 
    magic_damage INT,
    armor INT, 
    magic_resist INT, 
    critical_damage INT, 
    movement_speed INT, 
    attack_range INT, 
    weapon VARCHAR(100), FOREIGN KEY(weapon) REFERENCES weapons(name)
    )
"""

with db.cursor() as cursor:
    cursor.execute(create_champions_table_query)
    db.commit()

sql_query = '''INSERT INTO weapons(
    name,
    attack_damage,
    magic_damage,
    attack_speed,
    ability_haste)
    VALUES (%s, %s, %s, %s, %s)'''

values_list=(
    essence_reaver.name,
    essence_reaver.attack_damage,
    essence_reaver.magic_damage,
    essence_reaver.attack_speed,
    essence_reaver.ability_haste
)

with db.cursor() as cursor:
    cursor.execute(sql_query, values_list)
    db.commit()

sql_query = '''INSERT INTO champions(
        name,
        health,
        mana,
        health_regen,
        mana_regen,
        attack_damage,
        magic_damage,
        armor,
        magic_resist,
        critical_damage,
        movement_speed,
        attack_range,
        weapon)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

values_list=(
    karthus.name,
    karthus.health,
    karthus.mana,
    karthus.health_regen,
    karthus.mana_regen,
    karthus.attack_damage,
    karthus.magic_damage,
    karthus.armor,
    karthus.magic_resist,
    karthus.critical_damage,
    karthus.movement_speed,
    karthus.attack_range,
    essence_reaver.name,
)

with db.cursor() as cursor:
    cursor.execute(sql_query, values_list)
    db.commit()

select_champion = """SELECT * FROM champions WHERE name = 'karthus'"""
cursor = db.cursor()
cursor.execute(select_champion)
result = cursor.fetchall()
mydict1 = {}
mydict1["name"]=result[0][0]
print(result[0])
print(result[0][0])
print(mydict1)
print("now trying full query")

champion_name='karthus'
select_champion = f"SELECT * FROM champions WHERE name = '{champion_name}'"
cursor = db.cursor()
cursor.execute(select_champion)
result = cursor.fetchall()
mydict={}
mydict["name"]:result[0][0]
mydict["health"]:result[0][1]
mydict["mana"]:result[0][2]
mydict["health_regen"]:result[0][3]
mydict["mana_regen"]:result[0][4]
mydict["attack_damage"]:result[0][5]
mydict["magic_damage"]:result[0][6]
mydict["armor"]:result[0][7]
mydict["magic_resist"]:result[0][8]
mydict["critical_damage"]:result[0][9]
mydict["movement_speed"]:result[0][10]
mydict["attack_range"]:result[0][11]
mydict["weapon"]:result[0][12]
print(mydict)