import streamlit as st
from PIL import Image

def main():
    st.title("Photos-Hub")
    menu = ["Home", "Pictures", "Login", "Sign-Up"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")

    elif choice == "Login":
        st.subheader("Login Section")

        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password", type='password')
        if st.sidebar.checkbox("Login"):
            st.success("Logged in as {}".format(username))

            task = st.selectbox("Task",["Upload Picture", "Remove Picture"])
            if task == "Upload Picture":
                pass


    elif choice == "Sign-Up":
        st.subheader("Create New Account")
        new_user = st.text_input("Usernane")
        new_password = st.text_input("Password",type='password')

        if st.button("Sign Up"):
            st.success("Successfully Created Account : {}".format(new_user))
            st.info("Proceed to Login page.")

    elif choice == "Pictures":
        st.subheader("Pictures Of Champions")

        ####### PICTURE OF VI AND JINX ########
        image =Image.open("/app/frontend-dir/league-of-legends/vi-jinx.png")
        # resizing the image to 720p
        new_width = int(new_height / image.height *image.width)
        image.resize((new_width, new_height))
        st.image(image, caption='Jinx-Vi')
        st.button("Download", key="3")

        ####### PICTURE OF MASTER YI ########
        image =Image.open("/app/frontend-dir/league-of-legends/master-yi.png")
        # resizing the image to 720p
        new_width = int(new_height / image.height *image.width)
        image.resize((new_width, new_height))
        st.image(image, caption='Master Yi')
        st.button("Download", key="4")

        ####### PICTURE OF KARTHUS ########
        image =Image.open("/app/frontend-dir/league-of-legends/karthus.png")
        # resizing the image to 720p
        new_width = int(new_height / image.height *image.width)
        image.resize((new_width, new_height))
        st.image(image, caption='Karthus')
        st.button("Download", key="5")




if __name__ == '__main__':
    main()