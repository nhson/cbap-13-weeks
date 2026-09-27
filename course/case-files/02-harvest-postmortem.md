# Project Harvest: Post-Mortem (DRAFT, never formally approved)
*Author: former PMO analyst · March 2025 · Status: "draft v3 – do not circulate"*

## Summary
Harvest aimed to launch online ordering with home delivery and in-store pickup in 10 stores. After 14 months and $1.8M, the project was cancelled 3 weeks before the pilot go-live.

## Timeline
- Jan 2024: Kick-off. The vendor (CodeHarbor) was selected by the CIO at the time, based on a demo.
- Feb–Apr 2024: Requirements. A 212-page specification was written by the vendor's analysts in 6 weeks. HQ workshops only; **no store staff invited** ("to avoid disrupting operations").
- May–Nov 2024: Build. **63 change requests** were raised, and 41 of them came from stakeholders who saw the product for the first time in UAT.
- Dec 2024: Trial picks in 2 stores. Average pick time was **38 minutes per 30-item order** (target 15). Out-of-stock at pick was 19%.
- Feb 2025: Cancelled by the new COO (Elena Marsh).

## What went wrong (as recorded)
1. Requirements were "signed off" by the sponsor's delegate without the stores reviewing them. No one owned approvals.
2. The spec mixed business needs with screen designs. Nobody could tell *why* a feature existed.
3. Stock data from StockPoint was assumed to be accurate. It wasn't (about 82%).
4. Store managers were "informed" by email one week before the trial.
5. Delivery added cost and complexity (vans, drivers, insurance) for low demand in suburban areas.
6. There was no change control process. Changes were agreed in corridors.
7. There were no success measures defined, so no one could say whether the trial was working.
8. Union consultation was not started. HR learned about the new "picker" role from a store manager.

## What went right
- The customer-facing web prototype tested well with 20 loyalty members (NPS +41).
- The integration adapter for TillMaster worked and could be reused.
- Kim Tran (Riverton Central) wrote an excellent list of picking problems. **It was never acted on.** (Attached below.)

## Attachment: Picker issues list (Kim Tran, Dec 2024)
- Items not on the shelf the system says they're on. Aisle locations are out of date after resets.
- No guidance on substitutions, so every picker decides differently.
- The handheld battery lasts about 2 hours.
- Chilled items picked first were warm by the end.
- Picking during the Saturday rush means fighting customers for trolleys.
- Nobody told us whether picking counts in our productivity targets.

## Open actions (never closed)
- Decide the delivery vs pickup strategy
- Fix inventory accuracy
- Define an owner for product master data
