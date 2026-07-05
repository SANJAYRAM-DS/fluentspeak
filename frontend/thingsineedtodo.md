# Things I Need To Do

## Environment
- Create a Python virtual environment in `backend/`.
- Install the backend dependencies from `backend/requirements.txt`.
- Keep `.env` local and make sure it contains the PostgreSQL and Groq values.
- Set `DJANGO_SECRET_KEY`, `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST`, and `POSTGRES_PORT`.
- Set `api1` through `api5` or `GROQ_API_KEY` for Groq access.
- Optionally set `GROQ_BASE_URL` and `GROQ_MODEL` if you want a different provider endpoint or model.

## Local Services
- Start PostgreSQL and create the database used by the Django project.
- Start Redis because Celery and any cache-based work will need it.
- Make sure network access to Groq is allowed from your machine.

## Django Setup
- Run database migrations after dependencies are installed.
- Create a Django superuser if you want admin access.
- Load or seed the 50 predefined topics into the `topics` table.
- Optionally seed starter scenarios and vocabulary words for testing.

## Runtime
- Start the Django development server from `backend/`.
- Start a Celery worker if you want background jobs to run.
- If you later add scheduled tasks, start a Celery beat process too.

## API Checks
- Test `POST /api/v1/auth/register`.
- Test `POST /api/v1/auth/login` and `POST /api/v1/auth/refresh`.
- Test `GET /api/v1/me` and `PATCH /api/v1/me`.
- Test `GET /api/v1/topics` and `GET /api/v1/topics/{id}`.
- Test `POST /api/v1/conversations`.
- Test `POST /api/v1/conversations/{id}/turns`.
- Test `GET /api/v1/conversations/{id}/messages`.
- Test `GET /api/v1/vocabulary/learned` and `GET /api/v1/vocabulary/stats`.

## Completed
- Added the topic seeding command at `backend/apps/topics/management/commands/seed_topics.py`.
- Added `analytics_events` storage in `backend/apps/analytics/models.py`.
- Added refresh-token blacklist logout in `backend/apps/users/views.py`.
- Added Django template screens for auth, dashboard, chat, vocabulary, and progress.
- Added a standalone frontend in `frontend/` with HTML, CSS, and JavaScript pages.

## Nice To Have
- Add Docker Compose for PostgreSQL, Redis, and Django.
- Add fixture or migration-based demo data.
- Add a streaming frontend that consumes the SSE turn endpoint.
