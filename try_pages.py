import io
import streamlit as st
from PIL import Image
import numpy as np

from st_pages import Page, add_page_title, show_pages

st.header("Responsible person's page :writing_hand:")

st.subheader("More and more people recycle everyday.")
st.write("This helps to reduce the need for landfill and more costly forms of disposal.\
          Recycling also reduces the need for extracting (mining, quarrying and logging),\
          refining and processing raw materials all of which create substantial air and water pollution.")
st.write("**Here you can choose 🚀 to try out an app \
         that offers ideas for reusing an old thing\
          or you can read information about ways to dispose of different types of waste**")

show_pages(
    [
        Page("try_pages.py", "Home", ":house:"),
        Page("example_app/streamlit_app.py", "Give it a chance!", "🚀"),
        Page("example_app/easy_disposal.py", "Proper disposal is easy!", "🌞"),
        Page("example_app/glass.py", "Glass", "🥛"),
        Page("example_app/metal.py", "Metal", "📎"),
        Page("example_app/paper.py", "Paper", "📰"),
        Page("example_app/plastic.py", "Plastic", "♻️"),        
    ]
)

st.image("pictures/home_page.jpg")
