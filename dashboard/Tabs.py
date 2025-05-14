import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv("/Users/jvpurushotham/Desktop/J V Purushotham/Final_data/Tabs.csv")

df = load_data()

st.title("📱 Tablet Finder Tool")
st.markdown("Use the filters in the sidebar to find your ideal tablet.")

# Sidebar filters
st.sidebar.header("Filter Options")

# Brand
brands = df["Brand"].unique()
selected_brand = st.sidebar.multiselect("Brand", brands)

# Model
models = df["Model"].unique()
selected_model = st.sidebar.multiselect("Model", models)

# RAM
selected_ram = st.sidebar.slider("RAM (GB)", int(df["RAM_GB"].min()), int(df["RAM_GB"].max()), (int(df["RAM_GB"].min()), int(df["RAM_GB"].max())))

# Storage
selected_storage = st.sidebar.slider("Storage (GB)", int(df["Storage_GB"].min()), int(df["Storage_GB"].max()), (int(df["Storage_GB"].min()), int(df["Storage_GB"].max())))

# Screen Size
selected_screen = st.sidebar.slider("Screen Size (inches)", float(df["Screen_Size_Inches"].min()), float(df["Screen_Size_Inches"].max()), (float(df["Screen_Size_Inches"].min()), float(df["Screen_Size_Inches"].max())))

# Rating Group
rating_group = st.sidebar.multiselect("Rating Group", df["Rating_Group"].unique())

# Price
selected_price = st.sidebar.slider("Price (₹)", int(df["Price"].min()), int(df["Price"].max()), (int(df["Price"].min()), int(df["Price"].max())))

# Sentiment
selected_sentiment = st.sidebar.multiselect("Review Sentiment", df["Review_Sentiment"].unique())

# WiFi Type
wifi_types = df["WiFi_Type"].unique()
selected_wifi = st.sidebar.multiselect("WiFi Type", wifi_types)

# Colour
colours = df["Colour"].unique()
selected_colour = st.sidebar.multiselect("Colour", colours)

# Applying filters
filtered_df = df[
    (df["Brand"].isin(selected_brand) if selected_brand else True) &
    (df["Model"].isin(selected_model) if selected_model else True) &
    (df["RAM_GB"].between(selected_ram[0], selected_ram[1])) &
    (df["Storage_GB"].between(selected_storage[0], selected_storage[1])) &
    (df["Screen_Size_Inches"].between(selected_screen[0], selected_screen[1])) &
    (df["Rating_Group"].isin(rating_group) if rating_group else True) &
    (df["Price"].between(selected_price[0], selected_price[1])) &
    (df["Review_Sentiment"].isin(selected_sentiment) if selected_sentiment else True) &
    (df["WiFi_Type"].isin(selected_wifi) if selected_wifi else True) &
    (df["Colour"].isin(selected_colour) if selected_colour else True)
]

# Displaying the results
st.subheader(f"Filtered Results: {len(filtered_df)} tablet(s) found")
st.dataframe(filtered_df[[
    "Product_Title", "Brand", "Model", "RAM_GB", "Storage_GB",
    "Screen_Size_Inches", "WiFi_Type", "Colour", "Price", "Overall_Rating", "Review_Sentiment", "Rating_Group", "Product_URL"
]])

# Adding the download button after filtering the data
st.download_button(
    label="Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_tablets.csv",
    mime="text/csv"
)


