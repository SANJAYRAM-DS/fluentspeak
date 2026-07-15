# PostgreSQL Database Setup Guide — FluentFlow AI

This is a step-by-step guide to set up the PostgreSQL database for the FluentFlow AI project on Windows.

---

## Table of Contents

1. [Install PostgreSQL](#1-install-postgresql)
2. [Open the PostgreSQL shell](#2-open-the-postgresql-shell)
3. [Create the database and user](#3-create-the-database-and-user)
4. [Configure your `.env` file](#4-configure-your-env-file)
5. [Run Django migrations](#5-run-django-migrations)
6. [Seed the topics](#6-seed-the-topics)
7. [Create a superuser](#7-create-a-superuser)
8. [Start the server](#8-start-the-server)
9. [Full SQL reference](#9-full-sql-reference)

---

## 1. Install PostgreSQL

### Option A: Windows installer (recommended)

1. Go to https://www.postgresql.org/download/windows/
2. Download the installer from **EDB** (EnterpriseDB)
3. Run the installer
4. During installation:
   - Choose the installation directory (default is fine)
   - **Set a password for the `postgres` superuser** — remember this, you'll need it
   - Keep the default port `5432`
   - Keep the default locale
5. Complete the installation

### Option B: Using Chocolatey

```powershell
choco install postgresql -y
```

### Option C: Using Scoop

```powershell
scoop install postgresql
```

After installation, make sure the PostgreSQL service is running:

```powershell
# Check if PostgreSQL is running
Get-Service -Name "postgresql*"

# If it's not running, start it
Start-Service -Name "postgresql-x64-17"   # version number may differ
```

---

## 2. Open the PostgreSQL shell

Open PowerShell or Command Prompt and connect to PostgreSQL:

```powershell
# Using psql (installed with PostgreSQL)
psql -U postgres
```

It will ask for the password you set during installation.

> **If `psql` is not found**, add the PostgreSQL bin directory to your PATH:
> ```powershell
> # Typical location — adjust the version number
> $env:PATH += ";C:\Program Files\PostgreSQL\17\bin"
> ```
> Or add it permanently via System Properties → Environment Variables → Path.

---

## 3. Create the database and user

Once inside the `psql` shell (`postgres=#`), run these commands one by one:

### Step 3a: Create the database

```sql
CREATE DATABASE fluentspeak;
```

### Step 3b: Create a dedicated user (optional but recommended)

```sql
CREATE USER fluentspeak_user WITH PASSWORD 'your_secure_password_here';
```

### Step 3c: Grant all privileges on the database to the user

```sql
GRANT ALL PRIVILEGES ON DATABASE fluentspeak TO fluentspeak_user;
```

### Step 3d: Grant schema permissions (PostgreSQL 15+ requires this)

```sql
\c fluentspeak
GRANT ALL ON SCHEMA public TO fluentspeak_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO fluentspeak_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO fluentspeak_user;
```

### Step 3e: Exit psql

```sql
\q
```

### Quick one-liner version (if you just want to use the `postgres` superuser)

If you don't want a separate user and just want to use the default `postgres` user:

```sql
CREATE DATABASE fluentspeak;
```

That's it. Just set `POSTGRES_USER=postgres` and `POSTGRES_PASSWORD=<your postgres password>` in your `.env`.

---

## 4. Configure your `.env` file

Open `backend/.env` and fill in your PostgreSQL credentials:

```env
# Django
DJANGO_SECRET_KEY=change-me-to-a-long-random-string
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

# PostgreSQL
POSTGRES_DB=fluentspeak
POSTGRES_USER=postgres                    # or fluentspeak_user if you created one
POSTGRES_PASSWORD=YOUR_PASSWORD_HERE      # ← replace with your actual password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Groq API keys (already filled)
api1 = "gsk_..."
api2 = "gsk_..."
api3 = "gsk_..."
api4 = "gsk_..."
api5 = "gsk_..."

# Redis (for Celery)
CELERY_BROKER_URL=redis://localhost:6379/0

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:5500,http://127.0.0.1:5500
```

### What each variable does

| Variable | Purpose | Example |
|----------|---------|---------|
| `DJANGO_SECRET_KEY` | Django's cryptographic signing key. Must be random and unique. | `kj3h2fsd98h2kj3h45k2j3h5` |
| `DJANGO_DEBUG` | Enables debug mode with detailed error pages. Set to `False` in production. | `True` |
| `POSTGRES_DB` | Name of the PostgreSQL database | `fluentspeak` |
| `POSTGRES_USER` | PostgreSQL username | `postgres` |
| `POSTGRES_PASSWORD` | PostgreSQL password | `mysecurepassword` |
| `POSTGRES_HOST` | Database server address | `localhost` |
| `POSTGRES_PORT` | Database server port | `5432` |

### How to generate a secure Django secret key

Run this in Python:

```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Or if Django isn't installed yet:

```python
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

---

## 5. Run Django migrations

From the `backend/` directory, with your virtual environment activated:

```powershell
# Navigate to backend
cd e:\fluentspeak\backend

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run migrations — this creates all the tables
python manage.py migrate
```

This will create the following tables in your `fluentspeak` database:

| Table | Description |
|-------|-------------|
| `users` | User accounts (email, password_hash, is_active, etc.) |
| `user_profiles` | Profile data (full_name, level, daily_goal, timezone) |
| `user_progress` | Learning stats (conversations_completed, words_learned, streak) |
| `topics` | 50 conversation topics |
| `scenarios` | User-created roleplay scenarios |
| `conversations` | Conversation sessions |
| `messages` | Individual messages within conversations |
| `message_feedback` | AI corrections and optimized responses |
| `conversation_states` | Conversation state tracking |
| `vocabulary_words` | Global vocabulary dictionary |
| `user_vocabulary` | Per-user vocabulary tracking |
| `ai_providers` | AI provider configuration |
| `audit_logs` | Activity audit trail |
| `analytics_events` | Analytics event storage |
| `notifications` | User notifications |

Plus Django's built-in tables for sessions, tokens, permissions, etc.

---

## 6. Seed the topics

Load the 50 predefined conversation topics:

```powershell
python manage.py seed_topics
```

You should see: `Seeded topics: 50 created, 0 updated`

---

## 7. Create a superuser

Create an admin account for testing:

```powershell
python manage.py createsuperuser
```

It will ask for your email and password.

---

## 8. Start the server

```powershell
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

Test it:
- Open `http://127.0.0.1:8000/api/v1/topics` (should return 401 without auth — that's correct)
- Register a user via POST to `/api/v1/auth/register`

---

## 9. Full SQL Reference

Here is the complete SQL to create everything from scratch if you prefer raw SQL over Django migrations. This matches the project's database schema exactly.

```sql
-- ============================================================
-- FluentFlow AI — Complete Database Schema
-- Run this AFTER creating the database with: CREATE DATABASE fluentspeak;
-- Connect to the database first: \c fluentspeak
-- ============================================================

-- USERS
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    is_verified BOOLEAN DEFAULT FALSE,
    is_staff BOOLEAN DEFAULT FALSE,
    is_superuser BOOLEAN DEFAULT FALSE,
    last_login TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- USER PROFILES
CREATE TABLE user_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL UNIQUE REFERENCES users(id) ON DELETE CASCADE,
    full_name VARCHAR(100) DEFAULT '',
    avatar_url TEXT DEFAULT '',
    level VARCHAR(20) DEFAULT 'beginner',
    daily_goal INTEGER DEFAULT 10,
    timezone VARCHAR(100) DEFAULT 'UTC'
);

-- USER PROGRESS
CREATE TABLE user_progress (
    user_id UUID PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
    conversations_completed INTEGER DEFAULT 0,
    words_learned INTEGER DEFAULT 0,
    current_streak INTEGER DEFAULT 0,
    total_minutes INTEGER DEFAULT 0
);

-- TOPICS
CREATE TABLE topics (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(100) NOT NULL UNIQUE,
    description TEXT DEFAULT '',
    difficulty VARCHAR(20) DEFAULT '',
    category VARCHAR(50) DEFAULT '',
    is_active BOOLEAN DEFAULT TRUE
);

-- SCENARIOS
CREATE TABLE scenarios (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(150) NOT NULL,
    description TEXT DEFAULT '',
    ai_role VARCHAR(100) NOT NULL,
    user_role VARCHAR(100) NOT NULL,
    goal TEXT DEFAULT '',
    max_turns INTEGER DEFAULT 10,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- CONVERSATIONS
CREATE TABLE conversations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    topic_id UUID REFERENCES topics(id) ON DELETE SET NULL,
    scenario_id UUID REFERENCES scenarios(id) ON DELETE SET NULL,
    title VARCHAR(255) DEFAULT '',
    status VARCHAR(20) DEFAULT 'active',
    current_turn INTEGER DEFAULT 0,
    summary TEXT DEFAULT '',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- MESSAGES
CREATE TABLE messages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    conversation_id UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
    role VARCHAR(20) NOT NULL,
    content TEXT NOT NULL,
    turn_number INTEGER DEFAULT 0,
    token_count INTEGER DEFAULT 0,
    latency_ms INTEGER DEFAULT 0,
    provider VARCHAR(50) DEFAULT '',
    model VARCHAR(50) DEFAULT '',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- MESSAGE FEEDBACK
CREATE TABLE message_feedback (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    message_id UUID NOT NULL UNIQUE REFERENCES messages(id) ON DELETE CASCADE,
    correction TEXT DEFAULT '',
    optimized_response TEXT DEFAULT '',
    next_question TEXT DEFAULT ''
);

-- CONVERSATION STATES
CREATE TABLE conversation_states (
    conversation_id UUID PRIMARY KEY REFERENCES conversations(id) ON DELETE CASCADE,
    stage VARCHAR(30) DEFAULT 'opening',
    tone VARCHAR(30) DEFAULT 'friendly',
    goal_progress INTEGER DEFAULT 0,
    last_vocab_word VARCHAR(100) DEFAULT '',
    summary TEXT DEFAULT '',
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- VOCABULARY WORDS
CREATE TABLE vocabulary_words (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    word VARCHAR(100) NOT NULL UNIQUE,
    definition TEXT NOT NULL,
    difficulty VARCHAR(20) DEFAULT '',
    examples JSONB DEFAULT '[]'::JSONB
);

-- USER VOCABULARY
CREATE TABLE user_vocabulary (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    vocabulary_id UUID NOT NULL REFERENCES vocabulary_words(id) ON DELETE CASCADE,
    mastered BOOLEAN DEFAULT FALSE,
    times_seen INTEGER DEFAULT 0,
    learned_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE (user_id, vocabulary_id)
);

-- AI PROVIDERS
CREATE TABLE ai_providers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    priority INTEGER DEFAULT 100,
    status VARCHAR(20) DEFAULT 'active'
);

-- AUDIT LOGS
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    action VARCHAR(100) NOT NULL,
    metadata JSONB DEFAULT '{}'::JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ANALYTICS EVENTS
CREATE TABLE analytics_events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    event_name VARCHAR(100) NOT NULL,
    payload JSONB DEFAULT '{}'::JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- NOTIFICATIONS
CREATE TABLE notifications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- ============================================================
-- INDEXES (performance)
-- ============================================================

CREATE INDEX idx_messages_conversation ON messages(conversation_id);
CREATE INDEX idx_messages_created ON messages(created_at);
CREATE INDEX idx_conversations_user ON conversations(user_id);
CREATE INDEX idx_conversations_updated ON conversations(updated_at DESC);
CREATE INDEX idx_user_vocabulary_user ON user_vocabulary(user_id);
CREATE INDEX idx_scenarios_user ON scenarios(user_id);
CREATE INDEX idx_audit_logs_user ON audit_logs(user_id);
CREATE INDEX idx_audit_logs_created ON audit_logs(created_at DESC);
CREATE INDEX idx_analytics_events_user ON analytics_events(user_id);
CREATE INDEX idx_notifications_user ON notifications(user_id);
CREATE INDEX idx_notifications_unread ON notifications(user_id, is_read) WHERE is_read = FALSE;
```

---

## Troubleshooting

### "psql: FATAL: password authentication failed"
- Double-check the password you set during PostgreSQL installation
- Try resetting it: `ALTER USER postgres PASSWORD 'newpassword';`

### "django.db.utils.OperationalError: could not connect to server"
- Make sure PostgreSQL service is running: `Get-Service postgresql*`
- Check the port: default is 5432

### "permission denied for schema public"
- PostgreSQL 15+ requires explicit schema permissions:
  ```sql
  \c fluentspeak
  GRANT ALL ON SCHEMA public TO fluentspeak_user;
  ```

### "relation already exists" when running migrations
- This means migrations have already been applied. Skip with:
  ```powershell
  python manage.py migrate --fake
  ```

---

## Notes

- **Django migrations are the recommended way** to create tables. The raw SQL in section 9 is provided as a reference only. Using `python manage.py migrate` ensures Django's internal tracking stays in sync.
- If you ever need to reset the database completely:
  ```sql
  DROP DATABASE fluentspeak;
  CREATE DATABASE fluentspeak;
  ```
  Then run `python manage.py migrate` and `python manage.py seed_topics` again.
