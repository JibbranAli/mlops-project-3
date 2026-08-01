import joblib

model = joblib.load("model/model.pkl")

hours = [[7]]

prediction = model.predict(hours)

print("Predicted Marks :", prediction[0])
