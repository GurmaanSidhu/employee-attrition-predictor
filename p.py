# 1) Imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("employee_attrition_ - employee_attrition_impure.csv")

# 3) Basic EDA
print("Shape:", df.shape)
print("\nDtypes:\n", df.dtypes)
print("\nHead:\n", df.head())
print("\nMissing values:\n", df.isna().sum())
print("\nDescribe:\n", df.describe())

# 4) Drop rows with any missing values (simple approach you can explain)
df = df.dropna()

# 5) Simple visuals (looks good in a report)
numeric_cols = ['MonthlyIncome', 'Age', 'JobSatisfaction', 'YearsAtCompany']
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, col in zip(axes.flat, numeric_cols):
    sns.histplot(data=df, x=col, kde=True, ax=ax)
plt.tight_layout()
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
for ax, col in zip(axes.flat, numeric_cols):
    sns.boxplot(data=df, y=col, ax=ax)
plt.tight_layout()
plt.show()

# Correlation heatmap (numeric only)
corr = df[numeric_cols + ['OverTime']].corr(numeric_only=True)  # OverTime included after conversion below
sns.heatmap(corr, annot=True, fmt=".2f", cmap="crest")
plt.title("Correlation Heatmap")
plt.show()

# 6) IQR outlier removal (simple & explainable)
def remove_outliers_iqr(data, cols):
    clean = data.copy()
    for c in cols:
        Q1 = clean[c].quantile(0.25)
        Q3 = clean[c].quantile(0.75)
        IQR = Q3 - Q1
        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR
        clean = clean[(clean[c] >= lower) & (clean[c] <= upper)]
    return clean

df = remove_outliers_iqr(df, numeric_cols)

# 7) Convert Yes/No to 1/0
df['OverTime'] = df['OverTime'].map({'Yes': 1, 'No': 0})
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# 8) Features and target
X = df[['MonthlyIncome', 'Age', 'JobSatisfaction', 'YearsAtCompany', 'OverTime']]
y = df['Attrition']

# 9) Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 10) Logistic Regression (simple default)
log_clf = LogisticRegression()
log_clf.fit(X_train, y_train)
y_pred_log = log_clf.predict(X_test)
log_acc = accuracy_score(y_test, y_pred_log)
print("Logistic Regression Accuracy:", log_acc)
print("Logistic Regression Confusion Matrix:\n", confusion_matrix(y_test, y_pred_log))

# 11) Decision Tree (simple default)
tree_clf = DecisionTreeClassifier(random_state=42)
tree_clf.fit(X_train, y_train)
y_pred_tree = tree_clf.predict(X_test)
tree_acc = accuracy_score(y_test, y_pred_tree)
print("Decision Tree Accuracy:", tree_acc)
print("Decision Tree Confusion Matrix:\n", confusion_matrix(y_test, y_pred_tree))
