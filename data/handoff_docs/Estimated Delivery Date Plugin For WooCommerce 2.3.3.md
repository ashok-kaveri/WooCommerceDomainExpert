# Estimated Delivery Date Plugin For WooCommerce

Version 2.3.3 – Released: August 27th, 2026

## Included Story Cards
| Story Id | Title | Trello Card Link |
|---|---|---|
| 993 | [Bug Fix] Delivery date not suppressed by add-on on Blocks checkout and order-meta save | [993](https://trello.com/c/XpDEudel/993-bug-fix-delivery-date-not-suppressed-by-add-on-on-blocks-checkout-and-order-meta-save) |

## 993 - [Bug Fix] Delivery date not suppressed by add-on on Blocks checkout and order-meta save
### Brief Description
When the Backorder addon is active and configured to suppress the estimated delivery date, that setting is now respected everywhere. Previously the delivery date could still slip through on the Blocks checkout page and could be stored against the order, so it reappeared afterwards on the thank-you page, the order email, and the customer's My Account order view — even though the merchant had asked for it to be hidden. The delivery wording shown to the customer is also tidier now, with no leftover formatting where the text appears.

This mattered because a merchant hiding the delivery date on backordered items is usually doing so deliberately, to avoid promising a date they cannot meet. A date that leaked through anyway became a customer expectation the store could not honour.

### Prerequisites
- The store should be on version 2.3.3 or later of the Estimated Delivery Date plugin.
- The `Estimated Delivery Date For Backorders` add-on must be active. Check it under `wp-admin > Plugins > Installed Plugins` and activate it if needed.
- The add-on must be switched on and configured to suppress the date. Open `WooCommerce > Settings`, go to the `Backorder Estimated Delivery` tab, enable it, and choose the product or shipping class the suppression should apply to.
- One test product must be added to cart which is configured to suppress the estimated delivery date.
- To compare both checkout styles, be ready to switch the store's Cart and Checkout pages between the Blocks version and the classic (shortcode) version.

### Step-by-Step Support Walkthrough

**Scenario A — The date is hidden on the Blocks checkout**
1. With the Backorder add-on enabled and set to suppress the date for non backordered product, add that product to the cart on the storefront.
2. Open the Cart and Checkout pages while the store is using the Blocks versions.
3. Confirm no estimated delivery text appears for that product — and that the space where it used to sit is genuinely empty, with no stray leftover characters or empty formatting.

**Scenario B — The classic checkout behaves the same way**
1. Switch the store's Cart and Checkout pages back to the classic (shortcode) versions.
2. Repeat the same check on that product.
3. Confirm the suppression behaves identically to the Blocks version — the two checkout styles should always agree.

**Scenario C — The date stays hidden after the order is placed**
1. With suppression still enabled, complete an order containing the non backordered product.
2. On the thank-you page shown straight after payment, confirm no estimated delivery text appears.
3. Open the order confirmation email sent to the customer and confirm the delivery date is not there either.
4. Sign in as that customer, open `My Account > Orders`, view the order, and confirm the delivery date is not shown.
5. In WordPress admin, open the same order on the Edit Order screen and confirm the estimated delivery date field is blank.
6. Go back to the orders list and confirm the estimated delivery column shows no date for that order.

**Scenario D — Nothing changed when suppression is not in use**
1. Turn the Backorder add-on's suppression off, or use a product it does not cover.
2. Place a normal order and confirm the estimated delivery date still appears correctly on the thank-you page, in the order email, and under `My Account > Orders`.
3. With no delivery-date add-on active at all, load the Blocks Cart and Checkout pages and confirm the estimated delivery text reads exactly as it did before this release.

### Expected Behaviour
When the Backorder add-on is configured to suppress the estimated delivery date, that date is hidden consistently — on both the Blocks and classic Cart and Checkout pages, on the thank-you page, in the order email, in the customer's My Account order view, on the admin Edit Order screen, and in the orders list column. Nothing is stored against the order that could bring the date back later.

When suppression is not in play, everything behaves exactly as it did before: the estimated delivery date displays normally on every one of those screens. If a merchant reports that a hidden delivery date is still showing on backordered items, updating to this version is the resolution.
