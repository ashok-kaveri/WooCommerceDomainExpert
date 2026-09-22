# WooCommerce UPS Shipping Plugin with Print Label

Version 6.6.4 – Released: Sept 17th, 2026

## Included Story Cards
| Story Id | Title | Trello Card Link |
|---|---|---|
| 1019 | [New Feature] Add option to skip commercial invoice for regions not in WooCommerce's country list | [1019](https://trello.com/c/SI23TDil/1019-new-feature-add-option-to-skip-commercial-invoice-for-regions-not-in-woocommerces-country-list) |
| 1021 | [Bug Fix] Incorrect HazMat quantity sent to UPS when product weight unit doesn't match account unit during rate request and label creation | [1021](https://trello.com/c/ABAZCdTG/1021-bug-fix-incorrect-hazmat-quantity-sent-to-ups-when-product-weight-unit-doesnt-match-account-unit-during-rate-request-and-label-c) |
| 1020 | [Bug Fix] Round shipping rate cost to store decimal precision when Rate Adjustment / Currency conversion is applied | [1020](https://trello.com/c/kVgnvuV0/1020-bug-fix-round-shipping-rate-cost-to-store-decimal-precision-when-rate-adjustment-currency-conversion-is-applied) |
| 1028 | [Bug Fix] Complete missing translations and fix broken translation strings across UPS plugin | [1028](https://trello.com/c/YO9ijjdF/1028-bug-fix-complete-missing-translations-and-fix-broken-translation-strings-across-ups-plugin) |

## 1019 - [New Feature] Add option to skip commercial invoice for regions not in WooCommerce's country list
### Brief Description
WooCommerce groups Northern Ireland orders under the UK (GB) country code, so the plugin always generated a commercial invoice for these shipments, even though Northern Ireland to GB movements do not need one. Merchants previously had no way to change this. A new hook now lets a merchant's own site logic tell the plugin to skip commercial invoice generation for a specific order — for example, one shipping to a Northern Ireland postcode. Nothing about the shipping label or the destination country changes; only the commercial invoice generation step is skipped, and only for orders the merchant chooses.

### Prerequisites
- The store should be on version 6.6.4 or later of the UPS Shipping plugin.
- This is opt-in and does nothing by itself after updating. A small customization must be added to the site (for example through the free "Code Snippets" plugin) that tells the plugin which orders should skip the commercial invoice. Support or a developer provides this customization on request — it is not a toggle on the plugin's settings screen.
- Have a Northern Ireland postcode ready to test with (starts with "BT", e.g. BT1 1AA), plus a normal GB address, an EU address, and a non-EU address for the regression checks.

### Step-by-Step Support Walkthrough

**Scenario A — Northern Ireland orders skip the commercial invoice**
1. With the merchant's Northern Ireland customization active on the site, open or place an order shipping to a Northern Ireland postcode starting with "BT" (e.g. BT1 1AA), with GB as the country.
2. Generate the UPS shipment/label for that order.
3. Confirm no commercial invoice document is generated for this shipment.
4. Repeat with the postcode entered in lowercase (e.g. bt1 1aa) and confirm the invoice is still skipped.

**Scenario B — Other GB orders are unaffected**
1. Open or place an order to a non-Northern-Ireland GB address (e.g. London).
2. Generate the shipment and confirm the commercial invoice is generated exactly as it was before this update.

**Scenario C — EU and non-EU orders are unaffected**
1. With the store's "Skip commercial invoice for EU" setting enabled, confirm an EU-to-EU order still skips the invoice as it did before.
2. With the Northern Ireland customization active, ship an order to a non-GB EU country (e.g. France) and confirm invoice behaviour is unaffected — only GB/Northern Ireland orders are targeted.
3. Ship an order to a non-EU, non-GB destination (e.g. United States) and confirm the commercial invoice generates as before.

**Scenario D — No customization present**
1. On a store with no Northern Ireland customization added, confirm every order type behaves exactly as it did before this release. Nothing changes unless a merchant deliberately adds the customization.

### Expected Behaviour
Once a merchant's Northern Ireland customization is active, shipments to Northern Ireland postcodes (BT prefix, either case) no longer generate a commercial invoice, while the shipment is still built against GB as the destination country. UPS displays the destination on the printed label as "Northern Ireland" based on the postcode even though GB is the country code used — this is expected and not a defect. All other GB, EU, and non-EU orders continue to generate (or skip, per the existing EU setting) a commercial invoice exactly as before. With no customization added, nothing changes for any order.

### Snippet for Reference
The customization referred to above is added to the store separately from the plugin update — it is not built into the plugin, because not every merchant ships to Northern Ireland. Add it through the free "Code Snippets" plugin (Snippets → Add New), leave the type as "Function (PHP)", set it to run everywhere, and activate it.

```php
add_filter(
    'ph_ups_skip_commercial_invoice',
    function( $skip, $order, $from_address, $to_address ) {
        // Northern Ireland postcodes start with "BT";
        // WooCommerce reports the country as GB.
        $postcode = trim( $to_address['postcode'] );
        if ( 'GB' === $to_address['country']
            && preg_match( '/^BT/i', $postcode ) ) {
            return true;
        }
        return $skip;
    },
    10,
    4
);
```

This checks the shipping postcode for the Northern Ireland "BT" prefix on GB orders and skips the commercial invoice only for those. Every other GB, EU, and non-EU order is unaffected.

## 1021 - [Bug Fix] Incorrect HazMat quantity sent to UPS when product weight unit doesn't match account unit during rate request and label creation
### Brief Description
When a HazMat (dangerous goods) product's weight was stored in a different unit than the store's configured UPS unit-of-measure setting — for example, product weight in grams while UPS is set to KG — the quantity declared to UPS used the raw, unconverted number. This could send a wildly incorrect dangerous-goods quantity to UPS: a 350g item, for instance, could be declared as 350 kg instead of 0.35 kg. This happened both when fetching shipping rates and when generating shipping labels. The quantity sent to UPS is now correctly converted into the store's configured UPS weight unit in both places. Regular, non-HazMat shipments are unaffected.

### Prerequisites
- The store should be on version 6.6.4 or later of the UPS Shipping plugin.
- Nothing needs turning on — the fix applies automatically after updating.
- A product marked as HazMat (dangerous goods) is needed, along with control over its weight, the store's weight unit (WooCommerce > Settings > Products), and the plugin's UPS unit-of-measure setting.

### Step-by-Step Support Walkthrough

**Scenario A — Mismatched units at the rate request stage**
1. Set the store's weight unit to Grams in WooCommerce > Settings > Products, and set the plugin's UPS unit-of-measure setting to KG. Mark a product as HazMat with a weight of 350g.
2. Add the product to cart and go to checkout to trigger a UPS rate request.
3. Confirm the rate request completes normally and a rate is returned.
4. Repeat with the store weight unit set to Pounds and the plugin's UPS unit-of-measure set to LB, using a 12 lb HazMat product, and confirm rates still return normally.

**Scenario B — Mismatched units at label/shipment creation**
1. Using the same 350g HazMat product (store unit Grams, plugin UOM KG), place the order and generate the shipping label/shipment.
2. Confirm the label/shipment generates successfully with no errors.
3. Add the same HazMat product twice to a single order (quantity 2) and generate the label; confirm it still generates successfully.

**Scenario C — Matching units and regression check**
1. Set the store weight unit and the plugin's UPS unit-of-measure setting to the same unit (e.g. both KG) and confirm a HazMat rate request and label generation both still complete successfully.
2. Confirm non-HazMat products still generate valid rates and labels with no errors.
3. Confirm a HazMat order with multiple line items of the same product still completes label generation end-to-end.

### Expected Behaviour
For HazMat (dangerous goods) shipments, the quantity declared to UPS is now always converted to match the store's configured UPS weight unit, whether it is used for a rate request or for generating a shipping label — including when a product is ordered more than once. Support does not see the declared number directly on any screen, but the practical result is that a mismatch between the store's product weight unit and the UPS unit-of-measure setting no longer sends UPS a wrong dangerous-goods quantity, and rate requests and label generation both complete normally. Regular, non-HazMat shipments behave exactly as before.

## 1020 - [Bug Fix] Round shipping rate cost to store decimal precision when Rate Adjustment / Currency conversion is applied
### Brief Description
When a UPS rate went through a percentage or flat Rate Adjustment, a currency conversion, or a combination of these, the value shown on the order screen was correctly rounded, but the value actually stored for that order could carry extra decimal places (for example, $219.16 on screen but 219.156 stored). Orders that split into multiple packages, or multiple vendor packages on multi-vendor stores, made this worse, since adding several already-rounded package costs together compounded the drift instead of cancelling it out. Third-party tools that read the stored value directly — such as the Advanced Order Export For WooCommerce plugin — exported the unrounded figure instead of what the customer and store owner actually saw. The shipping cost is now rounded to the store's configured decimal precision only once, after every package for the order has already been combined into its final total, so the exported/stored figure always matches what's shown on screen no matter how many packages or adjustments contributed to it. This applies consistently to the newer Shipping Zone method, the legacy global UPS method, and rates recalculated from the admin Edit Order screen.

### Prerequisites
- The store should be on version 6.6.4 or later of the UPS Shipping plugin.
- Nothing needs turning on — the fix applies automatically after updating.
- To see the original symptom, a plugin that exports the raw order value is useful, such as the free "Advanced Order Export For WooCommerce" plugin, exporting as CSV rather than XLS (XLS can re-round the value on its own).
- A UPS shipping service with a percentage or flat Rate Adjustment configured, and/or a store where the UPS response currency differs from the store currency, so a currency conversion applies.
- An order that splits into multiple packages for the same UPS service is the clearest way to demonstrate the fix, since that is where the old drift was largest.

### Step-by-Step Support Walkthrough

**Scenario A — Reproducing and confirming the fix**
1. Configure a UPS service (e.g. Ground) with a percentage Rate Adjustment (e.g. +7%).
2. Add enough items/quantity to the cart that the order splits into multiple packages for that service, and place the order.
3. Open the order in WooCommerce admin and note the displayed shipping cost.
4. Export the order using the Advanced Order Export plugin, in CSV format, and confirm the exported shipping cost matches the order screen exactly, to the store's configured number of decimals.

**Scenario B — Other adjustment types**
1. Repeat with a flat (currency) Rate Adjustment instead of a percentage one, and confirm the displayed and exported values still match.
2. With no Rate Adjustment at all, confirm rates still display and export correctly.
3. With Negotiated Rates enabled, confirm the negotiated rate cost is rounded the same way as the standard rate.

**Scenario C — Currency conversion**
1. With the store currency different from the UPS response currency, so a conversion applies, and no Rate Adjustment, confirm the exported/stored cost is rounded correctly.
2. Combine a currency conversion with a percentage or flat Rate Adjustment and confirm the final cost is still rounded correctly.

**Scenario D — Coverage across methods and settings**
1. Check that both the Shipping Zone UPS method and the legacy global UPS method show the correct rounded cost.
2. In admin Edit Order, use Calculate Shipping Cost and confirm the recalculated rate is also rounded correctly.
3. In WooCommerce > Settings > General, set "Number of decimals" to 0 and confirm the UPS rate cost stores/exports as a whole number. Set it to 3 and confirm it stores/exports with 3 decimals. Reset it to the default (2) and confirm the fix still rounds correctly.

### Expected Behaviour
The stored and exported shipping cost for a UPS rate always matches what is shown on the order screen, to the store's configured decimal precision, regardless of how many packages the order split into, whether a percentage or flat Rate Adjustment was applied, whether a currency conversion applied, or any combination of these. This holds for the Shipping Zone method, the legacy global UPS method, and rates recalculated from the admin Edit Order screen, and for any configured "Number of decimals" setting.

## 1028 - [Bug Fix] Complete missing translations and fix broken translation strings across UPS plugin
### Brief Description
Translation completion for French, German, Italian, and Spanish was around 68%, and many strings across the settings screens, the Help & Support page, order/shipment messages, and JavaScript-driven popups (registration, cleanup, and the checkout address-suggestion popup) were never marked for translation at all — they always showed in English regardless of the site's language. Separately, the "Print Label" and "Print Return Label" buttons on the order screen could show with blank text for some merchants, and the French translation file had a string missing a placeholder that could produce garbled admin messages. All four languages are now at 100% translated with no missing or broken placeholders, the blank Print Label/Print Return Label button text is fixed, and the broken French placeholder is fixed.

### Prerequisites
- The store should be on version 6.6.4 or later of the UPS Shipping plugin.
- Nothing needs enabling in the plugin settings — this is a translation and code-level fix. To see it, switch the WordPress site language under Settings > General > Site Language to each of French, German, Italian, and Spanish in turn.
- Testing must actually switch the site language for each of the four languages; checking only in English will not catch these fixes.
- Known limitation: order confirmation emails ("Processing Order" and "Order Completed") are not covered by this fix. If a customer places an order in a language other than the site's default language, those emails still go out in the site's default language rather than the customer's selected language. Flag this if a merchant specifically asks about translated order emails.

### Step-by-Step Support Walkthrough

**Scenario A — Admin screens**
1. Switch the site language to French and open the UPS Settings page. Confirm all labels, descriptions, and buttons appear in French, not English.
2. Switch to German and open the Help & Support tab. Confirm all text, including error/status messages, is in German.
3. Repeat the same check for Italian and Spanish across both screens.

**Scenario B — Print Label / Print Return Label buttons**
1. With the site language set to Italian, generate a UPS shipping label from an order and confirm the "Print Label" button shows visible Italian text, not a blank button.
2. Confirm the same for the "Print Return Label" button, and repeat the check across French, German, and Spanish.

**Scenario C — Checkout and popups**
1. With the site language set to Spanish, go to checkout with an address UPS will offer a correction for, and confirm the address-suggestion popup heading and both address-choice buttons appear in Spanish.
2. With the site language set to German, trigger the UPS registration re-register confirmation prompt and confirm it displays in German.
3. With the site language set to Spanish, open the Cleanup settings screen and trigger its confirmation popup; confirm both the settings labels and the confirmation message are in Spanish.

**Scenario D — Shipment messages and general sanity**
1. With the site language set to French, void/cancel a shipment from the order screen and confirm the "contact UPS to void" message and any related confirmation text display fully in French, with no missing words or leftover placeholders.
2. Do a general pass across the settings page, checkout, and existing carriers/boxes in each of the four languages, confirming nothing else nearby looks or behaves broken.

### Expected Behaviour
With the site language set to French, German, Italian, or Spanish, every settings screen, the Help & Support page, the checkout address-suggestion popup, and shipment-related messages (including void/cancel) display fully translated text with no missing words or leftover placeholders, aside from brand names such as "UPS". The "Print Label" and "Print Return Label" buttons always show visible, translated text rather than appearing blank. Order confirmation emails are not part of this fix and continue to follow the site's default language rather than the customer's selected language.
