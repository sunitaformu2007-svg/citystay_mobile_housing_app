
import sqlite3
import json

class Booking:
    DB_NAME = 'bookings.db'

    def __init__(self, booking_id, tenant_id, landlord_id, property_id, group_rental=False, group_members=None, status='pending'):
        self.booking_id = booking_id
        self.tenant_id = tenant_id
        self.landlord_id = landlord_id
        self.property_id = property_id
        self.group_rental = group_rental
        self.group_members = group_members if group_members else []
        self.status = status

    @staticmethod
    def init_db():
        conn = sqlite3.connect(Booking.DB_NAME)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS bookings (
            booking_id TEXT PRIMARY KEY,
            tenant_id TEXT,
            landlord_id TEXT,
            property_id TEXT,
            group_rental INTEGER,
            group_members TEXT,
            status TEXT
        )''')
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect(Booking.DB_NAME)
        c = conn.cursor()
        c.execute('''REPLACE INTO bookings (booking_id, tenant_id, landlord_id, property_id, group_rental, group_members, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)''',
            (self.booking_id, self.tenant_id, self.landlord_id, self.property_id,
             int(self.group_rental), json.dumps(self.group_members), self.status))
        conn.commit()
        conn.close()

    @staticmethod
    def load(booking_id):
        conn = sqlite3.connect(Booking.DB_NAME)
        c = conn.cursor()
        c.execute('SELECT * FROM bookings WHERE booking_id=?', (booking_id,))
        row = c.fetchone()
        conn.close()
        if row:
            return Booking(
                booking_id=row[0],
                tenant_id=row[1],
                landlord_id=row[2],
                property_id=row[3],
                group_rental=bool(row[4]),
                group_members=json.loads(row[5]),
                status=row[6]
