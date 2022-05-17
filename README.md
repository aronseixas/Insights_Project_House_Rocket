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

## 5.1 - Hypothesis test

<b> H1: </b> Waterfront properties are 30% more expensive, on average.  
<b> False: </b> Waterfront properties are, on average, <b> 212.42% </b> more expensive.  
![image](https://user-images.githubusercontent.com/95039795/168894918-9803f4d3-2ee8-4fb6-a7dc-6a7db3a07446.png)  

<b> H2: </b> Buildings older than 1955 are 50% cheaper on average.  
<b> False: </b> The building built before 1955 are 1.64% cheaper than those built after 1955.  
![image](https://user-images.githubusercontent.com/95039795/168896240-dd5223d0-839d-4b2a-97c6-0ce5dd91dc53.png)  

<b> H3: </b> Properties without a basement have a total area (sqrt_lot) 40% larger than properties with a basement.   
<b> False: </b> The buildings with no basement are 22.79%  more expensive than those that have basement.  
![image](https://user-images.githubusercontent.com/95039795/168896581-e6279ead-e344-4729-a169-6657e734875e.png)  

<b> H4: </b> YoY (Year over Year) property price growth is 10%.  
<b> False: </b> The price growths between 2014 and 2015 is 0.70%.  
![image](https://user-images.githubusercontent.com/95039795/168896763-e43cd5f3-7ab9-42f9-899b-98dd256ed163.png)  

<b> H5: </b> Homes with 3 bathrooms have a 15% MoM (Month over Month) growth.  
<b> False: </b> The largest positive variation was <b> 13,73%. </b>  
![image](https://user-images.githubusercontent.com/95039795/168899180-6a2cad31-6e20-4e57-be52-2988a607496a.png)   
![image](https://user-images.githubusercontent.com/95039795/168899597-2aee847a-4133-45db-9e1c-00f4d4c45153.png)   
   
<b> H6: </b> Homes sold in winter are 50% cheaper than in other seasons.   
<b> False: </b>  The houses price in winter are <b>3.92%</b> cheaper.    
![image](https://user-images.githubusercontent.com/95039795/168899270-0b9ebd5e-6938-4c0f-aeef-80a537939bde.png)  

<b> H7: </b> Reformed homes are 50% cheaper than not reformed homes.  
<b> False: </b> Renovates houses are <b> 43.53% </b> cheaper.   
![image](https://user-images.githubusercontent.com/95039795/168899485-e245ab03-14be-41ef-8593-35b937fbaa9a.png)  

# 6. Business Results

In all portfolio, the number of houses suggested for purchase is 17.62%.  
![image](https://user-images.githubusercontent.com/95039795/168906520-15c74ece-6635-404c-88a0-609b3a593f27.png)

Assuming all suggested homes have been bought and sold. 

The restults are:  

<table border="1">
    <tr>
        <td>Total investiment:</td>
        <td>$ 1483423213.00</td>
    </tr> 
    <tr>
        <td>Sales revenue:</td>
        <td>$ 1631765534.30</td>
    </tr> 
    <tr>
        <td>Profit:</td>
        <td>$ 148342321.30</td>
    </tr> 
</table>

![image](https://user-images.githubusercontent.com/95039795/168906690-efe5c406-e574-4c36-b68c-b169c1e4cf12.png)

# 7. Next steps

  - Develop more robust methods for handling outliers.  
  - Apply machine learning methods to find better opportunities based on more features.
