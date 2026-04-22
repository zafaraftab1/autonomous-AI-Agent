# Purpose: Example tool that agent can call (simulates DB/API)

def get_user_details(user_id: str) -> str:
    """
    Simulates fetching user data from database
    """

    fake_db = {
        "1": {"name": "Aftab", "role": "AI Engineer"},
        "2": {"name": "John", "role": "DevOps Engineer"},
    }

    user = fake_db.get(user_id)

    if not user:
        return "User not found"

    return f"Name: {user['name']}, Role: {user['role']}"