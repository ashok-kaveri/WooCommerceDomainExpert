# Test Document Format & Execution Notes

Reference document the format is derived from (QA-authored, UPS v6.6.4):
<https://docs.google.com/document/d/1TQg3pegfJlS30YRVgU_KxOMiVLkej08oH5NX7NoZMNs/edit>

That doc is readable with the repo's service account:

```python
from google.oauth2 import service_account
from google.auth.transport.requests import Request
import requests

creds = service_account.Credentials.from_service_account_file(
    "credentials.json", scopes=["https://www.googleapis.com/auth/drive.readonly"])
creds.refresh(Request())
requests.get(f"https://www.googleapis.com/drive/v3/files/{DOC_ID}/export",
             params={"mimeType": "text/plain"},
             headers={"Authorization": f"Bearer {creds.token}"})
```

A worked example of the input data lives at
`data/test_documents/SI23TDil_steps.json`.

## Layout

1. **Cover page** — PluginHive logo centred, then `<Plugin Name> - V <version>`.
   No header, no page number.
2. **Body section** — logo top-right above a blue rule, page number centred below
   a blue rule, numbering restarted at 1.
3. **Document History** — signature table: rows `Created by` / `Reviewed by` /
   `Approved by`, columns `Name` / `Signature` / `Date` (`DD-MM-YY`).
4. **Testing details** — `Plugin name`, `Version`, `Changelog`, `Release details`,
   `Ticket Details`, `Trello Card`, `Observation`.
5. **Details of Replicated** — the "what we had" problem statement, plus evidence
   of the pre-fix behaviour where available.
6. **Pre-requisites** — store URL, plugin under test, supporting setup, and
   screenshots proving the environment was in the stated state.
7. **TEST RESULT** — summary table: `#`, `Test Case`, `Status`.
8. **One section per checklist group**, each case as
   `TC-nn — <checklist item text>` followed by `Steps`, `Expected Result`,
   `Evidence` (screenshots with captions), then a bold `Observation:` line.

## Palette

Sampled from the reference document — do not re-derive:

| Element | Value |
|---|---|
| Section headings | `#073763` |
| Table header / label cells | `#6D9EEB` |
| Table value cells | `#EFEFEF` |
| Header & footer rules | `#3D85C6` |
| Placeholder caption text | `#888888` |

Logo asset: `data/test_documents/assets/pluginhive_logo.png`.

## docx Gotchas

The renderer already handles these; preserve them if you touch it.

- **Column widths** need `w:tblLayout` fixed *and* the `w:tblGrid` `gridCol`
  widths updated. Setting cell widths alone is ignored by Word and Pages.
- **Page numbers** must use `w:fldSimple` with `instr="PAGE"`. A
  begin/instrText/end field triple renders literally as "PAGE" in Pages.
- **Header/footer** on the body section must have `is_linked_to_previous = False`,
  or the logo and page number are inherited backwards onto the cover page.

## Rendering The PDF

The document is authored as .docx, so the PDF needs a real .docx renderer —
reportlab cannot do it.

Preferred, portable:

```bash
soffice --headless --convert-to pdf --outdir data/test_documents "<file>.docx"
```

Fallback when LibreOffice is absent (macOS):

```applescript
tell application "Pages"
    set d to open POSIX file "<abs path>.docx"
    delay 6
    export d to POSIX file "<abs path>.pdf" as PDF
    delay 3
    close d saving no
end tell
```

Pages must already be running (`open -a Pages`), otherwise AppleScript fails with
`Application isn't running. (-600)`.

## Execution Notes

Learned on the UPS v6.6.4 run. These cost real time if rediscovered.

**Screenshots**

- Browser-tool screenshots cannot be written to disk, and the embedded browser
  blocks `localhost` (`ERR_BLOCKED_BY_CLIENT`), so pushing bytes to a local sink
  does not work either. Screen capture plus crop is the only route, and it needs
  Screen Recording permission for the Claude app.
- Calibrate the pane rect per session with
  `scripts/capture_browser.py --calibrate`; it injects magenta corner markers,
  screenshots, and reports the rect.
- Re-apply the browser viewport (1440x900 works well) at the start of every turn.
  The desktop app clears it at turn boundaries and post-reset captures are zoomed.

**WooCommerce / wp-admin**

- The checkout page slug is not reliably `/checkout/`. Read
  `woocommerce_checkout_page_id` from WooCommerce → Settings → Advanced.
- Set checkout fields by assigning `.value` then dispatching `input` and `change`,
  and trigger `jQuery(document.body).trigger('update_checkout')`. Wait for the
  AJAX to settle before reading shipping rates — reading too early returns none.
- Submit with `jQuery('form.checkout').trigger('submit')`. Clicking the button can
  reload the page and silently drop the form.
- Use Cash on delivery to reach `Processing` without a real payment.
- Orders use HPOS: `admin.php?page=wc-orders&action=edit&id=<id>`.

**PluginHive UPS plugin**

- The label flow is `Generate Packages` → `Confirm Shipment`, driven by GET links
  of the form `/wp-admin/?phupsgp=<b64>` and `/wp-admin/?wf_ups_shipment_confirm=<b64>`,
  where `<b64>` is base64 of `|<order id>` (order 5653 → `fDU2NTM=`).
- **Debug Mode silently breaks the flow.** With
  `woocommerce_wf_shipping_ups_debug` enabled, the plugin prints the raw request
  and response to the screen and halts, so the order never records the tracking
  number or Print Label button and the confirm looks like a no-op. Check this
  setting first. Turning it off is a shared-config change — ask, and restore it
  after the run.
- That same debug output is excellent evidence: the shipment confirm request
  shows exactly whether an `InternationalForms` / commercial-invoice node was
  sent. Capture it before switching debug off.
- Presence or absence of the `Commercial Invoice` button in the `UPS Shipment
  Label` metabox is the decisive assertion for invoice-related cases.

**Code Snippets**

- The snippets list is REST-driven; the row toggle can fail silently. Activate via
  `POST /wp-json/code-snippets/v1/snippets/<id>/activate` with the page's
  `wpApiSettings.nonce`, then GET the snippet and assert `active: true`.
