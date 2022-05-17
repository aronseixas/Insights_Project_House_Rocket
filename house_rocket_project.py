import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import folium

from datetime import datetime
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

st.set_page_config(layout='wide')


# Functions
@st.cache(allow_output_mutation=True)
def get_data(data_path):
    df_load_data = pd.read_csv(data_path)
    return df_load_data


def set_feature(data):
    # Add new features
    data['price_ft2'] = data['price'] / data['sqft_lot']
    return data


def introduction():
    # =====================================================
    # Introduction
    # =====================================================

    st.title('Insights Project - House Rocket')
    st.markdown('''---''')
    return None


def menu_configuration():
    # =====================================================
    # Menu Configuration
    # =====================================================

    # Sidebar configuration:
    st.sidebar.title('Navigation')
    navigation = st.sidebar.radio('Choose an option',
                                  ['Welcome', 'Data Overview', 'Map Recommendation', 'Commercial Attributes',
                                   'Houses Attributes'])
    return navigation


def welcome():
    st.markdown("Welcome to House Rocket companny.")
    st.markdown(
        "House Rocket is a fictitious company, belonging to the real estate industry, it is a company specialized "
        "in the purchase and sale of real estate, its profit consists of buying real estate for a price lower "
        "than the market average, and later selling it for a higher value. than the bought.")
    st.markdown(
        "In the current scenario, the company aims to use data science to find better business opportunities and "
        "maximize profits.")

    st.title('Business Issues')
    st.markdown('House Rocket aims to solve the following problems: ')
    st.markdown('1-  What properties should House Rocket buy and at what price?')
    st.markdown('2-  Once the house is purchased, what is the best price to sell it?')

    st.title('About the Data')

    data_size = data_recommendation.shape[0]
    data_feature = data.shape[1]
    zip_num = len(data_recommendation['zipcode'].unique())
    num_years = data_recommendation['date'].dt.year.unique()

    ca, cb, cc = st.columns(3)
    ca.metric(label='Number of houses', value=data_size)
    cb.metric(label='Number of Features', value=data_feature)
    cc.metric(label='Number of Zip Codes', value=zip_num)
    st.metric(label="Period", value=f'From May {num_years[0]} to May {num_years[-1]}')

    return None


def data_overview():
    # =====================================================
    # Data Overview
    # =====================================================

    st.title('Data Overview')
    st.sidebar.markdown('''---''')
    st.sidebar.title('Data Overview')
    f_attributes = st.sidebar.multiselect('Enter columns', data.columns.sort_values())
    f_zipcode = st.sidebar.multiselect('Enter zipcode', data['zipcode'].sort_values().unique())
    st.sidebar.markdown('''---''')

    st.markdown(
        'This section allows displaying all data and features used in the project. In addition, average information was summarized for each zip code')

    if (f_zipcode != []) & (f_attributes != []):
        data_aux1 = data.loc[data['zipcode'].isin(f_zipcode), f_attributes]
    elif (f_zipcode != []) & (f_attributes == []):
        data_aux1 = data.loc[data['zipcode'].isin(f_zipcode), :]
    elif (f_zipcode == []) & (f_attributes != []):
        data_aux1 = data.loc[:, f_attributes]
    else:
        data_aux1 = data.copy()
    all_data = st.checkbox('Show all dataset')
    if all_data:
        st.dataframe(data_aux1)
    else:
        st.dataframe(data_aux1.head())

    if (f_zipcode != []) & (f_attributes == []):
        # =================
        # Average metrics
        # =================

        # Grouping the data
        df1 = data_aux1[['id', 'zipcode']].groupby('zipcode').count().reset_index()
        df2 = data_aux1[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
        df3 = data_aux1[['sqft_living', 'zipcode']].groupby('zipcode').mean().reset_index()
        df4 = data_aux1[['price_ft2', 'zipcode']].groupby('zipcode').mean().reset_index()

        # Merge
        m1 = pd.merge(df1, df2, on='zipcode', how='inner')
        m2 = pd.merge(m1, df3, on='zipcode', how='inner')
        df = pd.merge(m2, df4, on='zipcode', how='inner')
        df.columns = ['ZIPCODE', 'TOTAL HOUSES', 'PRICE', 'SQRT LIVING', 'PRICE/ft2']

        st.title('Average Prices')
        st.dataframe(df)

        # =======================
        # Descriptive Statistics
        # =======================

        num_attributes = data_aux1.select_dtypes(include=['int64', 'float64'])
        mean = pd.DataFrame(num_attributes.apply(np.mean))
        median = pd.DataFrame(num_attributes.apply(np.median))
        std = pd.DataFrame(num_attributes.apply(np.std))
        max_ = pd.DataFrame(num_attributes.apply(np.max))
        min_ = pd.DataFrame(num_attributes.apply(np.min))
        df5 = pd.concat([max_, min_, mean, median, std], axis=1).reset_index()
        df5.columns = ['attributes', 'max', 'min', 'mean', 'median', 'std']

        st.title('Descriptive Statistics')
        st.dataframe(df5)

    else:

        # =================
        # Average metrics
        # =================

        # Grouping the data
        df1 = data[['id', 'zipcode']].groupby('zipcode').count().reset_index()
        df2 = data[['price', 'zipcode']].groupby('zipcode').mean().reset_index()
        df3 = data[['sqft_living', 'zipcode']].groupby('zipcode').mean().reset_index()
        df4 = data[['price_ft2', 'zipcode']].groupby('zipcode').mean().reset_index()

        # Merge
        m1 = pd.merge(df1, df2, on='zipcode', how='inner')
        m2 = pd.merge(m1, df3, on='zipcode', how='inner')
        df = pd.merge(m2, df4, on='zipcode', how='inner')
        df.columns = ['ZIPCODE', 'TOTAL HOUSES', 'PRICE', 'SQRT LIVING', 'PRICE/ft2']

        st.title('Average Prices')
        st.dataframe(df)

        # =======================
        # Descriptive Statistics
        # =======================

        num_attributes = data.select_dtypes(include=['int64', 'float64'])
        mean = pd.DataFrame(num_attributes.apply(np.mean))
        median = pd.DataFrame(num_attributes.apply(np.median))
        std = pd.DataFrame(num_attributes.apply(np.std))
        max_ = pd.DataFrame(num_attributes.apply(np.max))
        min_ = pd.DataFrame(num_attributes.apply(np.min))
        df5 = pd.concat([max_, min_, mean, median, std], axis=1).reset_index()
        df5.columns = ['attributes', 'max', 'min', 'mean', 'median', 'std']

        st.title('Descriptive Statistics')
        st.dataframe(df5)
    return None


def portfolio_maps():
    # =======================
    # Portfolio Maps
    # =======================

    st.title('Portfolio Map')
    st.markdown(
        'The map recommendation section displays the location of all properties present in the dataset. The properties are grouped into two groups according to the results obtained in the project.')
    st.markdown('In green the houses suggested for purchase and in red those not suggested.')

    # Base Map - Folium
    # Creating map

    density_map = folium.Map(location=[data_recommendation['lat'].mean(), data_recommendation['long'].mean()],
                             default_zoon_start=15)

    data_recommendation_dont_buy = data_recommendation.loc[data_recommendation['Recommendation'] == 'Dont_Buy']
    data_recommendation_buy = data_recommendation.loc[data_recommendation['Recommendation'] == 'Buy']

    marker_cluster = MarkerCluster().add_to(density_map)

    recommendation_dont_buy = st.checkbox('Show the recommendation for not buying')
    recommendation_buy = st.checkbox('Show the recommendation for buying')

    if (recommendation_dont_buy is True) and (recommendation_buy is False):
        for name, row in data_recommendation_dont_buy.iterrows():
            folium.Marker([row['lat'], row['long']], icon=folium.Icon(color="red"),
                          popup=f"Sold R${row['price']} on: {row['date']}. Features: {row['sqft_living']} sqft, "
                                f"{row['bedrooms']} bedrooms, {row['bathrooms']} bathrooms, year built: {row['yr_built']}").add_to(
                marker_cluster)
        folium_static(density_map)

    elif (recommendation_dont_buy is False) and (recommendation_buy is True):
        for name, row in data_recommendation_buy.iterrows():
            folium.Marker([row['lat'], row['long']], icon=folium.Icon(color="green"),
                          popup=f"Sold R${row['price']} on: {row['date']}. Features: {row['sqft_living']} sqft, "
                                f"{row['bedrooms']} bedrooms, {row['bathrooms']} bathrooms, year built: {row['yr_built']}").add_to(
                marker_cluster)
        folium_static(density_map)

    elif (recommendation_dont_buy is True) and (recommendation_buy is True):
        for name, row in data_recommendation_dont_buy.iterrows():
            folium.Marker([row['lat'], row['long']], icon=folium.Icon(color="red"),
                          popup=f"Sold R${row['price']} on: {row['date']}. Features: {row['sqft_living']} sqft, "
                                f"{row['bedrooms']} bedrooms, {row['bathrooms']} bathrooms, year built: {row['yr_built']}").add_to(
                marker_cluster)

        for name, row in data_recommendation_buy.iterrows():
            folium.Marker([row['lat'], row['long']], icon=folium.Icon(color="green"),
                          popup=f"Sold R${row['price']} on: {row['date']}. Features: {row['sqft_living']} sqft, "
                                f"{row['bedrooms']} bedrooms, {row['bathrooms']} bathrooms, year built: {row['yr_built']}").add_to(
                marker_cluster)
        folium_static(density_map)

    else:
        folium_static(density_map)
    return None


def commercial_attributes(data):
    # =======================
    # Commercial Attributes
    # =======================

    st.title('Commercial Attributes')
    st.sidebar.markdown('''---''')
    st.sidebar.title('Commercial Attributes')

    # ------- Average Price per Year -------
    # Graph Title

    st.header('Average price per year built')
    st.markdown('Display average property price based on building year')

    # setup filters
    min_year_built = int(data['yr_built'].min())
    max_year_built = int(data['yr_built'].max())
    st.sidebar.subheader('Select Max Year Built')
    f_year_built = st.sidebar.slider('Year Built', min_year_built, max_year_built, max_year_built)

    # Filtering
    data_commercial = data.loc[data['yr_built'] < f_year_built]
    df_commercial_year = data_commercial[['yr_built', 'price']].groupby('yr_built').mean().reset_index()

    # Ploting the figure
    fig = px.line(data_frame=df_commercial_year, x='yr_built', y='price')
    st.plotly_chart(fig, use_container_width=True)

    # -------- Average Price per day --------
    # Graph Title
    st.header('Average Price per day')
    st.markdown('Display average property price per day')
    st.sidebar.subheader('Select Max Date')

    # load data
    data = get_data(path)
    data['date'] = pd.to_datetime(data['date']).dt.strftime('%Y-%m-%d')

    # setup filters
    min_date = datetime.strptime(data['date'].min(), '%Y-%m-%d')
    max_date = datetime.strptime(data['date'].max(), '%Y-%m-%d')
    f_date = st.sidebar.slider('Date', min_date, max_date, value=max_date)

    # Changing the date attribute
    data['date'] = pd.to_datetime(data['date'])

    # Filtering
    data = data[data['date'] < f_date]
    df_commercial_day = data[['date', 'price']].groupby('date').mean().reset_index()

    # Ploting the figure
    fig = px.line(data_frame=df_commercial_day, x='date', y='price')
    st.plotly_chart(fig, use_container_width=True)

    # -------- Histogram --------
    # Graph Title
    st.header('Price Distribution')

    # Reload data
    data = get_data(path)

    # setup filters
    min_price = int(data['price'].min())
    max_price = int(data['price'].max())
    avg_price = int(data['price'].mean())
    f_price = st.sidebar.slider('Price', min_price, max_price, avg_price)
    st.sidebar.markdown('''---''')

    # Filtering
    df_price = data.loc[data['price'] < f_price]

    # Ploting the figure
    fig = px.histogram(df_price, x='price', nbins=50)
    st.plotly_chart(fig, use_container_width=True)
    return None


def houses_attributes():
    # ==============================================================
    # Properties Distribution by Categories
    # ==============================================================
    # Section Title
    st.sidebar.markdown('''---''')
    st.sidebar.title('Attributes Options')
    st.title('Houses Attributes')

    # Creating the columns
    c3, c4 = st.columns(2)
    c5, c6 = st.columns(2)

    # set filters
    f_bedrooms = st.sidebar.selectbox('Max number of bedrooms', data['bedrooms'].sort_values().unique())
    f_bathrooms = st.sidebar.selectbox('Max number of bath', data['bathrooms'].sort_values().unique())
    f_floors = st.sidebar.selectbox('Max number of floors', data['floors'].sort_values().unique())
    f_waterview = st.sidebar.checkbox('Only House with Water View')

    # Houses per bedrooms
    c3.header('Houses per bedrooms')
    df = data[data['bedrooms'] < f_bedrooms]
    fig_bedrooms = px.histogram(df, x='bedrooms', nbins=19)
    c3.plotly_chart(fig_bedrooms, use_containder_width=True)

    # Houses per bathrooms
    c4.header('Houses per bathrooms')
    df = data[data['bathrooms'] < f_bathrooms]
    fig = px.histogram(df, x='bathrooms', nbins=10)
    c4.plotly_chart(fig, use_containder_width=True)

    # Houses per floors
    c5.header('Houses per floors')
    df = data[data['floors'] < f_floors]
    fig = px.histogram(df, x='floors', nbins=19)
    c5.plotly_chart(fig, use_containder_width=True)

    # Houses per water view
    if f_waterview:
        df = data[data['waterfront'] == 1]
    else:
        df = data.copy()
    fig = px.histogram(df, x='waterfront', nbins=10)
    c6.header('Houses per water view')
    c6.plotly_chart(fig, use_containder_width=True)
    st.sidebar.markdown('''---''')

    return None


if __name__ == "__main__":
    # Load Data
    path = 'kc_house_data.csv'
    data = get_data(path)

    path_recommendation = 'houses_recommendations.csv'
    data_recommendation = get_data(path_recommendation)
    data_recommendation['date'] = pd.to_datetime(data_recommendation['date'])

    # Add new features
    data = set_feature(data)
    introduction()
    navigation = menu_configuration()
    if navigation == 'Welcome':
        welcome()
    elif navigation == 'Data Overview':
        data_overview()
    elif navigation == 'Map Recommendation':
        portfolio_maps()
    elif navigation == 'Commercial Attributes':
        commercial_attributes(data)
    elif navigation == 'Houses Attributes':
        houses_attributes()
