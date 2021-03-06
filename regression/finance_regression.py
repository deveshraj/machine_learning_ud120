#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    starter code for the regression mini-project
    
    loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project)

    draws a little scatterplot of the training/testing data

    you fill in the regression code where indicated
"""    
'''
net worth prediction: reg.predict([27])
slope: reg.coef_
intercept: reg.intercept_
r-squared on test dataset: reg.score(ages_test, net_worths_test)
r-squared on training dataset: reg.score(ages_train, net_worths_train)
plt.scatter(ages, net_worth)
plt.plot(ages, reg.predict(ages), color = 'blue', linewidth = 3)
plt.xlabel('ages')
plt.ylabel('net worth')
plt.show()
'''

#Use the salary(input) to predict the bonus(target)
import sys
import pickle
from sklearn import linear_model

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
dictionary = pickle.load( open("../final_project/final_project_dataset_modified.pkl", "r") )

### list the features you want to look at--first item in the 
### list will be the "target" feature
features_list = ["bonus", "salary"]
#features_list = ["bonus", "long_term_incentive"]
data = featureFormat( dictionary, features_list, remove_any_zeroes=True)
target, features = targetFeatureSplit( data )

### training-testing split needed in regression, just like classification
from sklearn.cross_validation import train_test_split
feature_train, feature_test, target_train, target_test = train_test_split(features, target, test_size=0.5, random_state=42)
train_color = "blue"
test_color = "red"



### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and 
### plots it correctly. Don't forget to change the test_color from "b" to "r"
### to differentiate training points from test points.

from sklearn import linear_model
#create and train the regression
reg = linear_model.LinearRegression()
reg.fit(feature_train, target_train)
#slope
print "Slope with outlier: ", reg.coef_
#intercept
print "Intercept: ",reg.intercept_
print "r-squared on test dataset: ", reg.score(feature_test, target_test)
print "r-squared on training dataset: " ,reg.score(feature_train, target_train)



### draw the scatterplot, with color-coded training and testing points
import matplotlib.pyplot as plt
for feature, target in zip(feature_test, target_test):
    plt.scatter( feature, target, color=test_color ) 
for feature, target in zip(feature_train, target_train):
    plt.scatter( feature, target, color=train_color ) 

### labels for the legend
plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")




### draw the regression line, once it's coded
try:
    plt.plot( feature_test, reg.predict(feature_test) )
except NameError:
    pass

# we’ll be drawing two regression lines, one fit on the test data (with outlier) 
#and one fit on the training data (no outlier)
reg.fit(feature_test, target_test)
plt.plot(feature_train, reg.predict(feature_train), color="b") 
print "Slope without outlier: ", reg.coef_
plt.xlabel(features_list[1])
plt.ylabel(features_list[0])
plt.legend()
plt.show()
