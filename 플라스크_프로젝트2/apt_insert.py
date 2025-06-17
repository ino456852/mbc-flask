import pymongo
import pandas as pd

# MongoDB 연결
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["apartment_db"]
collection = db["sales_data"]

# 실거래가 데이터 (CSV 파일 예시)
df = pd.read_excel("./아파트(매매)_실거래가_2024년전체.xlsx")

# 데이터 삽입 (insertMany 사용)
data = df.to_dict("records")
collection.insert_many(data)

print("데이터 삽입 완료!")