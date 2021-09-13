import os

# Primary config for cam-server
db_url = f"postgresql://{os.getenv('DEMAE_DB_USER')}:{os.getenv('DEMAE_DB_PASSWORD')}@{os.getenv('POSTGRES_HOST')}/{os.getenv('DEMAE_DB_DATABASE')}"

# Used to secure the web panel.
secret_key = os.getenv("DEMAE_SECRET_KEY")

# Sentry configuration for error logging.
use_sentry = True
sentry_dsn = os.getenv("DEMAE_SENTRY_DSN")
