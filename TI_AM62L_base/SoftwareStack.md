🛠️ Initial Software Architecture for AM62L base
🖥️ 1️⃣ Core System Components

✅ Yocto Linux (Minimal Build)

    Base: Poky (or a TI-specific Yocto layer) + systemd

    No GUI frameworks like X11/Wayland → Direct framebuffer rendering

    Filesystem: ext4 or SquashFS (if read-only for robustness)

✅ Rendering & UI (Without a Windowing System)

    Direct framebuffer rendering (DRM/KMS or FBdev)

    Options for drawing maps & UI:

        📍 Map Rendering: MapLibreGL (if OpenGL ES is available) or a custom rasterized tile engine

        🎨 UI Elements: LVGL (lightweight UI library for embedded Linux)

        🏎 Custom OpenGL ES renderer (for better performance on the AM62L GPU)

✅ Navigation & Connectivity

    GPS Handling: gpsd (daemon for GPS data processing)

    Sensor Data (ANT+, BLE, WiFi):

        ANT+: libant or direct integration via serial

        Bluetooth (HR monitor, cadence sensor, etc.): BlueZ

        WiFi for syncing data: wpa_supplicant

✅ Input & Interaction

    Physical buttons, rotary encoder, or touchscreen support

    Event handling: evdev for raw input events

✅ Power Management (For Future Optimization)

    Dynamic frequency scaling (DVFS) to reduce CPU power draw

    Display power management (turn off backlight when inactive)

    Suspend-to-RAM (Deep sleep when idle)

📂 System Software Stack Overview
🔹 Boot & Base System

    Bootloader: U-Boot

    Kernel: Custom Yocto-built Linux kernel (strip out unnecessary drivers)

    Filesystem: Read-only SquashFS (optional for robustness)

🔹 Graphics & UI

    Rendering Backend: DRM/KMS (for hardware-accelerated drawing)

    UI Framework: LVGL or custom OpenGL ES renderer

    Map Display:

        Option 1: Pre-rendered raster tiles (simpler, lower CPU load)

        Option 2: Vector rendering with OpenGL ES (more flexible, higher CPU/GPU demand)

🔹 Navigation & Sensors

    GPS: gpsd (parses NMEA sentences, interfaces with GPS chip)

    ANT+ & BLE: BlueZ for BLE, custom serial integration for ANT+

    Storage: Logs & ride data saved in a local SQLite database or binary format

🔹 Power Management (Later Optimization)

    CPU Scaling: Use Linux cpufreq to adjust clock speeds dynamically

    Backlight Control: Reduce brightness dynamically when idle

    Sleep Modes: Implement suspend-to-RAM for long idle periods
