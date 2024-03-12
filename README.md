# Problem Statement
_________

California leads the country in [youth homelessness](https://www.theguardian.com/us-news/2023/dec/19/california-us-street-homelessness-youth-unsheltered-annual-report). To help address this growing issue in Los Angeles, this project's aim is to use classification models leveraging public data on youth homelessness surveys to predict who is at risk of becoming homeless based on family conditions and geographic consideration. The goal of this project is to help LA city government gain a better understanding of who is most at risk by utilizing binary classification models. To enhance the models' accuracies, I will incorporate domain expertise and external research to conduct feature selection, identifying relevant factors influencing the likelihood of becoming homeless.


# Methodology
_________

## Data Collection and Cleaning

For data collection, I gathered three datasets on individual homeless youth surveys during 2017-2019 from the [Los Angeles Continuum of Care Homeless Counts](https://economicrt.org/publication/los-angeles-county-homeless-count-data-library/). Once I gathered all three datasets, the main challenge was reformatting the questions in an uniform fashion to concatenate the three datasets together, which involved consulting respective data dictionaries. Once I was able to successfully reformat the datasets, I examined 119 different columns and used this [2015 report](https://oclawin.org/wp-content/uploads/2015/08/FactSheet_GeneralCauses_and_challenges_2015.pdf), which goes over common reasons why young individuals may end up homeless such as domestic issues with their families, to determine my features.

This is what ended up as my final dataset that I would use to train my classification models:

- Data Dictionary

| Variable        | Data Type | Value Count  | Description                                                                               |
| -----------     | --------  | ------------ | ------------------------                                                                  |
| hmlsmorethan1Yr | int64     | 2577         | 0 - No, 1 - Yes: homeless more than 1 year this time                                      |
| dv_neglect      | int64     | 2577         | 0 - No, 1 - Yes, 2 - R, 3 - S, 4 - D, 5 - C, 6 - N: faced neglect                         | 
| dv_physical     | int64     | 2577         | 0 - No, 1 - Yes, 2 - R, 3 - S, 4 - D, 5 - C, 6 - N: faced physical abuse                  | 
| dv_physical_rel | int64     | 2577         | 0 - No, 1 - Yes, 2 - R, 3 - S, 4 - D, 5 - C, 6 - N: faced physical abuse by parents       | 
| dv_sexual_rel   | int64     | 2577         | 0 - No, 1 - Yes, 2 - R, 3 - S, 4 - D, 5 - C, 6 - N: faced sexual abuse by parents         |
| subsabuse       | int64     | 2577         | 0 - No, 1 - Yes, 2 - M, 3 - Y, 4 - A: substance abuse problem of long duration (18+ only) | 
| drugabuse       | int64     | 2577         | 0 - No, 1 - Yes, 2 - M: Drug Abuse                          | 
| SPA             | int64     | 2577         | 1 - 8: [Service Planning Area](http://publichealth.lacounty.gov/chs/SPAMain/ServicePlanningAreas.htm)         |

## EDA 

* Check for missing values, shape, and summary in concatenated dataset
* Check value counts of the target variable to determine the baseline
* Explore trends with given information from the surveys
* Seek for any correlations between potential features and target variable
* Create plots that illustrate and interpret noticeable patterns

### Model

| Model               | Balanced Accuracy | Recall  | Precision | F1 Score |Model          | Balanced Accuracy | Recall  | Precision | F1 Score |
|---------------------|-------------------|---------|-----------|----------|---------------|-------------------|---------|-----------|----------|
| Logistic Regression |                   |         |           |          |KNN            |                   |         |           |          |
| logr                | 0.504139          | 0.011236| 0.666667  | 0.022099 |knn            | 0.522754          | 0.089888| 0.516129  | 0.153110 |
| RandomOverSampler   | 0.533592          | 0.460674| 0.381395  | 0.417303 |RandomOverSampler   | 0.562180          | 0.331461| 0.457364  | 0.384365 |
| SMOTE               | 0.532262          | 0.455056| 0.380282  | 0.414322 |SMOTEN              | 0.544728          | 0.320225| 0.422222  | 0.364217 |
| ADASYN              | 0.526644          | 0.443820| 0.374408  | 0.406170 |ADASYN              | 0.549315          | 0.314607| 0.434109  | 0.364821 |
| WeightedLogr        | 0.545409          | 0.516854| 0.389831  | 0.444444 |Weightedknn         | 0.539010          | 0.146067| 0.530612  | 0.229075 |

### Streamlit app

* Using the best performing model to create the streamlit app