import streamlit as st
import pickle
import pandas as pd
import numpy as np
model = pickle.load(open('Mobile_Price_Classsification_model.pkl','rb'))


# Function to make predictions
def predict_price_range(features):
    # Make predictions
    prediction = model.predict(features)
    return prediction
st.sidebar.title("Dashboard")
app_mode = st.sidebar.selectbox("Select Page",["Home","About","Prediction"])
if(app_mode=="Home"):
    st.header("Mobile Price Range Prediction")
    image_path = "The-OnePlus-Nord-CE-3-Lite-5G---Vishal-Mathur--HT-_1680683337035.webp"
    st.image(image_path)
elif(app_mode=="About"):
    st.header("Mobile Price Range Prediction")
    image_path = "maxresdefault.jpg"
    st.image(image_path)


# Main function to run the Streamlit app
elif(app_mode=="Prediction"):

    # Set title and description
    st.title('Mobile Price Range Prediction')
    st.write('This app predicts the price range of mobile phones based on input features.')


    # Add input widgets for each feature
    battery_power = st.text_input('Battery Power','Enter Battery power in mah')
    front_camera = st.text_input('Front Camera','Enter Front Camera pixels')
    Four_g=st.text_input('Four_g','Enter 1 for yes and 0 for no')
    internal_memory=st.text_input("Internal memory",'Enter Value in gigabytes')
    mobile_weight=st.text_input("Weight ",'weight in gram')
    Primary_camera=st.text_input("pc",'Enter Primary Camera Pixels Value')
    Ram=st.text_input("Ram",'Ram in Megabytes')
    screen_height=st.text_input("Sc_h",'Enter Screen Height')
    screen_width=st.text_input("Sc_w","Enter Screen Width..")
    three_g=st.text_input("Three_g",'Enter 1 for yes and 0 for no')
    touch_screen=st.text_input("Touch_Screen",'Enter 1 for yes and 0 for no.')

    input_data = {
        'battery_power': (battery_power),
        'front_camera': (front_camera),
        'Four_g':(Four_g),
        'internal_memory':(internal_memory),
        'mobile_weight': (mobile_weight),
        'pc':(Primary_camera),
        'Ram':(Ram),
        'sc_h':(screen_height),
        'sc_w':(screen_width),
        'three_g':(three_g),
        'touch_screen':(touch_screen)
        # Add other features here
    }
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])

    # Predict the price range
    if st.button('Predict'):
        prediction = predict_price_range(input_df)
        if prediction[0]==0:
            st.write('Predicted Price range is 5000')
        elif prediction[0]==1:
            st.write('Predicted Price range is 12000')
        elif prediction[0]==2:
            st.write('Predicted Price Range is 18000')
        elif prediction[0]==3:
            st.write('Predicted Price Range is 25000')
        else:
            st.write("404 Error")





