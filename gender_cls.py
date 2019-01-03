#gender_cls
from sklearn import tree

#this is a random data set. Update the dataset with better data to get accurate results.
X = [[154,59,72],[148,57,76],[176,40,67],[157,58,68],[141,44,73],[148,42,65],[174,43,61],[156,47,77],[150,58,63],[141,55,61],[145,56,70]]
Y= ["male", "female","male","female","female","female","male","male","male","female","female"]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

prediction = clf.predict([[140,45,65]])

print (prediction)
