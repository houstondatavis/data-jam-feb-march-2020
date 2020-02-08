import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title('Climate Data Exploration')

st.write("A subtitle, once I know what I'm doing")

@st.cache
def load_data():
    us_cities = pd.read_csv("us_cities.csv") 
    return us_cities


us_cities = load_data()


example = us_cities.head()


number_rows = 100000



st.write("The first "+str(number_rows)+" rows of the US portion of the all cities CSV file loaded as a pandas dataframe")

example

us_cities_test = us_cities

city= st.sidebar.selectbox(
    'Which number do you like best?',
     us_cities_test['City'].unique())

city2 = "Houston"

us_cities2 = pd.read_csv("us_cities.csv") 

us_cities_test = us_cities2[us_cities2['City'] == city]
us_cities_test2 = us_cities2[us_cities2['City'] == "Houston"]

us_cities_test

st.write("The first X rows of the dataframe")

us_cities_test_ColSubset = us_cities_test[["AverageTemperature","AverageTemperatureUncertainty","dt"]]
us_cities_test_ColSubset2 = us_cities_test2[["AverageTemperature","AverageTemperatureUncertainty","dt"]]


us_cities_test_ColSubset.set_index("dt",inplace=True)
us_cities_test_ColSubset2.set_index("dt",inplace=True)



# data[data['Country'] == "United States"]

st.write(city)
#us_cities_test_ColSubset
st.line_chart(us_cities_test_ColSubset,width=1000, height=400,use_container_width=False)

st.write("Houston")
st.line_chart(us_cities_test_ColSubset2,width=1000, height=400,use_container_width=False)
#us_cities_test_ColSubset2

st.write("Example of df used in Charts")
us_cities_test_ColSubset

# st.write("Exp Merge")
# merge_exp = pd.merge([us_cities_test_ColSubset,us_cities_test_ColSubset2],right="City")
# st.line_chart(merge_exp,width=1000, height=400,use_container_width=False)


# us_cities_test
# st.write(type(us_cities_test))


us_cities_test = us_cities_test.rename(index=str,columns = {'Latitude':'latitude'}) 
us_cities_test = us_cities_test.rename(index=str,columns = {'Longitude':'longitude'}) 

us_cities_test




def fixCoordinates2(df,latitude_str,longitude_str):
    df[latitude_str] = df[latitude_str].str.replace("N","").astype(float)
    df[longitude_str] = df[longitude_str].str.replace("W","")
    df[longitude_str] = '-' + df[longitude_str].astype(str)
    df[longitude_str] = df[longitude_str].astype(float)
    return df

us_cities_test_fixed2 = fixCoordinates2(us_cities_test,"latitude","longitude")

us_cities_test_fixed2_subset = us_cities_test_fixed2[["AverageTemperature","latitude","longitude"]]

us_cities_test_fixed2_subset = us_cities_test_fixed2_subset[0:500]

us_cities_test_fixed2_subset


# st.map(us_cities_test_fixed2_subset)

# st.deck_gl_chart(
#     viewport={
#          'latitude': min(us_cities_test_fixed2_subset['latitude']),
#          'longitude': min(us_cities_test_fixed2_subset['longitude']),
#          'zoom': 11,
#          'pitch': 50,
#      },
#      layers=[{
#          'type': 'ScatterplotLayer',
#          'data': us_cities_test_fixed2_subset,
#          'getRadius':10,
#          'getFillColor':[255,25,0]
#      }])


# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['latitude', 'longitude'])

# map_data

# st.map(map_data)
