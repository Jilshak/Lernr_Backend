# Lernr Backend Setup Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git
- Redis server (for WebSocket functionality)
- Stripe account (for payment processing)
- Firebase account (for media storage)

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Lernr_Backend
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Configuration

Create a `.env` file in the project root directory with the following variables:

```env
# Django settings
secret_key=your_super_secret_django_key_here
debug=True

# Redis connection (for WebSockets)
redis=redis://127.0.0.1:6379/0

# Email settings (for password reset)
email_host=smtp.gmail.com
email_port=587
email_host_user=your_email@gmail.com
email_host_password=your_app_password
email_use_tls=True
email_from=your_email@gmail.com

# Stripe settings
stripe_secret_key=your_stripe_secret_key_here

# Firebase settings (optional, for media storage)
firebase_config={"apiKey": "...", "authDomain": "...", "projectId": "...", "storageBucket": "...", "messagingSenderId": "...", "appId": "..."}
```

### 5. Database Setup

```bash
# Create database migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (optional but recommended)
python manage.py createsuperuser
```

### 6. Start Redis Server

Make sure Redis is running on your system:

```bash
# On Windows (if using Redis for Windows)
redis-server

# On macOS (with Homebrew)
brew services start redis

# On Linux
sudo systemctl start redis
```

### 7. Run the Development Server

For development with WebSocket support:

```bash
daphne -p 8000 lernr.asgi:application
```

Or for simple HTTP development:

```bash
python manage.py runserver
```

## Testing the Installation

1. Visit `http://127.0.0.1:8000/admin/` to access the Django admin panel
2. Visit `http://127.0.0.1:8000/` to access the API root

## Common Issues and Solutions

### 1. ModuleNotFoundError

If you encounter import errors, make sure all dependencies are installed:

```bash
pip install -r requirements.txt
```

### 2. Redis Connection Error

Ensure Redis server is running:

```bash
redis-cli ping
```

Should return `PONG` if Redis is running correctly.

### 3. Database Migration Issues

If you encounter migration issues:

```bash
python manage.py makemigrations --merge
python manage.py migrate
```

### 4. Media File Upload Issues

Ensure the `media` directory exists in the project root:

```bash
mkdir media
```

## Development Workflow

1. Activate virtual environment
2. Start Redis server
3. Run development server
4. Make code changes
5. Create migrations if models changed
6. Test API endpoints

## API Testing

You can test the API endpoints using tools like:

- Postman
- curl
- Django REST Framework browsable API (visit endpoints in browser)

Example curl request for user authentication:

```bash
curl -X POST http://127.0.0.1:8000/token/ \
     -H "Content-Type: application/json" \
     -d '{"email": "user@example.com", "password": "password123"}'
```

## Next Steps

1. Explore the admin panel at `/admin/`
2. Review the API documentation
3. Test WebSocket functionality
4. Integrate with the frontend application
5. Configure production settings for deployment