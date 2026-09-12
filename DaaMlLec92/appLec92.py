import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
import joblib

#Loading Dataset
df=pd.read_csv('dataset/iris.csv')

#Encoding
encoder = LabelEncoder()
df['species'] = encoder.fit_transform(df['species'])

#Data Split
X = df.drop(columns=['species'])
y=df['species']

#Scaling
scaler = StandardScaler()
X=scaler.fit_transform(X)

#Split Data into Training And Testing
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=11)

#Model Training
model = RandomForestClassifier()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
acc = round(accuracy_score(y_test,y_pred)*100,2)
cm = confusion_matrix(y_test,y_pred)

joblib.dump(model,'models/model.pkl')

file =open('model_training_report.txt','w')
file.write("Model : Random Forest Classifier \n")
file.write("\nAccuracy Score : "+str(acc))
file.write("\nConfusion Matrix\n"+str(cm))
file.close()
print("Model Trained And Save Successfully")