# Woo Carrier Knowledge Research

This file describes the carrier-knowledge inputs the WooCommerce expert uses. It is not a future backlog.

## Current Source Coverage

- **`docs/kb_snapshots/` — the primary source.** 457 WooCommerce articles mirrored
  from `https://www.pluginhive.com/knowledge-base/` by `scripts/scrape_woo_kb.py`.
  Every snapshot carries its live `Source:` URL and a `Plugin:` tag, so answers can
  cite the article and be filtered per plugin. Rough distribution: general 100,
  UPS 86, FedEx 80, Bookings 74, Table Rate 34, Estimated Delivery 20,
  Canada Post 17, Multi-Carrier 16, Shipment Tracking 16, and a long tail.
- Plugin source: `multi-carrier-shipping-plugin-for-woocommerce`, `woocommerce-shipping-pro`
- Automation repo: `ups-woo-automation`
- Trello board `ph-Woo-WIP-Releases` for release cards

## Carrier Coverage Confirmed

The automation repo currently includes carrier env coverage for:
- Amazon Shipping
- Australia Post
- Blue Dart
- FedEx
- MyPost
- UPS
- USPS
- USPS Stamps

The broader documentation set also includes support material for additional carriers and carrier families such as:
- DHL
- Canada Post
- Purolator
- PostNord
- EasyPost or USPS via EasyPost

## Operating Rule For Card Interpretation

Cards should be interpreted with this rule:
- if the card clearly mentions a carrier, treat it as carrier-specific
- if the card does not mention a carrier, treat it as generic
- generic cards should use a stable default carrier path unless retrieved context says the scenario must stay carrier-neutral or explicitly multi-carrier

This matters because many PluginHive features are shared behaviours:
- the orders list and the order-screen shipment metabox
- label generation, bulk labels, return labels, void shipment
- packing methods and box packing
- shipping zones, methods, and shipping classes
- rate calculation and the request/response logs
- product-level shipping fields and per-carrier special services

## Navigation Facts

WooCommerce admin is URL-addressable — every screen has its own URL, so navigation
is a goto rather than a click chain:
- `admin.php?page=wc-orders` — orders list; append `&action=edit&id=<id>` for one order
- `edit.php?post_type=product` — products; per-product shipping fields live on the
  product's **Shipping** tab
- `admin.php?page=wc-settings&tab=shipping` — zones and method settings
- `admin.php?page=ph_multi_carrier_admin_menu` — the Multi-Carrier plugin menu
- `admin.php?page=ph_multi_carrier_<carrier>_registration` — carrier registration
- `admin.php?page=wc-status` — versions and logs
- storefront `/shop/`, `/cart/`, `/checkout/` — the only place buyer-visible rates
  can actually be verified

There is no app iframe, no single app endpoint, and no hamburger search here.

## Current Implementation

Shared carrier knowledge is implemented in:
- [pipeline/carrier_knowledge.py](pipeline/carrier_knowledge.py:1)

It provides:
- supported carrier profiles
- alias matching
- carrier-specific vs generic card detection
- default generic-carrier guidance
- carrier env path resolution for automation order creation

It is currently used by:
- [pipeline/user_story_writer.py](pipeline/user_story_writer.py:1)
- [pipeline/domain_validator.py](pipeline/domain_validator.py:1)
- [pipeline/smart_ac_verifier.py](pipeline/smart_ac_verifier.py:1)
- [pipeline/order_creator.py](pipeline/order_creator.py:1)
- [pipeline/handoff_docs.py](pipeline/handoff_docs.py:1)

## Practical Conclusion

The repo already has the right source inputs for multi-carrier reasoning.

The important rule for future agents is:
- keep carrier knowledge explicit
- keep it reused across validation, QA planning, automation setup, issue diagnosis, and handoff output
- do not downgrade the repo back to single-carrier assumptions just to mirror MCSL
- re-scrape the KB rather than letting the mirror drift: `scripts/scrape_woo_kb.py`
