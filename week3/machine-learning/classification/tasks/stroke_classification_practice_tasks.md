# Classification Practice Plan — Stroke Prediction Dataset

**Dataset:** Stroke Prediction Dataset (fedesoriano)
**Link:** https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset
**File:** `healthcare-dataset-stroke-data.csv`
**Target variable:** `stroke` (0 = no stroke, 1 = stroke)
**Rows/Cols:** ~5,110 rows × 12 columns

This dataset is *not* clean — it has missing values, a rare/imbalanced target class, mixed numeric/categorical features, and a near-empty category in `gender`. Good for real practice, not a toy exercise.

---

## Section 1: Initial Exploration
1. Load the dataset and inspect shape, dtypes, and a sample of rows.
2. Check for duplicate rows and duplicate `id` values.
3. Identify which columns are numerical, ordinal, and nominal categorical.
4. Compute the class distribution of `stroke` and state, in your own words, why this is a problem for naive accuracy-based evaluation.
5. Check for missing values column-by-column. Identify the exact percentage missing in `bmi`.
6. Investigate the `gender` column — count how many rows fall into the "Other" category and decide (with justification) what to do about it later.

## Section 2: Exploratory Data Analysis (EDA) — Univariate
7. Plot histograms/KDE plots for `age`, `avg_glucose_level`, and `bmi`. Comment on skewness.
8. Plot bar charts for all categorical variables (`gender`, `work_type`, `Residence_type`, `smoking_status`, `ever_married`) showing their frequency counts.
9. Create boxplots for `age`, `avg_glucose_level`, and `bmi` to visually detect outliers.
10. Compute skewness and kurtosis for the three continuous numeric variables.

## Section 3: EDA — Bivariate / Relationship with Target
11. Plot the distribution of `age` split by `stroke` (e.g. overlapping histograms or violin plots). What pattern do you notice?
12. Create grouped bar charts showing stroke rate (%) across each categorical variable (`work_type`, `smoking_status`, `ever_married`, `Residence_type`, `gender`) — not just raw counts.
13. Plot `avg_glucose_level` vs `age`, colored by `stroke`, as a scatter plot. Describe any visible clustering.
14. Build a correlation heatmap for the numeric variables (`age`, `avg_glucose_level`, `bmi`, `hypertension`, `heart_disease`) plus `stroke`.
15. Cross-tabulate `hypertension` and `heart_disease` against `stroke` and compute conditional stroke rates for each combination.
16. Write 3–4 bullet-point "insights" summarizing what the EDA tells you about stroke risk factors in this data, before you touch any model.

## Section 4: Preprocessing
17. Handle missing `bmi` values — try at least two strategies (e.g. median imputation vs. group-wise imputation by age bucket or gender) and briefly justify which one you'll keep.
18. Decide how to treat the "Other" gender category (drop the row(s), merge into another category, or keep as-is) and implement it.
19. Encode categorical variables appropriately — use one-hot encoding for nominal variables and consider whether any variable deserves ordinal encoding.
20. Detect outliers in `avg_glucose_level` and `bmi` using the IQR method or z-scores. Decide whether to cap, remove, or leave them, and justify your choice.
21. Scale/normalize the numeric features (try `StandardScaler` and `MinMaxScaler`, understand when each is preferred).
22. Drop or transform any column not useful for modeling (e.g. `id`), explaining why.
23. Address class imbalance in `stroke` — implement **at least two** of: class weighting, random undersampling, SMOTE oversampling. Keep the untouched version too, for comparison later.

## Section 5: Feature Engineering (a bit more advanced)
24. Create an `age_group` bucket feature (e.g. child/adult/senior) and re-examine stroke rate by bucket.
25. Create an interaction feature combining `hypertension` and `heart_disease` (e.g. a "risk_factor_count" column) and check its relationship with `stroke`.
26. Optionally bucket `avg_glucose_level` into clinically meaningful ranges (normal / prediabetic / diabetic) and compare against the raw continuous version's usefulness.

## Section 6: Model Building
27. Split the data into train/test sets using **stratified** splitting (explain why stratification matters here).
28. Train a baseline Logistic Regression model on the *imbalanced* data and evaluate it — deliberately observe how misleading plain accuracy is.
29. Train Logistic Regression again, this time using your imbalance-handling strategy from Task 23. Compare metrics.
30. Train at least two additional classifiers: e.g. Random Forest and either SVM, KNN, or Gradient Boosting (XGBoost/LightGBM if you want to push further).
31. Perform hyperparameter tuning (GridSearchCV or RandomizedSearchCV) on your best-performing model.
32. Use k-fold cross-validation (not just a single train/test split) to sanity-check that your best model's performance is stable across folds.

## Section 7: Model Evaluation
33. For every model, report: accuracy, precision, recall, F1-score, and ROC-AUC — not just accuracy.
34. Plot confusion matrices for at least your top 2 models and interpret false negatives specifically (why they matter more here than false positives).
35. Plot ROC curves and Precision-Recall curves for your top models on one comparative chart.
36. Discuss which metric should be prioritized for this specific problem (stroke prediction) and why — tie it back to real-world consequences of false negatives vs false positives.

## Section 8: Model Interpretation
37. Extract and plot feature importances from your tree-based model.
38. For Logistic Regression, interpret the sign and magnitude of coefficients for at least 3 features.
39. (Optional, more advanced) Use SHAP values to explain a few individual predictions — one correct, one false negative, one false positive.

## Section 9: Wrap-Up
40. Write a short "model comparison table" (markdown or dataframe) summarizing all models tried, their key metrics, and your final recommendation with justification.
41. Note at least 2 limitations of this dataset/analysis (e.g. sample size of positive class, lack of external validation, potential confounders) and how you'd address them with more resources.

---

### Suggested effort split
- Sections 1–3 (understanding + EDA): don't rush this — it's most of the learning value.
- Section 4 (preprocessing): this is where "proper" practice happens — don't just call `.dropna()` and move on.
- Sections 5–9: this is where you practice actual modeling discipline (imbalance handling, proper metrics, interpretation) rather than just `.fit()` → `.score()`.
