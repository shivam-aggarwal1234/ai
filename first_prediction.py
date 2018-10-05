from sklearn import tree

feature= [[130,0],[140,0],[150,1],[160,1]]
label = ['Apple','Apple','orange','orange']
clf = tree.DecisionTreeClassifier()
train = clf.fit(feature,label)
result = train.predict([[170,0]])
print(type([[170,1]]))
print(result)
