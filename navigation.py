import math
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
import pygame
import time

# Define airport locations with associated city names
airport_locations = {
    "Terminal A": {"coords": (40.6413, -74.1774), "city": "New York"},
    "Terminal B": {"coords": (40.6415, -74.1772), "city": "New York"},
    "Gate 1": {"coords": (40.6417, -74.1770), "city": "New York"},
    "Gate 2": {"coords": (40.6419, -74.1768), "city": "New York"},
    "Check-in Counter": {"coords": (40.6421, -74.1766), "city": "New York"},
}

class Map:
    # Purpose: Display a map using a map library or API.
    # Explanation: This function serves as a placeholder for displaying a map, which is typically done
    # through a map library or API. In this simplified example, it prints "Map displayed" to simulate the
    # display of a map.

    def display_map(self):
        print("Map displayed")

    # Purpose: Find a location using geolocation services.
    # Explanation: This function implements geolocation services to reverse-geocode provided latitude and
    # longitude coordinates and find the corresponding address. It then prints the found location's
    # latitude, longitude, and address.

    def find_location(self, latitude, longitude):
        location = self.reverse_geocode(latitude, longitude)
        print(f"Location found at latitude {latitude}, longitude {longitude}")
        print(f"Address: {location}")

    # Purpose: Reverse-geocode latitude and longitude to retrieve an address.
    # Explanation: This function uses the Nominatim geocoder, which is a geocoding service, to reverse-geocode
    # the provided latitude and longitude coordinates. It returns the address associated with these coordinates.

    def reverse_geocode(self, latitude, longitude):
        geo_locator = Nominatim(user_agent="GetLoc")
        location = geo_locator.reverse(f"{latitude}, {longitude}")
        return location.address

class Math(Map):
    # Purpose: Calculate a route between two sets of latitude and longitude coordinates.
    # Explanation: This function calculates the route distance between two geographic points using the geodesic
    # distance formula provided by the geopy library. It then prints the calculated route's distance in kilometers.

    def calculate_route(self, start_lat, start_long, end_lat, end_long):
        start_location = (start_lat, start_long)
        end_location = (end_lat, end_long)
        distance = geodesic(start_location, end_location).kilometers
        print(f"Route calculated from ({start_lat}, {start_long}) to ({end_lat}, {end_long})")
        print(f"Distance: {distance:.2f} km")
    #Purpose: o set up the initial environment for simulating a AR-like experience using the Pygame 
    #library. It initializes Pygame, creates a display window, and sets a caption. 
    def highlight_direction_in_ar(self):
        # Create a AR-like experience with Pygame
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("AR Navigation")

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Implement AR direction highlighting here
            pygame.draw.rect(screen, (255, 0, 0), (200, 200, 100, 100))  # Example: Red square
            pygame.display.update()

        pygame.quit()

    # Purpose: Simulate highlighting directions in a Argument Reality environment.
    # Explanation: In this simplified example, this function prints "Directions highlighted in AR" to simulate
    # the process of highlighting directions using a AR library or framework. However, in a complete
    # implementation, you would use a AR framework to provide real AR experiences.

    def highlight_direction_in_vr(self):
        print("Directions highlighted in AR")

    # Purpose: Convert degrees to radians.
    # Explanation: This is a utility function that provides the capability to convert angles from degrees
    # to radians. It's a common transformation required for various calculations involving geographic coordinates.

    @staticmethod
    def degrees_to_radians(degrees):
        return degrees * (math.pi / 180.0)

    # Purpose: Calculate the haversine distance between two sets of latitude and longitude coordinates.
    # Explanation: This function calculates the haversine distance, which is the distance between two points
    # on the Earth's surface, using the haversine formula. It returns the distance in kilometers.

    def haversine_distance(self, lat1, lon1, lat2, lon2):
        R = 6371  # Radius of the Earth in kilometers
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad

        a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c
        return distance

class Navigation(Map):
    # Purpose: Calculate the initial bearing between two sets of latitude and longitude coordinates.
    # Explanation: This function computes the initial bearing, which represents the angle in degrees
    # measured clockwise from the North direction, from one point to another. It uses a formula and returns the
    # result in degrees.
    #Purpose: Calculate the initial bearing between two sets of latitude and longitude coordinates.
    # Explanation: This function computes the initial bearing, which represents the angle in degrees 
    # measured clockwise from the North direction, from one point to another. It uses a formula and 
    # returns the result in degrees.
    def bearing(self, lat1, lon1, lat2, lon2):
        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)

        delta_lon = lon2_rad - lon1_rad

        y = math.sin(delta_lon) * math.cos(lat2_rad)
        x = math.cos(lat1_rad) * math.sin(lat2_rad) - math.sin(lat1_rad) * math.cos(lat2_rad) * math.cos(delta_lon)

        initial_bearing = math.atan2(y, x)
        initial_bearing = math.degrees(initial_bearing)
        initial_bearing = (initial_bearing + 360) % 360

        return initial_bearing
    #Purpose: Simulate a user's movement between predefined airport locations.
    # Explanation: This function simulates a user's movement between predefined airport 
    # locations by iterating through these locations, calculating directions, and printing 
    # messages about the user's movement. It also uses the bearing function to determine the initial bearing.
    def simulate_user_movement(self):
        def get_latest_user_location():
            # Iterate through predefined airport locations
            location_names = list(airport_locations.keys())
            num_locations = len(location_names)

            for i in range(num_locations):
                location_name = location_names[i]
                yield airport_locations[location_name]["coords"], location_name

        #Created a generator object to get test coordinates
        coordinate_generator = get_latest_user_location()

        while True:
            (lat, long), location_name = next(coordinate_generator)
            self.find_location(lat, long)
            print(f"User is at: {location_name}")

            if location_name == "Gate 2":
                print("You have reached your final destination.")
                break

            next_location = next(coordinate_generator)
            next_lat, next_long = next_location[0]
            initial_bearing = self.bearing(lat, long, next_lat, next_long)

            # We used the initial bearing to guide the user in the correct direction.
            # We could've displayed the bearing on a VR interface, but I'll print it here:
            if initial_bearing < 90 or initial_bearing > 270:
                print("Turn right")
            elif 90 <= initial_bearing <= 180:
                print("Turn left")
            elif 180 < initial_bearing < 270:
                print("Go straight")
            else:
                print("You are at your destination")

if __name__ == "__main__":
    navigation_instance = Navigation()
    navigation_instance.simulate_user_movement()
