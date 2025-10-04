# Lernr Backend Architecture

## High-Level Architecture

```mermaid
graph TB
    A[Frontend Applications] --> B[API Gateway]
    B --> C[Django REST Framework API]
    C --> D[(Database<br/>SQLite/PostgreSQL)]
    C --> E[Redis<br/>Channel Layer]
    C --> F[Stripe API]
    C --> G[Firebase Storage]
    H[WebSocket Clients] --> I[Django Channels]
    I --> E
    I --> C
```

## Component Details

### 1. Django Core Components

#### Main Project (lernr)
- **settings.py**: Configuration including database, authentication, middleware
- **urls.py**: Main URL routing to apps
- **asgi.py**: ASGI configuration for WebSocket support
- **routing.py**: WebSocket routing configuration
- **wsgi.py**: WSGI configuration for HTTP requests

#### Apps Structure

1. **Users App**
   - Custom user model with email-based authentication
   - JWT token management
   - Password reset functionality
   - Profile management

2. **Courses App**
   - Course creation and management
   - Video content handling
   - Progress tracking
   - Reviews and ratings
   - Shopping cart functionality

3. **Community App**
   - Real-time messaging system
   - Chat consumers for WebSocket handling

4. **Payments App**
   - Stripe integration for course purchases
   - Payment session creation

### 2. Data Layer

#### Database Models Relationships

```mermaid
graph LR
    A[CustomUser] --> B[Courses]
    A --> C[Reviews]
    A --> D[CartItem]
    A --> E[CoursesBought]
    A --> F[Messages]
    A --> G[CourseLessonProgress]
    B --> H[CourseVideo]
    B --> I[Category]
    B --> J[Reviews]
    B --> K[Quiz]
    H --> G
```

### 3. External Services Integration

1. **Stripe API**
   - Payment processing for course purchases
   - Product and price management

2. **Firebase Storage**
   - Media file storage (course thumbnails, videos, profile images)

3. **Redis**
   - Channel layer for WebSocket communication
   - Caching (potential future use)

4. **SMTP Server**
   - Email delivery for password reset functionality

### 4. Authentication Flow

```mermaid
sequenceDiagram
    participant U as User
    participant A as API
    participant S as Stripe
    participant F as Firebase
    
    U->>A: Register/Login
    A->>U: JWT Tokens
    U->>A: Access Protected Routes
    A->>A: Validate JWT
    U->>A: Request Payment
    A->>S: Create Payment Session
    S->>A: Session Details
    A->>U: Redirect to Stripe
    U->>S: Complete Payment
    S->>A: Webhook/Confirmation
    A->>A: Enroll User in Course
```

### 5. Real-time Messaging Flow

```mermaid
sequenceDiagram
    participant U1 as User 1
    participant U2 as User 2
    participant WS as WebSocket Server
    participant R as Redis
    participant DB as Database
    
    U1->>WS: Connect to Chat Room
    U2->>WS: Connect to Chat Room
    WS->>R: Join Room Group
    U1->>WS: Send Message
    WS->>R: Broadcast to Room
    R->>U2: Deliver Message
    WS->>DB: Persist Message
```

## API Layer Structure

### REST Endpoints Organization

```
/api/
├── /token/                    # Authentication
├── /user/                     # User management
├── /courses/                  # Course management
│   ├── /course/              # Courses CRUD
│   ├── /category/            # Categories CRUD
│   ├── /review/              # Reviews CRUD
│   ├── /cartItem/            # Cart management
│   ├── /bought_courses/      # Purchased courses
│   ├── /course_video/        # Course videos
│   ├── /course_lessons/      # Lesson progress
│   └── /quiz/                # Course quizzes
├── /community/               # Community features
│   └── /messages/            # Messaging
└── /payments/                # Payment processing
    ├── /stripe/              # Single course payment
    └── /stripe_cart/         # Cart payment
```

## Deployment Architecture

```mermaid
graph TB
    LB[Load Balancer] --> WS1[Django Server 1]
    LB --> WS2[Django Server 2]
    LB --> WSN[Django Server N]
    
    WS1 --> DB[(Database)]
    WS2 --> DB
    WSN --> DB
    
    WS1 --> R[(Redis)]
    WS2 --> R
    WSN --> R
    
    subgraph Application Servers
        WS1
        WS2
        WSN
    end
    
    subgraph Services
        DB
        R
        S[Stripe API]
        F[Firebase Storage]
    end
```

This architecture supports horizontal scaling with multiple Django instances sharing the same database and Redis instance for WebSocket communication.