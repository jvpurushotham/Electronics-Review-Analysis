# Flipkart Product Review Analysis & Dashboard   

An end-to-end data science project for scraping, analyzing, and visualizing  customer reviews for Mobiles, Laptops, and Tablets from Flipkart.  

## Project Structure   

Electronics-Review-Analysis/   
│     
├── Data Analysis/ ├── Laptops_Reviews_Analysis.ipynb  
|                  ├── Mobiless_Reviews_Analysis.ipynb   
|                  └── Tabs_Reviews_Analysis.ipynb    
├── Datasets/ ├── flipkart_reviews_laptops.csv     
|             ├── flipkart_reviews_mobiles.csv      
|             ├── flipkart_reviews_tabs.csv      
|             ├── Laptops_cleaned_Reviews.csv    
|             ├── Mobiless_cleaned_Reviews.csv  
|             ├── Tabs_cleaned_Reviews.csv  
|             ├── Laptops.csv  
|             ├── Mobiles.csv   
|             └── Taabs.csv   
├── Presentation and Document/ ├── Electronic_Review_Analysis.pdf   
|                              └── Review_Analysis_presentation.pptx
├── Web Scrapping/ ├── Laptops_scrapping.ipynb
|                  ├── Mobiles_scrapping.ipynb
|                  └── Tabs_scrapping.ipynb
├── Dashboard/ ├── Laptops.py
|              ├── Mobiles.py
|              └── Tabs.py
└── requirements.txt        

## Data Collection & Preprocessing   

## Source    

Reviews are scraped using requests and BeautifulSoup from Flipkart.      
Reviews are categorized into:     
**📱 Mobiles – 61 products**   
**💻 Laptops – 74 products**  
**📟 Tablets – 53 products**    
## ⚙️ Initial Preprocessing   

Assigned unique Product IDs   
Converted rating and review columns to numeric   
Extracted product-specific details:   
Mobiles: Model, Colour, Storage   
Laptops/Tablets: Brand, Model, Specifications  

## Text Cleaning    
Lowercased text   
Removed punctuation, stopwords, numbers, emojis, and filler text like "READ MORE"   
Stripped extra whitespace   

## Handling Missing Data    
Filled missing ratings with mean values   
Used Product ID mapping to fill missing model and rating info   
Dropped irrelevant columns and reordered    
Replaced remaining nulls with "Unknown"   

## Output    
Cleaned CSVs saved for Mobiles, Laptops, and Tablets  

## Exploratory Data Analysis (EDA)    

**Mobile EDA**
Histograms for rating, reviews, and price  
Price segmentation: Budget / Mid-Range / Premium   
Top 10 most-reviewed smartphones   
Sentiment vs Rating correlation    
LDA Topic Modeling   

**Laptop EDA**  
Price per GB RAM/Storage  
Engagement Score analysis   
Brand-wise comparison using pie, bar, and radar charts  
KMeans Clustering  
Keyword & Topic Modeling Visuals   

**Tablet EDA**   
Feature-based review keyword extraction (e.g., battery, display, camera)   
Popularity Score metric   
Parallel coordinates & 3D scatter plots   
Product clustering using KMeans   

## Interactive Dashboard (Streamlit)   

**Three dashboards are available with filtering options:**   

**📱 Mobiles: Filter by Storage, Color, Price, Rating, Sentiment**  
**💻 Laptops: Filter by Brand, Processor, RAM, Price, Reviews**   
**📟 Tablets: Filter by Screen Size, Battery Life, Brand, Rating**   
## Tech Stack  

Backend: pandas, numpy, matplotlib, seaborn, nltk, scikit-learn    
Frontend: Streamlit   

## User Experience   

Real-time filtering    
Responsive UI   
Interactive plots   
Actionable insights for:   
Analysts 📊   
Marketers 📢   
Consumers 🛍️   
  
## Learning Outcomes    
 
Practical experience in web scraping    
Deep understanding of data preprocessing for textual data   
Executed EDA, sentiment analysis, clustering, and topic modeling    
Built interactive dashboards using Streamlit    
Improved documentation and storytelling with data    

## Future Scope    

Expand to other platforms (Amazon, Snapdeal)    
Integrate image-based sentiment analysis    
Add real-time review tracking    

## Sreenshots     

![image](https://github.com/user-attachments/assets/95bd44b1-f844-4b52-9e91-604bbaf9a5bd)


![image](https://github.com/user-attachments/assets/630a2b0e-3853-4c7d-9f2e-0d333f39034d)


![image](https://github.com/user-attachments/assets/aa1f37f9-9bcb-48bd-9fe9-a12b4771a018)



## Requirements

**Install dependencies:**
pip install -r requirements.txt

## Run Dashboard   
cd dashboard/   
streamlit run Mobiles.py      
streamlit run Laptops.py       
streamlit run Tabs.py      
   
## Contributing   

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.    

## License

This project is licensed under the MIT License – see the LICENSE file for details.


## 👨‍💻 Author   

Developed by [J V Purushotham]    
Contact: jvpurushotham31@gmail.com     
