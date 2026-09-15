# PH Deposits for WooCommerce

Version 2.0.0 – Released: Sept 9th, 2026

## Included Story Cards
| Story Id | Title | Trello Card Link |
|---|---|---|
| 974 | [New Feature] Add Category-Based Deposit Rules | [974](https://trello.com/c/kyOb6gM0/974-new-feature-add-category-based-deposit-rules) |
| 983 | [Bug Fix] Fixed custom page deposit calculation issue | [983](https://trello.com/c/xteZWpcF/983-bug-fix-fixed-custom-page-deposit-calculation-issue) |
| 956 | [New Feature] Add Balance Payment Order Creation Days for Fixed/Percentage Deposits | [956](https://trello.com/c/2aw8uIWE/956-new-feature-add-balance-payment-order-creation-days-for-fixed-percentage-deposits) |
| 966 | [New Feature] Advanced Dashboard for Deposits – Revenue Overview, Order Balance Tracking & Payment Reminders | [966](https://trello.com/c/ad67o0AW/966-new-feature-advanced-dashboard-for-deposits-revenue-overview-order-balance-tracking-payment-reminders) |
| 975 | [New Feature] Add User Role Deposit Rules | [975](https://trello.com/c/vZFmmKNw/975-new-feature-add-user-role-deposit-rules) |

## 974 - [New Feature] Add Category-Based Deposit Rules
### Brief Description
Deposits could previously only be set storewide or product by product, so a large catalogue meant editing every product individually to move away from the storewide default. A new `Deposit Rules` tab lets a merchant apply a deposit to one or more whole product categories at once.

This card and story 975 are two halves of the same tab. A single rule can carry a Category condition, a User Role condition, or both — read the two sections together, because a support call about either will land on the same screen.

### Prerequisites
- The store should be on version 2.0.0 or later of PH Deposits for WooCommerce.
- The tab is at `WooCommerce Deposits → Deposit Rules`, with a rules list and an Add or Edit screen.
- Both the `Category` and `User Role` toggles start off on a new rule, and a rule with neither turned on cannot be saved — the form shows an inline message instead.
- For a clean demonstration, pick categories whose products have no deposit set on the product itself, since a product-level setting always wins.
- Deleting a rule is permanent — there is no undo, so a rule removed by mistake has to be recreated by hand.
- This unified tab is the premium plugin only. The marketplace plugin, PH Deposits and Partial Payments, still has the older design with separate `Category Deposit` and `User Role Deposit` tabs, so a merchant on that plugin will not see what is described here.

### Step-by-Step Support Walkthrough

**Scenario A — A category rule sets the deposit**
1. In WordPress admin, open `WooCommerce Deposits → Deposit Rules` and click `Add New Rule`.
2. Confirm the form shows a `Category` toggle and a `User Role` toggle, both off, plus a `Priority` field and the same deposit fields found on a product's own Deposits tab.
3. Turn the `Category` toggle on and multi-select one or two categories. A rule matches a product that is in any of the selected categories.
4. Set `Deposit Type` to Percentage with an amount of 30, then click `Save Rule`.
5. Confirm you return to the rule with a success message and the categories you picked still selected.
6. View a product from one of those categories on the storefront and confirm the deposit shown is 30% of the price, not the storewide default.

**Scenario B — A product's own setting always wins**
1. Open the edit screen for a product in that category, go to its `Deposits` tab, set a fixed amount deposit such as 50, and save.
2. View the product on the storefront again and confirm it now shows the 50 fixed deposit rather than the category rule's 30%.
3. This is the resolution order to remember on a call: storewide first, then any matching rules in priority order, then the product — and the product wins whenever it has been set explicitly.

**Scenario C — Priority decides between two matching rules**
1. Create a second rule with `Category` on, covering a different category, and give it a lower `Priority` number than the first rule.
2. Add a product to both categories.
3. Confirm the product uses the deposit from the rule with the lower priority number. There is one shared priority scale across every rule, whatever conditions it uses.

**Scenario D — Adding a role condition to a category rule**
1. Edit the first rule, turn the `User Role` toggle on as well, multi-select a role such as Wholesale Customer, and choose `Match only when BOTH the category and the role match`.
2. Save, then view a matching-category product as a customer who does not have that role, and confirm they no longer get the rule's 30% — they fall back to the storewide setting or another matching rule.
3. View the same product as a customer who does have that role and confirm they still get 30%.

**Scenario E — Validation and deleting a rule**
1. Create a new rule and try to save it with both the `Category` and `User Role` toggles off.
2. Confirm the form shows an inline message and does not save.
3. Return to the rules list and delete one of the test rules.
4. Confirm it disappears from the list, and that affected products fall back to the storewide deposit or the next matching rule.

### Expected Behaviour
A rule can apply a deposit to any number of product categories at once, matching a product that belongs to any of them. Deposits resolve storewide first, then through matching rules by priority, then the product — and an explicitly set product-level deposit always wins over any rule. Where several rules match, the lowest priority number wins on one shared scale. A rule with no condition enabled is rejected with a visible message rather than silently dropped, and deleting a rule returns affected products to the storewide setting or the next matching rule.

## 983 - [Bug Fix] Fixed custom page deposit calculation issue
### Brief Description
The `Pay Full Amount` and `Pay Deposit` box only displayed reliably on a product's own standard product page. On a custom page built with the Gutenberg Single Product block the box could appear with no price at all, and after switching variations it could go completely blank. On the standard product page, a product on sale showed its struck-through regular price rather than the active sale price, a variable product could keep showing the previous variation's price after switching, and selected add-on costs were left out of the deposit figures entirely. All of these now show the correct amount.

For support, this is the release to point at whenever a merchant says the deposit box is empty, shows the wrong price, or ignores the price the customer can actually see on the page.

### Prerequisites
- The store should be on version 2.0.0 or later of PH Deposits for WooCommerce.
- Nothing needs turning on — the fixes apply automatically after the update.
- You will need a product with deposits enabled, using the Design 2 deposit layout for the price-display checks.
- For the sale-price checks, use a product with an active sale price so the regular and sale prices differ, and a variable product with at least one variation on sale.
- Build the custom page from `Pages → Add New`, use the `+` button to insert the Single Product block, and pick a published product. A product inserted with a products shortcode will not work for this — that renders a shop listing card and never shows the deposit box at all.
- For the add-on checks, the Product Addons plugin needs to be active, and you will want both a simple and a variable product to test with.
- Do a hard refresh in the browser before testing, since the display scripts are cached.

### Step-by-Step Support Walkthrough

**Scenario A — The deposit box on a custom page, simple product**
1. Create a page with the Single Product block pointing at a simple product that has deposits enabled and the Design 2 layout.
2. View the page on the storefront and confirm the deposit box shows both a `Pay Full Amount` figure and a matching `Pay Deposit` figure, with neither left blank.
3. Repeat for each deposit type the product can use — percentage, fixed, and scheduled payment — and confirm the amounts are right for each.

**Scenario B — Sale prices on the standard product page**
1. Open a product with an active sale price on its normal product page.
2. Confirm `Pay Full Amount` shows the sale price the customer is actually being charged, not the struck-through regular price, and that `Pay Deposit` is calculated from that sale price.

**Scenario C — Switching variations**
1. Open a variable product with a variation on sale on its normal product page and select that variation.
2. Confirm the deposit box updates to that variation's current price, with no leftover figure from a previously selected variation.
3. Now open the same variable product through the Single Product block on a custom page and switch between variations several times.
4. Confirm the deposit box always shows a price and never goes blank.

**Scenario D — Add-on costs are included**
1. With the Product Addons plugin active, open a simple product that has both deposits and add-ons.
2. Select an add-on, and change its quantity if it has one.
3. Confirm `Pay Full Amount` and `Pay Deposit` both recalculate to include the add-on cost on top of the product price.
4. Repeat on a variable product with a variation selected, and confirm the add-on cost is included there too.

**Scenario E — Nothing else regressed**
1. Repeat the checks above across both the Design 1 and Design 2 layouts, with both percentage and fixed deposit types, on both simple and variable products.
2. Include a product that is not on sale, and a booking product if the store uses them.
3. Confirm all of these behave as they did before, and that nothing is reported as an error while loading pages, switching variations, selecting add-ons, or toggling between the full and deposit options.

### Expected Behaviour
The deposit box shows correct, non-blank `Pay Full Amount` and `Pay Deposit` figures on both custom pages built with the Single Product block and standard product pages, for simple and variable products alike. A product on sale uses its active sale price, a variable product always reflects the currently selected variation with no staleness, a block-based page never goes blank after a variation switch, and selected add-on costs are included in both figures. Both page types show matching amounts for the same product, and non-sale products, the Design 1 layout, fixed deposits, and booking products are unaffected.

## 956 - [New Feature] Add Balance Payment Order Creation Days for Fixed/Percentage Deposits
### Brief Description
Fixed and percentage deposits had no concept of a due date — the balance order was created the moment the deposit was paid and went straight to `Pending Balance Payment`, giving the customer no lead time. A new `Balance Payment Order Creation Days` setting lets a merchant delay that balance order by a number of days, so it is created dated ahead in `Scheduled` status instead. The existing reminder email then brings it due exactly as it already does for scheduled payment plans. The default is `0`, so a store that never touches the new field sees no change at all — this is purely additive.

### Prerequisites
- The store should be on version 2.0.0 or later of PH Deposits for WooCommerce.
- The storewide setting is at `WooCommerce → Deposits → Balance Payment`, directly below `Balance Payment Order Creation`.
- `Balance Payment Order Creation` must be set to create balance orders — either one order per deposit product or a single combined order. When it is set to not create any balance order, the new days field is hidden in both places.
- The per-product override is on the product's own `Deposits` tab, and only appears when that product's `Deposit Type` is `Fixed Amount` or `Percentage` — scheduled payment plans already carry their own due dates.
- Leaving the product field blank inherits the storewide value; entering `0` means create immediately.
- For the reminder check you will also need `Email Reminders Days Prior to the Order Date` set, and the hourly reminder job to run.

### Step-by-Step Support Walkthrough

**Scenario A — Delaying the balance order storewide**
1. Open `WooCommerce → Deposits → Balance Payment` and set `Balance Payment Order Creation` to create one order per deposit product.
2. Set `Balance Payment Order Creation Days` to 2 and save.
3. As a customer, buy a fixed amount or percentage deposit product and pay the deposit.
4. Confirm a balance order is created dated two days ahead with the status `Scheduled`, and that it is not yet payable.

**Scenario B — Zero days keeps the old behaviour**
1. Set `Balance Payment Order Creation Days` back to 0 and save.
2. Buy another fixed or percentage deposit product and pay the deposit.
3. Confirm the balance order is created immediately with the status `Pending Balance Payment`, exactly as before this release.

**Scenario C — A per-product override**
1. Edit a product, open its `Deposits` tab, and set `Deposit Type` to `Fixed Amount`.
2. Confirm `Balance Payment Order Creation Days` is visible.
3. Switch `Deposit Type` to `Scheduled Payment Plan` and confirm the field disappears, then switch back to `Fixed Amount` or `Percentage` and confirm it returns.
4. Enter a value different from the storewide one, such as 5, and save.
5. Buy that product's deposit and confirm its balance order is scheduled five days ahead, using the product's own value rather than the storewide number.

**Scenario D — The reminder brings the order due**
1. Set `Email Reminders Days Prior to the Order Date` to 1, and use a `Scheduled` balance order that falls due tomorrow.
2. Let the hourly reminder job run, or ask a developer to trigger it.
3. Confirm the customer receives the balance payment reminder email, and that the order moves from `Scheduled` to `Pending Balance Payment` so it can be paid.

**Scenario E — The field hides when no balance order is created**
1. Set `Balance Payment Order Creation` to not create any order for the remaining balance.
2. Confirm `Balance Payment Order Creation Days` disappears from the settings page and from every product's `Deposits` tab.

### Expected Behaviour
With the days value at its `0` default, balance orders are created immediately as `Pending Balance Payment`, unchanged from before. With a value above zero, the balance order is created dated that many days ahead in `Scheduled` status, and the existing reminder email and due-date handling take it from there without any extra configuration. A product's own value overrides the storewide one, the field only ever appears for fixed and percentage deposits, and it is hidden entirely when the store is not creating balance orders. When the store creates a single combined balance order and its products resolve to different day values, the earliest of them is used.

## 966 - [New Feature] Advanced Dashboard for Deposits – Revenue Overview, Order Balance Tracking & Payment Reminders
### Brief Description
There was no single place to see how deposits were performing or which orders still owed a balance — a merchant had to open orders one at a time. A new `Overview` page adds a revenue summary with drill-down cards and a chart, plus a filterable list of every deposit order and its outstanding balance. It also adds a `Mark as Paid` action for a balance collected in person, which completes the order and records who marked it and how much.

### Prerequisites
- The store should be on version 2.0.0 or later of PH Deposits for WooCommerce.
- The page is at `WooCommerce → Deposits → Overview`, the first item in the Deposits submenu, before `Settings`.
- Every figure is calculated live from existing orders, so the store needs real deposit orders to show anything. Have some in `Partially Paid`, `Pending Balance Payment`, and `Scheduled` status.
- Include at least one standalone deposit order that never had a balance order generated, so `Mark as Paid` can be checked against that case.
- Worth knowing before demonstrating `Mark as Paid`: it sets the order to WooCommerce's own `Completed` status, so if the store has the Completed order customer email enabled, the customer will receive that email just as they would for any manual change to Completed.
- `Screen Options` appears only on the `Deposit Order Details` tab, never on `Overview`.

### Step-by-Step Support Walkthrough

**Scenario A — The Overview tab**
1. Open `WooCommerce → Deposits → Overview` and confirm it opens on the `Overview` tab, and that `Overview` is the first item in the Deposits submenu.
2. Confirm six summary cards are shown: `Deposit Revenue`, `Total Remaining Balance`, `Deposit Orders`, `Overdue Orders`, `Paid Orders`, and `Partially Paid Orders`.
3. Hover over each card and confirm a tooltip explains what the number means and where clicking will take you, and that the tooltip is fully readable rather than cut off behind the chart below.
4. Click each card in turn and confirm it opens `Deposit Order Details` with the matching filter already selected — the `Overdue Orders` card should land on the `Overdue` filter, and so on.
5. Use the `Revenue Timeline` chart's date-range picker across a few options, such as `Month to date`, `Last quarter`, and a custom range, and confirm the collected and expected figures move with the range.
6. Confirm the `Customer Payment Insights` table lists the customers currently owing the most for the selected range.

**Scenario B — Deposit Order Details**
1. Open the `Deposit Order Details` tab and work through each filter: `All`, `Parent Orders`, `Balance`, `Upcoming`, `Overdue`, `Paid Orders`, and `Partially Paid`.
2. Confirm each filter lists only matching orders and that the count beside its name matches what is actually listed.
3. On the `All` filter, confirm the newest order appears first.
4. Search for an order number, then click a different filter, and confirm you see that filter's full results rather than the earlier search still narrowing them. Switching between the two tabs should behave the same way.
5. Find a balance order in the list and confirm it shows a `Parent: #NUM` link beneath its own order number, that the whole phrase including its icon is underlined as one link, and that clicking it opens the parent order.
6. Open the `Paid Orders` filter and confirm it shows a `Paid Amount` column in place of `Balance`, with no `Reminder` or `Action` columns.

**Scenario C — Marking a balance paid in person**
1. On a filter showing unpaid orders, confirm every unpaid row has a `Mark as Paid` button in the `Action` column with a `Not marked as paid yet` caption beneath it, lined up with the `Send` button next to it.
2. Click `Mark as Paid` and confirm a confirmation appears showing the exact amount before anything happens.
3. Confirm the confirmation, and check that the row updates in place without the page reloading — order status, balance, status and reminder all change to show it is paid, the checkbox goes, and the action shows a dash.
4. Open that order in `WooCommerce → Orders` and confirm it is now `Completed`, with an order note recording who marked it, the amount, and that it was an offline payment.
5. Repeat on a standalone deposit order that has no balance order of its own, and confirm no fresh unpaid balance order is created for the amount just recorded as paid.

**Scenario D — Reminders and the overdue badge**
1. Click `Send Reminder` on an unpaid row and confirm the button moves through `Sending…` to `Sent`, the customer receives the balance reminder email, and the last-sent caption below the button updates.
2. Check the `Overview` item in the admin sidebar and confirm a red badge shows the number of currently overdue orders when there are any.

**Scenario E — A store with no deposit orders**
1. On a store with no deposit orders at all, load the `Overview` page.
2. Confirm a single `No deposit data yet` panel is shown with a link to the deposit settings, and that no tabs appear anywhere — including if `view=orders` is typed directly into the address bar.

### Expected Behaviour
`Overview` is the first item under Deposits and opens on its summary tab, with six accurate cards that each explain themselves on hover and drill into the matching filtered order list. `Deposit Order Details` supports the full set of filters with live counts that match their contents, lists newest first, and always shows a filter's complete results after a search when the filter or tab changes. Balance orders link back to their parent as one underlined link, the paid view swaps `Balance` for `Paid Amount` and drops the action columns, and every unpaid row can be marked paid — confirming the amount first, completing the order, recording who did it in an order note, and updating the row without a reload. Marking a standalone order paid never spawns a replacement unpaid balance order. Reminders work as before, an overdue badge appears in the sidebar, and a store with no deposit orders sees a single empty-state panel with no tabs.

## 975 - [New Feature] Add User Role Deposit Rules
### Brief Description
Every customer previously saw the same deposit terms, whoever they were. A rule on the `Deposit Rules` tab can now target one or more customer roles, giving that role its own deposit rate — or switching deposits off for it entirely, so those customers always pay in full. Varying the rate is the differentiator; competing plugins only allow disabling deposits per role.

This is the other half of the same tab described in story 974. One rule can carry a User Role condition, a Category condition, or both with an explicit AND or OR choice, all sharing one priority scale.

### Prerequisites
- The store should be on version 2.0.0 or later of PH Deposits for WooCommerce.
- The tab is at `WooCommerce Deposits → Deposit Rules`, with a rules list and an Add or Edit screen.
- Both toggles start off on a new rule, and a rule with neither turned on cannot be saved.
- You will need test logins for at least two roles, plus the ability to browse logged out.
- Guests never match a role condition — a visitor who is not logged in always resolves through the storewide, category and product settings only.
- If a rule references a role that later disappears, say because the plugin that added it was deactivated, the rule still lists rather than breaking the page.
- This unified tab is premium only — the marketplace plugin still has the older separate role and category tabs.

### Step-by-Step Support Walkthrough

**Scenario A — A role gets its own deposit rate**
1. Open `WooCommerce Deposits → Deposit Rules` and click `Add New Rule`.
2. Turn the `User Role` toggle on and multi-select a role such as Customer — a rule matches any of them.
3. Set `Deposit Type` to Percentage with an amount of 20 and click `Save Rule`.
4. Confirm you return to the rule with a success message and the role still selected.
5. Log in as a user with that role and view a product that has no category rule or product-level deposit of its own.
6. Confirm the deposit shown is 20% of the price rather than the storewide default.

**Scenario B — Priority decides between rules of different types**
1. Still logged in as that role, view a product whose category is covered by a category-only rule with a lower `Priority` number than the role rule.
2. Confirm the category rule's deposit is used instead. There is no fixed ordering where roles always beat categories — the lower priority number wins, whichever condition it uses.

**Scenario C — Switching deposits off for a role**
1. Create a second rule with `User Role` on, selecting a role such as Wholesale Customer, and set `Enable Deposits` to No.
2. Log in as a user with that role and view a product with no lower-priority override.
3. Confirm no deposit option is offered at all and the customer pays in full.

**Scenario D — Guests are never affected**
1. Log out, or browse in a private window, and view the same products used above.
2. Confirm a guest always sees the storewide, category or product deposit and never a role rule's value.

**Scenario E — Combining a role condition with a category**
1. Edit the first rule, turn the `Category` toggle on as well, pick a category, and choose `Match when EITHER the category or the role matches`.
2. Save, then confirm a customer without that role buying from that category still gets the rule's 20%.
3. Confirm a customer with that role buying from any other category also still gets it. With OR, either condition matching is enough.

**Scenario F — Deleting a rule**
1. Return to the rules list and delete one of the test rules.
2. Confirm it disappears, and that affected customers fall back to the storewide, category and product resolution, or to the next matching rule.

### Expected Behaviour
A rule can target any number of customer roles, matching a customer who holds any of them, and can either give that role a different deposit rate or switch deposits off for it completely. Deposits resolve storewide first, then through matching rules by priority, then the product — with an explicitly set product-level deposit always winning. Category and role rules share one priority scale, so the lowest number wins regardless of condition type. Guests are never matched to a role condition and behave as though no role rules existed. A rule with no condition enabled is rejected with a visible message, and deleting a rule returns affected customers to the settings that applied before it.
