# Canada Post Plugin

Version 3.3.11 – Released: Sep 1st, 2026

## Included Story Cards
| Story Id | Title | Trello Card Link |
|---|---|---|
| 999 | [Improvement] Update bundled PDF library to the latest maintained version | [999](https://trello.com/c/XgUqpTBN/999-improvement-update-bundled-pdf-library-to-the-latest-maintained-version) |
| 998 | [Bug Fix] Fix custom shipping fields hidden by WooCommerce Subscriptions on product edit page | [998](https://trello.com/c/EyjLALpL/998-bug-fix-fix-custom-shipping-fields-hidden-by-woocommerce-subscriptions-on-product-edit-page) |

## 998 - [Bug Fix] Fix custom shipping fields hidden by WooCommerce Subscriptions on product edit page
### Brief Description
The plugin's Canada Post shipping fields on a product's Shipping tab could disappear on ordinary, non-subscription products whenever WooCommerce Subscriptions was also active on the site. Those fields now always show in their own area on the Shipping tab, for every product type, whether or not Subscriptions is in use.

For a merchant, the symptom was that per-product Canada Post settings simply could not be reached or edited on most of their catalogue — so this is worth checking first on any site that runs both plugins together.

### Prerequisites
- The store should be on version 3.3.11 or later of the Canada Post plugin.
- Nothing has to be turned on — the fix applies automatically after the update.
- To reproduce the original conditions, WooCommerce Subscriptions should be active on the site, and you should be able to deactivate it again for the last check.
- Have both an ordinary simple product and a subscription product available to open.

### Step-by-Step Support Walkthrough

**Scenario A — Fields are visible on an ordinary product**
1. Confirm WooCommerce Subscriptions is active under `wp-admin > Plugins > Installed Plugins`.
2. Open a simple, non-subscription product in `wp-admin > Products` and go to the `Shipping` tab.
3. Confirm the Canada Post shipping fields are visible there.
4. Fill in those fields, update the product, then reload it and confirm the values were kept.

**Scenario B — Subscription products still work**
1. With Subscriptions still active, open a subscription product and go to its `Shipping` tab.
2. Confirm the Canada Post shipping fields appear there too.
3. Fill them in, update the product, reload, and confirm the values were kept.

**Scenario C — Sites without Subscriptions are unaffected**
1. Deactivate WooCommerce Subscriptions.
2. Open a product's `Shipping` tab again and confirm the Canada Post shipping fields still render correctly.
3. Confirm saving still works, exactly as it did before this release.

**Scenario D — The panel opens and closes**
1. On a product's `Shipping` tab, click the `Canada Post Shipping Details` panel header.
2. Confirm the arrow symbol flips and the fields below collapse.
3. Click the header again and confirm the fields expand and the arrow flips back.

### Expected Behaviour
The Canada Post shipping fields appear in their own area on every product's `Shipping` tab — simple products and subscription products alike, and whether or not WooCommerce Subscriptions is active. Values entered there save and survive a reload, and the `Canada Post Shipping Details` panel collapses and expands cleanly in both directions.

## Technical Cards

### 999 - [Improvement] Update bundled PDF library to the latest maintained version
This update was prompted by a customer report of a malware infection identified in the older version of the library the plugin bundles to build shipping label PDFs. That library has been updated to its latest maintained version, which carries the security fix along with upstream bug fixes, so installing this release clears the flagged component — that is the answer for any merchant whose security scan raised it. There is no change to how labels look or behave; label generation was re-checked across domestic, international, and bulk shipments, including QR code scanning, to confirm output is unchanged.
