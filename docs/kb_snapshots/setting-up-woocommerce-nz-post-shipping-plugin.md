# How to Set Up PH NZ Post Shipping for WooCommerce

**Source:** https://www.pluginhive.com/knowledge-base/setting-up-woocommerce-nz-post-shipping-plugin/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# How to Set Up PH NZ Post Shipping for WooCommerce

This step-by-step guide explains how to set up **PH NZ Post Shipping for WooCommerce with Print Label** plugin to display real-time NZ Post shipping rates, generate shipping labels, and enable order tracking directly from your WooCommerce store. You can follow the complete setup process or jump to a specific section based on your requirements.

* * *

## In This Guide

  1. **Download, Install, and Activate the Plugin**
  2. **Activate the Plugin License**
  3. **Navigate to Plugin Settings**
  4. **Configure API Credentials**
  5. **Add Shipper Address Details**
  6. **Verify Your Product Settings**
     * Add Product Weight and Dimensions
     * Add NZ Post Shipping Details at Product Level
     * Set Product Weight and Dimensions Unit
     * Set Minimum Product Weight and Dimensions
  7. **Display NZ Post Shipping Rates**
     * Enable Real-Time Rates
     * Display Estimated Delivery Date
     * Add Fallback Rate
     * Add Currency Conversion Rate
  8. **Configure NZ Post Shipping Services**
     * Domestic Services
     * International Services
     * Adjust Shipping Rates
     * Display NZ Post Services Based on Shipping Zones
  9. **Configure Packaging Settings**
     * Individual Packaging
     * Flexible Packaging
     * Max Weight Limit
  10. **Configure Label Settings**
     * Label Format
     * Label Size
     * Default Domestic Shipping Service
     * Default International Shipping Service
     * Show All Services in Order Page
  11. **Printing NZ Post Shipping Labels**
     * Printing Your First NZ Post Label
     * Print NZ Post Return Label
     * Clear Label Data
  12. **How to Set Up NZ Post International Shipping**
     * Insurance
     * Default HS Tariff Code
     * Default Country of Origin
     * Nature of Transaction
     * Mixed Content Codes
     * Transaction Description
     * Print NZ Post International Documents
  13. **Set Up NZ Post Shipment Tracking**
     * Disable Tracking Notification for Customers
     * Hide Tracking in My Account
     * Customise the Tracking Message
  14. **Debug Settings**

* * *

## 1\. Download, Install, and Activate the Plugin

After purchasing the PH NZ Post Shipping for WooCommerce with Print Label plugin, download the ZIP file from your PluginHive account.

Log in to your PluginHive account and go to **My Account > API Downloads**. Download the plugin ZIP file. Then,

  * Log in as the WordPress Admin of your online store. Navigate to **Plugins > Add Plugin** in your WordPress dashboard.

* * *

  * Click **Upload Plugin** to upload the downloaded ZIP file.

* * *

  * Choose the file, and click **Install Now**.

* * *

  * Once installation is complete, click **Activate Plugin**.

* * *

## 2\. Activate the Plugin License

After installing and activating the plugin, you must activate your license to unlock all plugin features.

To get your license details, log in to your PluginHive Account and navigate to **My Account > API Keys**. Copy your Product Order API Key.

  * Next, in your WordPress dashboard, go to: **NZ Post > License**

* * *

  * Under **License Activation** , enter your Product Order API Key in the respective field, then click **Save Changes**.

* * *

  * Once you activate the license, the API Key Status will display **Activated** , confirming the plugin is fully licensed.

* * *

**Note:**  
An active plugin license is required for label generation and other premium features. Real-time NZ Post shipping rates will continue to display after license expiry, but label printing and other licensed functionality will stop working. Renew your license before it expires to avoid disruptions.

* * *

## 3\. Navigate to Plugin Settings

Once you activate the plugin, WooCommerce adds NZ Post Shipping as a new shipping method. You can access the plugin settings in two ways:

  * Navigate to **Plugins > Installed Plugins > PH NZ Post Shipping for WooCommerce with Print Label > Settings**.

* * *

  * Or navigate to **WooCommerce > Settings > Shipping > NZ Post**.

* * *

After opening the plugin settings, you will find the following tabs: **API & Shipper**, **Services** , **Labels** , **International** , **Packaging** , **Tracking** , **Debug** , and **Help & Support**.

* * *

## 4\. Configure API Credentials

Go to **WooCommerce > Settings > Shipping > NZ Post**. At the top of the **API & Shipper** tab, you will find the API Configuration section. These credentials are provided by NZ Post when you register for API access.

  * **Client ID:** Your NZ Post API Client ID. Required for authentication.
  * **Client Secret:** Your NZ Post API Client Secret. Required for authentication.
  * **Account Number:** Your NZ Post Account Number. Required for rate calculation and label generation.
  * **Site Code:** Your NZ Post Site Code. Required for label generation.

* * *

**Note:**  
All four API fields are mandatory. If you require a NZ Post Account Number and/or Site Code, please contact NZ Post.

* * *

## 5\. Add Shipper Address Details

Below the API Configuration section on the API & Shipper tab, you will find the **Shipper Settings**. Enter the address from which you dispatch your orders, such as your store, warehouse, or any other shipping location.

  * **Shipper Name:** The name associated with your NZ Post account. Used for rate calculation and label printing. Required (3–40 characters).
  * **Company Name:** Your company name as it should appear on shipments.
  * **Email:** Your contact email address (max 50 characters).
  * **Phone Number:** Your contact phone number. Required by NZ Post for shipment communication.
  * **Shipper Address Line 1:** Primary street address of the shipment origin. Required (max 40 characters).
  * **Address Line 2 (Optional):** Additional address information such as a floor or unit number (max 40 characters).
  * **Suburb:** Shipment origin suburb. Required (max 40 characters).
  * **City:** Shipment origin city. Required (max 40 characters).
  * **Postal Code:** Shipment origin postal code. Required.

* * *

Click **Save Changes** after filling in all required fields.

* * *

## 6\. Verify Your Product Settings

To get accurate NZ Post shipping rates and generate valid labels, your products must have correct weight and dimension values set in WooCommerce.

### Add Product Weight and Dimensions

  * Go to **WooCommerce > Products** and open the product you want to configure.

* * *

  * Under **Product Data** , click the **Shipping** tab and enter the product’s Weight, Length, Width, and Height.
  * Assign a Shipping Class if applicable.

* * *

### Add NZ Post Shipping Details at Product Level

In the same Shipping tab, scroll down to the **NZ Post Shipping Details** section and configure the following:

  * **Pre-Packed Product:** Enable if this item ships in its own pre-packed box. The plugin treats it as an individual package regardless of the packing method set in the Packaging settings.
  * **Insurance Value:** The insured value (in NZD) for this product. This field is only visible when Insurance is enabled in the International tab.
  * **HS Tariff Code:** The Harmonized System (HS) code for this product (6–10 digits, dots and spaces accepted as separators). Required for international shipments. Overrides the default HS code set in the International tab.
  * **Country of Origin:** The country where this product is manufactured. Used for international customs declarations. Overrides the default country set in the International tab.

* * *

**Note:**  
The NZ Post Shipping Details fields are also available at the variation level for variable products.

* * *

### Set Product Weight and Dimensions Unit

When creating products in WooCommerce, it is essential to set the correct weight and dimensions units so that NZ Post receives accurate data for rate calculation and label generation.

  * Go to **WooCommerce > Settings > Products**.
  * Under the **Measurements** section, set the Weight Unit and Dimensions Unit that match your products.
    * **kg/cm (Recommended):** Kilograms and centimetres — the standard unit set for NZ Post shipments.
    * **lbs / in:** Pounds and inches — use only if your store operates in imperial units.

* * *

**Note:**  
NZ Post API works in kilograms and centimetres. If you set your WooCommerce units to lbs/in, the plugin will convert the values automatically. However, we recommend setting your store units to kg/cm to avoid any conversion discrepancies.

* * *

### Set Minimum Product Weight and Dimensions

NZ Post requires product weight and dimensions to meet certain minimum values for rate calculation. Go to **WooCommerce > Settings > Shipping > NZ Post > Packaging** tab and set the **Minimum Product Weight** and **Minimum Dimensions** values.

* * *

> If a product has no dimensions configured, the minimum values set here are used as a fallback. Any product dimensions below the configured minimum are automatically adjusted before rates are fetched from NZ Post.

* * *

## 7\. Display NZ Post Shipping Rates

Go to **WooCommerce > Settings > Shipping > NZ Post > Services** tab to configure how shipping rates are fetched and displayed at checkout.

* * *

### Enable Real-Time Rates

Tick the **Real-Time Rates** checkbox to fetch live NZ Post shipping rates and display them on the Cart and Checkout pages. This option is enabled by default.

* * *

Once enabled, real-time rates will appear at checkout for customers to choose from.

* * *

### Display Estimated Delivery Date

Enable the **Estimated Delivery Date** option to show the expected delivery date alongside each shipping service on the Cart and Checkout pages and on the order edit page. When you enable this, the plugin fetches the estimated delivery date from the NZ Post API along with the rate.

* * *

Once enabled, a new column appears in the service list where you can configure Time Adjustment (Days). This allows you to add extra days for specific NZ Post services if needed.

* * *

**Note:**  
The estimated delivery date for Pace and Pace Express services cannot be adjusted, as these services return a fixed delivery estimate from the NZ Post API.

* * *

The delivery date will be displayed for customers at the cart and checkout page as shown below.

* * *

### Add Fallback Rate

Display the Fallback Rate at checkout if NZ Post does not return shipping rates for an order (for example, during an API timeout). This allows customers to complete checkout without interruption. Enter the flat rate amount in NZD in the **Fallback Rate** field.

* * *

Leave this field blank to disable the fallback.

### Add Currency Conversion Rate

If your WooCommerce store uses a currency other than NZD, enter the conversion rate from your store currency to New Zealand Dollar in the **WooCommerce Currency to NZ Conversion Rate** field. The plugin uses this value to send correctly converted amounts to NZ Post for rate calculation.

* * *

Click **Save Changes**. 

** _Note_** _: If the store currency is already set to_** _NZD_** _, the_** _Currency Conversion_** _field is automatically set to_** _1_** _and is disabled._

* * *

## 8\. Configure NZ Post Shipping Services

In the **Services** tab, below the rate settings, you will find the **Shipping Services** list. Enable the services you want to offer and customize how they appear to customers.

### Domestic Services

The plugin supports the following NZ Post domestic shipping services:

**CourierPost services:**

  * Courier Parcel (CPOLP)
  * Courier Parcel W/Island Contract (CPOLCT1)
  * Courier Parcel Nationwide Contract (CPOLCT3)
  * Express Tonight (CPOLPSED)
  * Courier Perishable Parcel (CPOLPPS)

* * *

**Pace services** (rates returned dynamically from the NZ Post API based on the delivery address):

  * **Pace – Express:** Same-day or fast express delivery for eligible areas.
  * **Pace – Priority:** 3-hour priority delivery for eligible areas.

* * *

### International Services

The following international services are available for shipments going outside New Zealand:

  * International – Courier (ICOU)
  * International – Courier Thermal (ICOU7)
  * International – Express (IEXP)
  * International – Economy Packet (IECON)
  * International – Economy Plus (IECOP)
  * International – Economy Plus Thermal (IECOP7)
  * International – Economy Tracked (IECOT)

Enable the services you want to offer at checkout. You can also set a custom **Display Name** for each service — this is the label shown to customers at checkout instead of the default service name.

* * *

### Adjust Shipping Rates

For each service, you can increase or decrease the rate displayed at checkout. Two adjustment types are available and can be used independently or in combination:

  * **Price Adjustment (NZD):** A fixed dollar amount added to or subtracted from the NZ Post rate. Use a minus sign (–) to subtract.
  * **Price Adjustment (%):** A percentage of the base rate added to or subtracted from it. Use a minus sign (–) to subtract.

When both are used together, the fixed amount is applied first, and the percentage is then calculated on the resulting value.

**Example** : If the Courier Parcel rate is NZD 10, a fixed adjustment of NZD 5 and a percentage adjustment of 10% gives a displayed rate of NZD 16.50 (NZD 10 + NZD 5 = NZD 15, then 10% of NZD 15 = NZD 1.50, total NZD 16.50).

* * *

### Display NZ Post Services Based on Shipping Zones

To show specific NZ Post services only to customers in certain regions, use WooCommerce Shipping Zones.

  * Go to **WooCommerce > Settings > Shipping > Shipping Zones**. You can edit the existing zone, or click **Add Zone** to create a new one.

* * *

  * Give the zone a name, select the relevant region(s), and click **Save Changes**.

* * *

  * Click **Add Shipping Method** , select **NZ Post Shipping** , and click **Continue**.

* * *

  * Click **Edit** next to the NZ Post Shipping method in the zone. 

* * *

  * Set a Method Title if needed, enable the services you want to offer for that zone, then click **Save Changes**.

* * *

Now, at cart/ checkout, the selected NZ Post services applicable to the customer’s zone will be displayed.

* * *

**Note:**  
When NZ Post services are configured inside a Shipping Zone, make sure the same services are disabled in the global Services settings. Otherwise the same services may appear from both configurations, resulting in duplicate rates at checkout.

* * *

## 9\. Configure Packaging Settings

The plugin allows you to define how products are packed and shipped using NZ Post services. Go to **WooCommerce > Settings > Shipping > NZ Post > Packaging** tab and select your preferred parcel packing method.

* * *

### Individual Packaging

Each item in the order is packed into its own separate box. Shipping costs are calculated per item and a separate label is generated for each product.

* * *

**Example** : If a customer orders 2 units of a product, each unit ships in its own box and two separate labels are generated.

* * *

### Flexible Packaging

Pack items into custom boxes that you define or into NZ Post’s pre-loaded standard Trackpak boxes. The plugin automatically selects the best-fitting box based on product dimensions and weight. After you select this packing method, the **Packing Algorithm** setting appears. Choose how the plugin fits items into boxes.

  * **Volume Based Packing:** Packs items based purely on available box volume. This is the default algorithm.
  * **Stack First Packing:** Stacks items vertically before filling the remaining space.
  * **Based on Volume Used & Item Count:** Balances both volume utilisation and item count to avoid overfilling boxes.

* * *

The plugin comes pre-loaded with the following standard NZ Post Trackpak boxes:

  * A4 Trackpak (32.5 × 25 × 2 cm, max 25 kg)
  * A4 Bubble Trackpak (32.5 × 25 × 2 cm, max 25 kg)
  * A5 Trackpak (28 × 18.5 × 2 cm, max 25 kg)
  * A5 Bubble Trackpak (28 × 18.5 × 2 cm, max 25 kg)
  * DLE Trackpak (24 × 13 × 2 cm, max 25 kg)
  * Foolscap Trackpak (38 × 27.5 × 2 cm, max 25 kg)
  * Lineflow Trackpak (44 × 39.5 × 2 cm, max 25 kg)
  * Eco A5 Trackpak (28 × 18.5 × 2 cm, max 25 kg)
  * Eco DLE Trackpak (24 × 13 × 2 cm, max 25 kg)
  * Eco Foolscap Trackpak (38 × 27.5 × 2 cm, max 25 kg)
  * Xtra Large Trackpak (44.5 × 44 × 2 cm, max 25 kg)

* * *

You can enable or disable individual pre-loaded boxes in the Box Details table, and add your own custom boxes by clicking **Add Box**. For each custom box, enter a name, outer dimensions (Length, Width, Height), inner dimensions, empty box weight, maximum item quantity, and maximum weight per box.

* * *

You can remove and reset the selected boxes using the respective buttons. Click **Save Changes** to save.

* * *

### Max Weight Limit

Pack items together into a single box until the maximum weight limit is reached, then start a new box. This default packing method requires only product weights and does not use product dimensions.

  * **Box Weight:** The weight of the empty box itself in your store’s configured weight unit. The default is 0.
  * **Max Package Weight:** The maximum total weight (items + box weight) allowed per package. The default is 10.
  * **Max Package Quantity:** Maximum number of items allowed per package. Set to 0 for no item count limit.
  * **Packing Process:** Pack heavier items first (descending order) or pack lighter items first (ascending order).

* * *

**Note:**  
Make sure all products have accurate weights set on the product page. Incorrect or missing weights will cause inaccurate package generation and shipping rates.

* * *

## 10\. Configure Label Settings

Go to **WooCommerce > Settings > Shipping > NZ Post > Labels** tab. This tab controls the label format, size, default services, and order page service visibility for label generation.

* * *

### Label Format

Choose the file format for generated shipping labels from the **Label Format** dropdown:

  * **PDF (Default):** Standard format suitable for most label printers.
  * **PNG:** High-quality image format for standard printers.

* * *

### Label Size

Choose the label paper size from the **Label Size** dropdown:

  * **174 × 100 (Standard, Default):** Recommended for most dedicated label printers.
  * **150 × 100:** Alternative standard label size.

* * *

### Default Domestic Shipping Service

Select the NZ Post domestic service that will be pre-selected in the **Create Shipment** dropdown on the order edit page when generating a label for a domestic order. This saves time during manual label creation.

* * *

### Default International Shipping Service

Select the NZ Post international service that will be pre-selected in the **Create Shipment** dropdown on the order edit page when generating a label for an international order.

* * *

### Show All Services in Order Page

Enable this option to display all available NZ Post services in the **Create Shipment** dropdown on the order edit page — not just the services enabled in the Services tab. This is useful when you want to use a different service for label generation than what is shown at checkout.

* * *

Click **Save Changes**.

* * *

## 11\. Printing NZ Post Shipping Labels

After configuring the plugin, customers can view the available NZ Post shipping services on the Cart and Checkout pages, select their preferred service, and place the order.

### Printing Your First NZ Post Label

Once an order is placed, generate and print the shipping label from the WooCommerce order page:

Go to **WooCommerce > Orders** and open the relevant order.

* * *

In the **NZ Post Shipment Label** metabox on the order edit page, click **Generate Packages**. The plugin creates packages based on your Packaging settings.

* * *

### Add/Edit/Delete Packages

Once packages are generated, the package view appears on the order edit page. You have the following options before creating the shipment:

  * **Edit Package:** Click the edit icon next to a package to modify its weight, dimensions, or the products assigned to it. If you enable Insurance in the International tab, the plugin displays an Insurance Amount field for each package, allowing you to set the insured value individually for every box.

* * *

  * **Add Package:** Click Add Package to create an additional package for the order. 

* * *

  * Assign products to it, enter the dimensions and weight, and click Save Package(s) to save it. You can add as many packages as the order requires.

* * *

  * **Delete Package:** Click the delete icon to remove a package. Make sure all products are assigned to at least one package before creating the shipment.

* * *

**Calculate Shipping Cost**

Before creating the shipment, click the **Calculate Shipping Cost** button to fetch the latest real-time NZ Post rates for your package(s) based on the current dimensions, weight, and destination address. This lets you compare available services and their rates on the order page before committing to a service. If Estimated Delivery Date is enabled in the Services tab, the expected delivery date is also shown alongside each rate.

* * *

**Print NZ Post Shipping Label**

Once you have reviewed the rates, select the NZ Post service from the dropdown and click **Create Shipment**.

* * *

After creating the shipment, the plugin sends the request to NZ Post and generates the shipping label. NZ Post generates labels asynchronously; the plugin will automatically poll until the label is confirmed as ready.

* * *

Once the label is ready, click **Print Label** to download and print the shipping label PDF or PNG.

* * *

> Once the plugin generates a shipping label, you can print it directly from the WooCommerce Orders list by clicking the Print Label icon at the end of the corresponding order row.

* * *

### Print NZ Post Return Label

Once an outbound label has been generated for an order, you can generate a return label from the same metabox on the order edit page.

  * Open the order and scroll to the **NZ Post Shipment Label** metabox.
  * Under the existing shipment, select the return service from the dropdown.
  * Click **Generate Return Label**.

* * *

  * Once generated, the return tracking number appears. Click **Print Return Label** to download and print it.

* * *

### Clear Label Data

If you need to remove label data from an order, click the **Clear Data** button in the NZ Post Shipment Label metabox. This removes the label information from WooCommerce only — it does not cancel the shipment with NZ Post.

* * *

**Note:**  
To cancel an actual shipment, contact NZ Post directly. Clear Data only clears the data stored within WooCommerce.

* * *

## 12\. How to Set Up NZ Post International Shipping

If you plan to ship products internationally, configure the required customs settings in the International tab. Go to **WooCommerce > Settings > Shipping > NZ Post > International** tab.

* * *

### Insurance

Enable **Insurance** to include additional cover for international shipments. When enabled, an Insurance Value field becomes available on each product’s Shipping tab so you can specify an insured amount per product. The following international services support additional cover:

  * International – Economy Plus (IECOP) — NZD 250 standard cover
  * International – Economy Plus Thermal (IECOP7) — NZD 250 standard cover
  * International – Courier (ICOU) — NZD 2,000 standard cover
  * International – Courier Thermal (ICOU7) — NZD 2,000 standard cover
  * International – Express (IEXP) — NZD 2,000 standard cover
  * International – Economy Tracked (IECOT) — NZD 250 standard cover

* * *

### Default HS Tariff Code

Use this default Harmonized System (HS) tariff code for products that do not have a product-specific HS code. Enter 6–10 digits. You can use dots or spaces as separators (for example, `1234.56.78.90`), but do not use hyphens.

* * *

### Default Country of Origin

Select the default country where your products are manufactured. This value is sent on international customs forms for products that do not have a country of origin set at the product level. The default is New Zealand (NZ).

* * *

### Nature of Transaction

Select the category of goods that appears on CN22 and CN23 customs forms. Available options:

  * B2C – E-Commerce goods (default)
  * X2B – Returned goods
  * C2C – Gift (non-commercial)
  * B2X – Commercial sample
  * X2X – Documents
  * B2B – Commercial sale of goods
  * X2X – Mixed content
  * X2X – Other

* * *

### Mixed Content Codes

This field appears when X2X – Mixed content is selected as the Nature of Transaction. Select at least one additional transaction code to describe the mix of goods in the shipment. The codes 991 (Mixed content) and 999 (Other) are not permitted here as additional codes.

* * *

### Transaction Description

This field appears when X2X – Other is selected as the Nature of Transaction. Enter a free-text description of the transaction (maximum 120 characters). Required when Other is selected.

* * *

Click **Save Changes**.

* * *

### Print NZ Post International Documents

To print customs forms for international shipments, add a product to the WooCommerce cart and enter an international shipping address.

After placing the order, go to **WooCommerce > Orders**, open the order, and click **Generate Package**.

* * *

Once you generate the package, click **Create Shipment** to create the NZ Post international shipment.

* * *

After you create the shipment, click **Print Label**. The plugin generates the NZ Post shipping label along with the required customs documentation (CN22/CN23), where applicable.

* * *

The customs form includes shipment details such as the sender and recipient information, package contents, declared value, and other information required by customs authorities to process international shipments.

* * *

## 13\. Set Up NZ Post Shipment Tracking

The plugin generates a tracking number with every shipping label. The plugin includes tracking information in the WooCommerce order completion email and displays it on the customer’s My Account page.

Go to **WooCommerce > Settings > Shipping > NZ Post > Tracking** tab.

* * *

### Disable Tracking Notification for Customers

By default, the plugin includes shipment tracking information in the WooCommerce Order Completed email sent to customers. Enable the **Disable Tracking Notification for Customers** option to exclude tracking information from these emails.

* * *

When this option is disabled (default), customers receive an email containing their tracking number and a clickable tracking link once the order is shipped.

* * *

### Hide Tracking in My Account

Enable **Hide Tracking in My Account** to prevent tracking information from appearing on the customer-facing My Account > Orders page. Customers will not see tracking numbers or shipment details in their account order history.

* * *

When this option is disabled (default), customers can access their NZ Post tracking number and tracking link from **_My Account > Orders_ **and open the NZ Post tracking page with a single click.

* * *

### Customise the Tracking Message

You can personalise the tracking information shown to customers using the following fields:

  * **Tracking Message Title:** The heading shown above the tracking section in order completion emails and on the My Account page. The default placeholder is _Shipment Tracking_.
  * **Tracking Message:** The message body sent to customers alongside their tracking number. Use [ID] as a placeholder — it is automatically replaced with the actual tracking number(s) when the email is sent.  
**Default:** _Your order is shipped via NZ Post. To track your shipment(s), please follow the shipment ID(s): [ID]._

* * *

Click **Save Changes**.

* * *

## 14\. Debug Settings

Go to **WooCommerce > Settings > Shipping > NZ Post > Debug** tab.

  * **Debug Mode:** Enable Debug Mode to display detailed API request and response information directly on the Cart and Checkout pages. Use this temporarily to diagnose rate calculation or connectivity issues. Disable it once troubleshooting is complete.
  * **Silent Debug Mode:** Enable Silent Debug Mode to log debug information in the background without displaying anything to customers on the Cart or Checkout pages. This is the preferred option for troubleshooting on a live store. Logs can be reviewed under **WooCommerce > Status > Logs**.

* * *

Click **Save Changes**.

**Note:**  
Disable Debug Mode on your live store once troubleshooting is complete. Leaving it enabled exposes API response data on your frontend pages.

* * *

## Need Help?

If you have any questions about setting up the PH NZ Post Shipping for WooCommerce with Print Label plugin or run into any issues, reach out to the [PluginHive support team](https://www.pluginhive.com/support/). We are happy to help you get everything configured correctly.

[ Previous  How to Set Up PH India Post Shipping for WooCommerce  ](https://www.pluginhive.com/knowledge-base/setting-up-india-post-shipping-for-woocommerce-with-print-label/)
