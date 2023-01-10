import mysql
import mysql.connector

db = mysql.connector.connect(
    host="mydb",
    user="root",
    passwd="123456",
    database="eass",
    auth_plugin='mysql_native_password'
)

create_champions_table_query = """
CREATE TABLE champions(
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
    weapon VARCHAR(100) FOREIGN KEY REFERENCE weapons(name)
)
"""

with db.cursor() as cursor:
    cursor.execute(create_champions_table_query)
    db.commit()

create_weapons_table_query = """
CREATE TABLE champions(
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


def insert_champion(values_list):
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

    for row in result:
        mydict = {
        "name":row[0],
        "health":row[1],
        "mana":row[2],
        "health_regen":row[3],
        "mana_regen":row[4],
        "attack_damage":row[5],
        "magic_damage":row[6],
        "armor":row[7],
        "magic_resist":row[8],
        "critical_damage":row[9],
        "movement_speed":row[10],
        "attack_range":row[11],
        "weapon":row[12]
    }
    return mydict

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