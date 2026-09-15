# Booking & Appointment Plugin for WooCommerce

Version 6.0.1 – Released: Sept 2nd, 2026

## Included Story Cards
| Story Id | Title | Trello Card Link |
|---|---|---|
| 991 | [Bug Fix] Calendar UI design issue fixed | [991](https://trello.com/c/vE9xEYBb/991-bug-fix-calendar-ui-design-issue-fixed) |
| 990 | [New Feature] Booking Follow-Up Emails — configurable Order Status and Booking Status filters | [990](https://trello.com/c/KdE6wzUH/990-new-feature-booking-follow-up-emails-configurable-order-status-and-booking-status-filters) |
| 997 | UI-Improvement | [997](https://trello.com/c/sungX1Fn/997-ui-improvement) |
| 986 | [Bug Fix] Booking Reminder Emails sent for unpaid bookings regardless of payment status | [986](https://trello.com/c/IW8lrbYN/986-bug-fix-booking-reminder-emails-sent-for-unpaid-bookings-regardless-of-payment-status) |

## 991 - [Bug Fix] Calendar UI design issue fixed
### Brief Description
A group of calendar display fixes across the booking calendar designs. Time slots now line up properly in the box design, reopening the From or To time field shows that field's own day rather than a leftover one, moving to another month no longer carries hidden leftovers into the next selection, and a booking that runs past midnight now highlights both days it covers. The duplicate dropdown arrow on the admin month selector is gone too.

Nothing about pricing or availability changed — these were all display and highlighting problems, so a merchant's existing bookings and rules are unaffected.

### Prerequisites
- Plugin version 6.0.1 or later.
- Nothing needs turning on — the fixes apply automatically after the update.
- You will need to switch between calendar designs under `Bookings → Settings → Display Customiser` to cover all of them: the box design, the persistent calendar design, and the design used by the admin month selector.
- For the across-day and midnight checks, use a time-based product that allows booking across days, with short slots (five minutes works well) and a slot that ends after midnight.
- The plugin's scripts are cached by version, so do a hard refresh on any page you had already opened in the same browser session — otherwise you may still be looking at the old behaviour.

### Step-by-Step Support Walkthrough

**Scenario A — Box design time slots and time fields**
1. On the storefront, open a product using the box calendar design and start an across-day booking so the time slot picker opens.
2. Confirm the slots sit in a clean grid from the first row, with none of them tucked into or overlapping the `<` `>` navigation bar.
3. With an across-day booking already chosen, click the From time field and confirm the picker opens showing the From date's own slots with the From time highlighted.
4. Now click the To time field and confirm it shows the To date's own slots highlighted, with no highlight left over from the From picker.

**Scenario B — Box design month navigation**
1. With a booking already selected, use the calendar's month navigation to move to a different month.
2. Confirm the booking summary resets to `Please Pick a Date`.
3. Pick a fresh date and time in the new month and confirm the resulting booking is correct, with nothing carried over from the selection you made before navigating.

**Scenario C — Highlighting on the persistent calendar design**
1. Open a product using the persistent calendar design and select a three-day range using the `>` day arrow.
2. Click `<` once and confirm the range shrinks by one day from the correct end, with the day you started from still highlighted.
3. Select a slot that runs past midnight, for example 11:50pm to 00:10am, and confirm both the start day and the end day are highlighted on the date calendar.
4. Use the day arrows again and confirm both days stay highlighted.
5. Make a booking that spans the end of one month into the next, then page day by day across the month boundary and back several times in both directions. Confirm the earlier month always shows the full selected range highlighted, and that the result does not change depending on how you got there.
6. View a day whose next day is unavailable and confirm the `>` arrow stays hidden rather than reappearing a moment later.

**Scenario D — Admin parity and the month selector**
1. In WordPress admin, open `Bookings → Add Booking` and repeat the highlighting checks from Scenario C. Behaviour should match the storefront exactly, since this screen shares the same calendar.
2. With the design that uses the admin month selector active, open `Bookings → Add Booking` and confirm the month dropdown shows exactly one arrow, not two.

**Scenario E — Same-day bookings did not change**
1. Repeat a normal same-day booking on each calendar design.
2. Confirm selection, highlighting, and the booking summary all behave exactly as they did before this release.

### Expected Behaviour
Time slots render in a clean grid, the From and To time fields always show their own date's slots and highlight, and moving between months leaves nothing stale behind. Selected ranges stay correctly highlighted however the customer pages through days or months, a booking crossing midnight highlights both days, and a navigation arrow that is correctly hidden stays hidden. The admin `Add Booking` calendar behaves identically to the storefront, its month dropdown shows a single arrow, and same-day bookings are unchanged.

## 990 - [New Feature] Booking Follow-Up Emails — configurable Order Status and Booking Status filters
### Brief Description
Merchants can now choose exactly which bookings receive a follow-up email. Two multi-select settings were added to the Follow up Email section — one for order status and one for booking status — and a follow-up is sent only when the booking matches a selected value in *both*. This brings Follow-up emails in line with Reminder emails, which already worked this way.

There is one deliberate change in behaviour worth telling merchants about: cancelled bookings previously still received a follow-up email, and now they never do.

### Prerequisites
- Plugin version 6.0.1 or later.
- The settings live under `Bookings → Settings → Reminder and Follow up Emails`, inside the `Follow up Email` card: `Select order status` and `Select booking status`.
- Out of the box, `Select order status` is set to `Completed` only and `Select booking status` is set to `All`, which covers every booking status except Cancelled. A store that never opens this screen keeps its previous sending behaviour, apart from cancelled bookings.
- `Cancelled` is deliberately not offered as a booking status option — cancelled bookings are always excluded and there is no way to override that.
- To exercise the filters you will need bookings in more than one order status and booking status, so plan a few test orders before starting.

### Step-by-Step Support Walkthrough

**Scenario A — Defaults on a store that has not touched the settings**
1. On a store freshly updated and never saved on this screen, open `Bookings → Settings → Reminder and Follow up Emails`.
2. In the `Follow up Email` card, confirm `Select order status` shows `Completed` selected, not `All`.
3. Confirm `Select booking status` shows `All` selected, with the individual options greyed out.
4. Confirm follow-up emails still go out for previously eligible bookings, exactly as before the update.

**Scenario B — Filtering by booking status**
1. In `Select booking status`, deselect `All`, leave everything selected except `Unpaid`, and save.
2. Let a follow-up run for a booking whose booking status is `Unpaid` and confirm no email is sent.
3. Let one run for a booking whose booking status is `Paid` and confirm the email still sends normally under the same configuration.

**Scenario C — Filtering by order status**
1. In `Select order status`, deselect `All`, select `Completed` and `Processing`, and save.
2. Let a follow-up run for an order in `Processing` and confirm the email sends.
3. Remove `Completed` from the selection, save, and confirm a genuinely completed order now gets no follow-up email.

**Scenario D — How the All option behaves**
1. In either dropdown, select `All` and confirm the selection collapses to `All` alone with every individual option greyed out.
2. Select an individual status instead and confirm `All` greys out and is removed from the selection.
3. Save, reload the page, and confirm the selection you made is what comes back.

**Scenario E — An empty selection stops every follow-up email**
1. Clear either dropdown completely, so neither `All` nor any individual status is selected, and save.
2. Confirm no follow-up email is sent at all for that dimension — including for orders that would obviously qualify, such as a genuinely completed one.
3. Reload the page and confirm the empty selection was kept rather than quietly reset to the default.
4. This is intended behaviour, but it means an accidentally emptied dropdown silently switches follow-up emails off completely. It is the first thing to check when a merchant reports that follow-up emails stopped.

**Scenario F — Refunds and the email template choice**
1. Take a fully refunded booking and confirm it is still eligible for a follow-up under the default settings.
2. Take a partially refunded order and confirm the booking status did not change — a partial refund leaves it as it was, so eligibility is unchanged.
3. Set `Select the Email Template` to `WooCommerce Emails` in the `Follow up Email` card.
4. Confirm both status dropdowns stay visible and editable on the settings tab, and that a saved filter still blocks or allows follow-up emails in exactly the same way as under `Plugin Default`.

### Expected Behaviour
A follow-up email is sent only when the order's status and the booking's status are both selected in their respective settings; either one being unselected blocks it. Stores that never open the screen keep their previous behaviour, except that cancelled bookings no longer receive follow-ups. `All` and the individual options are mutually exclusive in both directions, an explicitly emptied dropdown is honoured and stops that dimension entirely, and both filters apply whichever email template is selected. Reminder emails are unaffected — they are a separate feature.

## 997 - UI-Improvement
### Brief Description
The `Booked From` and `Booked To` display labels can no longer be set to the words `From` or `To`. Those two values clashed with something the plugin stores internally, which caused a booking order to fail with an error when a merchant tried to update or refund it in admin. The settings screen now warns about this up front, marks the field if one of those words is typed, disables saving until it is corrected, and refuses the save outright as a second line of defence.

### Prerequisites
- Plugin version 6.0.1 or later.
- The fields are on `Bookings → Settings → Display Customiser`: `Booked From` and `Booked To`.
- Nothing needs turning on — the warning and the block are always active.
- The check is case-insensitive and ignores surrounding spaces, so `From`, `from`, `FROM`, and ` From ` are all treated the same.
- This prevents the problem going forward; a site that already saved `From` or `To` still needs the label changed to a safe value before its booking orders will save.

### Step-by-Step Support Walkthrough

**Scenario A — The warning is visible before anything is typed**
1. Open `Bookings → Settings → Display Customiser`.
2. Confirm a note appears under both `Booked From` and `Booked To` explaining that `From` and `To` are not allowed, and suggesting alternatives such as `Booking From` or `From Date`.

**Scenario B — Typing a reserved word blocks the save**
1. Type `From` into `Booked From`.
2. Confirm the field border turns red and the `Save Settings` button becomes unavailable.
3. Try the other spellings — `from`, `FROM`, and the word with spaces around it — and confirm each is blocked the same way.
4. Repeat with `To` in the `Booked To` field.
5. Change the value to something valid such as `Booking From` and confirm the red border clears and `Save Settings` becomes available again.

**Scenario C — Valid labels save normally**
1. Set both labels to valid, distinct values, and change a few other fields too, such as the check-in and check-out labels.
2. Save and confirm everything saved with no errors.
3. Open a booking order in `WooCommerce → Orders`, click `Update`, and then process a refund. Confirm both complete without an error.

**Scenario D — The Save button reflects every check on the page**
1. Select four or more options under `Booking Personalization for Admin Calendar` so that its own warning appears and `Save Settings` is disabled.
2. With that still invalid, type a perfectly valid label into `Booked From`.
3. Confirm `Save Settings` stays disabled — fixing the label must not re-enable saving while the other setting is still invalid.
4. Reduce the personalization selection to three or fewer options and confirm `Save Settings` becomes available again.

### Expected Behaviour
`From` and `To` cannot be saved as the `Booked From` or `Booked To` label in any spelling, and the merchant is told why before they try. `Save Settings` is unavailable exactly while either field holds a reserved value, and becomes available again as soon as it is corrected — while still respecting the other validation on the same page. Every other Display Customiser setting saves as before, and updating or refunding a booking order no longer fails.

## 986 - [Bug Fix] Booking Reminder Emails sent for unpaid bookings regardless of payment status
### Brief Description
Reminder emails were going out for bookings that were never actually paid for — a failed card payment or an order awaiting a bank transfer would still trigger a reminder, and the email itself would say the booking was unpaid while reading as though it were confirmed. Merchants can now choose which order statuses and which booking statuses are eligible for a reminder, using two multi-select settings, and a reminder is sent only when the booking matches a selected value in both.

Existing stores see no change until they choose to narrow the settings, because both start out set to `All`.

### Prerequisites
- Plugin version 6.0.1 or later.
- The settings live under `Bookings → Settings → Reminder and Follow up Emails`, in the Reminder Email section: `Order Statuses for Reminder Emails` and `Booking Statuses for Reminder Emails`.
- Both default to `All`, which reproduces the previous behaviour exactly, so no configuration is needed after updating.
- `Cancelled` is deliberately not offered as a booking status option — cancelled bookings were always excluded and still are.
- To fix the reported problem for a merchant, deselect `All` in `Booking Statuses for Reminder Emails` and then deselect `Unpaid`.
- For the deposit scenario, a deposits or split-payment plugin is needed so an order can reach a partially paid state.

### Step-by-Step Support Walkthrough

**Scenario A — Nothing changes until the merchant narrows the settings**
1. On a freshly updated store, open the Reminder Email settings and confirm both dropdowns show `All` selected with the individual options greyed out.
2. Confirm reminders still send as before for previously eligible bookings — test one with a booking status of `Paid` and one with `Unpaid`.

**Scenario B — Stopping reminders for unpaid bookings**
1. In `Booking Statuses for Reminder Emails`, deselect `All`, leave everything selected except `Unpaid`, and save.
2. Let a reminder run for a booking whose booking status is `Unpaid` and confirm no email is sent. This is the fix for the reported complaint.
3. Let one run for a booking whose booking status is `Paid` and confirm it still sends normally.

**Scenario C — Filtering by order status**
1. In `Order Statuses for Reminder Emails`, deselect `All`, leave everything selected except `Partially Paid`, and save.
2. Let a reminder run for an order whose status is `Partially Paid` and confirm no email is sent.
3. Let one run for an order in `Processing` and confirm it still sends normally.

**Scenario D — Deposit orders, where the two statuses can disagree**
1. Place an order through the deposits plugin and note both the order status and the booking status.
2. Be aware they often differ: paying a deposit moves the order status to `Partially Paid`, but the booking status usually stays `Unpaid` until an admin changes it by hand in the Edit Booking popup. Both settings have to allow the actual combination for a reminder to go out.
3. With `Partially Paid` selected in both dropdowns and a booking that really is partially paid on both counts, confirm the reminder is sent.
4. Deselect `Partially Paid` from the booking status list and confirm the reminder is now blocked.

**Scenario E — A skipped reminder never arrives late**
1. Let a reminder be skipped because the status was not eligible at the time it was due.
2. Change the status to something eligible, for example from `Unpaid` to `Paid`.
3. Confirm the missed reminder is not sent afterwards — there is no retry, whether the status changes before or after the booking's start time.
4. Confirm that once a booking's start time has passed, no reminder is attempted at all regardless of status. This matters on a support call: a merchant who fixes a payment after the fact should not expect the reminder to arrive.

**Scenario F — The email template choice**
1. Set `Select the Email Template` to `WooCommerce Emails` in the Reminder Email section.
2. Confirm both status dropdowns stay visible and editable on the settings tab.
3. Confirm a saved filter still blocks or allows reminders in exactly the same way as under `Plugin Default` — the template only affects how an eligible email is put together, never whether it is eligible.

### Expected Behaviour
A reminder is sent only when the order's status and the booking's status are both selected in their respective settings, so an unpaid booking no longer receives one once `Unpaid` is deselected. Stores that leave both settings at `All` behave exactly as they did before, and cancelled bookings are still always excluded. An explicitly emptied dropdown is honoured and stops reminders for that dimension entirely — the same accidental kill-switch to check first if a merchant says reminders stopped. Deposit orders are judged on their real order status and booking status independently, a skipped reminder is never sent late, and both filters apply whichever email template is selected. Follow-up emails are unaffected — they are a separate feature.
