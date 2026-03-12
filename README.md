# DeliveryWorker-Insurance

# 🛡️ GigShield — AI-Powered Parametric Income Insurance for India's Gig Workers

> **Guidewire DEVTrails 2026 | University Hackathon**
> Persona: Food Delivery Partners (Zomato / Swiggy)

---

## 🧩 Problem Statement

India's food delivery partners (Zomato, Swiggy) earn ₹12,000–₹20,000/month and operate entirely on gig-based, week-to-week income. When external disruptions occur — heavy rain, floods, extreme heat, local curfews, or strikes — they are **forced off the road with zero income and zero safety net**.

**GigShield** is an AI-enabled parametric insurance platform that automatically detects these disruptions, triggers claims, and pays out lost wages — without the worker filing a single form.

---

## 👤 Chosen Persona

**Food Delivery Partners** on Zomato and Swiggy operating in Tier-1 Indian cities (Mumbai, Delhi, Bengaluru, Chennai, Hyderabad).

### Persona Profile

| Attribute | Detail |
|---|---|
| Name | Raju / Priya (typical gig worker) |
| Platform | Zomato / Swiggy |
| Vehicle | 2-wheeler (bike/scooter) |
| Daily Hours | 8–12 hours |
| Weekly Earnings | ₹2,500 – ₹4,500 |
| Pain Point | Loses 20–30% monthly income during rain, heatwaves, or curfews |
| Tech Comfort | WhatsApp-native, basic smartphone user |

---

## 🎯 Coverage Scope (What We Insure)

> ⚠️ **We ONLY insure loss of income. No health, no accidents, no vehicle repair — ever.**

| Covered ✅ | NOT Covered ❌ |
|---|---|
| Lost wages during heavy rainfall (IMD-verified) | Health / medical bills |
| Lost income during extreme heat (>43°C outdoor work ban) | Vehicle repair or damage |
| Lost earnings during local strikes / curfews | Accidents |
| Income loss during AQI-triggered delivery bans | Life insurance |
| Loss due to platform-wide app outages (>2 hrs) | Rider's personal decisions |

---

## 📋 Persona-Based Scenarios & Application Workflow

### Scenario 1 — "The Mumbai Monsoon Blackout"
> Raju works in Andheri, Mumbai. On July 14, the IMD issues a Red Alert — rainfall exceeds 65mm in 3 hours. Zomato suspends all deliveries. Raju loses an entire day (₹700). **GigShield auto-detects the Red Alert, validates Raju's active policy, and triggers a ₹700 payout to his UPI in under 10 minutes.**

### Scenario 2 — "The Delhi Heatwave"
> Priya delivers in South Delhi. NDMA issues an outdoor work advisory when temperatures cross 45°C. She cannot work 10am–5pm. **GigShield detects the advisory, calculates 7 lost hours × her hourly rate (₹80/hr), and pays ₹560 automatically.**

### Scenario 3 — "The City Strike"
> A bandh is called in Bengaluru affecting 3 zones. Raju's GPS shows he is in a locked-down zone. He logs into GigShield — the system has already flagged the disruption and initiated his claim. **Payout: ₹650 within the hour.**

### Application Workflow

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
|---|---|---|---|
| Basic Kavach | Up to ₹1,500/week | ₹25/week | Part-time riders |
| Standard Raksha | Up to ₹3,000/week | ₹45/week | Full-time riders |
| Premium Suraksha | Up to ₹5,000/week | ₹75/week | Top earners / peak season |

### AI-Adjusted Pricing Factors

The weekly premium is **dynamically adjusted** by our ML model using:

- **Zone Risk Score** — Historical flood/heat/strike frequency in the worker's operating zone
- **Seasonal Risk** — Monsoon months → premium may increase 10–15%
- **Claim History** — Low-claim workers get loyalty discounts (up to ₹10/week off)
- **Platform Tenure** — Verified long-term Zomato/Swiggy partners get lower risk scores
- **AQI Trends** — High-pollution zones (Delhi winter) priced higher

> **Example:** Raju operates in Dharavi (Mumbai) — historically flood-prone. His Standard Raksha plan is ₹52/week instead of ₹45. Priya operates in Koramangala (Bengaluru) — low-risk zone, so she pays ₹40/week.

---

## ⚡ Parametric Triggers (5 Core Triggers)

No manual claim filing. Disruption is detected — payout fires automatically.

| Trigger | Data Source | Threshold | Payout Basis |
|---|---|---|---|
| **Heavy Rainfall** | IMD API / OpenWeatherMap | Red Alert (≥64.5mm/3hr) or Orange Alert (≥35mm) | % of daily avg earnings × hours affected |
| **Extreme Heat** | IMD / NDMA advisory feed | Outdoor work advisory issued (≥43°C) | Hours of advisory × hourly rate |
| **Flood / Road Closure** | Google Maps Traffic API (mock) | Worker's zone classified "inaccessible" | Full affected shift payout |
| **Local Strike / Curfew** | News API + Government RSS feeds | Zone-level curfew or bandh detected | Full shift payout |
| **Platform App Outage** | Platform API / mock | Delivery app down >2 continuous hours | Hours × hourly rate |

---

## 🤖 AI/ML Integration Plan

### 1. Dynamic Premium Calculation (Week 2–3)
- **Model:** Gradient Boosted Trees (XGBoost) trained on historical weather + claim data
- **Inputs:** Worker's city zone, platform, work hours, season, historical disruption frequency
- **Output:** Weekly premium price (₹/week), dynamically adjusted each renewal

### 2. Fraud Detection Engine (Week 5–6)
- **GPS Spoofing Detection:** Cross-validate worker's last GPS ping against platform logs and IP geolocation
- **Anomaly Scoring:** Flag claims where the worker's last activity log shows deliveries during the "disruption window" (model trained on behavioral baseline)
- **Duplicate Prevention:** Fingerprinting by phone number, bank account, device ID
- **Historical Comparison:** Deny claims if IMD/NDMA data doesn't corroborate the reported disruption in the claimed zone
- **Suspicious Pattern Detection:** Workers who only activate policies right before known weather events (last-minute signups get a 7-day cooling period)

### 3. Risk Profiling (Week 1–2)
- **Clustering Model:** K-Means clustering of zones by risk profile (flood-prone, heat-prone, strike-prone)
- **Worker Scoring:** Individual risk score (0–100) factoring tenure, zone, and platform behavior

### 4. Payout Calculation Model
- **Formula:** `Payout = min(daily_avg_earnings × (hours_affected / work_day_hours), weekly_coverage_limit)`
- **Daily average** derived from worker's self-declared + platform-verified weekly income

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | React.js (Web) + Progressive Web App (mobile-friendly) |
| **Backend** | Node.js + Express.js |
| **Database** | PostgreSQL (policies, claims) + Redis (real-time trigger cache) |
| **AI/ML** | Python (scikit-learn, XGBoost) via FastAPI microservice |
| **Weather API** | OpenWeatherMap API (free tier) + IMD RSS feeds |
| **Traffic/Maps** | Google Maps Platform (mock mode for hackathon) |
| **News/Curfew** | NewsAPI.org (free tier) for strike/curfew detection |
| **Payments** | Razorpay Test Mode (UPI simulator) |
| **Notifications** | Twilio SMS / WhatsApp Business API (sandbox) |
| **Hosting** | Vercel (frontend) + Railway / Render (backend) |
| **CI/CD** | GitHub Actions |

### Why Web (PWA) over Native Mobile?
- No app store friction — workers access via WhatsApp link or browser
- Works on low-end Android phones (2GB RAM) with basic browser
- Instant updates without app store approval cycles
- Offline-capable PWA for low-connectivity areas

---

## 📁 Repository Structure

```
gigshield/
├── frontend/               # React PWA
│   ├── src/
│   │   ├── pages/          # Onboarding, Dashboard, Claims, Policy
│   │   └── components/
├── backend/                # Node.js + Express API
│   ├── routes/             # auth, policy, claims, triggers
│   ├── models/             # DB schemas
│   └── services/           # WeatherService, FraudService, PayoutService
├── ml-service/             # Python FastAPI
│   ├── premium_model/      # XGBoost premium calculator
│   ├── fraud_model/        # Anomaly detection
│   └── risk_profiler/      # Zone + worker risk scoring
├── mock-apis/              # Simulated Zomato/Swiggy/Payment APIs
├── docs/                   # Architecture diagrams, API specs
└── README.md
```

---

## 🗓️ 6-Week Development Plan

### Phase 1 (March 4–20): Ideation & Foundation ✅
- [x] Persona definition and scenario mapping
- [x] Weekly premium model design
- [x] Parametric trigger identification
- [x] Tech stack selection
- [ ] Basic project scaffolding (frontend + backend boilerplate)
- [ ] Mock API structure for weather and platform data

### Phase 2 (March 21 – April 4): Automation & Protection
- [ ] Worker registration & onboarding flow
- [ ] Insurance policy creation with weekly premium calculation
- [ ] AI premium model (XGBoost) — v1
- [ ] 5 parametric trigger integrations (weather, heat, curfew, outage)
- [ ] Claims management system
- [ ] Basic fraud checks (duplicate, GPS validation)

### Phase 3 (April 5–17): Scale & Optimise
- [ ] Advanced fraud detection (GPS spoofing, behavioral anomaly)
- [ ] Razorpay test mode payout integration
- [ ] Worker dashboard (earnings protected, active coverage)
- [ ] Admin/Insurer dashboard (loss ratios, predictive analytics)
- [ ] Final pitch deck + 5-min demo video

---

## 🔒 Key Design Principles

1. **Zero-touch claims** — Workers never file a form. The system detects, validates, and pays.
2. **Weekly-first finance** — Premium and payout cycle matches the gig economy's weekly earnings rhythm.
3. **Hyper-local risk** — Pricing is pin-code level, not city-level.
4. **WhatsApp-native UX** — Every key action (policy status, claim update, payout confirmation) reachable via WhatsApp message.
5. **Income-only coverage** — Absolutely no feature creep into health, accident, or vehicle coverage.


