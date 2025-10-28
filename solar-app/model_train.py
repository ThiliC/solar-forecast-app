from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
from sklearn.metrics import r2_score
import joblib

# 1️⃣ Create fake data (x = features, y = output)
X, y = make_regression(n_samples=100, n_features=3, noise=5, random_state=42)

# 2️⃣ Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3️⃣ Create and train a model
model = LinearRegression()
model.fit(X_train, y_train)

# 4️⃣ Test the model
predictions = model.predict(X_test)
score = r2_score(y_test, predictions)
print("R^2 on test:", round(score, 2))

# 5️⃣ Save the model to a file
joblib.dump(model, "model.pkl")
print("✅ Model saved as model.pkl")
