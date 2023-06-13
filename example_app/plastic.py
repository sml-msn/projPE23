import streamlit as st
import pandas as pd
import numpy as np

from st_pages import add_page_title

add_page_title()

st.write("We are producing over 380 million tons of plastic every year,\
          and some reports indicate that up to 50 percent of that is \
         for single-use purposes – utilized for just a few moments, \
         but on the planet for at least several hundred years.\
          It's estimated that more than 10 million tons of plastic is dumped into our oceans every year.")

st.subheader("Can I recycle plastic bags, wraps and films?")
st.write("These items are recyclable, but they cannot go in your household bin. \
         Retail and grocery stores often accept these materials for recycling. \
         If necessary, be sure to cut off the sealable zippers from sandwich bags before recycling them.")

st.subheader("Can plastic bottles and caps be recycled?")
st.write("Yes, typically the caps and labels can be left on the bottles as well.")
st.subheader("Can polystyrene foam (styrofoam) be recycled?")
st.write("Very few localities accept styrofoam in curbside recycling.")
st.subheader("Can plastic containers, cups and utensils be recycled?")
st.write("It depends on what types of plastic the containers and\
          cups are made of and whether your local program accepts them.\
          Items with food debris cannot be recycled. \
         Plastic utensils also cannot be recycled. ")
st.subheader("Can I recycle compostable or bio-based plastics?")
st.write("_Compostable Plastic_: No. Compostable plastics are not intended for recycling \
         and can contaminate and disrupt the recycling stream if mixed with non-compostable plastics. \
         If your community does not have a composting recycling\
          pick-up program that accepts compostable plastic,\
          contact your garbage/recycling company or \
         local government to find out if there are any drop-off locations for your compostable plastic items.")
st.write("_Biobased Plastics_: To determine what waste disposal options\
          are available for a biobased plastic item, \
         it is necessary to read the product's label as to its compostability and recyclability.")
st.header("Local recycling")
df = pd.DataFrame(np.array([[56.83855123705221, 60.64731955945884],
                            [56.83472414413396, 60.623979144317644], 
                            [56.846843692461, 60.615760582200394]]),
    columns=['lat', 'lon'])
st.map(df)

st.write("Gagarina Street, 47")
st.write("+7 (950) 190-38-56")

st.subheader("VTORSYSTEM")
st.write("Lunacharsky Street, 171")
st.write("+7 (343) 261-32-01")

st.subheader("IP Snegirev A.V.")
st.write("Mamina-Sibiryak Street, 85")
st.write("+7 (904) 983-93-31")

st.subheader("N.B. What do the symbols mean on the bottom of plastic bottles and containers?")
st.write("These symbols were created to identify the type of plastic used to make the container.\
          This can help you determine whether the item is recyclable by your local program.\
          The resin number is contained in a triangle that looks very similar to the recycling symbol.\
          However, this symbol does not necessarily mean it can be collected for recycling in your community.")
st.image("pictures/codes.jpg")