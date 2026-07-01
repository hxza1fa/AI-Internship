# Telco Customer Churn — Classification Practice Tasks

Dataset: https://www.kaggle.com/datasets/blastchar/telco-customer-churn
Target column: `Churn` (Yes/No) — binary classification, imbalanced (~73/27).

---

## Section 1: Exploration & Data Understanding
1. Load the data and check dtypes, shape, and nulls. Note: `TotalCharges` is stored as an object/string — figure out why (hint: blank strings for customers with 0 tenure) and decide how to handle it.
2. Compute the class balance of `Churn`. Write down — before modeling — why accuracy alone will be a misleading metric here, and which metric(s) you'll prioritize instead.
3. For each categorical feature, check cardinality and unique values. Identify which features have a "No internet service" / "No phone service" category and decide whether to collapse these into "No" or keep them distinct — justify your choice.
4. Look at the relationship between `tenure` and `Churn`. Bucket tenure into ranges (e.g., 0-12, 13-24, 25-48, 49+ months) and examine churn rate per bucket.
5. Check for multicollinearity between `tenure`, `MonthlyCharges`, and `TotalCharges`. Decide if you need to drop or transform any of them.

## Section 2: Preprocessing
6. Convert `TotalCharges` to numeric, handle resulting NaNs (don't just drop rows blindly — justify your imputation choice given what causes the NaNs).
7. Drop `customerID` and justify why it should never be used as a feature.
8. Encode `SeniorCitizen` consistently with the other binary Yes/No columns (it's currently 0/1 while others are Yes/No strings).
9. Apply two different encoding strategies to the categorical variables: one-hot encoding for nominal features, and label/ordinal encoding where it makes sense (e.g., `Contract` has a natural order: month-to-month < one year < two year). Compare how this choice affects a tree-based model vs. a linear model later.
10. Scale numerical features (`tenure`, `MonthlyCharges`, `TotalCharges`) appropriately for distance-based and linear models. Explain which models in your pipeline actually need this and which don't.
11. Split into train/test sets using **stratified** sampling on `Churn` — explain why stratification matters here.
12. Engineer at least 2 new features from existing ones (e.g., average charge per month of tenure, total number of additional services subscribed, a binary flag for "has any streaming service"). Justify each feature's potential predictive value before testing it.

## Section 3: Baseline Modeling
13. Train a Logistic Regression model as your baseline. Report accuracy, precision, recall, F1, and ROC-AUC — not just accuracy.
14. Plot and interpret the confusion matrix. Identify whether the model is biased toward predicting the majority class.
15. Plot the ROC curve and the Precision-Recall curve. Explain why PR curve might be more informative than ROC here given the class imbalance.

## Section 4: Handling Class Imbalance
16. Without resampling, try adjusting the classification threshold (instead of the default 0.5) to optimize for recall on the churn class. Show how precision/recall trade off as you move the threshold.
17. Apply class weighting (`class_weight='balanced'`) in a model that supports it and compare results to the unweighted baseline.
18. Apply SMOTE (or another oversampling technique) on the **training set only** (important: don't leak into test set) and compare results against class weighting. Which performed better and why might that be?

## Section 5: Model Comparison
19. Train at least 3 more classifiers: Random Forest, Gradient Boosting (XGBoost/LightGBM/GradientBoostingClassifier), and K-Nearest Neighbors.
20. Build a comparison table across all models (Logistic Regression, KNN, Random Forest, Gradient Boosting) with accuracy, precision, recall, F1, and ROC-AUC side by side.
21. For the tree-based models, extract and plot feature importances. Compare them against the coefficients from your logistic regression — do they agree on what drives churn?

## Section 6: Model Tuning
22. Perform hyperparameter tuning (GridSearchCV or RandomizedSearchCV) on your best-performing model from Section 5, using cross-validation, not just the single train/test split.
23. Use k-fold cross-validation (e.g., k=5) to validate that your tuned model's performance is stable and not a fluke of a particular split.

## Section 7: Error Analysis
24. Pull out the false negatives (customers predicted to stay who actually churned) and false positives. Look at their feature distributions — is there a pattern in the customers your model misses?
25. Given this is a churn problem, discuss the business cost asymmetry between false positives and false negatives (cost of unnecessarily retaining a happy customer vs. losing a customer you didn't flag). Based on this, decide whether you'd optimize the decision threshold differently than in Section 4.

## Section 8 (Stretch/Optional): Going Further
26. Try a stacking or voting ensemble combining your top 2-3 models.
27. Use SHAP values to explain individual predictions for a handful of customers, not just global feature importance.
28. Write a short "model selection memo" — pretend you're presenting to a non-technical stakeholder: which model would you deploy and why, considering interpretability vs. performance trade-offs?

---

### General reminders while working
- Always fit any encoders/scalers/imputers on the training set only, then transform the test set — to avoid data leakage.
- Keep a baseline (dumb classifier, e.g., predict majority class) result to compare everything against.
- Document your reasoning for each preprocessing/modeling decision in markdown cells, not just code.
