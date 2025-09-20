# 1. Import libraries
import pandas as pd
from datetime import datetime, timedelta
from google.colab import files

# 2. Upload CSV file
print("Please upload your cart_abandonment_demo.csv file")
uploaded = files.upload()

# 3. Load data
df = pd.read_csv('cart_abandonment_demo.csv')

# 4. Define Universe: users who abandoned carts in last 7 days
cutoff = datetime.strptime('2025-09-20', '%Y-%m-%d') - timedelta(days=7)
df['cart_abandoned_date'] = pd.to_datetime(df['cart_abandoned_date'])
universe = df[df['cart_abandoned_date'] >= cutoff].copy()

# 5. MECE Segmentation logic
def segment(row):
    if row['avg_order_value'] > 3000:
        return 'High AOV Abandoners'
    elif 1000 < row['avg_order_value'] <= 3000 and row['engagement_score'] > 0.5:
        return 'Mid AOV Engaged'
    else:
        return 'Other Bucket'
universe['Segment Name'] = universe.apply(segment, axis=1)

# 6. Apply size constraints
seg_sizes = universe['Segment Name'].value_counts()
valid_segs = seg_sizes[(seg_sizes >= 500) & (seg_sizes <= 20000)].index
universe['Valid'] = universe['Segment Name'].apply(lambda x: 'Yes' if x in valid_segs else 'No')

# 7. Calculate scores per segment
total_size = len(universe)
grouped = universe.groupby('Segment Name')
result = []
for name, group in grouped:
    size = len(group)
    conv_pot = round(group['engagement_score'].mean(), 2)
    profitability = round(group['profitability_score'].mean(), 2)
    size_ratio = size / total_size
    overall_score = round(0.4*conv_pot + 0.3*profitability + 0.3*size_ratio, 2)

    if name == 'High AOV Abandoners':
        rules = 'AOV > 3000'
    elif name == 'Mid AOV Engaged':
        rules = '1000 < AOV ≤ 3000 & Engagement > 0.5'
    else:
        rules = 'ELSE'

    valid = 'Yes' if 5 <= size <= 20000 else 'No'

    result.append({
        'Segment Name': name,
        'Rules Applied': rules,
        'Size': size,
        'Conv_Pot': conv_pot,
        'Profitability': profitability,
        'Overall Score': overall_score,
        'Valid': valid
    })

seg_df = pd.DataFrame(result)

# 8. Show segment summary
print(seg_df)

# 9. Export results CSV
seg_df.to_csv('audience_segments_output.csv', index=False)
print("Segment summary saved as 'audience_segments_output.csv'")

# 10. Download output file
files.download('audience_segments_output.csv')
