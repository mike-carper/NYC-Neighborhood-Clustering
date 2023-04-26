# NYC-Neighborhood-Clusters

Groups New York City neighborhoods (PUMAs) together based on characteristics measuring access and livability

K-means clustering methodology

All data cleaned and prepared by NYC Planning's Enterprise Data Management division and downloaded from Equitable Development Data Explorer repository (https://github.com/NYCPlanning/db-equitable-development-tool/tree/main/resources). Input variables are all from ACS 5-Year 2015-2019, unless otherwise noted.

Input Variables:
    
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
