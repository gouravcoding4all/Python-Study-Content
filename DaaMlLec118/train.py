# importing required libraries
import pandas as pd
import numpy as np
import joblib

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#loading the dataset
df = pd.read_csv(r"datasets/clean_data.csv")

#feature selection
df = df.drop(columns=['Student_Id'])

#Data division features and target variable
X = df.drop(columns=['Dropout'])
y = df['Dropout']

#Extract categorical and numerical columns
cat_cols = X.select_dtypes(include='object').columns
num_cols = X.select_dtypes(include=np.number).columns

# Handling outliersw in the family income columns
X.Family_Income = X.Family_Income.map(lambda val : 100000 if val>100000 else val)

# pipeline for model building
cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent'))
    ('encoder', OneHotEncoder())
    ])

num_pipeline = Pipeline([
    ('imputer',SimpleImputer(strategy='mean')),
    ('scaler',StandardScaler())
    ])

preprocessor = ColumnTransformer(transformers=[
    ('cat',cat_pipeline, cat_cols),
    ('num',num_pipeline, num_cols)
    ])

model = Pipeline([
    ('preprocessor',preprocessor),
    ('model',LogisticRegression())
    ])

#Train-test split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#Model training
model.fit(X_train,y_train)

joblib.dumb(model,'models/dropout_model.pkl')

#Model prediction
y_pred = model.predict(X_test)

#Model Evaluation
acc = accuracy_score(y_test,y_pred)
cm = confusion_matrix(y_test,y_pred)
cr = classification_report(y_test,y_pred)

print("Accuracy",acc)
file = open('models/model_evaluation.txt','w')
file.write(f"Accuracy:{acc}\n")
file.write(f"Confusion Matrix:\n{cm}\n")
file.close()

print("Model evaluation metrics saved to'models/model_evaluation.txt'")
print("Model saved to 'models/dropout_model.pkl'")
print("Model Training and Evaluation Completed Successfully.")