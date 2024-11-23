import pandas as pd
import numpy as np
import pickle

# Load the trained model
try:
    with open('lr_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    print("Model file not found. Please check the file path.")
    exit()
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Generate random input data for prediction
def generate_random_data():
    return pd.DataFrame({
        'Age': [np.random.randint(20, 60)], 
        'BusinessTravel': [np.random.choice(['Travel_Rarely', 'Travel_Frequently', 'Non-Travel'])], 
        'DailyRate': [np.random.randint(1000, 5000)], 
        'Department': [np.random.choice(['Sales', 'Research & Development', 'Human Resources'])], 
        'DistanceFromHome': [np.random.randint(1, 30)], 
        'Education': [np.random.randint(1, 5)], 
        'EducationField': [np.random.choice(['Life Sciences', 'Medical', 'Marketing', 'Technical Degree', 'Human Resources', 'Other'])], 
        'EnvironmentSatisfaction': [np.random.randint(1, 5)], 
        'Gender': [np.random.choice(['Male', 'Female'])], 
        'HourlyRate': [np.random.randint(20, 100)], 
        'JobInvolvement': [np.random.randint(1, 5)], 
        'JobLevel': [np.random.randint(1, 5)], 
        'JobRole': [np.random.choice(['Sales Executive', 'Research Scientist', 'Laboratory Technician', 'Manager', 'Healthcare Representative', 
                                    'Manufacturing Director', 'Human Resources', 'Sales Representative'])], 
        'JobSatisfaction': [np.random.randint(1, 5)], 
        'MaritalStatus': [np.random.choice(['Married', 'Single', 'Divorced'])], 
        'MonthlyIncome': [np.random.randint(2000, 20000)], 
        'MonthlyRate': [np.random.randint(10000, 30000)], 
        'NumCompaniesWorked': [np.random.randint(0, 10)], 
        'OverTime': [np.random.choice(['Yes', 'No'])], 
        'PercentSalaryHike': [np.random.randint(10, 25)], 
        'PerformanceRating': [np.random.randint(1, 5)], 
        'RelationshipSatisfaction': [np.random.randint(1, 5)], 
        'StockOptionLevel': [np.random.randint(0, 3)], 
        'TotalWorkingYears': [np.random.randint(1, 40)], 
        'TrainingTimesLastYear': [np.random.randint(0, 10)], 
        'WorkLifeBalance': [np.random.randint(1, 5)], 
        'YearsAtCompany': [np.random.randint(0, 20)], 
        'YearsInCurrentRole': [np.random.randint(0, 15)], 
        'YearsSinceLastPromotion': [np.random.randint(0, 10)], 
        'YearsWithCurrManager': [np.random.randint(0, 15)], 
        'StabilityInRole': [np.random.uniform(0.1, 1.0)], 
        'LoyaltyToManager': [np.random.uniform(0.1, 1.0)], 
        'AvgTrainingPerYear': [np.random.uniform(0.5, 5.0)], 
        'AgeWhenStarted': [np.random.randint(18, 40)], 
        'AvgYearsPerCompany': [np.random.randint(1, 15)], 
        'IncomePerKm': [np.random.randint(100, 1000)], 
        'CompanyLoyalty': [np.random.uniform(0.1, 1.0)], 
        'PromotionFrequency': [np.random.randint(0, 5)], 
        'AvgMonthlyIncomePerYear': [np.random.randint(1000, 5000)]
    })

# Generate random data
X_new = generate_random_data()

# Predict using the loaded model
try:
    y_pred = model.predict(X_new)
    print("Input Data for Prediction:")
    print(X_new)
    print("\nPrediction Result:", y_pred)
except Exception as e:
    print(f"Error during prediction: {e}")
