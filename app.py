import streamlit as st
import mishkal.tashkeel
from ghalatawi.autocorrector import AutoCorrector

autoco = AutoCorrector()

def tashkeel_app(text):
    vocalizer = mishkal.tashkeel.TashkeelClass()
    tashkeeled_text = vocalizer.tashkeel(text)
    return tashkeeled_text

def correct_spelling(text):
    return autoco.spell(text)

def main():
    st.title("Tashkeel and Spell Checker App")
    st.write("This app adds Tashkeel (Arabic diacritics) and checks spelling for the given text.")

    tashkeel_input = st.text_area("Enter your text for Tashkeel:")

    if st.button("Add Tashkeel"):
        if tashkeel_input:
            tashkeeled_text = tashkeel_app(tashkeel_input)
            st.write("Tashkeeled Text:")
            st.write(tashkeeled_text)
        else:
            st.warning("Please enter some text for Tashkeel.")

    spell_input = st.text_area("Enter your text for Spell Check:")

    if st.button("Check Spelling"):
        if spell_input:
            corrected_text = correct_spelling(spell_input)
            st.write("Corrected Text:")
            st.write(corrected_text)
        else:
            st.warning("Please enter some text for Spell Check.")

if __name__ == "__main__":
    main()
