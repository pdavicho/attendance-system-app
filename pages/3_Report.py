import streamlit as st
from Home import face_rec

st.set_page_config(page_title='Reporting', layout='wide')
st.subheader('Reporting')

#Retrive logs and show in Report
#Extract data from Redis List
name = 'attendance:logs'
def load_logs(name, end=-1):
    logs_list = face_rec.r.lrange(name, start=0, end=end) #Extract all data from the redis database
    return logs_list

#Tabs to show the info
tab1, tab2 = st.tabs(['Register Data', 'Logs'])

with tab1:
    if st.button('Refresh Data'):
    #Retrive the data from Redis Database
        with st.spinner('Retriving Data from redis DB...'):
            redis_face_db = face_rec.retrive_data(name='academy:register')
            st.dataframe(redis_face_db[['Name', 'Role']])


with tab2:
    if st.button('Refresh Logs'):
        st.write(load_logs(name=name))
    