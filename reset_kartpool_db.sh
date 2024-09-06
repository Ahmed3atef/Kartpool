#!/bin/bash

# Set the database name and PostgreSQL superuser
DB_NAME="kartpool"
PG_SUPERUSER="postgres"

# Log into PostgreSQL and perform the database operations
echo "Logging into PostgreSQL as superuser and resetting the database..."

# Drop the database if it exists
sudo -u $PG_SUPERUSER psql -c "DROP DATABASE IF EXISTS $DB_NAME;"

# Create a new database
sudo -u $PG_SUPERUSER psql -c "CREATE DATABASE $DB_NAME;"

echo "Database $DB_NAME has been reset."
