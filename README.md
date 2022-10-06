# Citibike_Data

## Overview of the Project:
##### The purpose of the analysis was to use Tableau to illustrate specif parts of the City Bike data set. Using tableau I was able to create charts that allowed me to choose specific variables within the data that I wanted to see the relationship for. Along with picking the independent and dependent variables for each chart, I was able to go in much more depth by filtering the data by specific time measures and attibutes to compare the data across different populations and sugroups. 
The first Deliverable allowed me to veiw the data in jupyter and change the datatype for the datetime column in the dataset and reexport the edited CSV. This would allow me to use the proper date variable in tableau and prepare the Second deliverable which consisted of 5 different charts that build upon one another. 
---
## Results:
### Checkout Time for Users
##### The first graph that I created is a line graph that is focused on the checkout times forbike users. To create this visual I used the Trip duration variables in the columns selection and filtered one for hours and the other for minutes. This helped create an x-axis with a timeline ticked by minutes , but segmented by hour. The y-axis is measured by the number of bikes by putting the bike count variable in the rows. The tripduration was filtered over the course of three hour segments to get a good idea of the number of bikes used for certain durations of time. The peak user value is shown at the 5 minute trip duration time stamp. 

![image](https://user-images.githubusercontent.com/105329532/194214579-955fb072-88b8-4eff-952e-2ed2fbb53539.png)

### Checkout Times by Gender
##### This graph has the same key focus as the one above. The only diffrence is that now I am filtering out a specific variable that specifies the group of people the data represents rather than the entire population. I created an alias for the gender variable that allowed me to filter the data by Male, Female and Unkown by the color mark. This is why there are now three diffrent lines with different colors on the graph. Each represents the bike usage time dureation by gender.

![image](https://user-images.githubusercontent.com/105329532/194214429-1e047deb-6a1c-4b84-ba27-84c0f5edccf3.png)

### Trips by Weekday per Hour 
##### This graph was a heat map that highlights the frequency of trips throughout the week and the peak times that people make theses bike trips in the week. The darker the red pigment is , the higher the count of users for that time duration. The lighter shades represent less popular times for people to make trips. For example anytime from 12am - 5am is unpopular throughout the entire week, but 5pm - 6pm on Monday, Tueasday amd Wednesday are when the most amount of people are making bike trips. I created the chart by filtering the bike count by color mark, changing the hour startime to show a 12 hour time stamp on the y- axis and provide the days of the week on the x axis by filtering the trip duration by weekday.

![image](https://user-images.githubusercontent.com/105329532/194215123-d45c3f0d-de2d-4926-a351-32138aadab1f.png)

### Trips by Gender (Weekday per Hour)
##### This heatmap is the the same concept as the one before. Gender is another filtered layer added to better understand the groups that the data is representing. With this information we can now see that the majority of the population that was making up the 5-6pm trip time are the male population based on the heavily pigmented cells within the segmentation. We would not know this more detailed information had we not used gender as an added varaible to the Columns. 

![image](https://user-images.githubusercontent.com/105329532/194215253-f942d856-d359-4dd3-bd4b-5b1e02814ecd.png)

### User Trips by Gender by Weekday
##### This heatmap consisted of a couple diffrent filters that make the data even more complex and detailed. Ontop of the gender filter, we now have included a usertype variable in the row segment. This catgorzes the the gender in sepearate groups, males who are customers and males who are subscribers. We have created subgorups. For example the data shows that the most popular trip users are male subscribers on Thurdays. This creates a very specific story about the types of people who make bike trips and when. 

![image](https://user-images.githubusercontent.com/105329532/194215378-e171f15d-02d4-442a-b80b-698f4d129e9f.png)

---

### Summary:

##### There is a high-level summary of the results and two additional visualizations are suggested for future analysis (5 pt)
The data walks us through first a very high level point of veiw of the data and then slowly progressed into more detail. The first chart was super vague and told us only about the overall population. By the time the last heat map was created we began to discover the taget audience of the bike trip users and the scedule of the users. 

##### I think the two visualizations I would add are:
* ##### 1. a filter for the birth year variable so that we not only know the gender of the users but the age group as well which may hep us better understand why certain times for using the bikes are more popular than others.

* ##### 2. I think that using the longitude and latitiude variables along with the counts would create a nice map visual of where the majority of users congregate. 






