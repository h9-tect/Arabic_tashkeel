import os
import streamlit as st
from Shakkala import Shakkala

# create Shakkala object
sh = Shakkala('./', version=3)

# load the model
model, graph = sh.get_model()

def predict_harakat(input_text):
    # prepare input
    input_int = sh.prepare_input(input_text)

    # run the model
    with graph.as_default():
        logits = model.predict(input_int)[0]

    # get the logits
    predicted_harakat = sh.logits_to_text(logits)

    # final output
    final_output = sh.get_final_text(input_text, predicted_harakat)
    
    return final_output

def main():
    st.title("Arabic Text Harakat Prediction")
    
    input_text = st.text_area("Enter your Arabic text:")
    
    if st.button("Predict"):
        if input_text:
            result = predict_harakat(input_text)
            st.markdown("## Predicted Text:")
            st.write(result)
        else:
            st.warning("Please enter some Arabic text to predict harakat.")

if __name__ == "__main__":
    main()
