REPORTS = [
    {
        "id": 1,
        "name": "Trade Lane Revenue Performance",
        "description": "Tracks booked and actual revenue by trade lane, origin, and destination port. Includes TEU volume and yield per TEU.",
        "use_case": "Use when preparing for quarterly business reviews, assessing trade lane profitability, or identifying underperforming routes.",
        "scope": "Booking-level aggregated by lane. Last 24 months. Excludes spot bookings under threshold. Dimensions: trade, lane, port pair, service.",
        "department": "Commercial",
        "report_type": "SSRS",
        "frequency": "Every Monday",
        "grain": "Booking-level",
        "topics": ["Revenue", "Volume"],
        "owner_name": "Jane Smith",
        "owner_email": "jane@cmacgm.com",
        "report_link": "https://reports.cmacgm.com/trade-lane-revenue",
        "keywords": ["revenue", "trade lane", "TEU", "volume", "yield", "port", "booking", "quarterly", "profitability", "lane performance"]
    },
    {
        "id": 2,
        "name": "Contract Utilization & Compliance Tracker",
        "description": "Monitors contract commitment vs. actual utilization by account, including compliance rate and shortfall volume.",
        "use_case": "Use when reviewing contract performance with key accounts, flagging under-utilized contracts before expiry, or preparing for renewal negotiations.",
        "scope": "Contract-level. Active contracts only. Dimensions: account, contract type, trade, validity period.",
        "department": "Contracts",
        "report_type": "SSRS",
        "frequency": "Every Friday",
        "grain": "Contract-level",
        "topics": ["Contracts", "Compliance"],
        "owner_name": "Mark Rivera",
        "owner_email": "mark@cmacgm.com",
        "report_link": "https://reports.cmacgm.com/contract-utilization",
        "keywords": ["contract", "utilization", "compliance", "account", "shortfall", "renewal", "expiry", "commitment"]
    },
    {
        "id": 3,
        "name": "Account-Level Booking Dashboard",
        "description": "Summarizes TEU volume, revenue, and booking frequency by named account over a rolling period.",
        "use_case": "Use when reviewing a specific account's activity, preparing for a customer meeting, or identifying accounts showing volume decline.",
        "scope": "Account-level summary. Rolling 12 months. Dimensions: account, service, trade, booking channel.",
        "department": "Commercial",
        "report_type": "C-Report",
        "frequency": "1st of each month",
        "grain": "Account-level",
        "topics": ["Revenue", "Volume"],
        "owner_name": "Amy Lin",
        "owner_email": "amy@cmacgm.com",
        "report_link": "https://reports.cmacgm.com/account-bookings",
        "keywords": ["account", "booking", "customer", "TEU", "volume", "revenue", "decline", "activity"]
    },
    {
        "id": 4,
        "name": "Shipment Performance Report",
        "description": "Tracks outbound shipment volume and on-time delivery performance at the shipment line level, by carrier and warehouse.",
        "use_case": "Use when investigating carrier delivery delays, auditing fulfillment accuracy by warehouse, or preparing for a logistics review meeting.",
        "scope": "Shipment line-level. Last 24 months. Excludes cancelled and test orders. Dimensions: carrier, warehouse, region, product category.",
        "department": "Logistics",
        "report_type": "SSRS",
        "frequency": "Every Monday",
        "grain": "Shipment line-level",
        "topics": ["Shipment", "Performance"],
        "owner_name": "David Park",
        "owner_email": "david@cmacgm.com",
        "report_link": "https://reports.cmacgm.com/shipment-performance",
        "keywords": ["shipment", "on-time", "delivery", "carrier", "warehouse", "logistics", "fulfillment", "delay", "outbound"]
    },
    {
        "id": 5,
        "name": "Customer Care Case Volume Tracker",
        "description": "Tracks incoming case volume by category, priority, and resolution time across customer care teams.",
        "use_case": "Use when monitoring team workload, identifying recurring issue types, or preparing SLA compliance reports.",
        "scope": "Case-level. Rolling 6 months. Dimensions: case type, priority, agent, resolution status.",
        "department": "Customer Care",
        "report_type": "C-Report",
        "frequency": "Every business day",
        "grain": "Case-level",
        "topics": ["Customer", "Performance"],
        "owner_name": "Sarah Chen",
        "owner_email": "sarah@cmacgm.com",
        "report_link": "https://reports.cmacgm.com/case-volume",
        "keywords": ["case", "customer care", "SLA", "resolution", "workload", "priority", "agent", "ticket"]
    },
    {
        "id": 6,
        "name": "Finance P&L Summary by Trade",
        "description": "Monthly profit and loss summary broken down by trade, including revenue, cost, and margin contribution.",
        "use_case": "Use when reviewing financial performance by trade for monthly close, board reporting, or identifying margin erosion by route.",
        "scope": "Trade-level aggregated. Last 12 months. Excludes intercompany transactions. Dimensions: trade, cost center, GL account.",
        "department": "Finance",
        "report_type": "SSRS",
        "frequency": "1st of each month",
        "grain": "Trade-level",
        "topics": ["Revenue", "Cost", "Margin"],
        "owner_name": "Laura Bennett",
        "owner_email": "laura@cmacgm.com",
        "report_link": "https://reports.cmacgm.com/finance-pl",
        "keywords": ["P&L", "profit", "loss", "margin", "cost", "revenue", "finance", "monthly close", "board", "GL"]
    },
    {
        "id": 7,
        "name": "Carrier Cost & Lane Analysis",
        "description": "Breaks down shipping cost per unit by carrier, lane, and origin warehouse. Includes transit time averages.",
        "use_case": "Use when negotiating carrier contracts, benchmarking lane costs, or identifying cost reduction opportunities by route.",
        "scope": "Order-level aggregated by lane. Last 12 months. Dimensions: carrier, origin, destination, product weight band.",
        "department": "Logistics",
        "report_type": "C-Report",
        "frequency": "1st of each month",
        "grain": "Order-level",
        "topics": ["Cost", "Shipment"],
        "owner_name": "David Park",
        "owner_email": "david@cmacgm.com",
        "report_link": "https://reports.cmacgm.com/carrier-cost",
        "keywords": ["carrier", "cost", "lane", "transit", "negotiation", "benchmark", "route", "shipping cost"]
    },
    {
        "id": 8,
        "name": "Trade Forecast vs Actuals",
        "description": "Compares forecasted vs actual TEU volume and revenue by trade and service, with variance explanation.",
        "use_case": "Use when presenting to leadership on forecast accuracy, identifying trades with consistent over or under-performance, or adjusting capacity plans.",
        "scope": "Trade and service level. Rolling 6 months forward, 12 months back. Dimensions: trade, service, vessel, direction.",
        "department": "Trade",
        "report_type": "SSRS",
        "frequency": "Every Monday",
        "grain": "Trade-level",
        "topics": ["Forecast", "Volume", "Revenue"],
        "owner_name": "James Okoye",
        "owner_email": "james@cmacgm.com",
        "report_link": "https://reports.cmacgm.com/trade-forecast",
        "keywords": ["forecast", "actuals", "variance", "TEU", "capacity", "trade", "service", "vessel", "over-performance", "under-performance"]
    },
    {
        "id": 9,
        "name": "Governance KPI Dashboard",
        "description": "Consolidates key performance indicators across all departments into a single executive-level dashboard.",
        "use_case": "Use for monthly executive reviews, board presentations, or cross-department performance benchmarking.",
        "scope": "Summary-level. All departments. Rolling 12 months. Refreshed after monthly close. Dimensions: department, KPI category.",
        "department": "Governance",
        "report_type": "C-Report",
        "frequency": "1st of each month",
        "grain": "Summary-level",
        "topics": ["Performance", "KPI"],
        "owner_name": "Michelle Torres",
        "owner_email": "michelle@cmacgm.com",
        "report_link": "https://reports.cmacgm.com/governance-kpi",
        "keywords": ["KPI", "executive", "governance", "dashboard", "board", "performance", "benchmark", "cross-department"]
    },
    {
        "id": 10,
        "name": "Data Quality & Completeness Monitor",
        "description": "Tracks data completeness, null rates, and anomaly flags across key operational data sources.",
        "use_case": "Use when investigating data issues impacting downstream reports, auditing source data quality, or preparing for a data governance review.",
        "scope": "Field-level completeness scores. All major source tables. Refreshed daily. Dimensions: source system, table, field, data domain.",
        "department": "Data Management",
        "report_type": "SSRS",
        "frequency": "Every business day",
        "grain": "Field-level",
        "topics": ["Data Quality", "Monitoring"],
        "owner_name": "Kevin Zhang",
        "owner_email": "kevin@cmacgm.com",
        "report_link": "https://reports.cmacgm.com/data-quality",
        "keywords": ["data quality", "completeness", "null", "anomaly", "source", "audit", "governance", "pipeline"]
    },
    {
        "id": 11,
        "name": "Customer Satisfaction & NPS Tracker",
        "description": "Tracks Net Promoter Score and satisfaction ratings from post-shipment surveys, segmented by trade and service type.",
        "use_case": "Use when preparing customer experience reports, identifying service types with low satisfaction, or tracking NPS trend over time.",
        "scope": "Survey response level. Rolling 12 months. Excludes incomplete responses. Dimensions: trade, service, customer segment, survey wave.",
        "department": "Customer Care",
        "report_type": "C-Report",
        "frequency": "Quarterly",
        "grain": "Survey-level",
        "topics": ["Customer", "Performance"],
        "owner_name": "Sarah Chen",
        "owner_email": "sarah@cmacgm.com",
        "report_link": "https://reports.cmacgm.com/nps-tracker",
        "keywords": ["NPS", "satisfaction", "survey", "customer experience", "net promoter", "rating", "feedback"]
    },
    {
        "id": 12,
        "name": "Contract Expiry & Renewal Pipeline",
        "description": "Lists all active contracts approaching expiry within a configurable window, with renewal status and account owner.",
        "use_case": "Use when planning renewal outreach, prioritizing accounts at risk of lapsing, or tracking the commercial pipeline for the next quarter.",
        "scope": "Contract-level. Active and recently expired contracts. Configurable expiry window (default 90 days). Dimensions: account, trade, contract type, account owner.",
        "department": "Contracts",
        "report_type": "SSRS",
        "frequency": "Every Monday",
        "grain": "Contract-level",
        "topics": ["Contracts", "Pipeline"],
        "owner_name": "Mark Rivera",
        "owner_email": "mark@cmacgm.com",
        "report_link": "https://reports.cmacgm.com/contract-renewal",
        "keywords": ["renewal", "expiry", "pipeline", "contract", "lapse", "account", "outreach", "90 days"]
    },
]

DEPARTMENTS = ["Customer Care", "Finance", "Commercial", "Governance", "Logistics", "Trade", "Contracts", "Data Management"]
REPORT_TYPES = ["SSRS", "C-Report"]
FREQUENCIES = ["Ad-hoc", "Every business day", "Every Monday", "Every Friday", "1st of each month", "Quarterly"]

# Follow-up questions triggered when input is vague, keyed by department
FOLLOWUP_QUESTIONS = {
    "Commercial": {
        "question": "What are you mainly trying to understand for Commercial?",
        "options": [
            "Track revenue or volume performance by trade or lane",
            "Monitor contract utilization or compliance",
            "Analyze customer or account-level trends",
            "Compare actuals vs. forecast"
        ],
        "keyword_map": {
            "Track revenue or volume performance by trade or lane": ["revenue", "volume", "trade", "lane"],
            "Monitor contract utilization or compliance": ["contract", "utilization", "compliance"],
            "Analyze customer or account-level trends": ["account", "customer", "booking"],
            "Compare actuals vs. forecast": ["forecast", "actuals", "variance"]
        }
    },
    "Logistics": {
        "question": "What aspect of Logistics are you focused on?",
        "options": [
            "Carrier delivery delays or on-time performance",
            "Shipment volume or fulfillment throughput",
            "Shipping cost by carrier or lane",
            "Warehouse or regional performance"
        ],
        "keyword_map": {
            "Carrier delivery delays or on-time performance": ["carrier", "on-time", "delay", "delivery"],
            "Shipment volume or fulfillment throughput": ["shipment", "volume", "fulfillment"],
            "Shipping cost by carrier or lane": ["cost", "carrier", "lane"],
            "Warehouse or regional performance": ["warehouse", "region", "performance"]
        }
    },
    "Finance": {
        "question": "What financial topic are you investigating?",
        "options": [
            "P&L or margin performance by trade",
            "Cost analysis and breakdown",
            "Budget vs. actuals comparison",
            "Monthly close or board reporting"
        ],
        "keyword_map": {
            "P&L or margin performance by trade": ["P&L", "margin", "profit", "loss"],
            "Cost analysis and breakdown": ["cost", "breakdown", "analysis"],
            "Budget vs. actuals comparison": ["budget", "actuals", "variance"],
            "Monthly close or board reporting": ["monthly close", "board", "executive"]
        }
    },
    "Contracts": {
        "question": "What contract topic do you need visibility into?",
        "options": [
            "Contract utilization and shortfall",
            "Upcoming renewals or expiring contracts",
            "Compliance tracking by account",
            "New contract pipeline"
        ],
        "keyword_map": {
            "Contract utilization and shortfall": ["utilization", "shortfall", "commitment"],
            "Upcoming renewals or expiring contracts": ["renewal", "expiry", "pipeline"],
            "Compliance tracking by account": ["compliance", "account", "tracking"],
            "New contract pipeline": ["pipeline", "new", "commercial"]
        }
    },
    "Customer Care": {
        "question": "What customer care area are you focusing on?",
        "options": [
            "Case volume and workload",
            "SLA or resolution time performance",
            "Customer satisfaction or NPS",
            "Agent or team performance"
        ],
        "keyword_map": {
            "Case volume and workload": ["case", "volume", "workload"],
            "SLA or resolution time performance": ["SLA", "resolution", "time"],
            "Customer satisfaction or NPS": ["NPS", "satisfaction", "survey"],
            "Agent or team performance": ["agent", "team", "performance"]
        }
    },
    "Trade": {
        "question": "What trade topic are you looking into?",
        "options": [
            "Forecast vs. actuals by trade or service",
            "Capacity planning and vessel performance",
            "Trade lane profitability",
            "Volume trends by direction"
        ],
        "keyword_map": {
            "Forecast vs. actuals by trade or service": ["forecast", "actuals", "variance"],
            "Capacity planning and vessel performance": ["capacity", "vessel", "planning"],
            "Trade lane profitability": ["profitability", "lane", "trade"],
            "Volume trends by direction": ["volume", "direction", "trend"]
        }
    },
    "Governance": {
        "question": "What governance topic do you need?",
        "options": [
            "Executive KPI summary across departments",
            "Cross-department performance benchmarking",
            "Board or leadership reporting",
            "Regulatory or audit reporting"
        ],
        "keyword_map": {
            "Executive KPI summary across departments": ["KPI", "executive", "summary"],
            "Cross-department performance benchmarking": ["benchmark", "cross-department", "performance"],
            "Board or leadership reporting": ["board", "leadership", "reporting"],
            "Regulatory or audit reporting": ["regulatory", "audit", "compliance"]
        }
    },
    "Data Management": {
        "question": "What data management need are you addressing?",
        "options": [
            "Data quality or completeness issues",
            "Source system anomalies or errors",
            "Data governance audit",
            "Pipeline or refresh monitoring"
        ],
        "keyword_map": {
            "Data quality or completeness issues": ["quality", "completeness", "null"],
            "Source system anomalies or errors": ["anomaly", "error", "source"],
            "Data governance audit": ["governance", "audit", "compliance"],
            "Pipeline or refresh monitoring": ["pipeline", "refresh", "monitoring"]
        }
    }
}
