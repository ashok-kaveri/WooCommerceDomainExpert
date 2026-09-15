# FedEx Shipping Plugin for WooCommerce with Print Label

Version 8.7.2 – Released: Sept 10th, 2026

## Included Story Cards
| Story Id | Title | Trello Card Link |
|---|---|---|
| 1004 | [New Feature] Notify by email when FedEx account connection is lost | [1004](https://trello.com/c/KvLRHffk/1004-new-feature-notify-by-email-when-fedex-account-connection-is-lost) |
| 1008 | [Bug Fix] Clear stale Effective Address session data when address doesn't qualify for validation | [1008](https://trello.com/c/tQz1zo0c/1008-bug-fix-clear-stale-effective-address-session-data-when-address-doesnt-qualify-for-validation) |
| 1002 | [New Feature] Hide Hold at Location for non-FedEx shipping methods on Classic Checkout | [1002](https://trello.com/c/bmwmpr07/1002-new-feature-hide-hold-at-location-for-non-fedex-shipping-methods-on-classic-checkout) |
| 1009 | [New Feature] Refresh Effective Address when shipping address changes on Edit Order | [1009](https://trello.com/c/Iop9f4R1/1009-new-feature-refresh-effective-address-when-shipping-address-changes-on-edit-order) |
| 1000 | [Bug Fix] Prevent product shipping fields from being hidden by WooCommerce Subscriptions | [1000](https://trello.com/c/mpNlUhTw/1000-bug-fix-prevent-product-shipping-fields-from-being-hidden-by-woocommerce-subscriptions) |
| 1001 | [Bug Fix] Fix fatal error from unguarded Package Generator / Storage Handler class instantiation during rate calculation | [1001](https://trello.com/c/H5MXPRFi/1001-bug-fix-fix-fatal-error-from-unguarded-package-generator-storage-handler-class-instantiation-during-rate-calculation) |

## 1004 - [New Feature] Notify by email when FedEx account connection is lost
### Brief Description
If a store's FedEx account stopped being accepted — because its credentials were revoked or expired — the plugin had no way to say so. Rates, labels and tracking simply kept failing, and unless Debug Mode logging happened to be switched on there was nothing to look at. The plugin now spots the problem across every FedEx action, always records it whether or not Debug Mode is on, and emails the store owner as soon as the connection is lost. The email carries a link to reconnect and a way to download the relevant log. Once the connection works again the alert resets, so the merchant is told again if it happens another time.

For support, this turns a silent failure into a named one — and it is the fastest answer to "FedEx rates just stopped appearing".

### Prerequisites
- The store should be on version 8.7.2 or later of the FedEx Shipping plugin.
- `Notify on Connection Lost` must be turned on. Find it under `WooCommerce → Settings → Shipping → FedEx → Advanced` tab, in the `Troubleshooting` section.
- The email's wording can be edited under `WooCommerce → Settings → Emails → FedEx Connection Lost`.
- The site must be able to send email, and you need access to the recipient inbox.
- The store must be registered with FedEx through the current registration method. A store still on the older registration never receives these notifications, so a merchant who reports seeing none may simply be on the legacy setup — check that first.
- To demonstrate a lost connection safely, be ready to temporarily invalidate the FedEx credentials and restore them afterwards.

### Step-by-Step Support Walkthrough

**Scenario A — Turning the notification on**
1. In WordPress admin, open `WooCommerce → Settings → Shipping → FedEx` and go to the `Advanced` tab.
2. In the `Troubleshooting` section, confirm the `Notify on Connection Lost` option is present, turn it on, and save.
3. Open `WooCommerce → Settings → Emails` and confirm a `FedEx Connection Lost` email is listed, and that its content can be edited there.

**Scenario B — The connection loss is detected and recorded**
1. Temporarily replace the FedEx credentials with an invalid value.
2. Trigger a rate request from the storefront by going to checkout with a product in the cart, and confirm the connection loss is recorded in the logs.
3. Repeat across the other FedEx actions and confirm each is recorded too: generating a label, live tracking, requesting a pickup, uploading a document or image, and cancelling a shipment.
4. Turn Debug Mode off and repeat one of the above. Confirm the connection loss is still recorded — this no longer depends on Debug Mode being on.
5. Turn Debug Mode on and confirm it is recorded there as well.

**Scenario C — The notification email**
1. With the setting on and the connection broken, check the recipient inbox for the `FedEx Connection Lost` email.
2. Confirm exactly one email arrives for the first failure, and that a second consecutive failure does not send a duplicate.
3. Click the reconnect link in the email and confirm it opens the right place to reconnect the account.
4. Click the download log link and confirm the log downloads. It is restricted to signed-in users with permission to manage WooCommerce, so confirm it is not accessible otherwise.

**Scenario D — The alert resets after a recovery**
1. Restore the correct FedEx credentials and make a successful request, such as fetching rates at checkout.
2. Break the connection again and confirm a fresh notification email is sent. A single ongoing outage only ever produces one email, but a new outage after a recovery produces a new one.

**Scenario E — Turning it off**
1. Turn `Notify on Connection Lost` off and save.
2. Break the connection again and confirm no email is sent.

### Expected Behaviour
A FedEx connection that stops being accepted is detected across rate requests, label generation, tracking, pickups, document uploads and shipment cancellations, and is always recorded in the logs whether or not Debug Mode is on. The store owner receives exactly one `FedEx Connection Lost` email per outage, with a working reconnect link and a permission-protected log download. A successful request resets the alert so the next outage notifies again, turning the setting off stops the emails, and stores on the older FedEx registration are not notified at all.

## 1008 - [Bug Fix] Clear stale Effective Address session data when address doesn't qualify for validation
### Brief Description
Once FedEx had validated an address and stored a suggested correction, switching to an address that does not qualify for validation — an unsupported country, or one missing its address line or country — left that earlier suggestion in place. It could then be wrongly applied to the new address. The suggestion is now cleared whenever validation does not apply to the address in front of it.

This card covers the checkout side only. Story 1009 covers the same Effective Address on the admin Edit Order screen — they are separate fixes on separate screens, so read them together when a merchant reports a wrong address on an order.

### Prerequisites
- The store should be on version 8.7.2 or later of the FedEx Shipping plugin.
- Nothing needs turning on — the fix applies automatically after the update.
- FedEx address validation should be in use, with the Effective Address setting enabled.
- You will need one shipping address in a country FedEx supports for address validation that produces a suggested correction, and one in a country it does not support.
- Do the checks in one continuous browsing session without clearing cookies, since the point of the fix is that nothing carries over between orders in the same session.

### Step-by-Step Support Walkthrough

**Scenario A — A suggestion is stored as normal**
1. On the storefront, check out with a shipping address in a supported country that FedEx will suggest a correction for.
2. Confirm the suggested address is stored against the order and behaves as expected.

**Scenario B — An unsupported country does not inherit it**
1. Straight afterwards, in the same browsing session, go to checkout again and place another order using a shipping address in a country that is not supported for address validation.
2. Confirm the earlier suggested address is cleared and is not carried onto this order.
3. Confirm no address validation note is added to this order, since validation never applied to it.

**Scenario C — An incomplete address does not inherit it either**
1. Again in the same session, check out with a shipping address that is missing its address line or its country, so validation cannot run.
2. Confirm any previously stored suggestion is cleared rather than left in place.
3. A common way to reach this in real use is a customer who completes a valid address, then ticks `ship to a different address` and enters an unsupported or incomplete one.

### Expected Behaviour
A stored address suggestion only ever applies to the address it was produced for. As soon as the shipping address changes to one that does not qualify for validation — an unsupported country or a missing address line or country — the stored suggestion is cleared, so it can never be applied to the wrong address. Orders that do not qualify for validation get no address validation note.

## 1002 - [New Feature] Hide Hold at Location for non-FedEx shipping methods on Classic Checkout
### Brief Description
The Hold at Location field appeared on Classic Checkout no matter which shipping method the customer picked, including couriers other than FedEx — even though Hold at Location only applies to FedEx shipments. A new setting keeps the field to FedEx methods only, so it hides as soon as a non-FedEx method is selected and reappears when a FedEx one is chosen.

The setting is off by default, so a store that updates without changing anything keeps the previous behaviour of showing the field for every method.

### Prerequisites
- The store should be on version 8.7.2 or later of the FedEx Shipping plugin.
- `Hold at Location` itself must be enabled in the FedEx shipping settings. The new option is one of its sub-settings and only appears once Hold at Location is ticked — unticking it hides the new option again, with no page reload needed.
- The new option is `Show Hold at Location only for FedEx methods`.
- The store must be using Classic Checkout — this covers that checkout style.
- To cover both layouts you will want a shipping zone where only one method is offered, and another where several are offered as selectable options, including at least one non-FedEx method and ideally two FedEx ones.

### Step-by-Step Support Walkthrough

**Scenario A — The setting appears in the right place**
1. Open the FedEx shipping settings and untick `Hold at Location`.
2. Confirm `Show only for FedEx methods` is not shown.
3. Tick `Hold at Location` and confirm the new option appears straight away, without reloading the page.
4. Turn `Show Hold at Location only for FedEx methods` on and save.

**Scenario B — A checkout offering several methods**
1. Go to Classic Checkout in a zone that offers several shipping methods.
2. Select a FedEx method and confirm the Hold at Location field appears.
3. Switch to a non-FedEx method and confirm the field disappears immediately, without the page reloading.
4. With two FedEx methods offered alongside a non-FedEx one, switch between the two FedEx options and confirm the field stays visible throughout, hiding only when the non-FedEx method is chosen.

**Scenario C — A checkout offering only one method**
1. Go to Classic Checkout in a zone that offers a single FedEx method and confirm the field appears.
2. Switch to a zone whose only method is non-FedEx, and load the checkout page fresh without touching anything.
3. Confirm the Hold at Location field is hidden from the moment the page loads, rather than only hiding after the customer interacts with something.

**Scenario D — Turning the setting off**
1. Turn `Show Hold at Location only for FedEx methods` off and save.
2. Go back to Classic Checkout and confirm the Hold at Location field is shown for every method again, FedEx or not — the behaviour a store had before this release.
3. On a store that has just updated and never touched the new option, confirm the same thing: the field shows for all methods until a merchant deliberately turns the option on.

### Expected Behaviour
With the option on, Hold at Location appears only while a FedEx shipping method is selected, on both single-method and multi-method Classic Checkout layouts, updating as the customer switches without a page reload, and hidden correctly from the first page load. Switching between two FedEx methods keeps it visible. With the option off — including on any store that simply updates — the field shows for every method exactly as before. The option itself only appears while Hold at Location is enabled.

## 1009 - [New Feature] Refresh Effective Address when shipping address changes on Edit Order
### Brief Description
Address validation only ever ran at checkout, so when an admin edited an order's shipping address the Effective Address stayed as it was — still showing a suggestion for the old address. Saving a changed shipping address on the Edit Order screen now re-runs validation automatically. A new suggestion is saved to the order with a note recording the effective address used for the shipment, and if validation produces nothing usable the old suggestion is cleared rather than left behind.

Validation only runs when the shipping address actually changed, so saving an order for any other reason leaves the existing address alone.

### Prerequisites
- The store should be on version 8.7.2 or later of the FedEx Shipping plugin.
- The `Effective Address` setting must be enabled in the FedEx settings. With it off, nothing re-validates and no note is added.
- The store must be registered with FedEx through the current registration method. This does not apply to stores on the older registration.
- You will need one address FedEx will suggest a correction for and one it will not.
- The behaviour is the same whether the store uses High-Performance Order Storage or the older order storage, so cover both if you can.

### Step-by-Step Support Walkthrough

**Scenario A — Changing the address re-runs validation**
1. In WordPress admin, open an order on the Edit Order screen.
2. Change the shipping address to a different one that FedEx will suggest a correction for, and save.
3. Confirm the order's effective address updates to reflect the newly validated address.
4. Confirm an order note is added stating the effective address used for the shipment.

**Scenario B — A new address with no suggestion clears the old one**
1. On the same order, change the shipping address again to one FedEx will not flag or correct, and save.
2. Confirm the previously suggested address is cleared rather than left in place.
3. Try the same where validation cannot return anything at all, and confirm the order still saves normally and is not left carrying a stale address.

**Scenario C — Saving without an address change leaves things alone**
1. Open the Edit Order screen and save the order without touching the shipping address — change only the order status or a billing field.
2. Confirm the existing effective address is untouched and no new validation note is added.
3. Confirm the same when only the customer's name, email or phone number is changed.
4. Change a shipping field, change it back to its original value, and save. Confirm this does not trigger a pointless re-validation.

**Scenario D — Which changes count**
1. Confirm validation runs when just one shipping field changes on its own — the country, the postcode, the city, or the state.
2. Edit the same order's shipping address several times in a row and confirm each validation uses the latest saved address, with the note reflecting the most recent one.
3. Confirm an address typed but not saved does not change the effective address.
4. Try an address containing special characters or apartment and unit details, and one missing its optional fields, and confirm both behave correctly.

**Scenario E — With the setting off**
1. Turn the `Effective Address` setting off.
2. Change and save a shipping address on the Edit Order screen.
3. Confirm no re-validation happens and no order note is added.

### Expected Behaviour
Saving a changed shipping address on the Edit Order screen re-runs address validation automatically, saving any new suggestion to the order along with a note naming the effective address used. When validation returns nothing usable or does not apply, the old suggestion is cleared rather than left stale, and the order always saves successfully even if validation fails. Saving without changing the shipping address changes nothing and adds no note. The behaviour is identical on both order storage types, and nothing happens at all when the Effective Address setting is off or the store is on the older FedEx registration.

## 1000 - [Bug Fix] Prevent product shipping fields from being hidden by WooCommerce Subscriptions
### Brief Description
On a product's Shipping tab, the FedEx Shipping Details fields could vanish when WooCommerce Subscriptions was active on an older WooCommerce version. Both plugins added their fields to the same place at the same time, and depending on which loaded first, the FedEx fields could end up trapped inside a container belonging to Subscriptions and never appear. Those fields now always render before that container opens, so the problem cannot happen whatever the load order or WooCommerce version.

The merchant-facing symptom was that per-product FedEx weight and dimension overrides simply could not be reached or edited, so this is the first thing to check on any site running both plugins.

### Prerequisites
- The store should be on version 8.7.2 or later of the FedEx Shipping plugin.
- Nothing needs turning on — the fix applies automatically after the update.
- WooCommerce Subscriptions should be active to reproduce the original conditions, and you should be able to deactivate it again for the regression check.
- Have a simple product, a variable product, and a subscription product available to open.
- One third-party plugin, `Constellation by Kestrel`, bundles its own copy of the Subscriptions admin code and triggered the same problem, so include it if the store in question uses it.

### Step-by-Step Support Walkthrough

**Scenario A — Fields are visible with Subscriptions active**
1. Confirm WooCommerce Subscriptions is active under `wp-admin → Plugins → Installed Plugins`.
2. Open a simple product in `wp-admin → Products`, go to the `Shipping` tab, and confirm the FedEx Shipping Details section is fully visible.
3. Repeat on a variable product.
4. Repeat on a subscription product, if Subscriptions adds one as its own product type.
5. Confirm Subscriptions' own fields on the same Shipping tab still render properly and were not blanked or broken.

**Scenario B — Sites without Subscriptions are unaffected**
1. Deactivate WooCommerce Subscriptions.
2. Open a product's `Shipping` tab again and confirm the FedEx Shipping Details section still renders correctly.

**Scenario C — Saved values are intact**
1. Set the FedEx per-item weight and dimension overrides on a product, save, then reload the edit screen and confirm the values were kept.
2. Do the same on a site that already had FedEx product-level values saved before this update, and confirm those existing values still load and save correctly.

**Scenario D — The third-party plugin case**
1. With `Constellation by Kestrel` active alongside the FedEx plugin, open a simple product's `Shipping` tab and confirm the FedEx Shipping Details section is fully visible and not cut off.
2. Repeat on a variable product.
3. Confirm Constellation's own `One time shipping` option still renders correctly on the same tab.

### Expected Behaviour
The FedEx Shipping Details section appears on every product's `Shipping` tab — simple, variable and subscription products alike — whether or not WooCommerce Subscriptions is active, on any WooCommerce version, and alongside third-party plugins that bundle the same Subscriptions admin code. Per-item weight and dimension overrides save and reload correctly, existing saved values are untouched, and the other plugins' own fields on that tab continue to render normally.

## 1001 - [Bug Fix] Fix fatal error from unguarded Package Generator / Storage Handler class instantiation during rate calculation
### Brief Description
One store hit a repeating fatal error every time shipping rates were worked out at checkout, many times a minute in production. Certain parts of the plugin are only prepared during WordPress's normal start-up, but some third-party integrations ask WooCommerce to calculate shipping earlier than that — before those parts are ready. The plugin now checks and prepares what it needs on the spot instead of failing, closing the gap for both the shipment packaging step and the recipient address lookup.

The combination to watch for on a support call is a store running WPML multi-currency or WooCommerce PayPal Payments and reporting a fatal error, or a blank page, at cart or checkout. Updating to this release is the resolution.

### Prerequisites
- The store should be on version 8.7.2 or later of the FedEx Shipping plugin.
- Nothing needs turning on — the fix applies automatically after the update.
- To reproduce the original conditions you need one of the integrations that triggers early rate calculation: WPML with multi-currency enabled, or WooCommerce PayPal Payments.
- FedEx should be registered and returning rates on the site.

### Step-by-Step Support Walkthrough

**Scenario A — WPML multi-currency**
1. With WPML multi-currency enabled, add a product to the cart and load the checkout page so the currency recalculation runs.
2. Confirm the page loads and shipping rates are returned, with no fatal error and no blank page.

**Scenario B — WooCommerce PayPal Payments**
1. With WooCommerce PayPal Payments active, load the cart and then the checkout page.
2. Confirm rate calculation completes normally with no fatal error.

**Scenario C — Nothing else regressed**
1. On a site with neither of those integrations triggering early calculation, run a normal checkout and confirm rates still display correctly.
2. Generate a shipping label for an order as usual and confirm label generation is unaffected.

### Expected Behaviour
Shipping rates calculate successfully at cart and checkout even when a third-party integration asks for them earlier than usual, with no fatal error and no blank page. Stores without those integrations see rates exactly as before, and label generation is unchanged. A merchant reporting a repeating fatal error at checkout alongside WPML multi-currency or WooCommerce PayPal Payments should be moved to this version.
