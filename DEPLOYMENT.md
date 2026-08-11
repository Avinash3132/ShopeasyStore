# ShopEasy deployment preparation

## What changed

- `settings.py` now supports PostgreSQL through `DATABASE_URL` and falls back to SQLite locally.
- `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, and `CSRF_TRUSTED_ORIGINS` are environment-driven.
- WhiteNoise is configured for static files.
- `MEDIA_URL` and `MEDIA_ROOT` are defined.
- Gunicorn was added for production WSGI serving.
- PostgreSQL support was added through `psycopg`.
- `db.sqlite3` is no longer part of the deployment-ready project.
- The old `products/` image folder was moved to `media/products/` so the existing database image paths continue to work.
- The old `requirements.txt` contained unrelated Flask packages; it now contains only dependencies used by ShopEasy and its deployment.
- `.gitignore`, `.env.example`, `Procfile`, `build.sh`, and `.python-version` were added.
- A private `data/initial_data.json` snapshot was created from the existing SQLite database.

## Local testing

Create a virtual environment and install:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
```

For local development, set `SECRET_KEY` in your environment or use the local-development fallback.

Then:

```bash
python manage.py migrate
python manage.py runserver
```

## Production

Use a host that supports Python/Django and PostgreSQL. Netlify is not the right
place to run this monolithic Django application.

Set these environment variables on the host:

```text
SECRET_KEY=<new-long-random-secret>
DEBUG=False
ALLOWED_HOSTS=<your-hostname>
CSRF_TRUSTED_ORIGINS=https://<your-hostname>
DATABASE_URL=<postgresql-connection-string>
```

Build:

```bash
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

Start:

```bash
gunicorn ecommerce.wsgi:application
```

## Preserve the existing data

After the PostgreSQL database is connected and migrations have run:

```bash
python manage.py loaddata data/initial_data.json
```

Then reset PostgreSQL sequences:

```bash
python manage.py sqlsequencereset auth contenttypes sessions store orders
```

Execute the generated SQL against PostgreSQL.

The fixture preserves the existing user password hashes, products, categories,
and orders from the uploaded SQLite database.

## Important: existing public GitHub repository

Your original public repository contains `db.sqlite3` and a hard-coded Django
`SECRET_KEY`. Because the secret and database have already been exposed, treat
the old secret as compromised.

Before making the repository public again:

1. Generate a completely new `SECRET_KEY`.
2. Remove `db.sqlite3` from Git tracking.
3. Remove the database and old secret from Git history if they were committed.
4. Do not commit `.env` or `data/initial_data.json`.

Adding `.gitignore` alone does not remove files that Git already tracks.

## Media

The sample product images are included under `media/products/`. For a small
portfolio deployment this can work if the host provides persistent storage.
For production-scale usage, move user uploads to object storage such as S3-
compatible storage or a dedicated media service.
