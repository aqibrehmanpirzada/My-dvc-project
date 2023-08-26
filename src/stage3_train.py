import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
import joblib
from logger import logging


def train_and_evaluate_model(train_data_path, test_data_path, model_type='xgboost', save_path=None):
    # Load Data
    train_df = pd.read_csv(train_data_path)
    test_df = pd.read_csv(test_data_path)

    # Preprocess Data
    X_train = train_df.drop(columns=['Log_GDP'], axis=1)
    y_train = train_df['Log_GDP']
    X_test = test_df.drop(columns=['Log_GDP'], axis=1)
    y_test = test_df['Log_GDP']

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train the Model
    if model_type == 'linear':
        model = LinearRegression()
    else:
        model = XGBRegressor()

    model.fit(X_train_scaled, y_train)

    # Evaluate the Model
    y_pred = model.predict(X_test_scaled)
    rmse = mean_squared_error(y_test, y_pred, squared=False)

    # Save the Model
    if save_path:
        model_filename = 'trained_model.pkl'
        model_path = save_path + model_filename
        joblib.dump(model, model_path)
        print(f"Model saved at {model_path}")

    return model, rmse
    logging.info("Training is Done Finally")

# Example usage
train_data_path = "/media/aqib/Software/MLOPS Project/Project 1/My-dvc-project/artifacts/processed_data/train.csv"
test_data_path = "/media/aqib/Software/MLOPS Project/Project 1/My-dvc-project/artifacts/processed_data/test.csv"
model_save_path = "/media/aqib/Software/MLOPS Project/Project 1/My-dvc-project/artifacts/Models/"

trained_model, rmse = train_and_evaluate_model(train_data_path, test_data_path, model_type='xgboost', save_path=model_save_path)
print("Root Mean Squared Error:", rmse)
logging.info("Root Mean Squared Error: %s", rmse)
