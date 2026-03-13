# %%
import pandas as pd
import joblib
pd.options.display.max_columns = 50
# %%
model = joblib.load('best_model.pkl')
encoder = joblib.load('ordinal_encoder.pkl')
# %%
data = pd.read_csv('test_data_raw.csv')
# %%
data.head()
# %%
ordinal_cols = [
    'Education',
    'EnvironmentSatisfaction',
    'JobInvolvement',
    'JobSatisfaction',
    'PerformanceRating',
    'RelationshipSatisfaction',
    'WorkLifeBalance',
    'BusinessTravel'
]
# %%
data_uji = data.copy()
data_uji[ordinal_cols] = encoder.transform(data_uji[ordinal_cols])
# %%
data_uji.head()
# %%
data_uji['Gender'] = data_uji['Gender'].apply (lambda x: 1 if x == 'Male' else 0)
data_uji['OverTime'] = data_uji['OverTime'].apply (lambda x: 1 if x == 'Yes' else 0)
data_uji['Attrition'] = data_uji['Attrition'].apply (lambda x: 1 if x == 'Yes' else 0)
# %%
nominal_cols = [
    'Department',
    'EducationField',
    'JobRole',
    'MaritalStatus'
]
data_uji = pd.get_dummies(data_uji, columns=nominal_cols, drop_first=True)
# %%
employee_ids = data_uji.index
# %%
model_features = model.feature_names_in_
data_uji = data_uji.reindex(columns=model_features, fill_value=0)
# %%
predictions = model.predict(data_uji)
# %%
data_uji.head()
# %%
result_df = pd.DataFrame({
    'EmployeeID': data['EmployeeId'],
    'ActualAttrition': data['Attrition'],
    'Prediction Result': ['Yes' if pred == 1 else 'No' for pred in predictions]
})
# %%
result_df.head(20)
# %%
result_df.to_csv('prediction.csv', index=False)