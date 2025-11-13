import argparse
import glob
import sqlite3

# Get the argument from launch.json or terminal
parser = argparse.ArgumentParser()
parser.add_argument("--db_pattern")
args = parser.parse_args()
pattern = args.db_pattern
print(f"Database pattern: {pattern}")
# Expand the pattern (find matching DB files)
# db_list = glob.glob(pattern)

# if not db_list:
#     print("❌ No database files found. Check your pattern.")
# else:
#     print("✅ Found databases:")
#     for db in db_list:
#         print(" -", db)

#     # Go through each DB file
#     for db in db_list:
#         try:
#             conn = sqlite3.connect(db)
#             cur = conn.cursor()
#             print(f"\n📂 Connected to: {db}")

#             # Example queries — adjust column names if needed
#             cur.execute("SELECT MAX(device_temperature) FROM Snapshots;")
#             max_temp = cur.fetchone()[0]

#             cur.execute("""
#                 SELECT time
#                 FROM Snapshots
#                 WHERE device_temperature = (SELECT MAX(device_temperature) FROM Snapshots)
#                 LIMIT 1;
#             """)
#             time_max = cur.fetchone()[0]

#             cur.execute("SELECT COUNT(*) FROM Detections;")
#             detections = cur.fetchone()[0]

#             print(f"  🔥 Max temperature: {max_temp}")
#             print(f"  🕒 Time of max temp: {time_max}")
#             print(f"  🎯 Detections: {detections}")

#         except Exception as e:
#             print(f"⚠️ Error with {db}: {e}")
#         finally:
#             conn.close()
