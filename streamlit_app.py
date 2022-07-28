import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header('👌Breakfast favourites')
streamlit.text('🌚Blueberry oatmeal & omega 3')
streamlit.text('🌾Kale, spinach & rocket smoothie')
streamlit.text('🥚Hardboiled free range eggs')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list_index),['Avocado','Strawberries])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe[fruits_to_show]
