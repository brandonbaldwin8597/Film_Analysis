import streamlit as st
import pickle
import pandas as pd


st.sidebar.title('Movie Settings')
html_temp = """
<div style="background-color:red;padding:5px">
<h2 style="color:white;text-align:center;">Recommended Movie Generator</h2>
</div>"""
st.markdown(html_temp,unsafe_allow_html=True)


length = st.sidebar.radio("What length of movie do you prefer?",('Short', 'Average', 'Long'))
movie_era = st.sidebar.radio("What movie era do you prefer?",('Vintage', 'Classic', 'Modern'))
popularity = st.sidebar.radio("Number of Movie Ratings", ('Small Market', 'Main Stream', 'Popular'))
gross = st.sidebar.pills("Revenue status:", options=['Profitable', 'Unprofitable'])
genre = st.sidebar.multiselect("Select your favorite genre(s)", ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
       'Drama', 'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror',
       'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Sport',
       'Thriller', 'War', 'Western'])


my_dict = {
    "Movie Length": length,
    "Movie Era": movie_era,
    "Popularity": popularity,
    'Gross': gross,
    "Genre": genre
}

df = pd.DataFrame.from_dict([my_dict],)


st.header("Your movie settings:")
st.table(df)

# columns= ['age',
#  'hp_kW',
#  'km',
#  'Gearing_Type_Automatic',
#  'Gearing_Type_Manual',
#  'Gearing_Type_Semi-automatic',
#  'make_model_Audi A1',
#  'make_model_Audi A2',
#  'make_model_Audi A3',
#  'make_model_Opel Astra',
#  'make_model_Opel Corsa',
#  'make_model_Opel Insignia',
#  'make_model_Renault Clio',
#  'make_model_Renault Duster',
#  'make_model_Renault Espace']


# df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)

# st.subheader("Press predict if configuration is okay")

# if st.button("Predict"):
#     prediction = model.predict(df)
#     st.success("The estimated price of your car is €{}. ".format(int(prediction[0])))