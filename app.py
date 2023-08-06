import streamlit as st
import mishkal.tashkeel

def tashkeel_app(text):
    vocalizer = mishkal.tashkeel.TashkeelClass()
    tashkeeled_text = vocalizer.tashkeel(text)
    return tashkeeled_text

def main():
    st.title("تطبيق تشكيل الكلمات العربية")
    st.write("هذا التطبيق يقوم بتشكيل الكلمات العربية ")

    tashkeel_input = st.text_area("قم بوضع النص في المربع أدناه:")

    if st.button("شَكَّلَهَا"):
        if tashkeel_input:
            tashkeeled_text = tashkeel_app(tashkeel_input)
            st.write("Tashkeeled Text:")
            st.write(tashkeeled_text)
        else:
            st.warning("لم تقم بوضع أي نص ")

if __name__ == "__main__":
    main()
