import mysql
import mysql.connector
from models import Champion

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
    weapon VARCHAR(100)
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


def insert_champion(champion: Champion):
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
        weapon
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    
    values_list=list()
    for i in Champion:
        values_list.append()

    with db.cursor() as cursor:
        cursor.execute(sql_query, values_list)
        db.commit()


def insert_weapon(values_list):
    sql_query = '''INSERT INTO champions(
        name,
        attack_damage,
        magic_damage,
        attack_speed,
        ability_haste
        VALUES (%s, %s, %s, %s, %s)'''

    with db.cursor() as cursor:
        cursor.execute(sql_query, values_list)
        db.commit()


def db_champion(champion_name):
    select_champion = """SELECT * FROM champions WHERE name = '{}'""".format(champion_name)
    cursor = db.cursor()
    cursor.execute(select_champion)
    result = cursor.fetchall()
    mydict=dict()
    for row in result:
        mydict["name"]:row[0]
        mydict["health"]:row[1]
        mydict["mana"]:row[2]
        mydict["health_regen"]:row[3]
        mydict["mana_regen"]:row[4]
        mydict["attack_damage"]:row[5]
        mydict["magic_damage"]:row[6]
        mydict["armor"]:row[7]
        mydict["magic_resist"]:row[8]
        mydict["critical_damage"]:row[9]
        mydict["movement_speed"]:row[10]
        mydict["attack_range"]:row[11]
        mydict["weapon"]:row[12]

    return mydict

def db_champion2(champion_name):
    select_champion = """SELECT JSON_ARRAYAGG(JSON_OBJECT(
        'name', name,
        'health', health,
        'mana', mana,
        'health_regen', health_regen,
        'mana_regen', mana_regen,
        'attack_damage', attack_damage,
        'magic_damage', magic_damage,
        'armor', armor,
        'magic_resist', magic_resist,
        'critical_damage', critical_damage,
        'movement_speed', movement_speed,
        'attack_range', attack_range
        'weapon', weapon)) FROM chapions WHERE name = '{}';""".format(champion_name)

    cursor = db.cursor()
    cursor.execute(select_champion)
    return cursor


def db_weapon(weapon_name):
    select_weapon = """SELECT * FROM weapons WHERE name = '{}'""".format(weapon_name)
    cursor = db.cursor()
    cursor.execute(select_weapon)
    result = cursor.fetchall()

    for row in result:
        mydict = {
        "name":row[0],
        "attack_damage":row[1],
        "magic_damage":row[2],
        "attack_speed":row[3],
        "ability_haste":row[4]
    }
    return mydict