import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("/Users/jvpurushotham/Desktop/J V Purushotham/Final_data/Laptops.csv")
    return df

df = load_data()

st.title("💻 Laptop Query Tool")

# Sidebar filters
st.sidebar.header("🔍 Filter Options")

# Brand filter
brands = st.sidebar.multiselect("Select Brand(s):", options=df['Brand'].unique(), default=df['Brand'].unique())

# RAM filter
min_ram = int(df['RAM_GB'].min())
max_ram = int(df['RAM_GB'].max())
ram_range = st.sidebar.slider("Select RAM (GB):", min_value=min_ram, max_value=max_ram, value=(min_ram, max_ram))

# Storage filter
min_storage = int(df['Storage_GB'].min())
max_storage = int(df['Storage_GB'].max())
storage_range = st.sidebar.slider("Select Storage (GB):", min_value=min_storage, max_value=max_storage, value=(min_storage, max_storage))

# Price range
min_price = int(df['Price'].min())
max_price = int(df['Price'].max())
price_range = st.sidebar.slider("Select Price Range (₹):", min_value=min_price, max_value=max_price, value=(min_price, max_price))

# OS filter
os_options = st.sidebar.multiselect("Select OS Version(s):", options=df['OS_Version'].dropna().unique(), default=df['OS_Version'].dropna().unique())

# Sentiment filter
sentiment_options = st.sidebar.multiselect("Select Review Sentiment(s):", options=df['Review_Sentiment'].dropna().unique(), default=df['Review_Sentiment'].dropna().unique())

# Rating Level
rating_levels = st.sidebar.multiselect("Select Rating Level(s):", options=df['Rating_Level'].unique(), default=df['Rating_Level'].unique())

# Filter based on selections
filtered_df = df[
    (df['Brand'].isin(brands)) &
    (df['RAM_GB'].between(*ram_range)) &
    (df['Storage_GB'].between(*storage_range)) &
    (df['Price'].between(*price_range)) &
    (df['OS_Version'].isin(os_options)) &
    (df['Review_Sentiment'].isin(sentiment_options)) &
    (df['Rating_Level'].isin(rating_levels))
]

st.subheader("📋 Filtered Results")
st.write(f"Showing {len(filtered_df)} result(s):")
st.dataframe(filtered_df[['Product_Title', 'Brand', 'RAM_GB', 'Storage_GB', 'Price', 'Overall_Rating', 'Review_Sentiment', 'Review_Length', 'Price_Bucket', 'Product_URL']])

# Adding a download button to download the results which are filtered
st.download_button(
    label="Download Filtered Results as CSV",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name='filtered_products.csv',
    mime='text/csv'
)


