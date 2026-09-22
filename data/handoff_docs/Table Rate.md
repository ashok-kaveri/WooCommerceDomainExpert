# Table Rate

Version v3.4.4 – Released: Sept 17th, 2026

## Included Story Cards
| Story Id | Title | Trello Card Link |
|---|---|---|
| 1034 | [Bug Fix] Fix shipping rate cost/fee decimal separator corruption on multilingual stores | [1034](https://trello.com/c/wOGyecUO/1034-bug-fix-fix-shipping-rate-cost-fee-decimal-separator-corruption-on-multilingual-stores) |
| 970 | [Compatibility] Table Rate x WPML | [970](https://trello.com/c/7fM6Le24/970-compatibility-table-rate-x-wpml) |

## 1034 - [Bug Fix] Fix shipping rate cost/fee decimal separator corruption on multilingual stores
### Brief Description
On stores running in more than one language, a Table Rate shipping rule could quietly end up charging the wrong amount. If a value such as `26,52` was typed while the store's decimal separator was a comma, and the rule was later read while a dot was the active separator, the decimal point was lost and the value was read as `2652` — roughly a hundred times too much. The same risk applied to fees and to the weight, item-count and price ranges that decide which rule applies.

Rule values are now stored in one consistent internal form the moment they are saved, so they read back correctly whatever language or separator is active later. Rules saved before this release are checked once when the update runs and corrected where the original value can still be worked out safely. Where a value has already lost its decimal point and cannot be recovered with confidence, the plugin does not guess — it raises an admin notice listing the rules a person needs to look at.

For support, this is the answer to "our shipping cost suddenly jumped to an absurd figure" on a multilingual store.

### Prerequisites
- The site must be running the updated Table Rate build from this release. The one-time check of existing rules runs by itself on update — there is nothing to switch on.
- To see or demonstrate the separator behaviour, know where the store's separator is set: `WooCommerce → Settings → General → Currency options`.
- For the multilingual scenarios, the site needs WPML active with at least one secondary language already set up, and that language should use a comma as its decimal separator.
- To demonstrate the admin notice, you need a site that already had Table Rate rules saved before this update. A freshly built store has nothing for the check to flag.
- Nothing else has to be enabled on the plugin side.

### Step-by-Step Support Walkthrough

**Scenario A — A new rule on a single-language store**
1. In WordPress admin, open `WooCommerce → Settings → General` and confirm under `Currency options` that the decimal separator is a dot.
2. Open the Table Rate shipping settings and add a rule with a `Cost` of `26.52`. Save.
3. Add the matching product to the cart and go to the storefront checkout. The shipping cost shown must be exactly `26.52` — not `2652` or `26520`.
4. Back in the rule, set a `Fee` of `5.75` and a weight range of `1.5` to `10.25`. Save, reload the settings screen, and confirm all three values still read exactly as entered.
5. Set `Fixed Base Cost` to `12.90` on the shipping method, save, and confirm it still shows `12.90` and not `1290`.

**Scenario B — A new rule entered in a secondary language**
1. Switch the site's active language to a secondary WPML language that uses a comma decimal separator.
2. Add a rule with the `Cost` entered as `26,52`, using the comma exactly as the admin screen presents it. Save.
3. Switch back to the default language and open the same rule. The `Cost` must still read `26.52` — the correct value, not an amount inflated a hundredfold.
4. Place a test order in the secondary language using that rule and confirm the shipping charged at checkout is the intended amount.

**Scenario C — Rules that already existed before the update**
1. On a site that already had Table Rate rules, apply the update.
2. Open the Table Rate settings and compare the costs, fees and weight, item and price ranges against what the merchant expects. No existing rule should have quietly changed to a different amount.
3. Look at the WordPress admin dashboard for a notice about shipping rules that may have lost a decimal point. If no notice appears, scan the rules for suspiciously round figures — a rule reading `2650` where `26.50` was intended is the pattern to watch for.
4. If the notice does appear, confirm it names a sensible handful of rules rather than every rule on the site, and that re-saving one of the flagged rules with the correct value clears it from the list.
5. Reload the dashboard, or move to another admin page, and confirm the notice is still shown. It must not vanish after the first page load.

**Scenario D — Edge cases worth checking on a support call**
1. Enter a cost with thousands grouping — `1,234.56`, or `1.234,56` depending on the active language — and confirm it saves and calculates as one thousand two hundred thirty four point five six, not a garbled or truncated figure.
2. Leave `Cost` and `Fee` blank on a new rule, save, and confirm the rule saves cleanly with no stray zero or error text left in the field.
3. Import a spreadsheet of rules that uses comma decimals and confirm the imported values display and calculate correctly afterwards.

### Expected Behaviour
Shipping rule costs, fees and ranges keep the value the merchant typed, regardless of which language or decimal separator is active when the rule is saved or read back. Rules saved before this release are corrected in place where that can be done safely; where a value has already lost its decimal point, the plugin flags the affected rules in an admin notice that persists across page loads rather than guessing at a correction. Checkout charges the intended amount in every language, including on stores that use comma decimals.

## 970 - [Compatibility] Table Rate x WPML
### Brief Description
WPML asked for a fresh compatibility retest of Table Rate, the previous one having been done in July 2020, with both products having moved on considerably since. The retest found a set of admin strings that could not be translated, and tab labels that stayed in English when the settings were opened from a Shipping Zone. Those are now fixed: the licence-screen strings are available for translation, the licence-not-activated banner shows its translated text when the site language changes, and the `Shipping Rules`, `Settings` and `Import/Export` tabs translate correctly no matter which route is used to reach them.

One finding is not fixable and support should be ready to say so: the `Choose file` and `No file chosen` labels on the file-upload control are drawn by the web browser itself, not by the plugin, so they cannot be offered for translation. That is normal browser behaviour and not a plugin defect.

### Prerequisites
- The site must be running the updated Table Rate build from this release.
- WPML must be active with String Translation available, and at least one secondary language set up so the site language can be switched.
- Access to the Table Rate licence screen is needed for the licence-string and banner checks.
- To see the licence-not-activated banner, the site must be in a state where the licence has not been activated.
- No plugin or store setting has to be turned on for this work.

### Step-by-Step Support Walkthrough

**Scenario A — Licence-screen strings are now translatable**
1. In WordPress admin, open the WPML String Translation screen.
2. Search for `Deactivated`, `Save Changes`, `Deactivates a License so it can be used on another site.` and `Manage your License`. Each should be listed and available to translate.
3. Provide a translation for one of them, switch the site to that language, open the Table Rate licence screen, and confirm the translated wording is shown.

**Scenario B — The licence-not-activated banner**
1. On a site where the Table Rate licence has not been activated, find the banner that warns the plugin will not receive future updates.
2. Translate that message in WPML String Translation.
3. Switch the site language and confirm the banner now shows the translated text. Previously it stayed in English even when a translation existed.

**Scenario C — Tab labels reached from a Shipping Zone**
1. Open `WooCommerce → Settings → Shipping`, pick a shipping zone, and open its Table Rate Shipping method.
2. Look at the `Shipping Rules`, `Settings` and `Import/Export` tabs and confirm they show in the site's active language.
3. Compare against the same tabs on the main Table Rate settings page. Both routes should now read identically in the chosen language.

**Scenario D — The known limitation on the file-upload control**
1. Open the Table Rate `Import/Export` tab and look at the file-upload control.
2. The `Choose file` and `No file chosen` labels will stay in the browser's own language and will not appear in WPML String Translation.
3. If a merchant reports this, explain that these two labels come from the browser rather than from the plugin, so no plugin-side translation is possible.

**Scenario E — General sanity check**
1. Move through the Table Rate settings and licence screens in a secondary language.
2. Confirm nothing nearby reads or behaves oddly — rules still save, the tabs still switch, and the licence screen still functions.

### Expected Behaviour
With WPML active, the Table Rate licence-screen strings and the licence-not-activated banner can be translated and show their translated text when the site language is switched. The `Shipping Rules`, `Settings` and `Import/Export` tab labels translate correctly whether the settings are opened from the main Table Rate page or from a Shipping Zone. The `Choose file` and `No file chosen` labels remain untranslatable by design, because the browser supplies them.
