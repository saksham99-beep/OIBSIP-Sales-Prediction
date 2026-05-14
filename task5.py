#Sales Price Prediction using Python
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("Advertising.csv")

# Remove unnecessary column
df = df.drop(columns=["Unnamed: 0"])

# Features and target
X = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy check
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Custom prediction
tv = float(input("Enter TV advertising amount: "))
radio = float(input("Enter Radio advertising amount: "))
newspaper = float(input("Enter Newspaper advertising amount: "))
input_data = pd.DataFrame(
    [[tv, radio, newspaper]],
    columns=["TV", "Radio", "Newspaper"]
)

prediction = model.predict(input_data)

print("Predicted Sales:", prediction[0])
