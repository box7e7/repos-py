######Linear regression#######
##############################

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

from sklearn.linear_model import LinearRegression
lr = LinearRegression(fit_intercept = True)
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
mean_squared_error(y_test,y_pred)

###Statsmodels#####
###################

import statsmodels.api as sm
results = sm.OLS(y, X).fit()
predictions=results.predict()

print(results.summary())

####Label Encoder####
from sklearn import preprocessing
le = preprocessing.LabelEncoder()

####Standard scaler####
from sklearn.preprocessing import StandardScaler
X=X.apply(lambda col: le.fit_transform(col)) 

#####KNN#####
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(3)
knn.fit(X_train, y_train) 
y_pred = knn.predict(X_test)



####Confusion matrix####
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
accuracy_score(y_test, y_pred)
confusion_matrix(y_test, y_pred)

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True); Plot using seanborn

#####Random forest#####
#Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

#Predict
y_pred=clf.predict(X_test)


####Decison Tree####
from sklearn import tree
clf = tree.DecisionTreeClassifier(max_depth=4)
clf = clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)


####Logistic Regression####
logisticRegr = LogisticRegression()
logisticRegr.fit(X_train, y_train)
y_pred=logisticRegr.predict(X_test)

