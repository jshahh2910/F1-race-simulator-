# 🏎️ F1 Race Strategy Simulator

A Python-based simulation of a Formula 1 race that models real-world racing dynamics such as tire strategies, pit stops, driver performance, and overtakes.

This project simulates a full race lap-by-lap, where each driver's performance evolves based on multiple factors including skill level, tire degradation, and strategic decisions. The race outcome is dynamic and varies with each run due to controlled randomness and strategic differences.

---

## 🚀 Features

- 🛞 **Tire Strategy System**  
  Soft, Medium, and Hard compounds with different performance and degradation characteristics.

- ⛽ **Pit Stop Simulation**  
  Strategic pit stops with realistic time penalties and tire changes.

- 📉 **Tire Wear & Degradation**  
  Lap times increase as tire wear builds up, impacting performance over time.

- 🧠 **Driver Skill Impact**  
  Higher-skilled drivers achieve consistently faster lap times.

- 🎲 **Controlled Randomness**  
  Adds realistic variation to lap times, preventing deterministic outcomes.

- 🏎️ **Overtake Simulation**  
  Dynamic position changes based on cumulative race performance.

- 🟣 **Fastest Lap Tracking**  
  Identifies the driver with the fastest lap of the race.

- 🏁 **Race Leaderboard**  
  Final standings with time gaps, similar to real F1 race results.

---

## 🛠️ Tech Stack

- **Python**
- Core concepts used:
  - Object-Oriented Programming (OOP)
  - Lists & Dictionaries
  - Simulation Logic
  - Sorting Algorithms

---

## 🧠 How It Works

Each lap of the race is simulated using a combination of factors:

- Base lap time  
- Driver skill (reduces lap time)  
- Tire performance (affects speed)  
- Tire wear (increases lap time over laps)  
- Random variation (adds realism)

Drivers update their state every lap:
- Total race time  
- Tire wear  
- Lap history  

Pit stops reset tire wear and change performance dynamics mid-race.

---

## 📊 Sample Output
