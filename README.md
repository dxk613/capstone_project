# Problem Statement
_________

California leads the country in [youth homelessness](https://www.theguardian.com/us-news/2023/dec/19/california-us-street-homelessness-youth-unsheltered-annual-report). To help address this growing issue in Los Angeles, this project's aim is to use classification models leveraging 2017-2019 data on youth homelessness surveys from [Los Angeles Continuum of Care Homeless Counts](https://economicrt.org/publication/los-angeles-county-homeless-count-data-library/) to predict who is at risk of becoming homeless based on social and demographic conditions. This project will designate "Whether homeless more than 1 year this time" as the target variable. The goal of this project is to help LA city government gain a better understanding of who is most at risk by utilizing multiple classification models. To enhance the models' accuracies, I will incorporate domain expertise and external research to conduct feature selection, identifying relevant factors influencing the likelihood of becoming homeless.

After running tests for each model, I will select the best performing model to incorporate in my streamlit app which will tell how likely a young person will become homeless based on social and demographic inputs. 

# Methodology
_________

## Clean Data

* Ensure all three datasets match with one another
* Concatenate all three datasets once all three match with one another

## EDA 

* Check for missing values, shape, and summary in concatenated dataset
* Check value counts of the target variable to determine the baseline
* Explore trends with given information from the surveys
* Seek for any correlations between potential features and target variable
* Create plots that illustrate and interpret noticeable patterns

### Model

* Designate "Whether homeless more than 1 year this time" as the target variable
* Designate following features based on exploratory analysis and external research on youth homelessness 
* Utilize classification models such as Logistic and Random Forest 
* Compare different metrics such as ROC and test score to compare models' performances

### Streamlit app

* Using the best performing model to create the streamlit app