# Canada Post

Version v3.3.12 – Released: Sep 17th, 2026

## Included Story Cards
| Story Id | Title | Trello Card Link |
|---|---|---|
| 1023 | [Bug Fix] Auto-check COD when generating packages for COD gateway orders | [1023](https://trello.com/c/WPk3vJip) |
| 1033 | [Bug Fix] Complete missing translations and fix broken translation strings across Canada Post plugin | [1033](https://trello.com/c/Ui7DvZTB) |

## 1023 - [Bug Fix] Auto-check COD when generating packages for COD gateway orders

### Brief Description
When an order is paid with Cash on Delivery, the Cash on Delivery option in the Canada Post panel on the order is now selected automatically as soon as packages are generated. Staff no longer have to remember to tick it before creating the label, so the amount Canada Post must collect from the recipient is no longer missed.

### Prerequisites
- Nothing new has to be switched on for this to work. The selection happens on its own, and no setting was added for it.
- Cash on Delivery must be available as a payment method at checkout, under WooCommerce > Settings > Payments, so that orders paid this way exist on the store.
- The store must already be able to create Canada Post labels — a completed Canada Post registration in wp-admin and the plugin build covered by this guide.
- Stores that already use the plugin's own Cash on Delivery option in the Canada Post settings need no change; that setting keeps working exactly as before.

### Step-by-Step Support Walkthrough

**Scenario A — a Cash on Delivery order, the normal path**
1. On the storefront, place a test order and choose Cash on Delivery at checkout.
2. Open that order in WooCommerce > Orders.
3. In the Canada Post section of the order, click **Generate All The Packages** — or **Re-generate Package(s)** if packages are already there.
4. Look at the Cash on Delivery option in that same Canada Post section: it is already ticked, with nobody having touched it.
5. Generate the shipping label. The amount to collect from the recipient is carried through onto the label.

**Scenario B — staff decide not to collect on a particular order**
1. On a Cash on Delivery order, generate the packages as in Scenario A.
2. Untick the Cash on Delivery option on the order before creating the label.
3. Generate the label. It carries no amount to collect, and the store-wide Cash on Delivery setting in the Canada Post settings is untouched — the change applies to that one order only.

**Scenario C — orders paid by any other method**
1. Place an order paid by a different method, such as a card payment, PayPal, or bank transfer, and generate the packages.
2. The Cash on Delivery option is *not* ticked automatically.
3. If the store has the plugin's own Cash on Delivery option enabled in the Canada Post settings, that store-wide behaviour continues to drive the option exactly as it did before this release.

**Scenario D — a store that packs orders manually**
1. On a store set to pack orders manually, place a Cash on Delivery order and generate the packages.
2. Use **Calculate Shipping Cost** on the order.
3. The Cash on Delivery option is still ticked automatically and the page behaves normally, with no errors on screen.

### Expected Behaviour
Cash on Delivery orders reach the label step with collection already selected, so the amount owed appears on the Canada Post label without staff action. This does not add any charge to the WooCommerce order total — it only tells Canada Post what to collect on delivery. Orders paid by other methods, and the store's own Cash on Delivery setting, behave exactly as before, and staff can still opt out on any single order by unticking the option before creating the label.

## 1033 - [Bug Fix] Complete missing translations and fix broken translation strings across Canada Post plugin

### Brief Description
The shipping-label notification email now follows the site's active language even when the merchant has left the subject and message fields blank, instead of always going out in English. The French translation supplied with the plugin has also been refreshed, so the plugin's admin wording reads correctly and completely on French sites.

### Prerequisites
- A second language must already be set up and active on the site through a translation tool such as WPML or Loco Translate. On an English-only site nothing changes.
- To see the translated default email, the **Email Subject** and **Content of Email With Label** fields in the Canada Post Shipping Labels settings must be left blank, so the plugin's own defaults are used.
- The store must already be able to create Canada Post labels and send the label notification email.
- The refreshed translation shipped in this release is French. Other languages still depend on whatever translation the site itself supplies.

### Step-by-Step Support Walkthrough

**Scenario A — the default label email in a second language**
1. With a second language active on the site, open the Canada Post settings and go to the Shipping Labels section.
2. Leave **Email Subject** and **Content of Email With Label** blank, and save.
3. Generate a shipping label for an order so that the label notification email goes out.
4. Open the email that was sent. Both the subject line and the message body arrive in the site's active language rather than English.

**Scenario B — the merchant's own wording still wins**
1. In the same Shipping Labels settings, type a custom **Email Subject** and custom **Content of Email With Label** in the second language, and save.
2. Generate a label again.
3. The email uses the merchant's wording exactly as typed. Custom text is never overwritten by a translation.

**Scenario C — English sites are unaffected**
1. Switch the site back to its default English language.
2. Leave the two email fields blank and generate a label.
3. The default subject and message still read correctly in English, worded as before.

**Scenario D — admin wording on a French site**
1. With French active, walk through the plugin's settings screens and the messages shown on orders and shipments.
2. Confirm the wording reads as complete French sentences — no half-translated text, and no stray placeholder symbols sitting where a name, number, or amount should appear.
3. In the site's translation tool, check the plugin's French translation: there should be no entries reported as missing or left unfinished.

### Expected Behaviour
On a site running a second language, the Canada Post label notification email and the plugin's admin wording appear translated instead of falling back to English, and French sites in particular no longer show incomplete or broken sentences. Anything the merchant has typed themselves is always used as-is. English-only stores see no difference at all, and label creation and email sending continue to work as before in every language.
