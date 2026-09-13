import sqlite3

# Connect to database (creates test.db automatically)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Run the CREATE TABLE command
cursor.execute("""
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER,
    name TEXT,
    created_at DATE,
    published BOOLEAN
);
""")

# Check the table structure
cursor.execute("PRAGMA table_info(videos);")
columns = cursor.fetchall()

print("TABLE 'videos' CREATED SUCCESSFULLY!")
print("-" * 40)
print(f"{'CID':<5} {'NAME':<12} {'TYPE':<10}")
print("-" * 40)
for col in columns:
    print(f"{col[0]:<5} {col[1]:<12} {col[2]:<10}")

conn.close()