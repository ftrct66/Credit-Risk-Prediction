# Credit-Risk-Prediction
Authors: Fitri Octaviani
 
# Overview
The general objective is to develop a machine-learning model that can accurately predict credit risk based on historical data.
 
# Success Criteria
The following metrics will be used to determine the project's success:
1. Our analytical capabilities provide banks with actionable insights into the credit risk of customers
2. Ensuring a minimum of 90% accuracy in identifying customers with high credit risk.

# Data Description
The data used in this project is from Kaggle.
- Field Description:
  Berikut adalah variabel dan definisi dari setiap kolom dalam dataset.

| Column | Description |
|--------|-------------|
| CLIENTNUM | Client number. Unique identifier for the customer holding the account |
| Attrition_Flag | Internal event (customer activity) variable - if the account is closed then 1 else 0 |
| Customer_Age | Demographic variable - Customer's Age in Years |
| Gender | Demographic variable - M=Male, F=Female |
| Dependent_count | Demographic variable - Number of dependents |
| Education_Level | Demographic variable - Educational Qualification of the account holder (example: high school, college graduate, etc.) |
| Marital_Status | Demographic variable - Married, Single, Divorced, Unknown |
| Income_Category | Demographic variable - Annual Income Category of the account holder (< $40K, $40K - 60K, $60K - $80K, $80K-$120K, > |
| Card_Category | Product Variable - Type of Card (Blue, Silver, Gold, Platinum) |
| Months_on_book | Period of relationship with bank |
| Total_Relationship_count | Total no. of products held by the customer |
| Months_Inactive_12_mon | No. of months inactive in the last 12 months |
| Contacts_Count_12_mon | No. of Contacts in the last 12 months |
| Credit_Limit | Credit Limit on the Credit Card |
| Total_Revolving_Bal | Total Revolving Balance on the Credit Card |
| Avg_Open_To_Buy | Open to Buy Credit Line (Average of last 12 months) |
| Total_Amt_Chng_Q4_Q1 | Change in Transaction Amount (Q4 over Q1) |
| Total_Trans_Amt | Total Transaction Amount (Last 12 months) |
| Total_Trans_Ct | Total Transaction Count (Last 12 months) |
| Total_Ct_Chng_Q4_Q1 | Change in Transaction Count (Q4 over Q1) |
| Avg_Utilization_Ratio | Average Card Utilization Ratio |
| Naive_Bayes_Classifier_attribution | Naive Bayes |
| Naive_Bayes_Classifier_attribution | Naive Bayes |

# Modelling
The model is used in Gaussian Naive Bayes, Gradient Boosting, and KNeighbors. After that, the selection of the best model was carried out based on the evaluation of model performance through cross-validation. The best model obtained is GradientBoosting and is calculated using hyperparameter tuning with a train set accuracy of 96% and a test set of 91%.

# Project Conclusion
1. Based on Exploratory Data Analysis (EDA) :
- The credit_risk column in the data set shows an unequal class distribution, with lower risk than high risk
- The average age of customers is 46 years with an age range of 26 to 73 years
- The average customer relationship with the bank is around 36 months (3 years)
- The average credit limit is about $8632
- There is a pattern showing that individuals with lower levels of education tend to have lower credit risk
- The average customer uses the “Blue” category card compared to other categories
- In terms of credit risk, males are more at risk than females
2. Business Insights :
- In the world of finance, credit risk management plays an important role in ensuring a balance between lending to customers and minimizing risk. To achieve this goal, a solid strategy is needed that focuses on prudent risk management.
- By understanding the customer's risk profile, we can design specific strategies for each segment. This makes it possible to provide credit offers that are more in line with the abilities and characteristics of each group thereby reducing overall risk.
- Collaborating with credit research institutions and external data service providers can provide additional insights. Outside information can provide a broader view of the customer and the economic environment that may affect the customer's ability to pay.
