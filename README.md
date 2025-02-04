# Simple Chat
## Installation
### Prerequisites

Before you can run this project, make sure you have the following installed:

- Python 3.12 or higher
- Django 5.1.5
- pip (Python package installer)

### Running the app with Python
```shell
git clone https://github.com/bodyabandura/sample-chat.git
cd sample_chat

# on macOS
python3 -m venv venv
source venv/bin/activate

# on Windows
python -m venv venv
venv\Scripts\activate

# next commands after venv
pip install -r requirements.txt

python manage.py migrate

uvicorn sample_chat.asgi:application # Starts uvicorn server
(Chat login will be available at http://127.0.0.1:8000/chat/)

```
