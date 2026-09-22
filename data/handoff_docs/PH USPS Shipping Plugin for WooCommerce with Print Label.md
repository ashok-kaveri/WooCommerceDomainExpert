# PH USPS Shipping Plugin for WooCommerce with Print Label

Version 1.0.6 – Released: Sept 17th, 2026

## Included Story Cards
| Story Id | Title | Trello Card Link |
|---|---|---|
| 1014 | [Bug Fix] Correctly treat US territories and Freely Associated States as domestic shipments | [1014](https://trello.com/c/ev3Ft1j2/1014-bug-fix-correctly-treat-us-territories-and-freely-associated-states-as-domestic-shipments) |

## 1014 - [Bug Fix] Correctly treat US territories and Freely Associated States as domestic shipments
### Brief Description
Orders shipping to Puerto Rico, the US Virgin Islands, Guam, American Samoa, the Northern Mariana Islands, or one of the Freely Associated States (Micronesia, the Marshall Islands, Palau) were being treated as international shipments, even though USPS prices and handles them as domestic. This caused rate fetching to fail, and shipment label creation, cancellation, and return shipments to fail or not proceed for these destinations. It also meant destinations that legally require a customs form were not getting one, and the label's state field could end up with unusable text since WooCommerce has no state list for these destinations.

These nine destinations are now correctly recognized as domestic for rates, shipment creation, cancellation, and returns, matching how USPS actually classifies and prices them: the United States, Puerto Rico, the US Virgin Islands, Guam, American Samoa, the Northern Mariana Islands, Micronesia, the Marshall Islands, and Palau. A subset of these still needs a customs form even though the postage is priced as domestic, and the label now always carries a valid two-letter code in the state field for these destinations.

### Prerequisites
- The store should be on version 1.0.6 or later of the USPS Shipping plugin.
- Nothing needs turning on — the fix applies automatically after the update.
- You will need test orders shipping to Puerto Rico, the US Virgin Islands, Guam, American Samoa, the Northern Mariana Islands, Micronesia, the Marshall Islands, and Palau, plus a genuine international destination (e.g. Canada or the UK) and a regular US state (e.g. California or New York) for regression checks.
- Because WooCommerce has no state dropdown for these destinations, one of the checks needs an order where the customer typed free text into the state field at checkout.

### Step-by-Step Support Walkthrough

**Scenario A — Rate fetching shows domestic pricing**
1. On the storefront, add a product to the cart and set the shipping address to Puerto Rico (for example, San Juan, 00926).
2. At checkout, confirm the USPS rates shown are domestic rates, not international.
3. Repeat for the US Virgin Islands, Guam, American Samoa, the Northern Mariana Islands, Micronesia, the Marshall Islands, and Palau, confirming domestic rates each time.

**Scenario B — Shipment creation and labels use the domestic flow**
1. Place a test order shipping to Puerto Rico, then open the order and create a USPS shipment/label for it.
2. Confirm the domestic label flow is used and no country or customs fields are asked for.
3. Repeat shipment creation for one of the other destinations listed above and confirm the label generates correctly with domestic ZIP code handling.

**Scenario C — Cancellation and returns**
1. Cancel a previously created shipment for a Puerto Rico order and confirm the cancellation completes without errors.
2. Create a return shipment for an order shipping to another destination from the list above and confirm it processes without errors.

**Scenario D — Genuine international shipments and regular US states are unaffected**
1. Place a test order shipping to a genuinely international destination, such as Canada or the UK, and confirm rates, shipment creation, cancellation, and returns still use the international flow exactly as before.
2. Place a test order shipping to a regular US state, such as California or New York, and confirm domestic behavior is unchanged.

**Scenario E — Customs form appears only where it should**
1. Create a USPS shipment for an order shipping to the United States, Puerto Rico, or the US Virgin Islands. Confirm no customs declaration/customs form is generated — these are fully domestic for customs purposes.
2. Create a USPS shipment for an order shipping to Guam, American Samoa, or the Northern Mariana Islands. Confirm a customs declaration/customs form is generated, even though the rate shown is domestic.
3. Create a USPS shipment for an order shipping to Micronesia, the Marshall Islands, or Palau. Confirm a customs declaration/customs form is generated here as well, for the same reason.

**Scenario F — The label's state field is always valid for territories and Freely Associated States**
1. Create a USPS shipment/label for an order shipping to one of Guam, American Samoa, the Northern Mariana Islands, Micronesia, the Marshall Islands, or Palau, where the customer typed free text into the state field at checkout.
2. Confirm the label sent to USPS uses the correct two-letter territory/country code (GU, AS, MP, FM, MH, or PW) as the state, not the free text the customer entered.
3. Confirm a normal US order with a real US state selected is unaffected and still sends the correct US state code.

### Expected Behaviour
Puerto Rico, the US Virgin Islands, Guam, American Samoa, the Northern Mariana Islands, Micronesia, the Marshall Islands, and Palau all now quote, ship, cancel, and return as domestic USPS shipments. The United States, Puerto Rico, and the US Virgin Islands generate no customs form, while Guam, American Samoa, the Northern Mariana Islands, Micronesia, the Marshall Islands, and Palau generate one even though they are priced as domestic. The shipping label always carries a valid two-letter code in the state field for these destinations regardless of what the customer typed at checkout. Genuinely international destinations and regular US states behave exactly as they did before this release.
