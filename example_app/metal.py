import streamlit as st
import pandas as pd
import numpy as np

from st_pages import add_page_title

add_page_title()

st.write("In 2018, 19.2 million tons of ferrous metals (iron and steel) were generated.\
          EPA estimates that the recycling rate of ferrous metals from durable goods was 27.8 percent.\
          The same year, 2.5 million tons of nonferrous metals (not containing iron) were generated. \
         The recycling rate for nonferrous metals was approximately 68 percent.")

st.subheader("How do I recycle metal? ")
st.write("There are different programs and options for metal recycling depending on your locality.\
          Check to find out what is available in your area. ")

st.header("Aluminum")
st.write("In 2018, 3.9 million tons of aluminum municipal solid waste was generated.\
          The total recycling rate for aluminum items was 34.9 percent. Both aluminum cans and foil can be recycled. ")
st.subheader("Should aluminum cans be crushed before recycling them?")
st.write("No, generally, aluminum cans should not be crushed before they are recycled.\
          For areas with single-stream recycling, \
         crushed cans are harder to detect when being sorted at recycling facilities. \
         If you live in an area with multi-stream recycling, crushing cans is not an issue.")
st.subheader("Can I recycle aluminum foil?")
st.write("Yes, aluminum foil can be recycled. Make sure to remove any food residue before recycling.")

st.header("Local recycling")
df = pd.DataFrame(np.array([[56.83195418409918, 60.6475336191012],
                            [56.836824529445266, 60.69406200132057], 
                            [56.83334795229576, 60.69680173978495]]),
    columns=['lat', 'lon'])
st.map(df)

st.subheader("Recycling point")
st.write("Vishnevaya Street, 22B")
st.write("+7 (963) 853-12-66")

st.subheader("Recycling point")
st.write("40 Years Komsomol Street, 4")
st.write("+7 (922) 206-84-28")

st.subheader("Vtor-Element LLC")
st.write("Betonshchikov Street, 5")
st.write("+7 (958) 137-87-48")
