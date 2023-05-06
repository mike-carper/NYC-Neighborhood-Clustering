# NYC-Neighborhood-Clusters

Groups New York City neighborhoods (PUMAs) together based on indicators measuring access to resources and resident quality of life

K-means clustering methodology (2 trials: k=2 and k=4 clusters, 8 input variables)

Analysis conducted by Mike Carper, data prepared by NYC Planning's Enterprise Data Management team and extracted from Equitable Development Data Explorer repository (https://github.com/NYCPlanning/db-equitable-development-tool/tree/main/resources)

Variables Considered (from ACS 5-Year 2015-2019, unless otherwise noted):
    
    * Park access: % of population with access to a park
    * Job access: jobs accessible within 30 mins by transit per 100 labor force participants, maxed at 100
    * Access to transit: % of population within 1/4 Mile of Subway Stations and SBS Stops (ACS 2017-2021 5-Year)
    * Affordable housing: % of households paying <30% of HH income, paying <50% of HH income
    * Home ownership: % of units that are owner-occupied
    * Broadband access: % of households with a computer
    * Computer access: % of households with broadband access
    * Employment rate: % of labor force participants 16 to 64 years old who are employed
    * Education: % of population 25 years and older with a bachelor's degree or higher, with a high school diploma or higher
    * Infant mortality rate: number of deaths per 1000 live births (ACS 2016-2020 5-Year)
    * Heat Vulnerability Index: index of various indicators measuring heat vulnerability (NYS DOH, 2017)

8 Chosen Indicators (from above list):
    
    * Park access, job access, computer access, bachelor's degree, employment rate, rent under 30% of HH income, subway and bus access, infant mortality rate
    
Trial 2 Clustering Results:
    
    * Cluster 3, the "Center City" cluster, has the highest score across each indicator, suggesting an overall greater level of resource access and quality of life than neighborhoods across the rest of the city.
    * Cluster 2, the "Low Density Perimeter" cluster includes lower density neighborhoods that are distant from the center city, which score low along the lines of job, park and subway access (and interestingly, infant morality, where a low score=high rate), and in the middle in terms of employment and computer access
    * Cluster 1, the "Infrastructure-Accessible, Resource-Neglected" cluster scores high in park, transit and job accessibility, but has the lowest scores in educational attainment, infant mortality, affordable rent and employment. Neighborhoods in this cluster are located conveniently, but quality of life indicators are low.
    * Cluster 0, the "In-Between" cluster has scores in the middle, with more decent quality of life indicator scores than Cluster 1, more accessibility to parks, jobs and subway stations than Cluster 2 but less than Cluster 1 or 3.
    
Trial 2 Cluster Demographics:
    
    * Cluster 3 has the greatest share of White non-Hispanic residents and the highest median income.
    * Cluster 1 has the lowest median income and greatest share of Black non-Hispanic and Hispanic residents.
    * Clusters 0 and 2 are the most representative of NYC as a whole in terms of race and ethnicity makeup.
    
    
