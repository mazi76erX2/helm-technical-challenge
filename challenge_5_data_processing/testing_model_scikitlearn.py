from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

from .movies_data_processing import merged_data

# Scikit-learn
# Split the merged dataset into training, validation, and test sets
train_data, test_data = train_test_split(merged_data, test_size=0.2, random_state=42)
train_data, val_data = train_test_split(train_data, test_size=0.2, random_state=42)

# Print the sizes of the resulting sets
print("Training set size:", len(train_data))
print("Validation set size:", len(val_data))
print("Testing set size:", len(test_data))

# Split the dataset into features (X) and target variable (y)
X = merged_data[['num_genres', 'year']]
y = merged_data['rating']

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)

# Make predictions on the test set using linear regression
y_pred_lr = model_lr.predict(X_test)

# Evaluate the linear regression model using mean squared error
mse_lr = mean_squared_error(y_test, y_pred_lr)
print("Linear Regression Mean Squared Error:", mse_lr)
