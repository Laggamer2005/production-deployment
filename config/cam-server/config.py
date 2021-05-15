import os

# Primary config for cam-server
db_url = f"postgresql://{os.getenv('CAM_DB_USER')}:{os.getenv('CAM_DB_PASSWORD')}@postgres/{os.getenv('CAM_DB_DATABASE')}"

# Put your super secret SendGrid API Key here
sendgrid_key = os.getenv("CAM_SENDGRID_KEY")
