MOCK_HOST = "http://localhost:9999"
MOCK_CHURCH_ID = "test-church"
MEMBER_ID = "fake-member-id"
TOKEN = "fake-token"
USER = "fake-user"
PASSWORD = "fake-password"
MOCK_CONFIG = {"host": MOCK_HOST, "church_id": MOCK_CHURCH_ID}

MOCK_MEMBER = {
    "id": MEMBER_ID,
    "active": False,
    "classification": "Adult",
    "person": {
        "firstName": "John",
        "lastName": "Doe",
        "fullName": "John Doe",
        "gender": "M",
        "age": 30,
        "birthDate": "2011-03-16T03:00:00Z",
        "contact": {"phone": "(11) 12345678"},
        "address": {
            "zipCode": "00000-000",
            "state": "SP",
            "city": "São Paulo",
            "address": "Beco do Batman",
            "district": "Pinheiros",
            "number": 2023,
            "full": "Rua Beco do Batman, 2023 - Pinheiros",
        },
    },
}
