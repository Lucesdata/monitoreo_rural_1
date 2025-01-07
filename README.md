# Rural Platform - PTAP Monitoring and Automation

## Project: Monitoring and Automation of Rural PTAPs

This repository hosts the development of the **Rural Platform**, an integrated system for the monitoring and automation of **Drinking Water Treatment Plants (PTAPs)** in the rural area of **Santiago de Cali, Colombia**. The project aims to optimize water management by implementing IoT technologies, real-time analytics, and automated control systems.

![Sensor Panel](panel.jpeg)

### Project Context

Efficient management of rural water treatment plants has been a challenge due to geographical dispersion and the lack of technological tools. This project aims to address that by enabling:
- Real-time remote monitoring.
- Automated control of treatment processes.
- Continuous analysis of critical parameters such as flow rate, water quality, and pressure.

**Monitored Plants**
1. **La Vorágine** - A flagship plant with a robust design serving as a model for other installations.  
2. **Pichindé**  
3. **Montebello**  
4. **Cascajal**  
5. **Kilometer 18**

![La Vorágine](voragine.png)

## System Features
- **Smart Control Panels**  
  Integration of sensors capturing data on the quality and quantity of processed water. Each plant is equipped with panels that monitor key parameters.

![Monitoring Display](display.jpeg)

- **Real-Time Visualization**  
  The interface includes interactive maps and dynamic charts for easy interpretation of data collected from all plants.

- **Automated Management**  
  Event-based configuration to adjust water treatment processes according to changes in incoming data, such as turbidity or flow variations.

## Technologies Used
- **Programming Language:** Python  
- **Development Framework:** Dash (Plotly)  
- **Database:** PostgreSQL  
- **IoT:** MQTT/HTTP protocols  
- **Frontend:** React.js components integrated with Dash  
- **Containers:** Docker for scalability and portability.

## Getting Started
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/plataforma_rural_01.git
