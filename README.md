# Value of Time Saved Calculator

A Flask web application that helps you determine whether paying for a faster or more convenient option is worth it based on the value of your time.

## Overview

This application calculates the value of time saved using the formula:

**Value of Time Saved = Time Saved (in hours) × Hourly Rate**

If the value of time saved is greater than or equal to the additional cost, then paying for the quicker or more convenient option may be justified. If the cost exceeds your time's value, the extra expense may not be worth it.

## Features

- 🕐 Input time in days, hours, and minutes for both free and paid options
- 💵 Calculate the value of time saved based on your hourly rate
- 📊 View recent calculations in a table (stored in browser cookies)
- 🗑️ Clear calculation history with one click
- 🐳 Fully Dockerized for easy deployment

## Running with Docker

### Using Docker Compose (Recommended)

```bash
docker-compose up
```

Then open your browser to `http://localhost:5000`

**Note for Production**: The docker-compose.yml file sets `FLASK_DEBUG=True` for development. For production deployments, remove this environment variable or set it to `False` to disable debug mode.

### Using Docker directly

```bash
# Build the image
docker build -t value-of-time-saved .

# Run the container (production mode)
docker run -p 5000:5000 value-of-time-saved

# Run the container (development mode with debug)
docker run -p 5000:5000 -e FLASK_DEBUG=True value-of-time-saved
```

Then open your browser to `http://localhost:5000`

## Running Locally (without Docker)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Then open your browser to `http://localhost:5000`

## How to Use

1. **Original Time Taken (Free)**: Enter how long the free/default option takes (in days, hours, and minutes)
2. **Time Taken Instead (With Cost)**: Enter how long the paid/faster option takes
3. **$ Cost**: Enter the cost of the faster option
4. **$ Hourly Value**: Enter your hourly rate (e.g., your income per hour)
5. Click **Calculate** to see the value of time saved
6. View all recent calculations in the table below
7. Click **Clear History** to remove all stored calculations

## Example

- Original time: 0 days, 2 hours, 0 minutes (taking the bus)
- Time with cost: 0 days, 0 hours, 30 minutes (taking a taxi)
- Cost: $15.00 (taxi fare)
- Hourly value: $25.00/hr (your hourly wage)

**Result**: 
- Time saved: 1.5 hours
- Value of time saved: $37.50
- Net value: $22.50 (worth it!)

## Technologies

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **Storage**: Browser Cookies
- **Deployment**: Docker

## License

See LICENSE file for details.
