import os

path = r"C:/Users/HP/OneDrive/Desktop/train_test_network.csv"
print(os.path.exists(path)) 

import pandas as pd
import numpy as np

print("=" * 65)
print("STEP 1 — LOADING DATA")
print("=" * 65)

df = pd.read_csv(path)
print(df.shape)

print(f"Shape           : {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"Memory usage    : {df.memory_usage(deep=True).sum() / 1e6:.1f} MB")
print("\nFirst 3 rows:")
print(df.head(3).to_string())
print("\nData Types:")
print(df.dtypes.to_string())


print("\n" + "=" * 65)
print("STEP 2 — HANDLING MISSING VALUES")
print("=" * 65)


nan_counts = df.isnull().sum()
print(f"\nTrue NaN count across all columns : {nan_counts.sum()}")
if nan_counts.sum() > 0:
    print(nan_counts[nan_counts > 0])

cat_cols = df.select_dtypes(include=["object"]).columns.tolist()

dash_report = {}
for col in cat_cols:
    count = (df[col] == "-").sum()
    if count > 0:
        pct = count / len(df) * 100
        dash_report[col] = {"dash_count": count, "pct": round(pct, 1)}

print(f"\nColumns with '-' placeholder (implicit missing):")
for col, info in dash_report.items():
    print(f"  {col:<30} {info['dash_count']:>7,} rows  ({info['pct']}%)")

df.replace("-", np.nan, inplace=True)

# Columns where ≥95 % rows are '-' are nearly empty → drop them
high_missing_cols = [
    col for col, info in dash_report.items() if info["pct"] >= 95
]
print(f"\nDropping {len(high_missing_cols)} near-empty columns (≥95% missing):")
print("  ", high_missing_cols)
df.drop(columns=high_missing_cols, inplace=True)

remaining_cat = df.select_dtypes(include=["object"]).columns.tolist()
for col in remaining_cat:
    missing = df[col].isnull().sum()
    if missing > 0:
        df[col] = df[col].fillna("Unknown")   # assignment works with Copy-on-Write
        print(f"  Filled {missing:,} NaN in '{col}' with 'Unknown'")

num_cols = df.select_dtypes(include=[np.number]).columns.tolist()

num_cols_for_fill = [c for c in num_cols if c != "label"]
for col in num_cols_for_fill:
    missing = df[col].isnull().sum()
    if missing > 0:
        median_val = df[col].median()
        df[col].fillna(median_val, inplace=True)
        print(f"  Filled {missing:,} NaN in '{col}' with median={median_val}")

print(f"\nTotal NaN remaining after treatment : {df.isnull().sum().sum()}")
print(f"Shape after missing value handling  : {df.shape}")


print("\n" + "=" * 65)
print("STEP 3 — HANDLING OUTLIERS")
print("=" * 65)

# Columns to check for outliers (exclude ID-like, port, label, flag cols)
skip_outlier_cols = {"src_port", "dst_port", "label",
                     "dns_qclass", "dns_qtype", "dns_rcode",
                     "http_status_code"}
outlier_target_cols = [
    c for c in num_cols if c not in skip_outlier_cols
]

print(f"\nApplying IQR-based capping to {len(outlier_target_cols)} numeric columns:")
print("  Method: Winsorization (clip values to [Q1 - 1.5×IQR, Q3 + 1.5×IQR])\n")

outlier_summary = []

for col in outlier_target_cols:
    Q1  = df[col].quantile(0.25)
    Q3  = df[col].quantile(0.75)
    IQR = Q3 - Q1

    if IQR == 0:
        outlier_summary.append({
            "column": col,
            "lower_bound": Q1,
            "upper_bound": Q3,
            "outliers_found": 0,
            "action": "skipped (IQR=0)"
        })
        continue

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    mask = (df[col] < lower) | (df[col] > upper)
    n_outliers = mask.sum()

    df[col] = df[col].clip(lower=lower, upper=upper)

    outlier_summary.append({
        "column": col,
        "lower_bound": round(lower, 4),
        "upper_bound": round(upper, 4),
        "outliers_found": n_outliers,
        "action": "capped" if n_outliers > 0 else "none found"
    })

report_df = pd.DataFrame(outlier_summary) 

report_df["pct"] = (report_df["outliers_found"] / len(df) * 100).round(2)
print(report_df.to_string(index=False))

print("\n" + "=" * 65)
print("STEP 4 — FINAL SUMMARY")
print("=" * 65)

print(f"\nFinal Shape        : {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"Remaining NaN      : {df.isnull().sum().sum()}")
print(f"Total outliers capped : {report_df['outliers_found'].sum():,}")
print(f"Columns dropped    : {len(high_missing_cols)}")

print("\nFinal column list:")
print(list(df.columns))

print("\nDescriptive statistics (numeric columns):")
print(df[outlier_target_cols].describe().round(2).to_string())

output_path = "train_test_network_clean.csv"
df.to_csv(output_path, index=False)
print(f"\n Clean dataset saved to: {output_path}")
