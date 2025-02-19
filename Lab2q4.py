import pandas as pd
import statistics
import seaborn as sns
import matplotlib.pyplot as plt

file_path = "C:/Users/navde/OneDrive - Amrita vishwa vidyapeetham/Desktop/Amritafiles/Sem4/MachineLearning/Lab Session Data.xlsx"
df = pd.read_excel(file_path, sheet_name="IRCTC Stock Price")

# Converting 'Date' column to datetime format for filtering
df["Date"] = pd.to_datetime(df["Date"])

df["Day"] = df["Date"].dt.day_name()  # Extract day of the week
price_data = df["Price"]  # Column D (Price)
chg_percent = df["Chg%"]  # Column I (Change Percentage)

#Calculating the Mean & Variance of Price Data
mean_price = statistics.mean(price_data)
variance_price = statistics.variance(price_data)
print(f"Mean of Price Data: {mean_price:.2f}")
print(f"Variance of Price Data: {variance_price:.2f}")

#Selecting Price Data for Wednesdays & Calculating Sample Mean
wednesday_data = df[df["Day"] == "Wednesday"]["Price"]
sample_mean_wed = statistics.mean(wednesday_data)
print(f"Mean Price on Wednesdays: {sample_mean_wed:.2f}")
print(f"Difference from Population Mean: {abs(sample_mean_wed - mean_price):.2f}")

#Selecting Price Data for April & Computing Sample Mean
april_data = df[df["Date"].dt.month == 4]["Price"]
sample_mean_april = statistics.mean(april_data)
print(f"Mean Price in April: {sample_mean_april:.2f}")
print(f"Difference from Population Mean: {abs(sample_mean_april - mean_price):.2f}")

#Probability of Making a Loss & Making a Profit on Wednesday
loss_prob = sum(chg_percent < 0) / len(chg_percent)
print(f"Probability of making a loss: {loss_prob:.4f}")
wednesday_chg = df[df["Day"] == "Wednesday"]["Chg%"]
profit_wed_prob = sum(wednesday_chg > 0) / len(wednesday_chg)
print(f"Probability of making a profit on Wednesday: {profit_wed_prob:.4f}")

#Conditional Probability of Making a Profit Given It’s a Wednesday
profit_given_wed = sum((wednesday_chg > 0)) / len(wednesday_chg)
print(f"Conditional probability of profit given it's Wednesday: {profit_given_wed:.4f}")

#Scatter Plot of Change% Against the Day of the Week
# Map days to numerical values for plotting
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
df["Day_Num"] = df["Day"].apply(lambda x: day_order.index(x) if x in day_order else None)

plt.figure(figsize=(10, 6))
sns.scatterplot(x=df["Day_Num"], y=df["Chg%"], alpha=0.7)
plt.xticks(ticks=range(len(day_order)), labels=day_order)
plt.xlabel("Day of the Week")
plt.ylabel("Chg% (Change in Stock Price)")
plt.title("Stock Price Change% vs. Day of the Week")
plt.show()

