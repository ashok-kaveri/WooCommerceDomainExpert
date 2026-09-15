# Estimated Delivery Date Plugin For WooCommerce

Version 2.3.2 – Released: August 20th, 2026

## Included Story Cards
| Story Id | Title | Trello Card Link |
|---|---|---|
| 988 | [Bug Fix] Fatal error wiping out Shipping Methods/Zone settings on PHP 8 sites | [988](https://trello.com/c/1scVNPmR/988-bug-fix-fatal-error-wiping-out-shipping-methods-zone-settings-on-php-8-sites) |

## 988 - [Bug Fix] Fatal error wiping out Shipping Methods/Zone settings on PHP 8 sites
### Brief Description
On stores running PHP 8, the Shipping Methods and Shipping Zone settings tabs could break and vanish completely — taking the settings rows and the Add Method, Remove Method(s), and Save changes buttons with them — if any saved row was left over from a much older version of the plugin. The same kind of old saved data could also break the estimated delivery date on the storefront for a shipping class, so no date appeared on the product, cart, or checkout pages. Both screens now handle older saved rows safely and keep working normally, so the settings pages stay usable and the storefront keeps showing delivery dates.

This fix works silently in the background. Merchants who were affected simply get their settings screens and delivery dates back after updating; merchants who were never affected see no change at all.

### Prerequisites
- The store should be on version 2.3.2 or later of the Estimated Delivery Date plugin.
- No setting has to be turned on for the fix itself — it applies automatically after the update.
- To walk through the storefront checks, at least one shipping class should exist with an Estimated Delivery rule saved against it, and a product assigned to that class.

### Step-by-Step Support Walkthrough

**Scenario A — Shipping Methods settings stay intact**
1. In WordPress admin, open `WooCommerce > Estimated Delivery Date settings` and go to the `Shipping Methods` tab.
2. Confirm every existing row is visible, along with the `Add Method`, `Remove Method(s)`, and `Save changes` buttons.
3. Add a new shipping method row, choose some `No Delivery On` days and `Working Days` values, and save.
4. Reload the tab and confirm the selections were kept.
5. Select an existing row with its checkbox, use `Remove Method(s)`, save, and confirm the row is gone.

**Scenario B — Shipping Zone settings stay intact**
1. Still under `WooCommerce > Estimated Delivery Date settings`, open the `Shipping Zone` tab.
2. Confirm every zone row renders with its `No. of Days`, `Cut-Off Time`, and `No Delivery On` fields in place.
3. Change the `No Delivery On` selection for one zone and save.
4. Reload the tab and confirm the change was kept.

**Scenario C — Storefront estimated delivery dates**
1. Set up an Estimated Delivery rule for a shipping class, giving it a `No. of Days` value and a `Cut-Off Time`.
2. On the storefront, open a product that belongs to that shipping class and confirm the estimated delivery date is shown on the product page.
3. Add the product to the cart and confirm the estimated delivery date is shown correctly in the cart and again at checkout.
4. Set up Estimated Delivery rules for two or more different shipping classes, add a product from each to the same cart, and confirm each item shows its own correct delivery date.
5. While browsing the product page, cart, and checkout with those rules active, check `WooCommerce > Status > Logs` and confirm nothing is being logged as a warning or error.

### Expected Behaviour
The Shipping Methods and Shipping Zone tabs load fully with all rows and buttons available, and edits save and persist on reload. On the storefront, every product with an Estimated Delivery rule shows its own correct delivery date on the product page, in the cart, and at checkout, with nothing logged as an error.

The original breakage only happened on stores whose saved settings were left in an outdated format that built up over several past plugin updates. That old format cannot be created through the settings screens on a current version, so the checks above are regression checks: they confirm that everyday use of these screens still works correctly after the fix. If a merchant reports a blank Shipping Methods or Shipping Zone tab, or a missing delivery date for one specific shipping class, updating to this version is the resolution.
