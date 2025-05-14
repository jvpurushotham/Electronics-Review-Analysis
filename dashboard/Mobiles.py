import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv('/Users/jvpurushotham/Desktop/J V Purushotham/Final_data/Mobiles.csv')

df = load_data()

df.fillna({'Model': 'Unknown', 'Colour': 'Unknown', 'Price': 0, 'Storage_GB': 0,
           'Overall_Rating': 0, 'No_of_Ratings': 0, 'No_of_Reviews': 0}, inplace=True)

st.title("📱 Mobile Query Tool - Find Your Best Phone")

st.sidebar.header("🔎 Filter Options")

# Sidebar Filters
# Brand/Model selection
model = st.sidebar.multiselect(
    "Select Model:",
    options=df['Model'].unique()
)

# Color selection
color = st.sidebar.multiselect(
    "Select Colour:",
    options=df['Colour'].unique()
)

# Price Range
min_price, max_price = st.sidebar.slider(
    "Select Price Range (₹):",
    int(df['Price'].min()), int(df['Price'].max()), (int(df['Price'].min()), int(df['Price'].max()))
)

# Storage (GB)
min_storage = st.sidebar.slider(
    "Minimum Storage (GB):",
    int(df['Storage_GB'].min()), int(df['Storage_GB'].max()), int(df['Storage_GB'].min())
)

# Overall Rating
min_rating = st.sidebar.slider(
    "Minimum Overall Rating (out of 5):",
    0.0, 5.0, 0.0, 0.1
)

# No of Ratings
min_no_of_ratings = st.sidebar.slider(
    "Minimum Number of Ratings:",
    int(df['No_of_Ratings'].min()), int(df['No_of_Ratings'].max()), int(df['No_of_Ratings'].min())
)

# No of Reviews
min_no_of_reviews = st.sidebar.slider(
    "Minimum Number of Reviews:",
    int(df['No_of_Reviews'].min()), int(df['No_of_Reviews'].max()), int(df['No_of_Reviews'].min())
)

# Applying Filters
query = df.copy()

if model:
    query = query[query['Model'].isin(model)]

if color:
    query = query[query['Colour'].isin(color)]

query = query[
    (query['Price'] >= min_price) & (query['Price'] <= max_price) &
    (query['Storage_GB'] >= min_storage) &
    (query['Overall_Rating'] >= min_rating) &
    (query['No_of_Ratings'] >= min_no_of_ratings) &
    (query['No_of_Reviews'] >= min_no_of_reviews)
]

# Sorting option
sort_by = st.sidebar.selectbox(
    "Sort By:",
    ['Price (Low to High)', 'Price (High to Low)', 'Overall Rating (High to Low)', 'Storage (High to Low)', 'No. of Ratings (High to Low)']
)

if sort_by == 'Price (Low to High)':
    query = query.sort_values(by='Price')
elif sort_by == 'Price (High to Low)':
    query = query.sort_values(by='Price', ascending=False)
elif sort_by == 'Overall Rating (High to Low)':
    query = query.sort_values(by='Overall_Rating', ascending=False)
elif sort_by == 'Storage (High to Low)':
    query = query.sort_values(by='Storage_GB', ascending=False)
elif sort_by == 'No. of Ratings (High to Low)':
    query = query.sort_values(by='No_of_Ratings', ascending=False)

# Displaying the Results
st.subheader("🔍 Matching Phones")

# Choose number of results to display
top_n = st.slider("How many phones do you want to see?", 5, 100, 10)

if not query.empty:
    st.dataframe(query[['Model', 'Colour', 'Price', 'Storage_GB', 'Overall_Rating', 'No_of_Ratings', 'No_of_Reviews', 'Product_URL']].head(top_n))
else:
    st.warning("No phones match your criteria. Try adjusting the filters.")

# Allowing download
@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df_to_csv(query)

st.download_button(
    label="Download Results as CSV",
    data=csv,
    file_name='filtered_mobiles.csv',
    mime='text/csv',
)


