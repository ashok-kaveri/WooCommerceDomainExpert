# Multi-Carrier Shipping Plugin for WooCommerce — Business Brief

Version 3.4.2 – Released: Aug 18th, 2026

## Release Overview
This release improves FedEx packaging support, prevents incorrect shipping quotes when product data is incomplete, and makes carrier registration more reliable for merchants and support teams. It also adds a faster reset option for default carrier boxes and removes a FedEx rate blocker for addresses that use longer regional codes.

## Included Updates
| Story Id | Title | Trello Card Link |
|---|---|---|
| 969 | [New Feature] Add FedEx Extra Small Box option | [969](https://trello.com/c/GID9FlZq/969-new-feature-add-fedex-extra-small-box-option) |
| 967 | [Bug Fix] Abort rate calculation entirely when a product is missing weight or dimensions | [967](https://trello.com/c/lds9zfwS/967-bug-fix-abort-rate-calculation-entirely-when-a-product-is-missing-weight-or-dimensions) |
| 972 | [Improvement] Move carrier registration credentials into a dedicated, more secure storage option | [972](https://trello.com/c/4wINAARi/972-improvement-move-carrier-registration-credentials-into-a-dedicated-more-secure-storage-option) |
| 979 | [New Feature] Added "Reset Box(es)" action to restore default carrier boxes | [979](https://trello.com/c/r6doUdJX/979-new-feature-added-reset-boxes-action-to-restore-default-carrier-boxes) |
| 987 | [Bug Fix] Fix FedEx rate errors for addresses with state/province codes longer than 2 characters | [987](https://trello.com/c/KPQ6k9Lc/987-bug-fix-fix-fedex-rate-errors-for-addresses-with-state-province-codes-longer-than-2-characters) |

## 969 - FedEx Extra Small Box option
*Merchants get a new built-in packaging choice for smaller FedEx shipments.*

### Brief Description
This update adds an Extra Small FedEx box option to the standard box list. It gives merchants a better fit for smaller shipments and keeps the setup simple by leaving the new box off until the merchant chooses to use it.

### What's New
- A new Extra Small FedEx box appears in the standard box list.
- The box is placed in the expected order with the other FedEx packaging options.
- The box stays off by default so merchants can choose when to use it.
- Qualifying domestic shipments can use it in the FedEx One Rate flow.

### Who Benefits
- Merchants shipping smaller parcels through FedEx.
- Support teams helping merchants fine-tune packaging choices.
- Stores that want more accurate box selection without adding custom boxes by hand.

### Availability
Available after updating to Version 3.4.2 and enabling the box in the merchant's shipping settings when needed.

## 967 - Stop rates when product shipping details are incomplete
*Checkout now avoids showing a misleading shipping price when cart data is incomplete.*

### Brief Description
This fix prevents partial shipping quotes from appearing when any product in the cart is missing the required weight or size details. Instead of showing a rate that ignores one of the products, the plugin waits until the missing information is corrected.

### What's New
- Rate calculation stops fully when required product shipping details are missing.
- The behavior is consistent across the supported packing approaches.
- Mixed carts no longer show a rate that only reflects part of the order.
- Valid product data continues to produce normal rates once corrected.

### Who Benefits
- Merchants who want more trustworthy checkout pricing.
- Support teams troubleshooting missing product setup.
- Customers who would otherwise see a rate that looks correct but is incomplete.

### Availability
Available immediately in Version 3.4.2 with no extra setup.

## 972 - More reliable carrier registration handling
*Carrier connections are less likely to be lost during routine settings changes.*

### Brief Description
This improvement separates carrier registration handling from general shipping settings so merchants are less likely to lose a newly connected carrier by saving an older browser tab later. Existing registrations continue working after update, which reduces support effort during rollout.

### What's New
- Carrier registrations remain protected when older settings tabs are saved later.
- Existing connected carriers continue working after update.
- The general settings area is cleaner and more focused on shipping setup.
- Merchants do not need to re-enter carrier details just because the release is installed.

### Who Benefits
- Merchants managing multiple carrier accounts.
- Support teams helping with onboarding or reconnection issues.
- Stores where multiple admins work in settings at the same time.

### Availability
Available automatically in Version 3.4.2 for existing and new carrier registrations.

## 979 - Reset Box(es) action for default carrier boxes
*Support and merchants can restore the built-in FedEx and USPS box list much faster.*

### Brief Description
This feature adds a one-click recovery option for merchants who removed or heavily changed the default carrier boxes. It reduces setup friction by restoring the standard box list in the store's active units after a confirmation prompt.

### What's New
- A new `Reset Box(es)` action is available in box packing settings.
- Default FedEx and USPS boxes can be restored without manual re-entry.
- The reset respects the store's active measurement units.
- A confirmation step helps prevent accidental resets.

### Who Benefits
- Merchants who need to recover from box setup mistakes.
- Support teams handling packaging resets during onboarding or troubleshooting.
- Stores that want a quick path back to the recommended default box list.

### Availability
Available in Version 3.4.2 from the box packing settings screen.

## 987 - Better FedEx rate support for longer regional codes
*FedEx checkout rates now work for more international address formats.*

### Brief Description
This fix improves FedEx rate availability for addresses that use longer state or province codes. It helps merchants serve more international shipping destinations without checkout rate failures caused by regional code formatting.

### What's New
- FedEx rates now return for addresses that use longer state or province codes.
- The improvement helps international addresses that do not follow the common two-letter pattern.
- Standard two-letter state and province codes continue to work normally.
- Merchants can complete checkout rate lookup more reliably across supported address formats.

### Who Benefits
- Merchants shipping with FedEx to international destinations.
- Support teams handling checkout rate complaints from region-specific address formats.
- Customers whose addresses previously failed to return a FedEx shipping option.

### Availability
Available immediately in Version 3.4.2 for FedEx-enabled stores.
