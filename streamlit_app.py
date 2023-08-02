import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('My family new healthy dinner')

streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale , Spinachk & Rocket and Smoothie')
streamlit.text(' 🐔 Hard bolied Free-Range egg')
streamlit.text(' 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list=my_fruit_list.set_index('Fruit')

#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice=streamlit.text_input('what fruit would you like information about ?','Kivi')
streamlit.write('The user entered ',fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
#my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
#streamlit.text("The fruit load list contains:")
streamlit.header("The fruit load list contains:")
#streamlit.text(my_data_row)
streamlit.dataframe(my_data_rows)

streamlit.header("What fruit would like to add!")
add_fruit=streamlit.text_input('what fruit would you like information about ?','jackfruit')
streamlit.write('The user entered ',add_fruit)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +add_fruit)






