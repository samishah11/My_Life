import streamlit as st

def main():
    st.title("My Life App")
    
    # Input text
    user_input = st.text_input("💬 Enter a word:")
    
    # Process input
    if user_input == "ssami":
        response = '❤️ I Love you my wife, my life and my love  ❤️'
    elif user_input == "sshah":
        response = "💖 Your Love husbend, your life and your love💖"
    else:
        response = "😊 Thank you for using 😊"
    
    # Display response
    if user_input:
        st.write(response)

if __name__ == "__main__":
    main()
