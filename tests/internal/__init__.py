MOCK_HOST = "http://localhost:9999"
MEMBER_ID = "fake-member-id"
TOKEN = "fake-token"
MOCK_CONFIG = {"host": MOCK_HOST, "church_id": "test-chuch"}

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
