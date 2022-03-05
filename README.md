# Misc-Models
Some Miscellaneous Machine Learning Models that I have Made
Some of these mdoels require the OpenML python api in order to function. Since the API key is not included, some of the functions in the notebook may not work for another user.


# liver-disorders
Based on a dataset from OpenML. The goal was to predict the amount of drinks a person averaged daily based on a variety of liver samples. After a bit of EDA I decided on using a sklearn pipeline involving several data transformations, some automatic feature selection, and a Poisson Regression model. A grid search was used to optimize many parameters. A custom Log Transfomer class was used because openml's api does not work with numpy's log transform function as it does not follow sklearn's coding guidelines. To get around this, I had to make a simple log transformer class for sklearn.

# student-performance
Yet another OpenML dataset. The goal was to predict the gender of a student based on a variety of different test scores and socioeconomic factors. After some EDA and basic feature engineering, I decided on using an sklearn pipeline that featured some transformations of the continuous variables as well as a Gradient Boosting Classifier model. A grid search was used to optimize many parameters.
