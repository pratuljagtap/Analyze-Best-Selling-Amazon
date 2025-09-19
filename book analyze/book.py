
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print(" Loading Amazon Bestsellers data...")
df = pd.read_csv('C:\\(yourfile path)\\bestsellers.csv')

print("\n First 5 rows:")
print(df.head())

print(f"\n Shape: {df.shape}")
print(f"\n🏷 Columns: {list(df.columns)}")
print(f"\n Summary stats:")
print(df.describe())

#  Clean data
print("\n Dropping duplicates...")
df.drop_duplicates(inplace=True)


df.rename(columns={
    "Name": "Title",
    "Year": "Publication Year",
    "User Rating": "Rating"
}, inplace=True)


df["Price"] = df["Price"].astype(float)

print("\n Top 10 Authors by # of Bestsellers:")
author_counts = df['Author'].value_counts()
print(author_counts.head(10))

print("\n Average Rating by Genre:")
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)


print("\n Exporting data...")

# Create exports folder if doesn't exist
os.makedirs('exports', exist_ok=True)

author_counts.head(10).to_csv("exports/top_authors.csv", header=["Book Count"])
avg_rating_by_genre.to_csv("exports/avg_rating_by_genre.csv", header=["Average Rating"])


plt.figure(figsize=(12, 6))
top_authors = author_counts.head(10)
bars = plt.barh(top_authors.index, top_authors.values, color='#FF9900', edgecolor='black')
plt.title(' Top 10 Authors by Number of Bestsellers', fontsize=16, fontweight='bold')
plt.xlabel('Number of Bestsellers')
plt.ylabel('Author')
plt.gca().invert_yaxis()  # Highest on top
for bar in bars:
    plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
             f'{int(bar.get_width())}', va='center', fontweight='bold')
plt.tight_layout()
# Create charts folder if doesn't exist
os.makedirs('charts', exist_ok=True)
plt.savefig('charts/top_authors.png', dpi=300)
plt.show()


plt.figure(figsize=(8, 5))
genre_ratings = avg_rating_by_genre.reset_index()
bars = plt.bar(genre_ratings['Genre'], genre_ratings['Rating'], color=['#3498db', '#e74c3c'], edgecolor='black')
plt.title('Average User Rating by Genre', fontsize=16, fontweight='bold')
plt.ylabel('Average Rating')
plt.ylim(0, 5)
for bar in bars:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
             f'{bar.get_height():.2f}', ha='center', fontweight='bold')
plt.tight_layout()
# Create charts folder if doesn't exist
os.makedirs('charts', exist_ok=True)
plt.savefig('charts/avg_rating_by_genre.png', dpi=300)
plt.show()

print("\n Done! Charts saved in /charts, exports in /exports.")
