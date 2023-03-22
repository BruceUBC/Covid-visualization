# COVID Visualization Dashboard



## Authors

-   Bruce Wu

## Overview 

This repository hosts the dasbhaord for COVID-19 data released by [*Our World in Data*](https://ourworldindata.org/coronavirus) which is present in the this [repository](https://github.com/owid/covid-19-data/tree/master/public/data) and are completely open access under the [Creative Commons BY license](https://creativecommons.org/licenses/by/4.0/). 
The proposal of the project can be found [here](https://github.com/UBC-MDS/covid_viz/blob/main/reports/proposal.md)

## Project Motivation 

One of the primary motivations for tracking the daily cases and deaths of COVID-19 in China is to better understand the impact of the virus on public health, especially given that the first cases of COVID-19 were reported in Wuhan, China in December 2019. Accurate and timely reporting of data can help policymakers make informed decisions about how to allocate resources and respond to outbreaks, as well as help researchers study the virus and its impact. Furthermore, tracking those data can help promote transparency, both within China and internationally, as there are several international affairs happened recently about the heated topic Covid-19. 


*The brief questions answered by this dashboard would be:* 
- As a traveler one would want to know the current COVID stringency situation at the destination country. 
- Study the impact of COVID on different countries based on GDP and population density. 
- Study a particular country based on timeline to see how it was impacted over the months due to COVID.

<br>


## Get involved 

**How to run the app locally and make contributions**

If you would like to contribute to our project, please read the CONTRIBUTING.md file and then follow these steps: 
- Ensure that you have R and Rstudio installed on your computer 
- Fork our repository and [clone](https://github.com/UBC-MDS/covid_viz.git) it onto your computer 
- Create a new branch (named according to the specifications in the CONTRIBUTING.md file)

*To run the app locally:* 
- Open the project (i.e., the app.R file) in Rstudio

- Ensure all the necessary packages are installed

    install.packages(c("shiny", "bslib", "shinythemes", "shinydashboard", "ggplot2", "leaflet", "jsonlite", "thematic", "showtext", "readr", "lubridate", "dplyr"))

-   Click "Run App"

*To propose new changes:* 
- Make your changes to the code in Rstudio 
- Commit your changes (with an informative commit message) 
- Push your changes to your fork - Submit a pull request

**Places for improvement** 
- Build upon the current map plot and add interactive elements to the plot. 
- Help in accumulating the missing data on country level and add text box widget for the cases, vaccination percentage and deaths according to the user selection.

## Contributing 

Interested in contributing? Check out the [contributing guidelines](CONTRIBUTING.md). Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License 

`Covid visualization` was created by Bruce Wu. It is licensed under the terms of the [MIT license](LICENSE).
