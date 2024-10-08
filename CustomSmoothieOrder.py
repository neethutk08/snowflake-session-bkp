# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col, when_matched
# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie!:cup_with_straw:")
st.write(
    """Choose the fruit you want in your custom Smoothie!
    """
)

name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your Smoothie will be :',name_on_order)
session = get_active_session()
my_dataframe =  session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
ingradients_list = st.multiselect(
    'Choose upto 5 ingredients:'
    ,my_dataframe
    ,max_selections=5
)
if ingradients_list:
    ingradients_string = ''
    for fruit_chosen in ingradients_list:
        ingradients_string += fruit_chosen + ''

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order) 
    values ('""" + ingradients_string + """','""" + name_on_order + """') """
    st.write(my_insert_stmt)
    st.stop()
    
