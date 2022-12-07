import streamlit as st

def main():
    st.title("Photos-Hub")
    menu = ["Home", "Login", "Sign-Up"]
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



if __name__ == '__main__':
    main()