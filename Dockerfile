FROM python:3.9-slim

# copy project files
COPY . /app
WORKDIR /app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# expose the port used by Streamlit (default 8501); AZ environments often set PORT
EXPOSE ${PORT}

# start the Streamlit application
# note: use --server.port to respect the PORT environment variable
CMD streamlit run streamlit_app.py --server.port ${PORT:-8501} --server.enableCORS false