# Weather Report Application 🌦️

A simple Python Weather Report Application that fetches real-time weather data using the OpenWeatherMap API.

## Features

* Search weather by city name
* Real-time weather data using API
* Displays:

  * Temperature
  * Humidity
  * Weather condition
  * Wind speed
* Weather emojis based on condition
* Saves weather reports to a text file
* Uses `.env` file to securely store API key
* Handles invalid city names and internet issues

## Technologies Used

* Python
* Requests Module
* OpenWeatherMap API
* dotenv

## Installation

### Clone Repository

```bash
git clone <your-github-repo-link>
```

### Install Required Modules

```bash
pip install requests python-dotenv
```

## Setup API Key

Create a `.env` file in the project folder and add:

```env
API_KEY=your_api_key_here
```

Get your API key from:

https://openweathermap.org/api

## Run the Project

```bash
python main.py
```

## Example Output

```text
-----------------------------------
          Weather Report
-----------------------------------
City           : Khammam
Weather        : Broken Clouds ☁️
Humidity       : 48%
Temperature    : 31 °C
Wind Speed     : 7.2 m/s
-----------------------------------
```

## Project Structure

```text
📁 Weather-App
 ┣ 📄 main.py
 ┣ 📄 .env
 ┣ 📄 weather_report.txt
 ┣ 📄 README.md
```

## Learning Outcomes

Through this project, I learned:

* API Integration
* JSON Parsing
* File Handling
* Exception Handling
* Environment Variables
* Python Formatting
* Working with Real-Time Data

## Author
Mohammed Ayesha Firdouse
## Connect With Me
LinkedIn: www.linkedin.com/in/ayeshafirdouse

