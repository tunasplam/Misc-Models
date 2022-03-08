# EDA
# What is going on in this EDA?
Here is what is going on step by step
- load up the dataset using OpenML API
- inspect the descriptive statistics of cont. variables and value counts of cat. variables
- pair plots, histograms, boxplots, scatterplots, and correlation matricies to get a sense of relationships
between variables
- I noticed that a couple of features were highly related so experimented with engineering new features that combined all of their information

# What was the verdict?
None of the columns required cleaning (the dataset was already cleaned when it was uploaded).  No outliers seemed to be problematic. height, normalized losses, stroke, compression-ratio, and bore got thrown out because they did not seem very informative.

City and highway mpg were incredibly related and also very informative on the price. decided to merge them by taking the arithmetic mean. The same also proved to be true about wheel base, curb weight, horsepower, width, length, and engine size. Taking the arithmetic mean of these features created a new feature with similar shape to the original features while also having a similar corelation to the target variable. These two new features also seemed somewhat normal in their distribution.

For model selection I decided on a random forest regressor. Although there seemed to be some clusters in some of the views, signifying that maybe a clustering algorithm could be used, I feel that clustering would prove more effective with data like vehicle type (sedan, SUV, truck, etc.) as well as brand (Toyota, Porsche, etc.). I also decided to one hot encode the lone categorical variable and standard scale the continuous ones.

# MODEL
# Whats Going on in this Notebook?
The model wwas buildt up, tuned on the train set using a grid search with 10-fold CV, and then tested on the test set. Several custom classes were created to enact the feature engineering steps in the sklearn pipeline. The final model chose did not necessarily have the best test score. The final model was chosen because it not only had a good test score (although not the best) but it also had a very low standard deviation, meaning it has a much higher probability of giving us a better test score on the test set.

# What was the results?
The model that was created was evaluated on a 33% holdout test set. It scored a mean absolute error of \$1171 (much much better than the models on OpenML might I add) which means that for each automobile in the test set, the average error in the model's prediction was 1171. Considering that this value is significantly lower than the standard deviation of the distribution of prices in the dataset, I would say that this model performed very excellently.
