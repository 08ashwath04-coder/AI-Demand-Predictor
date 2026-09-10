import os
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL=os.getenv('DATABASE_URL','sqlite:///./demandbridge.db')
JWT_SECRET=os.getenv('JWT_SECRET','dev-secret-change-me')
CORS_ORIGIN=os.getenv('CORS_ORIGIN','http://localhost:5173')
