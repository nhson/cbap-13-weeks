# IT Landscape: Systems Relevant to Click & Collect (Anil Kapoor, Enterprise Architecture)

```
[TillMaster POS v9] --real-time--> [Basket Rewards (loyalty, cloud)]
        |                                   |
   nightly batch                       app (points & coupons only)
        v
[StockPoint inventory (on-prem, 2011)] <--weekly-- [Supplier EDI / DC replenishment]
        ^
   spreadsheets
[Product master data: Category team spreadsheets]
[Brochure website (CMS)]      [Payment gateway: PayRail (card-present only today)]
[Workforce scheduling: RosterPro]   [Handhelds: 2016 models, ~40% failing]
```

## Key facts
- **StockPoint** has no API. The only way out is a nightly flat-file export. The vendor offers a paid "Connect" API module ($180k and 5 months).
- **Inventory accuracy** is 82% on average: 91% in dry grocery, 74% in fresh/chilled.
- **Aisle location data** exists for 60% of SKUs and goes stale after planogram resets (every 6–8 weeks).
- **TillMaster** can accept "pre-paid order" transactions with a firmware upgrade (v9.4). The Harvest adapter is reusable.
- **PayRail** supports online card-not-present payments, but it puts the web channel in PCI-DSS scope unless a hosted payment page is used.
- **Basket Rewards** has an API for earning and burning points. Digital coupons are *not* exposed through the API.
- **Handhelds:** a replacement is budgeted for next fiscal year only.
- **Security:** all new SaaS must pass a vendor security assessment (6–8 weeks).

## Anil's warning
"Whatever we choose, real-time stock is a myth with StockPoint. Near-real-time at best, and only if we fix the data first."
