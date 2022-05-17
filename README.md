# House Rocket - Insight Project

  ![Seattle_image](https://user-images.githubusercontent.com/95039795/168675366-c7624547-075c-4795-8cde-e1d96b42240a.jpg)
  
  
# 1. Business Issues

   1- What properties should House Rocket buy and at what price?  
   2- Once the house is purchased, what is the best price to sell it?  

# 2. Attribute List
  
  The database used was obtained through Kaggle: https://www.kaggle.com/datasets/harlfoxem/housesalesprediction  

<table border="1" align=center>
    <tr>
        <th>Attribute</th>
        <th>Meaning</th>
    </tr>
    <tr>
        <td>id</td>
        <td>Property identification number</td>
    </tr> 
    <tr>
        <td>date</td>
        <td>Salling date</td>
    </tr>
    <tr>
        <td>price</td>
        <td>Salling price</td>
    </tr>
    <tr>
        <td>bedrooms</td>
        <td>Number of bedrooms</td>
    </tr>
     <tr>
        <td>bethrooms</td>
        <td>Number of bethrooms (0.5 = no shower)</td>
    </tr>
     <tr>
        <td>sqft_living</td>
        <td>Measurement (square feet) of apartments interior space</td>
    </tr>
    <tr>
        <td>sqft_lot</td>
        <td>Measurement (square feet) of land space</td>
    </tr>
    <tr>
        <td>floors</td>
        <td>Number of floors</td>
    </tr>
    <tr>
        <td>waterfront</td>
        <td>Indicates whether or not a waterview is present (0 = no and 1 = yes)</td>
    </tr>
    <tr>
        <td>view</td>
        <td>An index from 0 (low) to 4 (high) that indicates the property quality view.</td>
    </tr>
    <tr>
        <td>condition</td>
        <td>An index from 0 (low) to 5 (high) that indicates the property condition.</td>
    </tr>
    <tr>
        <td>grade</td>
        <td>An index from 1 to 13 that indicates the construction and design of the building.<p>  
          Ranges from 1 to 13, where: 1-3 = low, 7 = medium, and 11-13 = high.</td></p>
    </tr>
    <tr>
        <td>sqft_above</td>
        <td>Propriety area above the soil.</td>
    </tr>
    <tr>
        <td>sqft_basement</td>
        <td>Basement area.</td>
    </tr>
    <tr>
        <td>yr_built</td>
        <td>Year of construction.</td>
    </tr>
    <tr>
        <td>yr_renovated</td>
        <td>Year of renovation.</td>
    </tr>
    <tr>
        <td>zipcode</td>
        <td>Property zipcode.</td>
    </tr>
    <tr>
        <td>Lat</td>
        <td>Latitude.</td>
    </tr>
    <tr>
        <td>Long</td>
        <td>Longitude.</td>
    </tr>
    <tr>
        <td>sqft_livining15</td>
        <td>Measure (square feet) of internal living space for the 15 nearest neighbors.</td>
    </tr>
    <tr>
        <td>sqft_lot15</td>
        <td>Measure (square feet) of the land plots of the 15 nearest neighbors.</td>
    </tr>
</table>

# 3. Business Assumptions

   - Duplicate "ID" values were excluded.
   - Properties with missing values were excluded.
   - House prices are influenced by region (zipcode) and season (seasons).
   - Proprietes with purchase potential are those that are in good condition and below the median price in the region.
   - For the sale price decision, three features are considered, the purchase price, the median price of the zipcode and the season.  
      - If the purchase price is lower than the region's average price in the given season, the sale price will be 30% higher than the purchase price.  
      - If greater, the increase will be 10%

# 4. Solution Strategy

## 4.1 - Final Product

  - Report with buying suggestions for properties.
  - Report with price suggestions for the properties.
  - Application containing details of houses and recommendations: https://analytics-house-hockets.herokuapp.com/

![App_layut](https://user-images.githubusercontent.com/95039795/168697739-7bce86c5-dca8-4a94-a543-9966a34d8a9d.png)

## 4.2 - Strategy

  -  <b> Step 1 Understanding the business problem: </b> The goal is to understand business needs and how data science can be applied to solve them.  
  -  <b> Step 2 Data Description: </b> The goal is to describe the database, check the presence of null and duplicate values and obtain statistical metrics such as mean, median, standard deviation, minimum, maximum.  
  -  <b> Step 3 Data Cleaning: </b> The goal is to eliminate nulls and duplicates, and obtaining new attributes based on the original variables in order to solve business problems.  
  -  <b> Step 4 Exploratory data analysis (EDA): </b> The goal of this step is, through hypothesis test, to explore the data to find insights and better understand the impact of variables in the proprietes prices.  
  -  <b> Step 5 Solving business questions: </b> The goal of this step is to generate reports containing the information proposed in the Business Issues section.   
  -   <b> Step 6 Business results: </b> The objective of this step is to convert the results into business value.  
  -   <b> Step 7 Business results: </b> Deploy the results in a dashboard containing details of the houses and recommendations. The cloud application platform choosed was Heroku.  

## 4.3 - Solution steps

### 4.3.1 Generating a report with property purchase suggestions </h3>

    - Group data by region (zipcode and season).
    - Calculate the median property price by region.
    - Purchase suggestion: Select properties in good condition (condition >=4) and purchase price below the median value.  
    
### 4.3.2 Generating a report with selling suggested prices for previously purchased properties.

    - Group sold houses data by region (zipcode and season).
    - Calculate the median proprety by region and season.
    - Select from the database the houses that were suggested for purchase.  
    
    Conditions:
        1- If the purchase price is higher than the median of the season, the sale price will be increased by 10%.
        2- If the purchase price is below the median of the season, the sale price will be increased by 30%.
      






# 5. Exploratory data analysis (EDA)

# 6. Business Results

# 7. Conclusions

# 8. Next steps



