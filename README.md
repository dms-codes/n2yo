# Satellite Tracking Script

This Python script allows you to track satellites using the N2YO API. It provides various functions to retrieve satellite information, including Two-Line Element Set (TLE) data, satellite positions, and radio passes information. You can use this script to monitor and track satellites of interest.

## Prerequisites

Before using this script, you need to obtain an API key from N2YO. Replace `"yourAPIkey"` in the script with your actual API key.

## Usage

To use the script, you can call the provided functions to retrieve specific information about satellites. Here are some of the available functions:

- `GetTLEData(NORADId)`: Retrieves TLE data for a satellite with the given NORAD ID.
- `GetSatPosData(NORAId, observer_lat, observer_long, observer_alt, seconds)`: Retrieves satellite position data for a specific satellite at a given observer's location.
- `GetRadioPasses(NORAId, observer_lat, observer_long, observer_alt, days, min_elevation)`: Retrieves radio pass information for a specific satellite over a specified number of days with a minimum elevation.

You can also use the `ReportRadioPasses` function to generate a report for radio passes of a specific satellite. The example provided at the end of the script demonstrates how to use this function.

## Example

```python
if __name__ == "__main__":
    observer_lat = -6.21462	
    observer_long = 106.84513
    observer_alt = 0
    print(ReportRadioPasses("33591", observer_lat, observer_long, observer_alt, 1, 10))
```

In this example, the script reports radio passes for a satellite with NORAD ID "33591" over the course of one day with a minimum elevation of 10 degrees.

## Dependencies

This script relies on the `requests` library to make HTTP requests to the N2YO API. Make sure you have it installed before running the script.

```bash
pip install requests
```

## Disclaimer

Please be aware of the terms and conditions of the N2YO API and comply with any usage restrictions or limitations imposed by the service provider.
