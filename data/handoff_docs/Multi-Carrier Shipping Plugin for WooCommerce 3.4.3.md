# Multi-Carrier Shipping Plugin for WooCommerce

Version 3.4.3 – Released: Aug 27th, 2026

## Included Story Cards
| Story Id | Title | Trello Card Link |
|---|---|---|
| 994 | [New Feature] Detect and notify on carrier connection lost (UPS, FedEx, USPS) | [994](https://trello.com/c/jjhNP9hJ/994-new-feature-detect-and-notify-on-carrier-connection-lost-ups-fedex-usps) |

## 994 - [New Feature] Detect and notify on carrier connection lost (UPS, FedEx, USPS)
### Brief Description
When a UPS, FedEx, or USPS connection is lost — for example because the carrier account was disconnected or its access expired — the store no longer fails quietly. The plugin now detects it the first time it happens, records it, and emails the store admin a `Multi-Carrier Connection Lost` notice so they can reconnect the account straight away. The email names the affected carrier, offers a direct link to reconnect it, and lets the admin download the error log. It only fires once per connection-lost episode rather than on every failed rate request, and the whole feature is optional.

Before this release, a lost carrier connection simply meant that carrier's rates stopped appearing at checkout until somebody noticed — which is a common cause of "my shipping rates disappeared" tickets.

### Prerequisites
- The store should be on version 3.4.3 or later of the Multi-Carrier Shipping plugin.
- At least one of UPS, FedEx, or USPS should already be registered and returning rates on the site.
- `Notify on Carrier Connection Lost` must be turned on. It is the master switch for the whole feature — with it off, no email is sent and nothing is recorded. Find it by editing the Multi-Carrier shipping method under `WooCommerce > Settings > Shipping`, then opening `Debug > Advanced Settings`.
- The `Multi-Carrier Connection Lost` email must also be enabled under `WooCommerce > Settings > Emails`, where it can be edited independently.
- The site should be able to send email, and you should have access to the recipient inbox to confirm delivery.
- To demonstrate a lost connection safely, be ready to temporarily replace the carrier's credentials with an invalid value and restore the correct ones afterwards.

### Step-by-Step Support Walkthrough

**Scenario A — Turning the feature on**
1. In WordPress admin, open `WooCommerce > Settings > Shipping` and edit the Multi-Carrier shipping method.
2. Go to `Debug > Advanced Settings` and confirm the `Notify on Carrier Connection Lost` setting is present.
3. Turn it on and save.
4. Open `WooCommerce > Settings > Emails` and confirm a `Multi-Carrier Connection Lost` email is listed there, and that it can be enabled, disabled, and edited on its own.

**Scenario B — A lost connection is detected**
1. Open the carrier registration screen for UPS and temporarily replace the credentials with an invalid value.
2. On the storefront, add a product to the cart and go to checkout so rates are requested.
3. Open `WooCommerce > Status > Logs` and confirm a connection-lost entry was recorded for that carrier, and that the admin notification email was sent.
4. Trigger several more rate requests for the same carrier and confirm no duplicate notification emails go out — only the first detection notifies while the connection stays lost.
5. Restore the correct credentials and request rates again. Confirm the successful request marks the connection active once more, with no further notices for that carrier until it is lost again.
6. Repeat the same check for FedEx and confirm its own `Multi-Carrier Connection Lost` email arrives.
7. Repeat it for USPS, including a checkout where rates are returned in the background rather than immediately, and confirm the connection-lost entry is still recorded in that case.

**Scenario C — The notification email the admin receives**
1. With the feature on and a carrier connection lost, check the recipient inbox for a `Multi-Carrier Connection Lost` email.
2. Confirm the email names the carrier the connection was lost for.
3. Click `Reconnect` in the email and confirm it opens the correct settings page for that carrier.
4. Click `Download Error Log` and confirm the correct log file downloads. The admin must be signed in for this to work.

**Scenario D — Tailoring the email**
1. Open `WooCommerce > Settings > Emails` and edit the `Multi-Carrier Connection Lost` email.
2. Leave `Recipient(s)` blank, trigger a lost connection, and confirm the email arrives at the site's admin address.
3. Enter two comma-separated addresses in `Recipient(s)`, trigger it again, and confirm both receive the email.
4. Leave `Subject` at its default and confirm the received subject reads `[Site Title] Multi-Carrier connection lost: <Carrier>`, with the store's own title and the real carrier name filled in.
5. Set a custom `Subject` using the `{site_title}` and `{carrier}` placeholders and confirm both are replaced correctly.
6. Leave `Email heading` at its default and confirm `Multi-Carrier connection lost` appears as the heading in the email body.
7. Set a custom `Email heading` and confirm it replaces the default in both the formatted and plain-text versions.
8. Leave `Additional content` blank and confirm no extra block appears; then add some text and confirm it appears in both versions of the email.
9. Confirm the email arrives with working `Reconnect` and `Download Error Log` buttons.
10. Set `Email type` to Plain text and confirm it arrives as plain text with those two actions shown as plain web addresses.
11. Add an address under `Cc(s)`, trigger a lost connection, and confirm it receives a copy.
12. Add an address under `Bcc(s)`, trigger it again, and confirm that address receives a copy without appearing to the main recipient.
13. Open the email preview for this template on the same screen and confirm it renders correctly with sample content and no errors.

**Scenario E — Turning it off, and the difference between the two switches**
1. Turn `Notify on Carrier Connection Lost` off under `Debug > Advanced Settings`, trigger a carrier failure, and confirm no email is sent and no connection-lost entry is recorded in the logs.
2. Turn it back on, but under `WooCommerce > Settings > Emails` untick `Enable this email notification` for the `Multi-Carrier Connection Lost` email.
3. Trigger a lost connection again and confirm no email goes out.
4. Re-tick `Enable this email notification`, trigger it once more, and confirm the email is sent again.

### Expected Behaviour
A lost UPS, FedEx, or USPS connection is detected the first time it happens and recorded under `WooCommerce > Status > Logs`, and the admin receives a single `Multi-Carrier Connection Lost` email naming the affected carrier, with a working `Reconnect` link and a downloadable error log. Repeated failures for the same carrier do not send duplicate emails, and the next successful rate request marks that carrier active again — making it eligible for a fresh notice only if the connection is lost a second time.

The two switches do different jobs, which is worth knowing on a support call: `Notify on Carrier Connection Lost` under `Debug > Advanced Settings` controls the whole feature, so turning it off stops both the email and the log entry, while unticking `Enable this email notification` on the email itself stops just that email. If a merchant reports that a carrier's rates stopped appearing at checkout, this email — or the log entry behind it — is now the fastest way to confirm whether the carrier account simply needs reconnecting.
