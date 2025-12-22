import streamlit as st
import pickle
import pandas as pd

# Settings and Title
st.set_page_config(layout="wide")
html_temp = """
<div style="background-color:blue;padding:5px">
<h1 style="color:white;text-align:center;">Movie Recommendation App</h1>
</div>"""
st.markdown(html_temp, unsafe_allow_html=True)

# Sidebar
st.sidebar.title('Movie Settings')
st.sidebar.divider()
length = st.sidebar.radio("Pick a preferred movie length",('Long', 'Average', 'Short', 'Any'))
movie_era = st.sidebar.radio("Pick a preferred era of film:",('Modern', 'Classic', 'Vintage', 'Any'))
popularity = st.sidebar.radio("Pick a popularity category:", ('Popular', 'Main Stream', 'Niche', 'Any'))
gross = st.sidebar.pills("Revenue status:", options=['1,000,000+', '100,000,000+'], selection_mode='multi', default=['1,000,000+', '100,000,000+'])

# Main Page
st.divider()
i, j, k = st.columns(3)
genre = j.multiselect("Select your favorite genre(s). Maximum of 3.", ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
       'Drama', 'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror',
       'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Sport',
       'Thriller', 'War', 'Western'], max_selections=3)

st.divider()

col1, col2, col3 = st.columns(3)
col1.metric("Length:", length)
col2.metric("Era:", movie_era)
col3.metric("Popularity:", popularity)

st.divider()

colA, colB, colC = st.columns(3)
colB.button("Show Results", type='primary', use_container_width=True)

# my_dict = {
#     "Movie Length": length,
#     "Movie Era": movie_era,
#     "Popularity": popularity,
#     'Gross': gross,
#     "Genre": genre
# }

# df = pd.DataFrame.from_dict([my_dict]))
# st.table(df)

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

# if st.button("Predict"):
#     prediction = model.predict(df)
#     st.success("The estimated price of your car is €{}. ".format(int(prediction[0])))