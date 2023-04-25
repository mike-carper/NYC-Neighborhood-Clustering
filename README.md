# NYC-Neighborhood-Clusters

Groups New York City neighborhoods (PUMAs) together based on characteristics measuring access and livability

K-means clustering methodology

Input Variables:

    * Park access: park_access["park_perc"]
    * Job access: job_access["job_perc"]*100/hh_econ["LF_19E"]
    * Access to transit: transit_parks['Percent']
    * Affordable housing: <30% of HH income: 100-housing["GRPI30_19P"],
                          <50% of HH income: 100-housing["GRPI50_19P"]
    * Home ownership: housing["OOcc1_19P"]
    * Broadband access: housing["Comp_19P"]
    * Computer access: housing["BbInt_19P"]
    * Employment rate: hh_econ["CvEm1_19E"]/hh_econ["LF_19E"]
    * Education: Bachelor's degree or higher: hh_econ["Bchpl_19P"]
                 HS graduation rate: 100-hh_econ['HS_19P']
    * Infant mortality: 100-mort_rate["infant_mortality_per1000_16_20"]*10
    * Heat Vulnerability Index: 100-hvi["HVI"]*20
