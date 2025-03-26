# Open-Source Bike Computer Hardware

Welcome to the hardware repository for the Open-Source Bike Computer project! This project aims to create an open, customizable, and modular bike computer for cyclists who want more control over their ride experience. Whether you’re an enthusiast or a developer, we invite you to collaborate, contribute, and make this project better!

## Project Overview

This open-source bike computer aims to provide an alternative to traditional, proprietary cycling computers by allowing users to build, modify, and extend their own device. Our goal is to create a versatile, power-efficient, and user-friendly bike computer with customizable features.

### Features Planned:
- **Custom Carrier Board:** A custom-designed carrier board that all of the components can be soldered or plugged into.
- **Battery Module:** Modular battery packs that can be easily swapped out, each equipped with a balancing board, allowing you to carry multiple charged packs for extended trips.
- **Button Interface & Tactile Scroll Wheel:** Physical buttons for user interaction, potentially including a tactile scroll wheel (inspired by devices like the Apple Watch or Suunto watches) for a smoother cycling experience.
- **Mapping & Navigation:** OpenStreetMap integration for pre-planned routes with on-device routing planned for future updates.
- **Connectivity:** Support for Wi-Fi, Bluetooth, ANT+, GPS, GLONASS, and a digital compass.
- **Data Views:** Initially, the device will provide fixed data views with plans for customization options later.
- **Additional Integrations:** Weather data, phone app syncing, and other features may be integrated as the project progresses.

### Ideas and Features in Consideration:
- **18650 Battery Support:** We’re exploring support for 18650 batteries due to their low cost, high capacity, and wide availability in the maker community.
- **Flashlight:** Phone-like flashlight, just becourse it is usefull.
- **Touchscreen and Physical Controls:** We understand the debate between touchscreens and physical buttons. While some users prefer a touchscreen for its flexibility, others prefer tactile buttons. The bike computer will likely include both options to cater to all preferences.
- **Solar Charging:** We are also considering solar panels to keep the device charged during extended rides, minimizing the need for manual charging.

## Current Stage & Roadmap

### Early Development Phase:
We’re still in the early stages of the hardware design process. 
The focus right now is on making hardware choices and gathering feedback from the cycling community to define the most important features.

### Next Steps:
- **Prototyping:** We plan to develop initial prototypes of the custom carrier board and battery modules.
- **Testing:** Testing will focus on power consumption, battery life, and performance under real-world cycling conditions.
- **Feature Implementation:** We’ll begin working on software that integrates with the hardware, focusing on basic features like navigation and data views before moving on to more advanced options like phone app syncing or weather integration.

## Contributing

We welcome contributions from everyone! Whether you want to suggest new features, improve the hardware, or assist with software development, there’s a place for you in this project.

To contribute:
1. Create a branch for your feature or bug fix.
2. Make your changes and submit a pull request (PR).
3. Provide clear documentation for any changes you make, especially if it involves hardware.

(If you are new to git or github feel free to reach out for help on how this process works, we all need to start somewhere)

### How You Can Help:
- **Suggest Features:** If you have ideas for new features, we’d love to hear them! The current list includes ideas like pacing apps, team communication, and wind/weather integration.
- **Help with Design:** If you have experience in hardware design, software, or UI/UX, your input would be invaluable.
- **Testing & Feedback:** Once prototypes are ready, testing them in real-world conditions will be key to improving the design.

## Known Challenges & Considerations:
- **Battery Life:** Maintaining a long-lasting battery is a top priority. Hard- and software choices will both influcence this.
- **Hardware Complexity:** With many features being considered (GPS, Bluetooth, ANT+, etc.), managing complexity in both the hardware and software will require careful planning and optimization.
- **Software Development:** Developing the software will be a significant challenge. While the hardware progresses, developing a clean, user-friendly interface and managing devices like GPS radios and sensors will take time.

## Inspiration and Community Input

This project has drawn inspiration from several existing solutions:
- **Cycling Computers**: We’re aware of the strengths and weaknesses of current cycling computers like those from Garmin and Wahoo, and we’re striving to improve their user experience with modern software and hardware.
- **Pebble OS**: Some contributors have suggested looking into Pebble OS as a potential open-source platform for managing the bike computer’s functionality, and it’s something we’re actively evaluating.
- **Alternative Approaches:** We’re also looking at alternative strategies such as UWB (Ultra-Wideband) for communication, integration with smart sensors, and possibly even solar charging for long rides.

## License

This project is open-source and licensed under the [GPL License](LICENSE). Feel free to use, modify, and distribute the project as you see fit!

---

Thank you for visiting the repository! We’re excited to build something that will improve the biking experience for everyone. Join the community, contribute your ideas, and let's build something great together!
