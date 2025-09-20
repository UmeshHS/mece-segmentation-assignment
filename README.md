# mece-segmentation-assignment

# Cart Abandoner MECE Audience Segmentation

## Overview
This project implements a Mutually Exclusive, Collectively Exhaustive (MECE) segmentation system for users who abandoned shopping carts. It segments users to help marketers run targeted retention campaigns based on user behavior and engagement metrics.

## Features
- Filters users who abandoned carts in the last 7 days.
- Creates MECE audience segments based on Avg Order Value (AOV) and engagement scores.
- Enforces segment size constraints for practical marketing use.
- Computes multiple audience scores: conversion potential, profitability, size ratio, and overall weighted score.
- Outputs clean CSV summary for marketing strategy.

## Dataset
The input dataset contains the following fields:
- `user_id` - Unique user identifier
- `cart_abandoned_date` - Cart abandonment date
- `last_order_date` - Last order date
- `avg_order_value` - Average order value per user
- `sessions_last_30d` - Number of sessions in last 30 days
- `num_cart_items` - Number of items in abandoned cart
- `engagement_score` - User engagement score
- `profitability_score` - User profitability score

## How To Run

1. Ensure you have Python 3.x installed.
2. Install required package:
    pip install pandas
3. Add your dataset CSV file (e.g., `cart_abandonment_demo.csv`) to the project directory.
4. Run the segmentation script:
    python segment_audience.py
5. The script outputs a segment summary CSV file (`audience_segments_output.csv`).

## Script Explanation
- Filters data for the last 7 days' cart abandoners.
- Segments users into high AOV, mid AOV & engagement, and an 'Other' bucket.
- Checks segment sizes against min (500) and max (20,000) thresholds.
- Calculates conversion potential, profitability, size ratio, and overall weighted score per segment.
- Flags segment validity based on size.

## Limitations & Future Work
- Current dataset and thresholds can be adapted for larger or real datasets.
- Future improvements could include ML-driven dynamic segmentation and downstream campaign lift analysis.

## Contact
For questions or contributions, feel free to reach out via GitHub issues or email.

---
