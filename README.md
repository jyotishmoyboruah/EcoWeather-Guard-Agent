# 🌍 EcoWeather Guard Agent (Kaggle Capstone)

An elegant, lightweight, cloud-native expert system submitted under the **Agents for Good** track for the July 2026 Kaggle AI Agents Intensive.

## 📋 Overview
EcoWeather Guard bridges the gap between raw, complex atmospheric metrics and real-world agricultural safety. It queries real-time coordinate data and evaluates it across 5 specialized environmental dimensions simultaneously.

## 🛠️ Specialized Analytical Modules
1. **🌪️ AeroForecast:** Monitors surface pressure shifts to spot sudden micro-climate trends.
2. **❄️ EcoFrost Guard:** Evaluates temperature and humidity combinations to flag frost risks for sensitive indigenous crops.
3. **🌱 HydroCrops Sowing Window:** Analyzes immediate rain levels to map soil preparation windows.
4. **🚨 MonsoonAlert Risk Level:** Tracks localized rainfall load profiles to issue early community safety alerts.
5. **🐄 ThermaHerd Index (THI):** Dynamically calculates livestock heat stress to provide instant herd-welfare advisories.

## 💻 Tech Stack & Architecture
- **Orchestration:** Google GenAI SDK (`gemini-2.5-flash`)
- **Data Engine:** Open-Meteo REST API (Model Context Protocol tool pattern)
- **Environment:** Cloud Jupyter Notebook Container (Optimized for minimal local memory overhead)

## 🚀 Setup & Execution Instructions
1. Clone this repository.
2. Create a local `.env` file using the configuration keys shown in `.env.template`.
3. Execute `agent.py` or step through the provided Jupyter Notebook cells to stream real-time coordinate reports.
graph TD
    %% Styling
    classDef tool fill:#2d3748,stroke:#4a5568,stroke-width:2px,color:#fff;
    classDef core fill:#1a202c,stroke:#3182ce,stroke-width:3px,color:#fff;
    classDef model fill:#2b6cb0,stroke:#4299e1,stroke-width:2px,color:#fff;
    classDef output fill:#2f855a,stroke:#48bb78,stroke-width:2px,color:#fff;

    %% Data Ingestion Layer
    A[User Coordinates: Tinsukia, Assam] --> B(weather_tools.py)
    B -->|HTTPX REST Request| C[Open-Meteo API Endpoint]
    C -->|Raw JSON Payload| B
    B -->|Parse to Clean Text String| D{agent.py Orchestrator}

    %% System Core
    D -->|Inject Clean Data Block| E[System Instruction Prompt]
    E -->|Single-Shot Execution| F[Gemini 2.5 Flash Engine]

    %% Multi-Layered Analysis
    F --> G[1. AeroForecast Module]
    F --> H[2. EcoFrost Guard Module]
    F --> I[3. HydroCrops Sowing Module]
    F --> J[4. MonsoonAlert Module]
    F --> K[5. ThermaHerd Index Module]

    %% THI Math Formula sub-path
    K -->|Math Execution| L["THI Formula Calculation"]
    L -->|Result: THI 86.37| M[Extreme Heat Stress Warning]

    %% Final Outputs
    G --> N[Unified Markdown Operational Advisory Report]
    H --> N
    I --> N
    J --> N
    M --> N

    %% Class Applications
    class B,C tool;
    class D,E core;
    class F model;
    class G,H,I,J,K,L,M,N output;
