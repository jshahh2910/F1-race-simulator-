total_laps = 50
base_lap_time = 90
pit_stop_time = 20 


# tire types / speed / wear rate
soft = {"name": "Soft", "speed": -1.5, "wear_rate": 0.8}
medium = {"name": "Medium", "speed": -0.5, "wear_rate": 0.5}
hard = {"name": "Hard", "speed": 0.5, "wear_rate": 0.3}

import random

class Driver:
    def __init__(self, name, skill, starting_tire, pit_lap, next_tire):
        #static 
        self.name = name 
        self.skill = skill
        self.current_tire = starting_tire
        self.pit_lap = pit_lap
        self.next_tire = next_tire

        # dynamic / changes during race
        self.total_time = 0
        self.tire_wear = 0
        self.lap_times = []
        self.fastest_lap = float('inf')
        self.starting_tire = starting_tire

# creating driver objects
driver1 = Driver("Max Verstappen", 98, soft, 18, hard)
driver2 = Driver("Lewis Hamilton", 95, medium, 20, hard)
driver3 = Driver("Charles Leclerc", 96, soft, 15, medium)
driver4 = Driver("Carlos Sainz", 93, hard, 32, medium)
driver5 = Driver("Oscar Piastri", 95, medium, 23, hard)


drivers = [driver1, driver2, driver3, driver4, driver5]

for lap in range(1, total_laps + 1):
    print(f"Lap {lap}:")
    for driver in drivers:
        # to calculate lap time
        skill_factor = driver.skill * 0.05
        tire_speed_effect = driver.current_tire["speed"]
        tire_wear_penalty = driver.tire_wear * 0.2
        randomness = random.uniform(-0.5, 0.5)

        lap_time = base_lap_time - skill_factor + tire_speed_effect + tire_wear_penalty + randomness

        # to update driver state
        driver.total_time += lap_time
        driver.lap_times.append(lap_time)
        # track fastest lap for each driver
        if lap_time < driver.fastest_lap:
            driver.fastest_lap = lap_time
        driver.tire_wear += driver.current_tire["wear_rate"]

        # pit stop check
        if lap == driver.pit_lap:
            driver.current_tire = driver.next_tire
            driver.tire_wear = 0
            driver.total_time += pit_stop_time

        position = drivers.index(driver) + 1
        print(f"  P{position} {driver.name} → Lap Time: {round(lap_time, 2)} sec")

    # simulate overtakes (simple: sort by current total time each lap)
    drivers.sort(key=lambda d: d.total_time)

    print()

# determine overall fastest lap
fastest_driver = min(drivers, key=lambda d: d.fastest_lap)
sorted_drivers = sorted(drivers, key=lambda driver: driver.total_time)

print("\n🏁 FINAL RESULTS:\n")

leader_time = sorted_drivers[0].total_time

for i, driver in enumerate(sorted_drivers, start=1):
    if i == 1:
        print(f"{i}. {driver.name} — {round(driver.total_time, 2)} sec")
    else:
        gap = driver.total_time - leader_time
        print(f"{i}. {driver.name} — +{round(gap, 2)} sec")

print("\n🔥 FASTEST LAP:")
print(f"{fastest_driver.name} — {round(fastest_driver.fastest_lap, 2)} sec")



