import streamlit as st

from st_pages import add_page_title

add_page_title()

st.subheader("Rule No.1 Hazardous waste must be handed over")
col1, col2, col3 = st.columns(3)

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("pictures/Рисунок1.jpg", width=100)
    with col2:
        st.image("pictures/Рисунок2.png", width=75)
        st.image("pictures/Рисунок3.jpg", width=75)
    with col3:
        st.image("pictures/Рисунок4.jpg", width=100)     

with st.container():
    col1_2, col2_2, col3_2 = st.columns(3)
    with col1_2:
       st.write("•	Stores: M video, Eldorado, Leroy Merlin, Lenta.")
    with col2_2:
       st.write("•	CBM of Complex solution of industrial waste problems (Engels St., 16, Alpinist St., 57 A).")
       st.write("•	Industrial Waste Safety Center")
    with col3_2:
       st.write("•	The company «Spetsavtokom».")
       st.write("•	The company LLC «TD Uralneftekhim» (Monterskaya str., 8).")
       st.write("•	ECOPROM LLC (Kosareva str., 91a).")

    
st.subheader("Rule No.2 Do not throw away clothes, shoes, toys, textiles, books")
col4, col5, col6, col7, col8 = st.columns(5)

with col4:
   st.image("pictures/Рисунок5.jpg")
with col5:
   st.image("pictures/Рисунок6.jpg")
with col6:
   st.image("pictures/Рисунок7.png")
with col7:
   st.image("pictures/Рисунок8.jpg")
with col8:
   st.image("pictures/Рисунок9.jpg")

st.write("•	Industrial Charity organization «Aistenok»\
          (Moskovskaya str., 25A).")
st.write("•	The Center for social assistance to families \
         and children «Karavella» (Moskovsky trakt str., 8 km, 8)")
st.write("•	Social project «The Thing of Good» \
         (Tatishcheva str., 90; Sheinkman str., 90; 8 Marta str., 149)")


st.subheader("Rule No.3 Sort the waste and hand it over for recycling")
col9, col10, col11, col12 = st.columns(4)
with col9:
   st.image("pictures/Рисунок10.jpg")
with col10:
   st.image("pictures/Рисунок11.jpg")
with col11:
   st.image("pictures/Рисунок12.jpg")
with col12:
   st.image("pictures/Рисунок13.jpg")

st.write("•	Industrial Charity organization «Aistenok» (Moskovskaya str., 25A).")
st.write("•	The Center for social assistance to families \
         and children «Karavella» (Moskovsky trakt str., 8 km, 8)")
st.write("•	Social project «The Thing of Good» \
         (Tatishcheva str., 90; Sheinkman str., 90; 8 Marta str., 149)")
st.write("•	Charity clothing resale «Blagomarket» (Boris Yeltsin str., 3)")


st.subheader("Rule No.4 Reduce the amount of household garbage")
col13, col14, col15 = st.columns(3)
with col13:
   st.image("pictures/Рисунок14.jpg", width = 150)
with col14:
   st.image("pictures/Рисунок15.jpg", width = 150)
with col15:
   st.image("pictures/Рисунок16.jpg", width = 150)

st.write("•	Bulky waste (furniture, building materials) should be disposed of in a separate container.")
st.write("•	The packaging should be crumpled to reduce the volume.")


st.subheader("Rule No.5 Do not create unnecessary garbage")
col16, col18 = st.columns(2)
with col16:
   st.image("pictures/Рисунок17.jpg", width = 150)

with col18:
   st.image("pictures/Рисунок19.jpg", width = 150)

st.write("•	If you often go shopping, you should buy a reusable bag.")
st.write("•	Do not use disposable tableware.")
st.write("•	If possible, take food and drinks in your own container.")

st.title("Take care of the :green[planet] :earth_africa:!")
