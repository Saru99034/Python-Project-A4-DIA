# Python-Project-A4-DIA
Project Python of Sarujan DENSON, Ahmed MAALOUL, Martin PUJOL Online Shoppers Intention

Introduction
This project focuses on predicting online shopper's intention using the Online Shoppers Intention dataset. The dataset provides information about various features related to online shopping behavior, and the goal is to build a model that can predict whether a user is likely to make a purchase.

Table of Contents

1. Data Exploration
   - Importing the data
   - Exploring dataset information
   - Statistical summary
   - Handling missing values
   - Data visualization
     
2. Data Preprocessing
   - Removing duplicate rows
   - Dimensionality reduction using PCA
   - Balancing the data
   - Normalization and encoding

3. Modeling
  (i) Logistic Regression
      - Training on downsampled data
      - Evaluating with confusion matrix, precision, and recall
      - Training on upsampled data and analyzing precision-recall 
        trade-off
  (ii) Neural Network
      - Training MLP on downsampled data
      - Approximating feature importances
      - Training MLP on upsampled data
  (iii) Random Forest
      - Training on downsampled data
      - Training on upsampled data

Conclusion

Evaluating models using ROC curves:
Outs of the models we tested, three stood out: Logistic Regression, Neural Network (MLP) and Random Forest. After evaluating their performance on the test data, Random Forest turned out to be the best classifier. So now, we are going to make predictions through API.

Creating a pipeline for easier processing
Exporting the model using pickle for API integration with Flask. This will allow us to process our new data and make a prediction
