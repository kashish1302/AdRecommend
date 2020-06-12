import streamlit as st
import pandas as pd
import re
import numpy as np
import umap
import matplotlib.pyplot as plt
import seaborn as sns


def execute(target_movie):
    cust_tags_list= pd.read_csv('Updating/Customer_tags.csv')
    mv_tags_list= pd.read_csv('Updating/Table_advert1.csv')
    target_tag_list = cust_tags_list[cust_tags_list.Customer_ID == target_movie].tag_list.values[0]
    mv_tags_list_sim = mv_tags_list[['Title','tag_list']]
    mv_tags_list_sim['jaccard_sim'] = mv_tags_list_sim.tag_list.map(lambda x: len(set(x).intersection(set(target_tag_list))) /len(set(x).union(set(target_tag_list))))
    text = ','.join(mv_tags_list_sim.sort_values(by = 'jaccard_sim', ascending = False).head(25)['tag_list'].values)
    bool_series = pd.notnull(mv_tags_list_sim["Title"])
    final_list=mv_tags_list_sim.sort_values(by = 'jaccard_sim', ascending = False).head(10)[bool_series]
    st.dataframe(final_list.Title)

st.write("""
# Ad Recommendation
Type in your name*
""")
target_movie = st.text_input('Input your sentence here:')
execute(target_movie)




