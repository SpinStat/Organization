
# **🛠️ Bill of Materials Prototype**
## **🔹 1️⃣ Core Processing Unit**
| Component | Description | Part Number / Notes |
|-----------|------------|---------------------|
| **SoC** | TI AM62L Cortex-A53 processor | AM62x series (AM62x-SK for early testing) |
| **PMIC (Power Management IC)** | Required to power AM62L | TI **TPS65219** or equivalent |
| **RAM (LPDDR4/DDR4)** | 512MB - 2GB RAM | Micron MT53E256M16D1DS |
| **Flash Storage** | 4GB+ eMMC | Kingston eMMC **EMMC04G-M627** |
| **MicroSD Slot (Optional)** | External storage for maps/logs | Generic microSD socket |

---

## **🔹 2️⃣ Power Management**
| Component | Description | Part Number / Notes |
|-----------|------------|---------------------|
| **Li-Ion Battery** | 3.7V, 2000mAh+ | Any protected 18650 or LiPo pack |
| **Battery Charger IC** | Manages charging from USB-C | TI **BQ25895** (single-cell Li-Ion charger) |
| **DC/DC Converters (Buck/Boost)** | Powers AM62L, display, and peripherals | TI **TPS62873** (for 3.3V, 5V rails) |
| **Power Switch (MOSFET or Load Switch)** | Turns off non-essential peripherals | TI **TPS22918** |

---

## **🔹 3️⃣ Display & User Interface**
| Component | Description | Part Number / Notes |
|-----------|------------|---------------------|
| **LCD Display** | 3.5"-4.3" 480x320/800x480 TFT with SPI/DSI | **ILI9488** (SPI) or **Newhaven 4.3” TFT** |
| **Touchscreen (Optional)** | Capacitive touch panel | FT5x06 touch controller |
| **Rotary Encoder / Buttons** | Physical UI control | Generic rotary encoder + 2-3 push buttons |
| **Buzzer (Optional)** | Audio feedback | Piezo buzzer (low-power) |

---

## **🔹 4️⃣ GPS, Wireless & Sensors**
| Component | Description | Part Number / Notes |
|-----------|------------|---------------------|
| **GPS Module** | GNSS (GPS, Galileo, Glonass) | **u-blox NEO-M9N** or **Quectel L96** |
| **BLE / ANT+ Module** | BLE 5.0 + ANT+ communication | **nRF52840** (for BLE & ANT+) |
| **Wi-Fi Module** | Syncing data over Wi-Fi | **Espressif ESP32-S3-WROOM** |
| **Accelerometer / IMU** | Motion & vibration sensing | **Bosch BMA400** or **MPU6050** |
| **Barometer / Altimeter** | Elevation data | **Bosch BMP390** |

---

## **🔹 5️⃣ Storage & Data Logging**
| Component | Description | Part Number / Notes |
|-----------|------------|---------------------|
| **eMMC / Flash Storage** | Stores maps & ride logs | Kingston eMMC 4GB+ |
| **MicroSD Slot (Optional)** | Expandable storage | Standard microSD socket |

---

## **🔹 6️⃣ I/O & Expandability**
| Component | Description | Part Number / Notes |
|-----------|------------|---------------------|
| **USB-C Port** | Charging & data transfer | USB-C Receptacle (e.g., **Molex 105444-0101**) |
| **UART to USB Debug** | Debugging interface | FTDI FT232RL or CP2102 |
| **GPIO / Expansion Header** | Extra pins for future peripherals | 2.54mm pin header |

---

## **🔹 7️⃣ PCB & Miscellaneous**
| Component | Description | Part Number / Notes |
|-----------|------------|---------------------|
| **Custom PCB (4-layer recommended)** | Main circuit board | Designed in **KiCad / Altium** |
| **Passive Components** | Resistors, capacitors, diodes | Various (0603/0805 SMD) |
| **Enclosure** | Protects the electronics | 3D-printed or CNC-machined case |

---

# **📌 Notes & Next Steps**
- 🔹 **Development Kits First?** **AM62x-SK evaluation board** before making a custom PCB.  
- 🔹 **PCB Design Considerations:**  
  - Minimum **4-layer PCB** for good signal integrity.  
  - Proper power sequencing for AM62L and peripherals.  
- 🔹 **Testing Order:**  
  - Start -> **core board (CPU, RAM, storage, power)**.  
  - Add **display & UI**.  
  - Integrate **GPS, BLE, Wi-Fi, sensors**.  

---
