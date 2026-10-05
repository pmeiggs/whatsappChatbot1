# Maps incoming keywords and button IDs to predetermined replies
RESPONSES = {
    "hi": {
        "body": "Welcome! Choose an option:",
        "buttons": [
            {"id": "hours", "title": "Opening hours"},
            {"id": "location", "title": "Location"},
            {"id": "contact", "title": "Contact us"},
        ],
    },
    "hours": {
        "body": "We're open Mon-Fri, 9am-5pm.",
        "buttons": [
            {"id": "hi", "title": "Back to menu"},
        ],
    },
    "location": {
        "body": "We're located at 123 Example Street.",
        "buttons": [
            {"id": "hi", "title": "Back to menu"},
        ],
    },
    "contact": {
        "body": "Email us at hello@example.com.",
        "buttons": [
            {"id": "hi", "title": "Back to menu"},
        ],
    },
}
