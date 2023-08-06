import streamlit as st
from ar_corrector.corrector import Corrector
import mishkal.tashkeel

def tashkeel_app(text):
    vocalizer = mishkal.tashkeel.TashkeelClass()
    tashkeeled_text = vocalizer.tashkeel(text)
    return tashkeeled_text

def correct_spelling(text):
    corr = Corrector()
    corrected_text = corr.contextual_correct(text)
    return corrected_text

def main():
    st.title("Tashkeel and Spelling Corrector App")
    st.write("This app adds Tashkeel (Arabic diacritics) and corrects spelling for the given text.")

    text_input = st.text_area("Enter your text:")

    if st.button("Add Tashkeel and Correct Spelling"):
        if text_input:
            tashkeeled_text = tashkeel_app(text_input)
            corrected_text = correct_spelling(tashkeeled_text)
            st.write("Tashkeeled and Corrected Text:")
            st.write(corrected_text)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
