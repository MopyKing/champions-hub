import streamlit as st
from PIL import Image
import requests
import pandas as pd
import json
import base64
import io
from html.parser import HTMLParser
# comment for din

def main():
    new_height = 720
    st.title("Champions-Hub")
    menu = ["Home", "pictures", "masteryi", "karthus", "poppy","champions", "weapons", "update-champion", "update-weapon"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        new_title = '<p style="font-family:sans-serif; color:black; font-size: 45px;">Welcome To Champions Hub!</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        new_title = '<p style="font-family:sans-serif; color:black; font-size: 30px;">In this application you will be able to do several things :</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        # 1. Display Information about the champion "Master-Yi"<br>2. Display Information about the champion "Karthus"<br>3. Display Information about the champion "Poppy"<br>4. Display the pictures of all the champions<br>5. Display champion information dynamically of your choice
        new_title = '<p style="font-family:sans-serif; color:black; font-size: 20px;">1. Display Information about the champion "Master-Yi"<br><br>2. Display Information about the champion "Karthus"<br><br>3. Display Information about the champion "Poppy"<br><br>4. Display the pictures of all the champions<br><br>5. Display champion information dynamically of your choice<br><br>6. Update champions information<br><br>7. Update  weapons information.</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.info('Please Navigate To The Scroll Bar "Menu" Located Top Left Corner Of This Window And Choose A Task')
        #st.subheader("Home")

    elif choice == "pictures":
        st.subheader("Pictures Of Champions")

        ####### PICTURE OF POPPY ########
        image_path = "/app/frontdir/league-of-legends/poppy.png"

        image = Image.open(image_path)
        # resizing the image to 720p
        new_width = int(new_height / image.height * image.width)
        image.resize((new_width, new_height))
        st.image(image, caption="Poppy")
        #st.button("Download", key="3")

        ####### PICTURE OF MASTER YI ########
        image = Image.open("/app/frontdir/league-of-legends/masteryi.png")
        # resizing the image to 720p
        new_width = int(new_height / image.height * image.width)
        image.resize((new_width, new_height))
        st.image(image, caption="Master Yi")
        #st.button("Download", key="4")

        ####### PICTURE OF KARTHUS ########
        image = Image.open("/app/frontdir/league-of-legends/karthus.png")
        # resizing the image to 720p
        new_width = int(new_height / image.height * image.width)
        image.resize((new_width, new_height))
        st.image(image, caption="Karthus")
        #st.button("Download", key="5")

        ####### PICTURE OF EVERFROST ########
        image = Image.open("/app/frontdir/league-of-legends/everfrost.png")
        st.image(image, caption="Everfrost")
        #st.button("Download", key="5")

        ####### PICTURE OF ESSENCE REAVER ########
        image = Image.open("/app/frontdir/league-of-legends/essence-reaver.png")
        st.image(image, caption="Essenec-Reaver")
        #st.button("Download", key="5")

    elif choice == "masteryi":
        new_title = '<p style="font-family:sans-serif; color:black; font-size: 42px;">Here you can view Master-Yi`s information !</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.markdown("View :red[Master-Yi] information below.")
        #if st.text_input("Champion name") == "masteryi":
        dfs = []
        response = requests.get("http://backend:90/v1/champions/masteryi")
        content = json.loads(response.text)
        dfs.append(pd.DataFrame([content]))
        df = pd.concat(dfs, ignore_index=True, sort=False).transpose()

        image = Image.open("/app/frontdir/league-of-legends/masteryi.png")
        # resizing the image to 720p
        new_width = int(new_height / image.height * image.width)
        image.resize((new_width, new_height))
        st.image(image, caption="Master Yi")
        st.table(df)

    elif choice == "karthus":
        new_title = '<p style="font-family:sans-serif; color:black; font-size: 42px;">Here you can view Karthus` information !</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.markdown("View :green[Karthus] information below.")
        #if st.text_input("Champion name") == "karthus":
        dfs = []
        response = requests.get("http://backend:90/v1/champions/karthus")
        content = json.loads(response.text)
        dfs.append(pd.DataFrame([content]))
        df = pd.concat(dfs, ignore_index=True, sort=False).transpose()

        image = Image.open("/app/frontdir/league-of-legends/karthus.png")
        # resizing the image to 720p
        new_width = int(new_height / image.height * image.width)
        image.resize((new_width, new_height))
        st.image(image, caption="Karthus")
        st.table(df)

    elif choice == "poppy":
        new_title = '<p style="font-family:sans-serif; color:black; font-size: 42px;">Here you can view Poppy`s information !</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.markdown("View :blue[Poppy] information below.")
        #if st.text_input("Champion name") == "poppy":      
        dfs = []
        response = requests.get("http://backend:90/v1/champions/poppy")
        content = json.loads(response.text)
        dfs.append(pd.DataFrame([content]))
        df = pd.concat(dfs, ignore_index=True, sort=False).transpose()

        image = Image.open("/app/frontdir/league-of-legends/poppy.png")
        # resizing the image to 720p
        new_width = int(new_height / image.height * image.width)
        image.resize((new_width, new_height))
        st.image(image, caption="Poppy")
        st.table(df)

    elif choice == "champions":
        new_title = '<p style="font-family:sans-serif; color:black; font-size: 42px;">Here you can display information about several champions !</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.markdown("If You Havent Entered A Name Yet - Ignore The Warning.")
        st.markdown("Try input one of the names : :red['masteryi'], :green['karthus'], :blue['poppy']")
        name = st.text_input("Champion name")
        while(True):
            if(name!=None or name!= ""):
                break
        dfs = []
        response = requests.get(url="http://backend:90/v1/champions/get-champion-by-name", params={"champion_name":name})
        content = json.loads(response.text)
        dfs.append(pd.DataFrame([content]))
        df = pd.concat(dfs, ignore_index=True, sort=False).transpose()
        image = Image.open("/app/frontdir/league-of-legends/{}.png".format(name))
        # resizing the image to 720p
        new_width = int(new_height / image.height * image.width)
        image.resize((new_width, new_height))
        st.image(image, caption=f"{name}")
        st.table(df)

    elif choice == "weapons":
        new_title = '<p style="font-family:sans-serif; color:black; font-size: 42px;">Here you can display information about several weapons !</p>'
        st.markdown(new_title, unsafe_allow_html=True)
        st.markdown("If You Havent Entered A Name Yet - Ignore The Warning.")
        st.markdown("Try input one of the names : :blue['everfrost'], :blue['essence-reaver']")
        name = st.text_input("Weapon name")
        while(True):
            if(name!=None or name!= ""):
                break
        dfs = []
        response = requests.get(url="http://backend:90/v1/weapons/get-weapon-by-name", params={"weapon_name":name})
        content = json.loads(response.text)
        dfs.append(pd.DataFrame([content]))
        df = pd.concat(dfs, ignore_index=True, sort=False).transpose()
        image = Image.open("/app/frontdir/league-of-legends/{}.png".format(name))
        st.image(image, caption="{name}")
        st.table(df)

    elif choice == "update-champion":
            new_title = '<p style="font-family:sans-serif; color:black; font-size: 42px;">Here you can update a Champion ! HOW COOL IS THAT ??</p>'
            st.markdown(new_title, unsafe_allow_html=True)
            st.markdown("Champion names are :red['masteryi'], :green['karthus'] And :blue['poppy']")
            st.info("when finished check the 'submit' box at the bottom")
            name = st.text_input("champion name")
            st.warning("THE NAME FIELD IS ALWAYS REQUIRED")
            health = st.text_input("health")
            mana = st.text_input("mana")
            health_regen = st.text_input("health regen")
            mana_regen = st.text_input("mana regen")
            attack_damage = st.text_input("attack damage")
            magic_damage = st.text_input("magic damage")
            armor = st.text_input("armor")
            magic_resist = st.text_input("magic resist")
            critical_damage = st.text_input("critical damage")
            movement_speed = st.text_input("movement speed")
            attack_range = st.text_input("attack range")

            champion = {
                "name": name,
                "health": health,
                "mana": mana,
                "health_regen": health_regen,
                "mana_regen": mana_regen,
                "attack_damage": attack_damage,
                "magic_damage": magic_damage,
                "armor": armor,
                "magic_resist": magic_resist,
                "critical_damage": critical_damage,
                "movement_speed": movement_speed,
                "attack_range": attack_range,
            }

            if st.checkbox('submit'):
                for i in champion:
                    if champion[i] == '' or champion[i] == None or champion[i] == ' ':
                        champion[i] = 0
                    else:
                        continue
                data_json=json.dumps(champion)
                headers = {'Content-Type': 'application/json'}
                response = requests.put(url="http://backend:90/v1/champions/update-champion", data=data_json, headers=headers)
                st.success('Successfully updated the champion `{}` !'.format(name))
                st.info('Please Navigate To The "Menu", Select `champions`, And Enter `{}` To See If It Worked.'.format(name))

    elif choice == "update-weapon":
            new_title = '<p style="font-family:sans-serif; color:black; font-size: 42px;">Here you can update a Weapon ! HOW COOL IS THAT ??</p>'
            st.markdown(new_title, unsafe_allow_html=True)
            st.markdown("Weapon names are :red['everfrost'] And :blue['essence-reaver]")
            st.info("when finished check the 'submit' box at the bottom")
            name = st.text_input("weapon name")
            st.warning("THE NAME FIELD IS ALWAYS REQUIRED")
            attack_damage = st.text_input("attack damage")
            magic_damage = st.text_input("magic damage")
            attack_speed = st.text_input("attack speed")
            ability_haste = st.text_input("ability haste")
            weapon = {
                "name": name,
                "attack_damage": attack_damage,
                "magic_damage": magic_damage,
                "attack_speed": attack_speed,
                "ability_haste": ability_haste,
            }

            dfs = []
            if st.checkbox('submit'):
                for i in weapon:
                    if weapon[i] == '' or weapon[i] == None or weapon[i] == ' ':
                        weapon[i] = 0
                    else:
                        continue
                data_json=json.dumps(weapon)
                headers = {'Content-Type': 'application/json'}
                response = requests.put(url="http://backend:90/v1/weapons/update-weapon", data=data_json, headers=headers)
                st.success('Successfully updated the weapon {} !'.format(name))
                st.info('Please Navigate To The "Menu", Select `weapons`, And Enter `{}` To See If It Worked.'.format(name))


if __name__ == "__main__":
    main()