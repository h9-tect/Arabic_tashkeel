import streamlit as st
import mishkal.tashkeel

def tashkeel_app(text):
    vocalizer = mishkal.tashkeel.TashkeelClass()
    tashkeeled_text = vocalizer.tashkeel(text)
    return tashkeeled_text

def main():
    st.title("Tashkeel App")
    st.write("This app adds Tashkeel (Arabic diacritics) to the given text.")

    text_input = st.text_area("Enter your text:")

    if st.button("Add Tashkeel"):
        if text_input:
            tashkeeled_text = tashkeel_app(text_input)
            st.write("Tashkeeled Text:")
            st.write(tashkeeled_text)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
