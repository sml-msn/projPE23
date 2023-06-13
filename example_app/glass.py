import streamlit as st
import pandas as pd
import numpy as np

from st_pages import add_page_title

add_page_title()
st.subheader("Fire :fire: + sand :hourglass_flowing_sand:")

st.write("Glass, especially glass food and beverage containers,\
          can be recycled over and over again. \
         Making new glass from recycled glass is typically cheaper than using raw materials. ")

st.subheader("Can I recycle different glass colors/types together?")
st.write("Most curbside recycling programs \
         accept different glass colors and \
         types mixed together and then sort the glass at the recovery facility.")
st.subheader("Can I recycle broken glass?")
st.write("No, broken glass should not go into the recycling bin.\
          Glass shards can harm workers and damage equipment.  ")
st.subheader("Can I leave my metal bottle cap on my glass bottle when I recycle?")
st.write("No, metal bottle caps should be recycled separately from the glass bottles.")

st.header("Local recycling")
df = pd.DataFrame(np.array([[56.83908653272441, 60.664743161437244],
                            [56.83864065320008, 60.64765229697966],
                            [56.83217829989505, 60.69366639157996]]),
                  columns=['lat', 'lon'])
st.map(df)

st.subheader("StekloVtorEkb")
st.write("Studentskaya Street, 49 Box No. 13")
st.write("+7 (922) 181-30-81")

st.subheader("Recycling point")
st.write("Gagarin Street, 47")
st.write("+7 (950) 190-38-56")

st.subheader("Recycling point")
st.write("40 Years Komsomol Street, 12")
st.write("+7 (908) 636-43-17")
