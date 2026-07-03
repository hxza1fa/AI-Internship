# Gradient Boosting Practice — Diamond Price Regression

**Dataset:** Diamonds
https://www.kaggle.com/datasets/shivam2503/diamonds

**File:** `diamonds.csv`
**Rows:** ~53,940 (medium-sized — enough to actually stress-test hyperparameters and see stable trends, unlike tiny toy datasets)
**Target:** `price` (continuous, USD)

**Features:**
- Numeric: `carat`, `depth`, `table`, `x` (length, mm), `y` (width, mm), `z` (depth, mm)
- Categorical (ordinal in nature): `cut` (Fair → Ideal), `color` (J → D, worst to best), `clarity` (I1 → IF, worst to best)
- `Unnamed: 0` / index column — drop it, it's just a row ID carried over from the CSV export

---

## Why this dataset works for a GBM test

- Big enough sample size to get stable metrics and actually see the effect of tuning `n_estimators` / `learning_rate`, instead of noise from a tiny test set.
- Three genuinely ordinal categorical features (`cut`, `color`, `clarity`) — a good test of encoding strategy (ordinal vs one-hot) and how much it matters for tree models vs linear ones.
- Known non-linear + skewed relationships (`carat` vs `price` is not a straight line, and `price` itself is right-skewed) — a clean before/after story for boosting vs. linear regression.
- A few built-in data quality issues (some rows have `x`, `y`, or `z` = 0, which is physically impossible) — gives you a real reason to do outlier/sanity-check preprocessing instead of skipping straight to modeling.

---

## EDA — trend analysis first

Goal here is to actually understand the data before touching a model, not just run `.describe()` and move on.

### 1. Structural checks
- `df.shape`, `df.info()`, `df.describe()` — confirm dtypes, look at min/max ranges.
- `df.isnull().sum()` — check for missing values (this dataset is usually clean, but verify).
- `df.duplicated().sum()` — check for exact duplicate rows; diamonds datasets often have some.

### 2. Target variable (`price`)
- Plot a histogram of `price`. You should see a strong right skew (many cheap diamonds, a long tail of expensive ones).
- Plot a histogram of `log1p(price)` next to it. Note how much more symmetric it looks — this is your first hint that a log-transform of the target might help, especially for any linear baseline you compare against.

### 3. Numeric features vs target
- Scatter plot `carat` vs `price` — this is the single strongest predictor. You'll notice the relationship isn't linear (it curves), and there's "banding" at common carat weights (0.5, 1.0, 1.5, 2.0) where prices jump — worth calling out in your notes.
- Scatter plots of `x`, `y`, `z` vs `price` — these should look similar to `carat` since they all measure diamond size. Good moment to check for multicollinearity between `carat`, `x`, `y`, `z`.
- Scatter plot `depth` vs `price` and `table` vs `price` — these should look weak/flat, showing they're much less informative than carat/size. Worth having as a contrast to the strong ones.
- Correlation heatmap of numeric features. Expect `carat`, `x`, `y`, `z` to be highly correlated with each other (~0.9+) — flag this now, decide later whether to keep all four or drop redundant ones.

### 4. Categorical features vs target
- Boxplot of `price` by `cut`. Slightly counterintuitive result to look for: "Fair" cut diamonds sometimes have *higher* median price than "Ideal" — because cut alone doesn't control for carat. Good talking point for why multivariate models (like GBM) matter over single-feature comparisons.
- Boxplot of `price` by `color` and by `clarity` — similar story, look for non-monotonic quirks and note them.
- Bar chart of category counts (`cut`, `color`, `clarity`) — check for class imbalance (e.g. "Ideal" cut is usually the most common category by far).

### 5. Interaction check (the important one)
- Scatter plot `carat` vs `price`, colored by `cut` (or by `clarity`). This is where the real story is: at the same carat weight, better cut/clarity diamonds command higher prices. This interaction is exactly what a boosted tree model can pick up automatically but a plain linear model can't without manual feature engineering — good one to reference later when comparing model results.

### 6. Outlier / data quality check
- Filter rows where `x == 0`, `y == 0`, or `z == 0` — these are data entry errors (a diamond can't have zero physical dimension). Count them, decide to drop them.
- Check for `depth` or `table` values far outside the typical range (roughly 50–70% and 50–70 respectively) — these are likely mismeasured or bad entries, not real signal.

---

## Preprocessing

1. **Drop the index column** (`Unnamed: 0` or similar).
2. **Handle bad rows** — drop rows where `x`, `y`, or `z` == 0 (physically invalid).
3. **Encode ordinal categoricals properly** — don't one-hot `cut`, `color`, `clarity`; they have a real order, so map them to integers respecting that order:
   - `cut`: Fair < Good < Very Good < Premium < Ideal
   - `color`: J < I < H < G < F < E < D
   - `clarity`: I1 < SI2 < SI1 < VS2 < VS1 < VVS2 < VVS1 < IF
   - (This is a good contrast case to try one-hot as well, and compare — trees usually don't care much, linear models will.)
4. **Train/test split** — 80/20, fixed `random_state`. With ~54k rows you can afford a slightly larger held-out set if you want more stable evaluation (e.g. 75/25).
5. **No scaling needed for GBM** — skip standardization unless you're also running a linear/distance-based baseline for comparison.
6. **Optional: log-transform `price`** — given the skew observed in EDA, train one version on raw `price` and one on `log1p(price)`, compare error metrics on the same original scale (`expm1` back before computing RMSE) to see if it actually helps GBM (it usually helps linear models more than trees).
7. **Optional: multicollinearity decision** — since `carat`, `x`, `y`, `z` are highly correlated, try dropping `x`, `y`, `z` and keeping only `carat` + `depth` + `table` as a leaner feature set, and compare against using all of them. Trees handle collinearity gracefully, so this is more of a "does it even matter" experiment than a necessity.

---

## Suggested workflow

1. Load → run full EDA above → write down 2-3 concrete observations (e.g. "carat is the dominant driver," "cut/color/clarity show non-monotonic patterns without controlling for size")
2. Clean bad rows, encode ordinals, split
3. Baseline: `LinearRegression` (try both raw and log-target versions)
4. Main event: `GradientBoostingRegressor` (or XGBoost/LightGBM), default params first
5. Compare RMSE / MAE / R² across: linear (raw), linear (log target), GBM (raw), GBM (log target)
6. Light tuning: `n_estimators`, `max_depth`, `learning_rate` — enough to see the effect on validation error, not a full grid search
7. Feature importance plot — confirm `carat` dominates, then check where `clarity`/`color`/`cut` rank relative to `depth`/`table`
8. Residual plot (predicted vs actual, and residuals vs `carat`) — check if errors grow for very expensive diamonds, which is common and worth noting
