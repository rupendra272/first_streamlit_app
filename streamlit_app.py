import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

   #def get_fruityvice_data(this_fruit_choice):
   #fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +this_fruit_choice)
   #fruityvice_normalized=pandas.json_normalized(fruityvice_response.json())
   #return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice=streamlit.text_input('what fruit would you like information about ?','Kiwi')
streamlit.write('The user entered ',fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
#try:
  # fruit_choice=streamlit.text_input('what fruit would you like information about ?')
  # if not fruit_choice:
     #  streamlit.error(" Please select the fruit to get information ")
  # else:
      #  back_from_function=get_fruityvice_data(fruit_choice)
      #  streamlit.dataframe(back_from_function)


streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
   with my_cnx.cursor() as my_cur:
      my_cur.execute("SELECT * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
      return my_cur.fetchall()

if streamlit.button('Get fruit load list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)


