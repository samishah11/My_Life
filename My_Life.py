import streamlit as st

def main():
    st.title("My Life App")
    
    # Input text
    user_input = st.text_input("💬 Enter a word:")
    
    # Process input
    if user_input == "ssami":
        response = '❤️ I Love you my wife and my life ❤️'
    elif user_input == "sshah":
        response = "💖 Your Love husbend and your life 💖"
    else:
        response = "😊 Thank you for using 😊"
    
    # Display response
    if user_input:
        st.write(response)

if __name__ == "__main__":
    main()
