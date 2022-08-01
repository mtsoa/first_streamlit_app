import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('My parents new healthy diner')
streamlit.header('👌Breakfast favourites')
streamlit.text('🌚Blueberry oatmeal & omega 3')
streamlit.text('🌾Kale, spinach & rocket smoothie')
streamlit.text('🥚Hardboiled free range eggs')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")


#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
# streamlit.text(fruityvice_response.json())
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please say something.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
#streamlit.stop()

streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
    return my_cur.fetchall()
  
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)
#fruit_choice = streamlit.text_input('What fruit would you like to add?','jackfruit')
#streamlit.write('Thanks for adding ', fruit_choice)
#streamlit.write('Thanks for adding ', add_my_fruit)
#my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
