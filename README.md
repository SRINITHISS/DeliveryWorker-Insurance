# 🛡️ GigShield — AI-Powered Parametric Income Insurance for India's Gig Workers  
**Guidewire DEVTrails 2026 | University Hackathon**  
**Persona: Food Delivery Partners (Zomato / Swiggy)**

---

## 🧩 Problem Statement

India's food delivery partners (Zomato, Swiggy) earn ₹12,000–₹20,000/month and operate entirely on gig-based, week-to-week income. When external disruptions occur — heavy rain, floods, extreme heat, local curfews, or strikes — they are forced off the road with zero income and zero safety net.  

👉 **No work = No pay = No safety net**

GigShield is an AI-enabled parametric insurance platform that automatically detects these disruptions, triggers claims, and pays out lost wages — without the worker filing a single form.

---

## 🧠 Why Parametric Insurance?

Traditional insurance requires:
- Manual claim filing  
- Document verification  
- Long settlement times  

Gig workers cannot afford delays.

👉 GigShield uses parametric insurance, where:
- Payout is triggered automatically  
- Based on real-world data (weather, events, demand)  
- No human intervention required  

**Result:**  
⚡ Instant payouts  
📉 Zero paperwork  
🤝 High trust for gig workers  

---

## 👤 Chosen Persona

Food Delivery Partners on Zomato and Swiggy operating in Tier-1 Indian cities (Mumbai, Delhi, Bengaluru, Chennai, Hyderabad).

### Persona Profile

| Attribute | Detail |
|----------|--------|
| Name | Raju / Priya (typical gig worker) |
| Platform | Zomato / Swiggy |
| Vehicle | 2-wheeler (bike/scooter) |
| Daily Hours | 8–12 hours |
| Weekly Earnings | ₹2,500 – ₹4,500 |
| Pain Point | Loses 20–30% monthly income during rain, heatwaves, or curfews |
| Tech Comfort | WhatsApp-native, basic smartphone user |

---

## 🎯 Coverage Scope (What We Insure)

⚠️ We ONLY insure loss of income. No health, no accidents, no vehicle repair — ever.

| Covered ✅ | NOT Covered ❌ |
|-----------|--------------|
| Lost wages during heavy rainfall (IMD-verified) | Health / medical bills |
| Lost income during extreme heat (>43°C outdoor work ban) | Vehicle repair or damage |
| Lost earnings during local strikes / curfews | Accidents |
| Income loss during AQI-triggered delivery bans | Life insurance |
| Loss due to platform-wide app outages (>2 hrs) | Rider's personal decisions |

---

## 📋 Persona-Based Scenarios & Application Workflow

### 🌧️ Scenario 1 — "The Mumbai Monsoon Blackout"
Raju works in Andheri, Mumbai. On July 14, the IMD issues a Red Alert — rainfall exceeds 65mm in 3 hours. Zomato suspends all deliveries. Raju loses an entire day (₹700). GigShield auto-detects the Red Alert, validates Raju's active policy, and triggers a ₹700 payout to his UPI in under 10 minutes.

---

### 🔥 Scenario 2 — "The Delhi Heatwave"
Priya delivers in South Delhi. NDMA issues an outdoor work advisory when temperatures cross 45°C. She cannot work 10am–5pm. GigShield detects the advisory, calculates 7 lost hours × her hourly rate (₹80/hr), and pays ₹560 automatically.

---

### 🚫 Scenario 3 — "The City Strike"
A bandh is called in Bengaluru affecting 3 zones. Raju's GPS shows he is in a locked-down zone. He logs into GigShield — the system has already flagged the disruption and initiated his claim. Payout: ₹650 within the hour.

---

### 📉 Scenario 4 — Demand Crash (NEW 🚨)

Post-festival slowdown → orders drop by 60%  
Worker stays online but earns only ₹200 vs ₹800  

👉 GigShield detects abnormal drop via platform trends  
👉 Pays ₹600 partial compensation  

---


## 🔄 Application Workflow

```
[Worker Onboarding]
        ↓
Enter Name, City, Platform (Zomato/Swiggy), Avg. Weekly Earnings
        ↓
AI Risk Profiling (zone, weather history, work pattern)
        ↓
Weekly Premium Quote Generated (₹25 – ₹75/week)
        ↓
Worker Selects Plan → Pays via UPI/wallet (weekly auto-debit)
        ↓
Policy Activated → Real-time disruption monitoring begins
        ↓
[DISRUPTION EVENT DETECTED by API]
        ↓
AI Fraud Check → Location & Activity Validation
        ↓
Claim Auto-Triggered → Payout to UPI within 10 minutes
        ↓
Worker notified via WhatsApp / SMS
```

---

## 💰 Weekly Premium Model

Gig workers are paid weekly — our premium model mirrors this exactly.

### Base Weekly Premium Tiers

| Plan | Weekly Coverage | Weekly Premium | Best For |
|------|---------------|---------------|----------|
| Basic Kavach | Up to ₹1,500/week | ₹25/week | Part-time riders |
| Standard Raksha | Up to ₹3,000/week | ₹45/week | Full-time riders |
| Premium Suraksha | Up to ₹5,000/week | ₹75/week | Top earners / peak season |

---

## 📊 Business Model

- Weekly premiums from workers (₹25–₹75)  
- Risk pooled across cities and workers  
- Low operational cost (AI automation)  

### 💰 Revenue Streams:
- Premium margin (after payouts)  
- Partnerships with platforms (Zomato/Swiggy)  
- Government or NGO subsidies (future)  

👉 **Key Insight:** Not all workers claim every week → ensures profitability  

---

## 🤖 AI-Adjusted Pricing Factors

- Zone Risk Score — Historical flood/heat/strike frequency  
- Seasonal Risk — Monsoon months → +10–15%  
- Claim History — Discounts up to ₹10/week  
- Platform Tenure — Lower risk for long-term workers  
- AQI Trends — Higher pricing in polluted zones  

**Example:**  
- Dharavi (Mumbai) → ₹52/week  
- Koramangala (Bengaluru) → ₹40/week  

---

## ⚡ Parametric Triggers (5 Core Triggers)

| Trigger | Data Source | Threshold | Payout Basis |
|--------|------------|----------|--------------|
| Heavy Rainfall | IMD API / OpenWeatherMap | ≥64.5mm/3hr or ≥35mm | % of income |
| Extreme Heat | IMD / NDMA | ≥43°C advisory | Hourly |
| Flood / Road Closure | Google Maps API | Zone inaccessible | Full shift |
| Local Strike / Curfew | News API | Zone restriction | Full shift |
| Platform App Outage | Platform API | >2 hrs | Hourly |

---

##  Edge Cases & Limitations

- False positives from API data → mitigated via multi-source validation  
- Workers going offline voluntarily → not covered  
- Sudden extreme events without data → delayed trigger  

👉 System prioritizes **accuracy over false payouts**

---

## 🤖 AI/ML Integration Plan

### 1. Dynamic Premium Calculation (Week 2–3)
- Model: XGBoost  
- Inputs: zone, platform, work hours, season  
- Output: weekly premium  

### 2. Fraud Detection Engine (Week 5–6)
- GPS validation  
- Activity anomaly detection  
- Device fingerprinting  
- Historical comparison  
- Cooling period for new users  

### 3. Risk Profiling (Week 1–2)
- K-Means clustering  
- Risk score (0–100)  

### 4. Payout Calculation Model


Payout = min(daily_avg_earnings × (hours_affected / work_day_hours), weekly_coverage_limit)


---

## 🏗️ Tech Stack

| Layer | Technology |
|------|-----------|
| Frontend | React.js (PWA) |
| Backend | Node.js + Express |
| Database | PostgreSQL + Redis |
| AI/ML | Python (scikit-learn, XGBoost) |
| APIs | Weather, Maps, News |
| Payments | Razorpay |
| Notifications | Twilio |
| Hosting | Vercel + Render |

---

## 📱 Why Web (PWA) over Native Mobile?

- No app store friction  
- Works on low-end phones  
- WhatsApp-accessible  
- Offline capable  

---

## 🔐 Data Privacy & Security

- Minimal data collection  
- GPS only during validation  
- Encrypted storage  
- No third-party sharing  

👉 Privacy-first approach  

---

## 📁 Repository Structure


gigshield/
├── frontend/
├── backend/
├── ml-service/
├── mock-apis/
├── docs/
└── README.md

---

## 🌍 Scalability & Future Expansion

- Expand to:
  - Ola / Uber drivers  
  - Blinkit / Zepto workers  

- Add triggers:
  - Fuel price spikes  
  - Political disruptions  

👉 Goal: India’s default gig worker safety net  

---

## 🔒 Key Design Principles

- Zero-touch claims  
- Weekly-first model  
- Hyper-local pricing  
- WhatsApp-native UX  
- Income-only focus  

---

##  Advantage

| Feature | GigShield | Traditional Insurance |
|--------|----------|----------------------|
| Claims | Automatic | Manual |
| Payout Time | <10 min | Days/Weeks |
| Target Users | Gig workers | General public |
| Pricing | Weekly | Monthly/Yearly |
| Data Usage | Real-time | Static |

