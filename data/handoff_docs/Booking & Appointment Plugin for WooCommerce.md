# Booking & Appointment Plugin for WooCommerce

Version 6.0.0 – Released: Aug 12th, 2026

## Included Story Cards
| Story Id | Title | Trello Card Link |
|---|---|---|
| 920 | [New Feature] Implemented Booking Edit Feature for the All Bookings Page | [920](https://trello.com/c/VOIpkf9I/920-new-feature-implemented-booking-edit-feature-for-the-all-bookings-page) |
| 921 | [Improvement] Search Widget UI and functionality for booking products | [921](https://trello.com/c/0bIjRcrE/921-improvement-search-widget-sw-updates-for-normal-booking-product) |
| 944 | [New Feature] Screen Options for the All Bookings Page | [944](https://trello.com/c/v0RjrOFw/944-new-feature-screen-options-for-the-all-bookings-page) |
| 929 | [Improvement] All Bookings page pagination count mismatch + improved load performance | [929](https://trello.com/c/s2LNE6LC/929-improvement-all-bookings-page-pagination-count-mismatch-improved-load-performance) |
| 946 | [Improvement] Move Google Calendar Sync Debug Logging to the Diagnostics Tab | [946](https://trello.com/c/IwZR8qii/946-improvement-move-google-calendar-sync-debug-logging-to-the-diagnostics-tab) |
| 940 | [Improvement] Added two-way sync with Outlook Calendar for events and bookings | [940](https://trello.com/c/LRkwzp4z/940-improvement-outlook-calendar-event-details-removal) |
| 939 | [Improvement] Replace periodic scan crons with per-booking scheduled jobs for follow-up emails | [939](https://trello.com/c/EyAduFah/939-improvement-replace-periodic-scan-crons-with-per-booking-scheduled-jobs-for-follow-up-emails) |
| 936 | [Improvement] Replace Periodic Reminder Email Scan Cron with Per-Booking Scheduled Jobs | [936](https://trello.com/c/GmamhiVR/936-improvement-replace-periodic-reminder-email-scan-cron-with-per-booking-scheduled-jobs-performance-issue-for-reminder-email) |
| 924 | [Improvement] Fixed Duplicate Deposit Orders and Booking Status Issues | [924](https://trello.com/c/Hvmw7M1q/924-improvement-fixed-duplicate-deposit-orders-and-booking-status-issues) |
| - | [Bug Fix] Fix currency switchers not converting the product-page price before date selection | [Card](https://trello.com/c/dscbwmBM) |

## 920 - [New Feature] Implemented Booking Edit Feature for the All Bookings Page
### Brief Description
Admins can now edit an existing booking directly from the All Bookings page instead of relying on the standard WooCommerce order edit flow. The new popup checks the same availability, asset, participant, and timing rules the customer-facing booking flow uses, so support can trust that any accepted change is still a valid booking.

### Prerequisites
- Plugin version 6.0.0 or later.
- The `Manage` / `Actions` column must be enabled from `Bookings → All Bookings → Screen Options`.
- `Bookings → Settings → Advanced → Enable Booking Modification` must be on for non-administrator roles, and each allowed role must be added to `Allow access to specific roles`.
- Administrators always have access, even if the role list is empty.
- Deposit, Non-adjustment, Recurring Deposit, and Product Add-on bookings are not supported by this edit flow.

### Step-by-Step Support Walkthrough
1. Go to `Bookings → Settings → Advanced`, turn on `Enable Booking Modification`, and save.
2. Open `Bookings → All Bookings`, expand `Screen Options`, enable the `Manage` column, and confirm the `Edit` action appears.
3. Open a booking that has not started yet and is not on a completed, cancelled, or refunded order.
4. Change the date, time, asset, participants, resource, or notes, then save the update.
5. Confirm the change is reflected in `Bookings → All Bookings`, the WooCommerce order, the customer's `My Account` view, and any connected calendar.
6. Try an invalid change, such as an unavailable slot, an over-capacity participant count, or a blocked time window, and confirm the update is refused.
7. If the edit changes the booking price, confirm support can either keep the original price or allow the updated balance flow to continue for the customer.

### Expected Behaviour
- Valid edits save cleanly and update the booking everywhere the merchant or customer can see it.
- Invalid edits are blocked before anything is partially changed.
- The customer is always informed about the updated booking details after a successful save.
- If a merchant says the feature is missing, the first checks are the `Manage` column in `Screen Options` and the role access rules in `Advanced`.

## 921 - [Improvement] Search Widget UI and functionality for booking products
### Brief Description
The Search Availability Widget now follows the same booking rules as the real product calendar, so search results and bookable slots stay in sync. This also improves the widget experience by auto-running searches as filters change, preserving selected filters on reload, and showing time choices in the visitor's local timezone.

### Prerequisites
- Plugin version 6.0.0 or later.
- The widget must be enabled from `Bookings → Settings → Advanced`.
- The widget settings now live on `Advanced`; they no longer appear under `Settings → Calendar Display`.
- To verify timezone behaviour, use a site timezone that differs from the tester's local timezone.
- To verify asset-order behaviour, use a product with multiple assets and auto-assign enabled.

### Step-by-Step Support Walkthrough
1. Go to `Bookings → Settings → Advanced` and confirm the Search Availability Widget settings are present there.
2. Open the storefront page with the search widget and run searches using date, participant, and asset filters.
3. Confirm the search updates automatically as the required filters are chosen, and that the manual search button still works.
4. Reload the results page and confirm the selected asset and participant count stay in place.
5. Compare a few widget results against the actual booking calendar on the corresponding product page and confirm both allow and reject the same booking windows.
6. Test an auto-assigned asset setup and confirm a customer cannot bypass the normal asset order by selecting a later asset in the search.
7. Test a product with a different local timezone from the site and confirm the displayed search times make sense for the visitor.

### Expected Behaviour
- Search results match the real booking calendar for the same product and date range.
- Filter changes can trigger the search automatically without breaking the manual search option.
- Selected filters stay visible after reload or when a results page is shared.
- Time choices reflect the visitor's local timezone, and asset selection follows the expected booking order.

## 944 - [New Feature] Screen Options for the All Bookings Page
### Brief Description
The All Bookings page now has a standard WordPress `Screen Options` panel so each admin can choose which columns they want to see and how many bookings appear per page. This makes the list easier to manage without changing the default experience for merchants who do nothing after the update.

### Prerequisites
- Plugin version 6.0.0 or later.
- Open `Screen Options` from the top-right corner of `Bookings → All Bookings`.
- The new `Manage` column stays hidden by default until an admin enables it.
- To see the `Manage` option itself, booking modification must be enabled under `Bookings → Settings → Advanced`.

### Step-by-Step Support Walkthrough
1. Go to `Bookings → Settings → Advanced` and enable booking modification if the merchant needs the `Manage` column.
2. Open `Bookings → All Bookings`, then open `Screen Options`.
3. Confirm the existing columns are selected by default and the new `Manage` column starts hidden.
4. Change `Items per page`, save, and confirm the list reloads using the new page size.
5. Enter a value above 200 and confirm the page size is immediately capped back to 200.
6. Hide a column, save, reload, and confirm the same admin still sees that saved layout.
7. Repeat with a second admin account and confirm that one user's layout does not overwrite another's.

### Expected Behaviour
- Each admin can control their own column layout and rows-per-page setting.
- The `Manage` column does not appear until someone explicitly turns it on.
- The page size cannot be pushed past 200.
- Saved `Screen Options` choices remain stable after reloads.

## 929 - [Improvement] All Bookings page pagination count mismatch + improved load performance
### Brief Description
The All Bookings page now shows item counts and page counts that match the filters the merchant is actually using. The same release also reduces the amount of work needed to load that page, so large booking lists feel faster and less confusing.

### Prerequisites
- Plugin version 6.0.0 or later.
- Best verified on a store with enough bookings to span multiple pages.
- Use a store with multiple statuses, products, date ranges, and assets to confirm the counts properly change with filters.

### Step-by-Step Support Walkthrough
1. Open `Bookings → All Bookings` with no filters and confirm the total count and page count match the visible booking set.
2. Check each status tab and confirm the item count and page count update to reflect only that tab.
3. Apply the `Product`, `Bookings Start Between`, `Bookings End Between`, and `Asset` filters one by one and confirm the counts update each time.
4. Combine several filters together and confirm the list, item count, and page count still describe the same filtered set.
5. Move between result pages with filters still applied and confirm the filtered total stays consistent.
6. On a large store, compare the page load experience with the previous release and confirm the list feels at least as responsive.

### Expected Behaviour
- Item counts and page counts always reflect the filtered result set, not the store-wide total.
- Combined filters still produce consistent counts across multiple pages.
- Renamed assets continue to display correctly in the list.
- Large booking lists load more smoothly than before.

## 946 - [Improvement] Move Google Calendar Sync Debug Logging to the Diagnostics Tab
### Brief Description
Google Calendar Sync debugging is now managed from the shared Diagnostics area instead of living on the Google Calendar Sync tab by itself. This gives support one place to turn logging on and off and makes it easier to gather enough detail when a merchant reports a calendar sync issue.

### Prerequisites
- Plugin version 6.0.0 or later.
- `Bookings → Settings → Google Calendar Sync` must already be enabled and connected before the debug option can be used.
- If a store already had the older Google Calendar debug setting turned on, that choice carries over automatically after updating.

### Step-by-Step Support Walkthrough
1. Open `Bookings → Settings → Google Calendar Sync` and confirm the old debug checkbox is no longer shown there.
2. Open `Bookings → Settings → Diagnostics` and confirm the Google Calendar debug option is available alongside the other debug rows.
3. Turn Google Calendar Sync off and confirm the Diagnostics option becomes unavailable until sync is enabled again.
4. Turn Google Calendar Sync back on, enable its Diagnostics option, save, and confirm the setting remains enabled after reload.
5. Trigger a test booking sync, then review the available log output from the Diagnostics area or from `WooCommerce → Status → Logs`.
6. Turn the Diagnostics option off again and confirm later sync activity no longer adds fresh entries.

### Expected Behaviour
- Support finds the Google Calendar debug option in `Diagnostics`, not on the Google Calendar Sync tab.
- The option is only usable when Google Calendar Sync itself is active.
- Turning logging on gives support usable sync evidence for new activity.
- Turning logging off stops fresh debug output from being added.

## 940 - [Improvement] Added two-way sync with Outlook Calendar for events and bookings
### Brief Description
Bookings and Outlook Calendar now stay in step in both directions. An event created in Outlook comes into the store as a real booking that blocks the slot, and a booking made in the store writes its details back onto the matching Outlook event. Details written back are merged into whatever the merchant or customer already typed in the event rather than replacing it — previously that text was silently lost on every sync — and the plugin can now read the Asset, Participant, and Resource choices out of an imported event's own description and apply them to the booking it creates.

### Prerequisites
- Plugin version 6.0.0 or later.
- `Bookings → Settings → MS Outlook Sync` must be connected to a working Outlook account.
- For the import checks, use a product that already has Assets, Participant types, or Resources configured, so those values can be matched.
- In an imported event's description, each value goes on its own line as `Label: Value` or `Label -> Value`, for example `Asset: Room A`. Only labels matching something configured on that product are applied; anything else is left alone.
- This prevents future description loss; it does not restore description text that was already overwritten before updating.

### Step-by-Step Support Walkthrough
1. In Outlook, create an event whose title matches a bookable product, add some description text of your own, and let it sync into the store.
2. Confirm a matching booking is created and the slot is blocked, then reopen the event and confirm your original description text is still there, with the booking details added below it.
3. Create another event for a product that has Assets, Participant types, or Resources configured, adding lines such as `Asset: Room A` and `Adult: 2` to its description.
4. Let it sync and confirm the resulting booking has that asset, participant count, and resource applied, matching what the same choices would produce at checkout.
5. Change the date or customer details on a booking that came from Outlook, let it sync again, and confirm the event shows one up-to-date set of booking details rather than repeated copies.
6. Place a normal booking through the storefront and confirm its Outlook event receives the booking details in the same format as an imported one.
7. If the merchant uses the Outlook debug option, confirm it now sits with the other debug settings on `Bookings → Settings → Diagnostics`, and that it is greyed out when Outlook sync itself is switched off.

### Expected Behaviour
- Events created in Outlook become bookings that block the slot, and bookings created in the store appear on the Outlook calendar.
- Description text already written in an Outlook event is preserved, with the booking details merged in below it.
- Asset, Participant, and Resource lines written in an imported event's description are applied to the booking when they match values configured on that product.
- Repeated syncs update the booking details in place instead of stacking duplicate copies.
- Store-created and Outlook-imported bookings use the same details format, and the Diagnostics tab is the single place to check Outlook debug logging.

## 939 - [Improvement] Replace periodic scan crons with per-booking scheduled jobs for follow-up emails
### Brief Description
Follow-up emails now track each booking individually instead of relying on a repeated store-wide scan. That makes follow-up delivery more reliable for merchants and gives support a clearer way to explain why a follow-up was sent, delayed, or skipped.

### Prerequisites
- Plugin version 6.0.0 or later.
- Follow-up email must be enabled in the Bookings email settings, with a follow-up delay configured.
- For a live demonstration, use a very short follow-up delay.
- Turn on the Follow-up Email debug option from `Bookings → Settings → Diagnostics` if support needs to inspect delivery behaviour.

### Step-by-Step Support Walkthrough
1. Go to the Bookings follow-up email settings, enable Follow-up Email, and use a short delay for testing.
2. Turn on the Follow-up Email debug option in `Bookings → Settings → Diagnostics`.
3. Place a test booking, complete the order, and wait for the configured delay after the booking ends.
4. Confirm the customer receives the follow-up email at the expected time.
5. Repeat with an order that is not yet completed and confirm the follow-up is not sent early.
6. Review the available debug output and confirm support can tell whether the email was scheduled, sent, or skipped.
7. Turn the follow-up email setting off and confirm future follow-ups stop while it remains off.

### Expected Behaviour
- Completed bookings receive follow-up emails after the configured delay.
- Bookings that are not ready for follow-up are not silently lost.
- Support can use Diagnostics to understand why a follow-up did or did not go out.
- Turning Follow-up Email off prevents new follow-ups from being sent while that setting remains off.

## 936 - [Improvement] Replace Periodic Reminder Email Scan Cron with Per-Booking Scheduled Jobs
### Brief Description
Reminder emails are now scheduled per booking instead of depending on a repeated background sweep across all bookings on the site. This reduces overhead on busy stores and helps ensure reminders arrive at the right time rather than after the booking has already started.

### Prerequisites
- Plugin version 6.0.0 or later.
- `Bookings → Settings → Notifications` must have Reminder Email enabled with a suitable notification lead time.
- For support testing, use a short lead time and a booking that starts soon.
- Existing future bookings from before the update should still be checked after the update settles.

### Step-by-Step Support Walkthrough
1. Open `Bookings → Settings → Notifications`, enable Reminder Email, and set a short lead time for testing.
2. Place a booking whose start time is close enough to observe the reminder.
3. Confirm the reminder email arrives shortly before the booking begins.
4. Repeat with Reminder Email turned off and confirm no reminder is sent.
5. Repeat with a booking that is cancelled before the reminder time and confirm no reminder goes out after cancellation.
6. Check a future booking created before the update and confirm it still receives its reminder.
7. If background processing catches up after the booking has already started, confirm the reminder is not sent late.

### Expected Behaviour
- Reminders are sent at the configured lead time before the booking starts.
- Cancelled bookings and bookings with Reminder Email turned off do not generate reminders.
- Older future bookings still remain covered after the update.
- Merchants should no longer receive reminders after the booked time has already passed.

## 924 - [Improvement] Fixed Duplicate Deposit Orders and Booking Status Issues
### Brief Description
Deposit-related balance orders no longer appear as separate bookings in the Bookings list, so merchants see one booking entry instead of duplicate-looking rows and inflated counts. The same release also fixes order save failures that could affect regular order work from WooCommerce admin.

### Prerequisites
- Plugin version 6.0.0 or later.
- Use a store that has PluginHive deposit-based booking flows enabled if the merchant wants to confirm the deposit scenarios.
- Test with both manually created balance orders and automatically created balance orders when possible.
- Deposit and balance orders still remain visible in `WooCommerce → Orders`; the change only affects the Bookings list and its counts.

### Step-by-Step Support Walkthrough
1. Create a booking that uses a deposit flow and confirm the original booking appears in `Bookings → All Bookings`.
2. Generate or complete the related balance payment order and confirm it does not appear as a second booking row in the Bookings list.
3. Check the status tabs in `Bookings → All Bookings` and confirm the counts still reflect only the actual booking orders.
4. Open `WooCommerce → Orders`, create or edit a normal order, and confirm the save completes normally.
5. If the store uses calendar-created bookings, confirm those bookings still appear correctly in the Bookings list and continue to save without error.

### Expected Behaviour
- Deposit and balance payment orders do not inflate the Bookings list or its counts.
- The original booking still appears normally in both the Bookings list and WooCommerce orders.
- Saving ordinary WooCommerce orders no longer fails unexpectedly.
- When a merchant reports an unusually high booking count, this card and the pagination-count fix should be checked together.

## [Bug Fix] Fix currency switchers not converting the product-page price before date selection
### Brief Description
Before this fix, a bookable product could show the right currency symbol but still keep the old number until the customer chose a date. The product page price now converts correctly even before date selection, so merchants using a supported currency switcher see a consistent price at every step of the booking flow.

### Prerequisites
- Plugin version 6.0.0.
- A supported currency switcher must be active and configured with at least two currencies.
- Use a non-default currency with a real exchange rate so the converted amount is visibly different.
- Test on a bookable product that shows a price before the customer selects a date.

### Step-by-Step Support Walkthrough
1. Open a bookable product page on the storefront and note the price shown before any date is selected.
2. Use the currency switcher to change to another configured currency.
3. Confirm the product page price itself changes to the converted amount, not just the currency symbol.
4. Select a date and time so the booking price is recalculated.
5. Change currency again and confirm the calculated booking price still converts correctly after selection.
6. If the merchant reports a mismatch, compare both the pre-selection price and the after-selection price before escalating.

### Expected Behaviour
- The pre-selection product price converts when the storefront currency changes.
- The post-selection booking price continues to convert correctly as well.
- Merchants see a consistent currency experience before and after choosing a date.
