# Product Addon

Version 1.4.0 – Released: August 20th, 2026

## Included Story Cards
| Story Id | Title | Trello Card Link |
|---|---|---|
| 952 | [Bug Fix] Product Addon: Theme-based compatibility fix, price calculation fix, and UI improvement | [952](https://trello.com/c/1dnS6Wya/952-bug-fix-product-addon-theme-based-compatibility-fix-price-calculation-fix-and-ui-improvement) |
| 980 | [Compatibility] Updated compatibility with the booking plugin (Admin Add Booking) | [980](https://trello.com/c/7uf1wUE3/980-compatibility-updated-compatibility-with-the-booking-plugin-admin-add-booking) |
| 957 | [New Feature] Product Addon with Variation Support | [957](https://trello.com/c/VERkirZf/957-new-feature-product-addon-with-variation-support) |

## 952 - [Bug Fix] Product Addon: Theme-based compatibility fix, price calculation fix, and UI improvement
### Brief Description
A group of fixes that make add-on pricing trustworthy and the shop-page buttons correct. An add-on that the merchant has switched off can no longer be priced into the cart from a product page that was already open, conditional add-ons are now only priced when their controlling option is actually selected, add-on text containing an apostrophe now displays cleanly in the cart and on the order, the `Select options` button now renders correctly on block themes, and that button now appears on every product an add-on group really covers.

### Prerequisites
- The store should be on version 1.4.0 or later of the Product Addon plugin.
- Nothing has to be turned on for these fixes — they apply automatically after the update.
- To walk through the scenarios, at least one Add-on Group should exist under `Product Add-ons` with a few add-ons configured, including one Checkbox add-on with a price and one Textbox or Textarea add-on.
- For the conditional checks, one add-on should have Conditional Logic pointing at an option belonging to another add-on, so both `AND` and `OR` can be tried.
- For the booking scenarios, the Booking & Appointment plugin should be active with a booking product that has add-ons.
- To compare button behaviour, have both a block theme (for example Twenty Twenty-Five or Pizzeria) and a classic theme available to switch between.

### Step-by-Step Support Walkthrough

**Scenario A — A switched-off add-on is never priced into the cart**
1. On the storefront, open a product that has an enabled Checkbox add-on with a price, and leave the page open without refreshing.
2. In a second browser or a private window, sign in to WordPress admin, open `Product Add-ons`, and switch that add-on off.
3. Go back to the first, still-open product page, select the add-on as a customer would, and add the product to the cart.
4. Confirm the cart shows neither the add-on's price nor its label, and the total reflects only the add-ons that are still switched on.
5. Repeat with an add-on that has selectable options, leaving one option chosen on the stale page, and confirm the cart total again reflects only the remaining enabled add-ons.

**Scenario B — Conditional add-ons follow their own AND / OR rule**
1. In `Product Add-ons`, set Add-on B's Conditional Logic Type to `AND` and point it at an option belonging to Add-on A.
2. On the storefront, add the product to the cart without selecting Add-on A's referenced option, and confirm Add-on B's price is not charged even though Add-on B itself is switched on.
3. Switch Add-on A off entirely, repeat the add to cart, and confirm Add-on B is still excluded.
4. Change Add-on B's Conditional Logic Type to `OR`, pointing it at options belonging to Add-on A and Add-on C.
5. Select only Add-on C's referenced option and confirm Add-on B's price is charged — with `OR`, one satisfied option is enough.
6. Now satisfy neither referenced option and confirm Add-on B is excluded again.

**Scenario C — Booking products behave the same way**
1. Open a booking product on the storefront that has an enabled add-on with a price, and leave the page open.
2. From a second session, switch that add-on off in `Product Add-ons`.
3. Return to the open booking form, complete the booking, and confirm the add-on's price and label are left out of the booking, exactly as they are for a normal product.

**Scenario D — Apostrophes display correctly**
1. On the storefront, open a product with a Textbox or Textarea add-on.
2. Enter a value containing an apostrophe, such as `don't`, and add the product to the cart.
3. Confirm the cart line shows `don't` exactly as typed, with no stray backslash before the apostrophe.
4. Complete the order, then open it in `WooCommerce > Orders` and confirm the add-on value still reads correctly on the order details page.
5. Repeat the same check on a booking product, since bookings are handled separately.

**Scenario E — The Select options button on block and classic themes**
1. Activate a block theme and open the shop page.
2. Find a product covered by an add-on group and confirm its `Select options` button looks and behaves like the buttons WooCommerce renders itself — compare it side by side with a normal variable product's button on the same shop page.
3. Switch to a classic theme, reload the same shop page, and confirm the button still renders as a normal classic-theme link, unchanged from before.
4. On both themes, open the Suggestion page and confirm a product with a required add-on shows `Select options` and sends the customer to the product page to choose the option, instead of dropping the product straight into the cart.

**Scenario F — The button appears on every product the group really covers**
1. In `Product Add-ons`, open an Add-on Group and leave both `Choose Products` and `Choose Categories` empty.
2. On the shop page, confirm a simple product now shows `Select options` rather than `Add to cart` — an unrestricted group applies to every product, and the add-on fields should be selectable on the product page.
3. Change the group's condition to `Does not apply to` and pick one product, Product X.
4. Confirm Product X shows `Add to cart`, because the group explicitly does not apply to it.
5. Confirm a different product, Product Y, which is not on that list, shows `Select options`, because everything outside the exclusion list is still covered.
6. Finally, check a product that no add-on group references at all and confirm it still shows `Add to cart` as normal.

### Expected Behaviour
Only add-ons that are currently switched on, and whose conditional rule is genuinely satisfied, are priced into the cart — for normal and booking products alike, even when the customer's page was opened before the merchant made the change. Add-on text keeps its apostrophes through the cart, checkout, and order details. The `Select options` button renders natively on both block and classic themes and appears on exactly the products an add-on group covers, including unrestricted groups and the non-excluded products of a `Does not apply to` group. Checking `WooCommerce > Status > Logs` after switching add-ons on and off, saving conditional logic, adding to the cart, and viewing orders should show nothing logged as an error.

## 980 - [Compatibility] Updated compatibility with the booking plugin (Admin Add Booking)
### Brief Description
The admin `Add Booking` screen now treats add-ons the same way the customer-facing product page does. Conditional add-on fields stay hidden until their condition is met instead of always showing and always being priced, and Color Options add-ons now display their colour swatches on this screen instead of appearing as blank space.

### Prerequisites
- The store should be on version 1.4.0 or later of the Product Addon plugin.
- The Booking & Appointment plugin should be active, with a booking product that has add-ons configured.
- One add-on should use Conditional Logic pointing at two other options, so both `AND` and `OR` can be tried.
- One add-on should be a Color Options add-on with specific colours configured, for example Black, Green, and Pink.
- Nothing else needs turning on — the fix applies automatically after the update.

### Step-by-Step Support Walkthrough

**Scenario A — Conditional add-ons follow their rule on the admin booking screen**
1. In WordPress admin, open `Bookings > Add Booking` and choose the booking product that has add-ons.
2. Set the conditional add-on to `AND` logic against two connected options, then select only one of the two.
3. Confirm the conditional add-on field stays hidden and its price is not added to the booking total.
4. Select the second connected option as well, and confirm the field appears and its price is added.
5. Change the conditional add-on to `OR` logic against the same two options and select just one.
6. Confirm the field appears immediately and its price is added.
7. Clear the selection so neither option is chosen, and confirm the field hides again and the price is removed.

**Scenario B — Color Options swatches render**
1. Still on `Bookings > Add Booking`, choose the product with the Color Options add-on.
2. Confirm every configured colour appears as a visible, correctly coloured square, matching what is set for that add-on in `Product Add-ons`.
3. Compare against the same product on the storefront product page and confirm the swatches match.

### Expected Behaviour
On `Bookings > Add Booking`, an `AND` conditional add-on shows and is priced only when every connected option is selected, an `OR` conditional add-on shows and is priced as soon as any one connected option is selected, and both react immediately when the selection changes. Color Options swatches always render as visible, correctly coloured squares. Nothing changes for customers on the storefront. Submitting the `Add Booking` form with the conditional add-ons and Color Options in play should leave nothing logged as an error under `WooCommerce > Status > Logs`.

## 957 - [New Feature] Product Addon with Variation Support
### Brief Description
An Add-on Group's `Choose Products` field now lists individual product variations alongside whole products, so a merchant can target a single variation such as `T-Shirt — L, Blue` from the group's own screen. Previously this had to be set up one product at a time on each Product Edit screen. It works for both `Applies To` and `Does not apply to`, and an explicitly picked variation always takes priority over its parent product.

### Prerequisites
- The store should be on version 1.4.0 or later of the Product Addon plugin.
- At least one variable product with several variations, for example a T-Shirt with size and colour combinations.
- At least one Add-on Group under `Product Add-ons` with add-on fields configured.
- Existing per-variation add-on setups on the Product Edit screen keep working, so no clean-up is needed before demonstrating this.
- For the last scenario, a simple product and a booking product with add-ons, to confirm they are unaffected.

### Step-by-Step Support Walkthrough

**Scenario A — Targeting one variation with Applies To**
1. In WordPress admin, open `Product Add-ons`, edit an Add-on Group, and open `Choose Products` with the condition set to `Applies To`.
2. Confirm individual variations are now listed alongside regular products, and pick one variation, for example `T-Shirt — L, Blue`.
3. Save the group, then open that product on the storefront and select the targeted variation.
4. Confirm the add-on fields appear for that variation, and add it to the cart.
5. Confirm the chosen add-ons and their prices carry through to the cart, checkout, and the finished order.
6. Switch to a sibling variation, for example `T-Shirt — M, Red`, and confirm the targeted add-on does not appear there.

**Scenario B — Parent product versus a specific variation**
1. In the same group, select the parent product only, with no variation picked, and save.
2. On the storefront, confirm the add-on now appears on every variation of that product, as it did before this release.
3. Now select both the parent product and one specific variation, and save.
4. Confirm the add-on applies only to that specific variation — the explicit pick always wins over the parent selection, and sibling variations are unaffected.
5. Clear `Choose Products` and `Choose Categories` completely and save.
6. Confirm the group now applies to every product and every variation, including variable products.

**Scenario C — Excluding with Does not apply to**
1. Set the group's `Choose Products` condition to `Does not apply to` and pick one specific variation.
2. On the storefront, select that variation and confirm the add-on fields do not appear.
3. Select a sibling variation and confirm the add-on fields do appear there normally — excluding one variation must not affect its siblings.
4. Change the exclusion to the parent product only, and confirm the add-on no longer appears on any variation of that product.
5. Select both the parent product and one of its variations in the exclusion list, and confirm the add-on is excluded from every variation of that product.

**Scenario D — What the merchant sees on the Product Edit screen**
1. Open the variable product in `wp-admin > Products`, go to the `Variations` panel, and expand the variation that is explicitly targeted by an `Applies To` group.
2. Confirm the panel shows the message that the variation is globally selected for that group, with a working link back to the Add-on Group, instead of the usual local field selector. Any earlier local selection for that group no longer applies, because the group now covers all of its fields.
3. Expand a variation that is not explicitly targeted, where only the parent is selected, and confirm the familiar local field selector is still there and still works.
4. Expand a variation explicitly excluded by a `Does not apply to` group, and confirm it shows the globally excluded message with a link back to the group.
5. Expand a variation whose parent product is excluded, and confirm a warning about the excluded parent appears above the local field selector, and the selector itself is greyed out and cannot be used.
6. Save the product, reopen it, and confirm variation-level selections were kept.
7. With the group set to apply everywhere, confirm no variation-specific selection area appears at all.

**Scenario E — Nothing else regressed**
1. Add a simple product with add-ons to the cart and confirm the add-ons apply exactly as they did before.
2. Do the same with a booking product that has add-ons.
3. Create or edit an order in `WooCommerce > Orders` containing a simple product and confirm it saves.
4. Load the cart and checkout with the configured add-ons, then check `WooCommerce > Status > Logs` and confirm nothing was logged as an error after saving groups with a mix of products and variations, switching variations on a product page, and completing checkout.

### Expected Behaviour
`Choose Products` lists individual variations next to regular products and accepts them under both `Applies To` and `Does not apply to`. Picking a variation targets or excludes only that variation; picking only the parent covers all of its variations; leaving both `Choose Products` and `Choose Categories` empty still applies the group to every product and every variation. Excluding one variation never affects its siblings. On the Product Edit screen, an explicitly targeted or excluded variation shows the matching message with a link to the group, and a variation under an excluded parent shows a warning with a disabled selector that cannot be worked around. What the customer sees on the product page always matches what is priced at checkout, and simple and booking products behave as they did in the previous version.
