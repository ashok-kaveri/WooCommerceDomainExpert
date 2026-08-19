# Multi-Carrier Shipping Plugin for WooCommerce

Version 3.4.2 – Released: Aug 18th, 2026

## Included Story Cards
| Story Id | Title | Trello Card Link |
|---|---|---|
| 969 | [New Feature] Add FedEx Extra Small Box option | [969](https://trello.com/c/GID9FlZq/969-new-feature-add-fedex-extra-small-box-option) |
| 967 | [Bug Fix] Abort rate calculation entirely when a product is missing weight or dimensions | [967](https://trello.com/c/lds9zfwS/967-bug-fix-abort-rate-calculation-entirely-when-a-product-is-missing-weight-or-dimensions) |
| 972 | [Improvement] Move carrier registration credentials into a dedicated, more secure storage option | [972](https://trello.com/c/4wINAARi/972-improvement-move-carrier-registration-credentials-into-a-dedicated-more-secure-storage-option) |
| 979 | [New Feature] Added "Reset Box(es)" action to restore default carrier boxes | [979](https://trello.com/c/r6doUdJX/979-new-feature-added-reset-boxes-action-to-restore-default-carrier-boxes) |
| 987 | [Bug Fix] Fix FedEx rate errors for addresses with state/province codes longer than 2 characters | [987](https://trello.com/c/KPQ6k9Lc/987-bug-fix-fix-fedex-rate-errors-for-addresses-with-state-province-codes-longer-than-2-characters) |

## 969 - [New Feature] Add FedEx Extra Small Box option
### Brief Description
Support can now offer an Extra Small FedEx box option in the built-in box list. It appears in the right place in the list, stays off by default, and can be used for qualifying FedEx One Rate shipments when the merchant chooses to turn it on.

### Prerequisites
- FedEx should already be registered on the site.
- The merchant should be using box packing in the shipping setup.
- To demonstrate the One Rate behavior, use a domestic FedEx shipment that fits the Extra Small box and has One Rate enabled in the merchant's FedEx setup.

### Step-by-Step Support Walkthrough
1. In WordPress admin, open `WooCommerce > Settings > Shipping` and edit the shipping setup for this plugin.
2. Open the box packing area and review the FedEx box list.
3. Confirm the Extra Small box is available and appears before the Small box.
4. Confirm it is off by default on a fresh setup or after an update.
5. Turn it on, save the settings, and place a FedEx test order that fits the Extra Small box.
6. If the merchant uses One Rate, verify the same box can be used in that pricing flow when the shipment qualifies.

### Expected Behaviour
The Extra Small box is available for FedEx box packing, stays off until the merchant enables it, and works with qualifying FedEx pricing once enabled.

## 967 - [Bug Fix] Abort rate calculation entirely when a product is missing weight or dimensions
### Brief Description
The plugin now stops the full rate request when any cart item is missing required shipping details. This prevents customers from seeing a partial shipping rate that looks valid but ignores one of the products in the cart.

### Prerequisites
- Use a shipping setup that is set to one of the supported packing approaches.
- Create a test product with missing weight, or missing size details when testing box packing.
- Add that product to the cart before checking rates.

### Step-by-Step Support Walkthrough
1. In WordPress admin, open the shipping setup and note which packing approach is active.
2. Add a product to the cart that is missing the required shipping details for that setup.
3. Go to cart or checkout and trigger shipping rate calculation.
4. Confirm no shipping rate is shown while the product data is incomplete.
5. Update the product so the missing shipping details are filled in.
6. Run the same checkout flow again and confirm the rate now appears normally.

### Expected Behaviour
If any product is missing the required shipping details, no shipping rate is shown. Once the product data is corrected, rate calculation resumes normally.

## 972 - [Improvement] Move carrier registration credentials into a dedicated, more secure storage option
### Brief Description
Carrier registrations are now protected from being lost when an older settings tab is saved later. Existing carrier connections continue to work, and support can reassure merchants that they do not need to re-register just because this release was installed.

### Prerequisites
- Use a site with at least one registered carrier account such as FedEx, UPS, or USPS.
- Have access to both the carrier registration screens and the main shipping settings screen.
- For a full demonstration, keep one older settings tab open while completing a new carrier registration in another tab.

### Step-by-Step Support Walkthrough
1. In WordPress admin, confirm the carrier account is already connected and returning rates.
2. Open the main shipping settings screen in one browser tab and leave it open.
3. In a second tab, register or reconnect a carrier account through the normal carrier registration flow.
4. Return to the first, older tab and save the general settings without refreshing it.
5. Go back to the carrier registration area and confirm the newly connected carrier is still shown as connected.
6. Place a test order and confirm rates still return normally after that save.
7. Review the main settings screen and confirm the old registration input fields are no longer mixed into the general settings area.

### Expected Behaviour
Carrier registrations remain connected after a stale settings save, existing connections continue working after update, and the main settings area stays focused on day-to-day shipping configuration.

## 979 - [New Feature] Added "Reset Box(es)" action to restore default carrier boxes
### Brief Description
Support now has a faster recovery path when a merchant has removed or heavily changed the default FedEx or USPS box list. The new reset action restores the built-in boxes for the store's measurement units and asks for confirmation before making the change.

### Prerequisites
- The merchant should be using FedEx or USPS box packing.
- The box list should already be visible in the shipping settings.
- This is easiest to demonstrate on a site where some default boxes were removed or edited.

### Step-by-Step Support Walkthrough
1. In WordPress admin, open `WooCommerce > Settings > Shipping` and edit the shipping setup.
2. Go to the box packing section and review the current FedEx or USPS box list.
3. Click `Reset Box(es)` and confirm the confirmation prompt appears before the reset runs.
4. Complete the reset and review the refreshed box list.
5. Confirm the built-in carrier boxes are restored in the store's current measurement units.
6. Confirm the FedEx Extra Small box is present in the reset list and remains off by default.
7. If custom boxes are present, select and unselect them to confirm the header checkbox only reflects actual selections.

### Expected Behaviour
The reset action restores the default carrier boxes safely, uses the store's active units, and does not make changes until the merchant confirms the action.

## 987 - [Bug Fix] Fix FedEx rate errors for addresses with state/province codes longer than 2 characters
### Brief Description
FedEx rates now return correctly for countries and regions that use longer state or province codes. This helps merchants serve addresses such as Australian regions or other markets where the regional code is longer than the two-letter format FedEx expects.

### Prerequisites
- FedEx should already be registered and returning rates on the site.
- Use a checkout address with a state or province code longer than two characters, such as an Australian or similar international address.
- Keep a normal two-letter state code example ready as a comparison check.

### Step-by-Step Support Walkthrough
1. Add a FedEx-eligible product to the cart and go to checkout.
2. Enter a shipping address that uses a longer state or province code.
3. Trigger shipping rate calculation and confirm FedEx rates are returned.
4. Repeat the same flow with a normal two-letter state code and confirm rates still return there as well.
5. If the merchant also uses label creation after checkout, complete a test order and verify the FedEx shipment flow still proceeds normally for the longer-code address.

### Expected Behaviour
FedEx rates should be returned for longer regional codes without blocking checkout, while normal two-letter state and province codes continue to work as before.
