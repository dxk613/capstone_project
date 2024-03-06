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