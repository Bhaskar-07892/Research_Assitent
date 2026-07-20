import sqlite3
import pickle
from langchain_core.documents import Document


class SQLiteDocStore:
    def __init__(self, db_path="data/parent_chunk/docstore.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS parent_docs (
                doc_id TEXT PRIMARY KEY,
                document BLOB
            )
        """)

        self.conn.commit()

    def mset(self, pairs):
        for doc_id, doc in pairs:
            binary_doc = pickle.dumps(doc)

            self.cursor.execute(
                """
                INSERT OR REPLACE INTO parent_docs
                (doc_id, document)
                VALUES (?, ?)
                """,
                (doc_id, binary_doc),
            )

        self.conn.commit()

    def mget(self, ids):
        docs = []

        for doc_id in ids:
            self.cursor.execute(
                "SELECT document FROM parent_docs WHERE doc_id=?",
                (doc_id,),
            )

            row = self.cursor.fetchone()

            if row:
                docs.append(pickle.loads(row[0]))
            else:
                docs.append(None)

        return docs

    def close(self):
        self.conn.close()