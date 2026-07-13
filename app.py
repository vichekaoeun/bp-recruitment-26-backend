"""
Orders API — starter file

Fill in the four endpoint handlers below.
Your server must listen on port 3000.

You can use any framework (Flask, FastAPI, etc.) or the stdlib http.server.
If you switch frameworks, make sure to update requirements.txt.
"""

import json
import sqlite3
from datetime import datetime, timezone
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

# ── Database setup ───────────────────────────────────────────────────────────

def get_db():
    """Return a connection to the in-memory database."""
    db = sqlite3.connect(":memory:")
    db.row_factory = sqlite3.Row
    db.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_email TEXT NOT NULL,
            amount REAL NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending',
            created_at TEXT NOT NULL
        )
    """)
    return db


# ── HTTP handler ─────────────────────────────────────────────────────────────

class OrderHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        # TODO: Implement POST /orders
        #
        # 1. Parse JSON body
        # 2. Validate: customer_email (string, required), amount (positive number, required)
        #    - status is optional, defaults to "pending"
        # 3. Insert into database
        # 4. Return 201 with the created order (include id and created_at)
        # 5. Return 400 with {"error": "..."} for invalid payloads
        #
        self.send_response(501)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"error": "not implemented"}).encode())

    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/orders":
            # TODO: Implement GET /orders
            #
            # 1. Query all orders (or filter by ?status= if provided)
            # 2. Return 200 with JSON array
            #
            self.send_response(501)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "not implemented"}).encode())

        elif parsed.path.startswith("/orders/"):
            # TODO: Implement GET /orders/<id>
            #
            # 1. Extract id from URL
            # 2. Look up order in database
            # 3. Return 200 with order if found
            # 4. Return 404 with {"error": "not found"} if not
            #
            self.send_response(501)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "not implemented"}).encode())

        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "not found"}).encode())

    def do_PATCH(self):
        parsed = urlparse(self.path)

        if parsed.path.startswith("/orders/"):
            # TODO: Implement PATCH /orders/<id>
            #
            # 1. Extract id from URL
            # 2. Parse JSON body — must contain "status"
            # 3. Update the order's status in the database
            # 4. Return 200 with updated order
            # 5. Return 400 if status is missing/invalid
            # 6. Return 404 if order not found
            #
            self.send_response(501)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "not implemented"}).encode())
        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "not found"}).encode())

    def log_message(self, format, *args):
        """Suppress default logging."""
        pass


# ── Start server ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 3000), OrderHandler)
    print("Listening on port 3000")
    server.serve_forever()
