# Setting Up WooCommerce Shipping Services

**Source:** https://www.pluginhive.com/knowledge-base/setting-up-woocommerce-shipping-services/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Setting Up WooCommerce Shipping Services

The **[WooCommerce Shipping Services](https://www.pluginhive.com/woocommerce-shipping-services/)** plugin streamlines your entire shipping workflow by automating essential tasks right from your WooCommerce dashboard.

With this plugin, you can:

  * Display real-time shipping rates at checkout
  * Purchase postage and print shipping labels
  * Schedule carrier pickups seamlessly
  * Enable comprehensive end-to-end shipment tracking

This setup guide will help you install and configure the plugin step-by-step, so you can start shipping within minutes.

* * *

  * ****Download, Install, and Activate Plugin****
  * **Choose Your Shipping Carrier and Configure Your Account**
    * Connect your Preferred Carrier
    * Configure more Carriers
    * View the added Carriers
    * Manage the shipping Carriers
  * **Setup your Pickup / Store Location**
    * **Verify Your Store Location in WooCommerce**
    * **Manage your Store Address in the Plugin**
  * **Verify the Store Units**
    * WooCommerce Store Settings
    * Plugin Settings
  * **Manage Products within the app**
    * Access products
    * Simple & Variant Products
    * Import Products
    * Force Import Products
    * Bulk Edit Product Details
    * Export & Import CSV
    * Product Page Details
    * Delete Products
  * **Set Up Packaging Methods**
    * Weight-Based Packing
    * Box-Based Packing
      * How does Box Packing Work
    * Stack-Based Packing
    * Quantity-Based Packing
    * Weight & Volume Based Packing
  * **How to Create Shipping Zones**
  * **Shipping Carrier Rates& Services for Checkout and Fulfilment**
    * Shipping Rule Configuration for Label Generation
    * Shipping Rule Configuration for Checkout Rates
  * **Optimising your Shipping and Printing configuration**
    * Add Tax IDs
    * Document Print Settings
    * Print Tax Invoice
    * Order Tracking
    * Order Confirmation Email
    * Customise Shipping Options
  * **Set up Multi-Vendor Shipping**
  * **Manage App Subscriptions**
  * **Understand the Orders Grid**
    * Orders
    * Labels (label batches)
    * Pickup
    * Manifest
    * Tracking
  * **Advanced/ More Actions on the Order Grid**
  * **Display Live Rates at Checkout**
  * **Generate Shipping Labels One by One**
    * Generate Labels One by One with Quick Ship
    * Generate Labels One by One without Quick Ship
  * **Generate Shipping Labels in Bulk**

* * *

## 1\. **Download, Install, and Activate Plugin**

The plugin is available for download on **PluginHive’s**[**WooCommerce Shipping Services**](https://www.pluginhive.com/woocommerce-shipping-services/) page. Go ahead and click on the ‘14 days free trial’ option.

* * *

Once you enter your name, email, phone number and select your country, proceed to click on ‘Start 14 days free trial’. 

* * *

You’ll now get an option to download the plugin upon clicking the ‘**Click Here** ’ link given. 

* * *

**Reference:**   
Please refer to the Installation and License Activation Instructions – [ **How to install and activate the license of a PluginHive WooCommerce Plugin?** ](https://www.pluginhive.com/knowledge-base/how-to-download-install-update-woocommerce-plugin/)

* * *

Once the WooCommerce Shipping Services plugin zip is downloaded to your system, navigate to **Plugins > Add Plugin** page in your WooCommerce store. Click on the **Upload Plugin** option at the top left and choose the WooCommerce Shipping Services zip file you downloaded, and click **Install Now** to install the plugin**.**

* * *

Visit the **Plugin WooCommerce Shipping Services settings** option by navigating to **Plugins > Installed Plugins** and clicking on **Register**.

* * *

After the registration, click on the 

  * **Let’s start Fulfilling** option, as shown below, to access the plugin setup wizard.

* * *

**Note:**   
The **Resync** option refreshes both the Store URL and the associated Email ID.

* * *

**Store setup settings list:**

  * **Realtime Rates****  
**Displays live shipping rates from carriers on the cart and checkout pages.
  * **Debug Mode****  
**Enables debugging information on the cart or checkout pages for troubleshooting.
  * **Silent Debug Mode****  
**Activates debug mode without displaying information on the cart or checkout pages and the logs can be found under**WooCommerce > Status > Logs**.
  * **Local Pickup Location****  
**Displays available local pickup options at checkout.
  * **Tax Calculation****  
**Allows selection of how taxes are applied to shipping rates based on store requirements.
  * **Fallback Rate****  
**Displays a default shipping rate if no live rates are returned by the plugin. The method title remains the same as the service name.
  * **Mark Shipped Orders As****  
**Automatically updates the WooCommerce order status (e.g., pending payment, completed, or draft) once an order is marked as Fulfilled.
  * **Custom Order Status Mapping****  
**Allows mapping of carrier tracking statuses to corresponding WooCommerce order statuses. This list will vary depending on the custom order statuses configured on your store.

**Delete WSS Account and Clear Plugin Data Button****  
**Clears all plugin data and sends a request to delete the WSS account. This action is irreversible.

* * *

Provide your **email address** and **phone number** to help our team assist you effectively during the onboarding and setup process.

* * *

## **Choose the shipping carrier and Configure your account**

The WooCommerce Shipping Services plugin supports direct integration with **over 30** **shipping carriers,** utilising your existing carrier accounts. When you first install the plugin, no carrier is connected by default. 

  * To add a shipping carrier, click on the **Start** option of ‘**Add Shipping Carrier Account** ’.

* * *

**To connect your preferred carrier:**

1\. Select a carrier from the list or use the **Search Bar** to quickly find the one you use.  
Example: If you’re using **USPS via Stamps.com** , type “**USPS Stamps** ” and select it.

2\. Select the carrier name (example: USPS via Stamps) and click the ‘**Add Account** ’ option.

3\. Enter your carrier account credentials (e.g., **User ID** and **Password** for USPS via [**Stamps.com**](http://stamps.com/)).

* * *

**Note:**   
For all carriers, you’ll need to enter the account credentials provided by your shipping provider. Once connected, the plugin will begin fetching live shipping rates and allow label generation.

* * *

4\. Enabling the activation checkbox means your account is set to **production mode**. This ensures that all WooCommerce orders are processed in **live mode** , and the shipping labels you generate are real, ready-to-use labels for actual shipments.

5\. After adding the account details, head to the **Other Details** section to complete any required carrier-specific fields, such as the below for USPS Stamps:

  * **Image Type:** Choose your preferred label format. PDF is widely recommended for easy printing.
  * **Paper Size for PDF:** Select the correct paper size (e.g., A4 or standard 4×6 label format).
  * **Pickup Time:** Enter the earliest time carriers can begin collecting shipments (e.g., 03:00 PM).
  * **Company Close Time:** Specify your business’s closing time (e.g., 06:00 PM) to help carriers plan pickups accordingly.
  * **Package Pickup Point:** Choose where packages will be collected from (e.g., Front Door, Reception, Mail Room, etc.). Pick a visible and accessible location to avoid missed pickups.

  * **Special Instructions for Pickup:** Add any helpful directions such as entry codes, parking info, or a contact person.
  * **Send Package Dimensions:** Ensure this option is enabled. This allows carriers to receive accurate package size details, reducing the chances of surcharges or delivery issues.

6\. Once done, click **Connect & Save** to finalise the setup.

**To Configure more Carrier(s):**

  * Navigate to **☰ Menu > Settings**, and click the **‘➕’ icon** next to Carriers to add another one.

**To View the added Carrier(s):**

  * Navigate to **☰ Menu > Settings**, and click on**Carriers** to see the added carrier(s) below.

**Managing Your Shipping Carriers:**

  * **Edit Carrier Details:** You can revisit any added shipping carrier at any time to update the **Account Information** or **Other Details** as needed.

**Delete Carrier:** If a shipping carrier is no longer in use, you can remove and archive it from your list of configured carriers (ensure that the account is not active)

* * *

## **Set up your Pickup / Store Address**

Proper store location configuration ensures accurate rate calculation, smooth label generation, and successful carrier pickups. Here’s how you can verify and manage your store address effectively using the plugin.

### **Verifying Your Store Address in WooCommerce**

Once you install and activate the **WooCommerce Shipping Services** plugin, your primary store location is automatically set as the**Store Address** that is in **WooCommerce > Settings** **> General**. This **address is critical** because it is used to:

  * Calculate accurate shipping rates
  * Schedule carrier pickups

* * *

**Tip:**   
Ensure your address is accurate—incorrect details can lead to inaccurate shipping rates and pickups being scheduled at the wrong location.

* * *

* * *

### **Accessing the Store Address Settings in the plugin**

1\. From your WordPress admin panel, navigate to the **Shipping** option to open the WooCommerce Shipping Services plugin.  
2\. On the plugin’s landing page, locate the **☰ icon (hamburger menu)** at the top left corner.  
3\. Click the icon to open the navigation menu. You’ll see various setup options listed.

4\. Use the **Search bar** at the top of the menu for quick access.

  * For example, type **“Address”** and it will highlight the full path to the setting:  
**☰ Menu > Settings > Address > US Store**

This search feature helps you find settings even if you’re not sure where to look.

### **Manage your Store Address in the plugin**

  * **Modify Location(s):** To update the default address that is pulled from your WooCommerce store settings, you will need to navigate to **☰ Menu > Settings > Address > ‘your store location’**(example: US Store, as shown below)**.**
  * **Add Location(s):** You can **add multiple store locations** based on your business needs by clicking on the plus(➕) icon next to ‘**Address** ’.
  * **Delete Location(s):** You can also **delete store locations** if they are no longer in use by clicking on the **Delete option** at the top right.

* * *

**Tip:**   
If you’re only shipping from one or two specific locations, we recommend removing any unused addresses to keep your shipping setup clear and efficient.

* * *

**Note:**   
Only **active store locations** will be considered for shipping rate calculations and label generation.

* * *

The address provided here serves as both:

  1. The **pickup location** for the courier agents
  2. The **warehouse or shipping origin** is printed on the shipping labels.

**From Address – Fields Overview:**

  * **Address Name** : This is just a label to help you identify the address in the plugin (like “Main Warehouse” or “Brooklyn Office”). It’s not shared with the carrier or printed on the shipping label.
  * **Person Name** : The name of the individual responsible for shipments from this location.
  * **Company Name** : The name of your business or store.
  * **Phone Number** : A contact number for pickup agents or carriers to reach out in case of pickup issues or delivery clarifications.
  * **Email ID** : Used for communication regarding shipping updates, failed pickups, or any required verification.
  * **Street Address 1, 2 & 3**: The complete street address, including building number, street name, floor, suite, or any additional location details.
  * **City** : The city where the pickup location is based.
  * **Postal Code** : The ZIP or postal code for the pickup address.
  * **Country** : The country where this address is located.
  * **Tax ID** : The registered tax identification number for your business, required for invoicing and customs (especially for international shipping).
  * **Tax ID Type** : Specifies the type of tax identification provided (e.g., GSTIN, VAT, EIN), depending on your country’s tax structure.
  * **Signature Image** : Upload the shipper’s signature as a JPEG, JPG, PNG, or GIF file (max size: 950 KB).

* * *

**Note:**   
Provide the contact details of the person in your team who manages shipping. These details help carriers coordinate pickups or resolve any delivery issues. The **Person Name** will be printed on the shipping label, so if you prefer not to display your personal name, you can enter a name like your brand name instead. The **Phone Number** and **Email ID** are used only for communication purposes and will not appear on the label.   
  
Make sure the **pickup address** entered here exactly matches the one you’ve registered with your carrier. Some carriers have strict requirements and may reject pickups or label generation if the address doesn’t match the one in their system.

* * *

* * *

## **Verify the Store Units For Accurate Rates & Labels**

To generate accurate shipping rates and shipping labels, it’s essential to make sure that both your **WooCommerce store** and the **WooCommerce Shipping Services plugin** are using the correct measurement units.

Here’s what you need to review:

### **WooCommerce Store Settings:**

On your WordPress admin panel, go to **WooCommerce > Settings > Products**. Under **Measurements** , confirm the following:

  * **Weight Unit** (e.g., kg/ g/ lbs/ oz)
  * **Dimensions Unit** (e.g., m/ cm/ mm/ in/ yd)

Make sure it matches the standards of the country you’re shipping from. These values directly affect how shipping rates are calculated and how labels are generated.

### **Plugin Settings:**

In the plugin, go to **☰ Menu > Settings > Stores**, and check:

  * **Weight and Dimensions Unit:** Ensure it aligns with your store’s measurement unit system**.**
  * **Default Package Details:** Set a **Default Weight** and **Default Dimensions** to speed up order processing and label generation.

Ensure the following additional fields are reviewed and configured appropriately as well:

  * **Store Currency:** Defines the currency used for transactions in your store (e.g., US Dollar).
  * **Basic Authentication:** If your store has an additional layer of password protection that restricts access to the store’s admin interface, then please enable this option and configure the **_Username_** and **_Password_** accordingly.
  * **Last Manual Order Import Time:** Shows the timestamp starting from when the orders were last manually synced up to the current date.
  * **Last Manual Product Import Time:** Shows the timestamp starting from when the products were last manually synced up to the current date.
  * **Brand Logo:** Upload your store’s logo to personalise shipping labels and documents.
  * **Branding Message:** Custom note or message that appears on shipping labels or customer-facing documents.

* * *

**Note:**   
The plugin automatically pulls all the store details from your WooCommerce store when first installed. However, if the product measurement units have been updated after installation, use the **‘Re-Sync Store’** option to reflect all the changes made.

* * *

* * *

## **Manage your Products within the plugin**

The Products section in the **WooCommerce Shipping Services plugin** allows you to quickly set up, manage, and update your product shipping details.

**Things to do before: Add Product Weight and Dimensions in WooCommerce (Recommended)**

WooCommerce lets you add weight and dimensions for each of your products directly in your store. These details are automatically picked up by the shipping plugin.

* * *

**Note:**   
If you make any changes to the weight or dimensions within the plugin, they will not sync back to your WooCommerce store. It’s recommended to manage product measurements from **WooCommerce** itself for consistency.

* * *

#### **Steps to Add Weight and Dimensions:**

  1. Go to your WordPress dashboard.
  2. Navigate to **Products > All Products**.
  3. Click on the product you want to update.
  4. Scroll to the **Product Data** section and click on the **Shipping** tab.
  5. Enter the **weight** and **dimensions** of the product.
  6. Save your changes.

This ensures accurate shipping rates based on the product’s size and weight.

### **Accessing Your Products**

  * Navigate to **☰****Menu > Products > All Products**.
  * **All WooCommerce store products sync automatically, so no manual steps are required.**
  * Any changes you make to products in WooCommerce (like name, weight, etc) will reflect in the plugin.

* * *

### **Working with Simple & Variant Products**

  * The plugin supports both simple and variant products.
  * For products with variants, click the ➕ icon next to a product to expand and view all variants with their shipping details.

* * *

### **Import Products**

If the product hasn’t been imported automatically into the plugin from WooCommerce, although this is unlikely, here’s what you should do.

**Steps to Manually Import Products:**

  1. In the **All Products** section, click **Import Products**.
  2. The plugin will instantly fetch all your latest WooCommerce products.

**When to use Import Products:**

  * You’ve recently added products in WooCommerce
  * You’ve modified some existing products in WooCommerce

This quick manual sync updates the product list immediately, ensuring all the WooCommerce products are available and ready for configuration in the plugin, without waiting for the next auto-update.

### **Force Import Product**

The plugin typically auto-syncs products from your WooCommerce store. If some products aren’t updated, start by using the **Import Products** option. If the issue persists, use the **Force Import** feature to fetch the latest product details like names, weights, and dimensions, ensuring everything stays up to date in the plugin.

**Here’s how to use it:**

  * Select the products you want to update.
  * Click on the **Force Import** option.

The plugin will cross-check your selected products with your WooCommerce store products and fetch any missing or updated details to ensure everything is synchronised.

* * *

### **Search and Filter Options**

Looking for a specific product? Use the **search bar** to quickly find it. You can also apply **filters** to narrow down the list and manage products more efficiently.

These filters are based on your product configurations, if you’ve set any of the options below for a product, you can use them to filter and view only those specific items:

  * Shipping class (product groups)
  * Alcohol presence
  * Dry ice
  * Dangerous goods
  * Shipping required
  * Delivery signature required

Filters help you easily organise and manage large product catalogues based on key shipping-related attributes.

* * *

### **Bulk Edit Product Details**

Want to update packaging details for multiple items?

  * Select the required products from the **All Products** page.
  * Click on the **Edit Product** option. 
  * Enter the **length, width, and height** , and these values will be applied to all selected products (perfect for items with similar packaging).

* * *

### **CSV Export & Import for Bulk Updates**

If your products have different sizes, customs information, or other unique details, the **Export CSV** and **Import CSV** options help you make bulk updates quickly and efficiently.

**How Export & Import CSV Works?**

  1. In the **All Products** page, click the **Export CSV** button to download a file with your current product data.
  2. Open the file and update the necessary fields, such as:
     * Length, Width, Height
     * Harmonisation (HS) code
     * Country and state of origin
     * Declared value
     * Delivery signature requirements
     * Custom product descriptions
  3. After editing, return to the same page and click **Import CSV**.
  4. A pop-up will appear where you can upload your updated file. A **sample CSV** and **format guide** are also available to ensure everything is structured correctly.

### **Bulk Import Page**

After using the **Import CSV** option or clicking on **Import Product** , you will be redirected to the **Bulk Import** page. This page helps you monitor the progress and results of your import.

You can track:

  * Total number of products that are completed or still pending
  * Batch status, such as In Progress, Batch Complete, or Failed
  * Any errors, with specific reasons provided, to help you take corrective action

This helps you take the right action quickly and ensure all your product data is complete and ready for shipping.

* * *

### **Exploring the Product Detail Page**

Once you’ve located a product, clicking on its name opens a detailed page where you can edit its **shipping attributes** , **customs information** , and **optional delivery services**.

**Shipping Section**

In this section, you can view and manage the physical and shipping-related details of the product:

  * **Weight** : The product’s actual weight is used to calculate shipping rates.
  * **Length, Width, Height** : Dimensions of the product for volumetric weight and packaging decisions.
  * **Custom Value** : The declared value of the product, often used for customs and insurance.
  * **Freight Class** : Classification used for freight shipments, based on density and handling requirements.
  * **Exclude From Shipping** : If enabled, the product will be excluded from shipping.
  * **Pre-Packed Product:**
    * This means the product is already packed and ready to be shipped on its own.
    * It will be shipped separately, not grouped with other items.
    * This setting overrides your general packaging rules.  
**_Example:_****_  
_**_If a customer orders three items, one marked as pre-packed and two that are not, the pre-packed item will be shipped separately, while the other two will be packed and shipped together._
  * **Document** : Marks the product as a document, not a physical item, for applicable carriers.

Everything you need to prepare this item for accurate shipping is just a few clicks away.

**Customs Section**

This section is important when shipping internationally, as it ensures your products clear customs smoothly. Here’s what you can configure:

  * **Harmonisation Code (mandatory):** A 6-digit code used by customs to classify the product. Required for international shipments to calculate duties and taxes accurately.
  * **Import Commodity Code:** Used in some countries for additional classification of goods during import.
  * **Country of Manufacture (mandatory):** Specifies where the product was made; essential for customs and trade compliance.
  * **State of Manufacture:** Adds more detail to the origin of the product, especially useful for domestic classification.
  * **District of Manufacture:** Helps identify the specific production area when required by certain trade agreements or regulations.
  * **Custom Description:** By default, the product name is used, but you can enter a more detailed description if it helps customs better understand the item.

These details ensure your product clears customs without delays or compliance issues.

**Special Services**

Need delivery confirmation for this product? Just head to this section and enable the Delivery Confirmation option. Choose between options like Adult Signature Required, Direct Signature, and more, based on what’s required for that item.

**Dry Ice**

This option is used when your shipment contains dry ice (solid carbon dioxide), commonly used for preserving perishable items like food or medical supplies.

  * Specify the weight of the dry ice and the units used (kgs/lbs)

**Dangerous Goods**

Enable this option if your shipment includes hazardous materials such as batteries, chemicals, or flammable substances.

When enabled:

  * **UN Code** : Enter the UN number for the material (e.g., _UN3480_ for lithium-ion batteries).
  * **Technical Name** : Specify the technical name of the substance (e.g., _Acetal_).
  * **Class Division** : Input the relevant hazard classification (e.g., _3_ for flammable liquids).
  * **Packaging Group** : Select the appropriate packaging group (e.g., _I, II, III, or Nil_ based on the substance).

This configuration ensures your shipment is handled safely, complies with legal requirements, and meets carrier documentation or restriction guidelines.

**Alcohol**

Enable this option if the shipment contains alcoholic beverages.

  * Requires adult signature on delivery.
  * Subject to specific carrier and regional regulations. Commonly used for shipping wine, spirits, and similar products.

### **Deleting Products from the Plugin**

Need to remove a product from the plugin view? 

  * In the All Products page, select the product and click **Delete**. 

This removes it only from the plugin, not from your actual store.

With these simple steps, you’re now ready to manage your product catalogue smoothly and confidently!

## **Set Up Packaging Methods**

In the plugin, **Packaging** refers to how your products are arranged into parcels or boxes for shipment. Configuring packaging correctly enables the plugin to **calculate accurate shipping rates, print labels** , and ensure the **carrier receives the correct weight and dimensions**.

Proper packaging setup also prevents carrier reweighing surcharges and streamlines your shipping workflow.To configure packaging, navigate to **☰********Menu > ****Plugin Settings > Shipping > Packaging** and select your preferred method.

**Available Packaging Methods**

The plugin offers five distinct packing strategies:

  1. Weight-Based Packing
  2. Box Packing
  3. Stack Packing
  4. Quantity-Based Packing
  5. Weight and Volume-Based Packing

* * *

**Note:**

  * Check the packaging weight and dimension units in the **Packaging** section. These units will reflect in the order summary, so it is important to configure them correctly.
  * If you’re using carrier-provided boxes, you can easily set them up within the plugin as well.

* * *

### **1\. Weight-Based Packing** __

This method considers the **total product weight** for packing. You can define a **maximum weight limit** for each box, and the plugin will automatically pack products accordingly. You can set up the**maximum weight limit** depending on the products you have and how you would like to ship them.

If the total weight of items exceeds this limit, the system automatically starts packing the remaining items into a new box.

  * **_Max weight:_**_This sets the maximum weight allowed per package or box. It primarily determines how many packages are created for an order._
  * **_Use Volumetric Weight in Package Generation:_**_This option allows shipping rates to be calculated based on the space a package occupies (volumetric weight), rather than just its actual weight. Since carriers charge based on whichever is greater, actual or volumetric weight, enabling this ensures more accurate shipping costs for larger, lightweight items._

Under the **Advanced Configuration** , you can:

  1. **_Apply Box Weight_****:**_This setting factors in the weight of the empty box and any extra packing materials when calculating the total shipping weight. This helps get more accurate shipping rates, since carriers charge based on the full weight of what’s being shipped, not just the products_.
  2. **_Apply Max Quantity:_**_When this option is enabled, it limits the number of items that can be packed into one box, based not only on quantity but also considering the max weight setting._

Example: If your box can hold up to 10 kg and the total order weighs 12 kg.  
The plugin will split it into 2 boxes.

  * 1 box with 10 kg
  * 1 box with 2 kg 

Two packages will be created based on the maximum weight that is set.

* * *

### **2\. Box Packing**

This method of packing is useful for businesses using custom or carrier-provided boxes.The plugin considers the **box dimensions, weight, and volume** to determine how products are packed.

* * *

**Note:**

  * To use the **box packing** method, make sure you have entered the product dimensions under the **Products** section.

* * *

The plugin automatically chooses the right box and decides how many items to pack in each one based on the size and weight limits you set. This helps ensure accurate shipping rates and correct label generation.

Box Packing is ideal if:

  * You use custom-sized boxes for shipping.
  * You rely on carrier-provided boxes (example: Stamps USPS, FedEx, UPS, Australia Post, UPS, Canada Post, Puralotor).
  * Your products have a fixed size (example: nuts, bolts, or automobile parts) where dimensions matter for accurate packaging and shipping costs.

* * *

**Note:**   
Under **Box Packing** settings, you’ll see two optional features that can be enabled based on your packaging needs:

  * **Use Volumetric Weight in Package Generation:** This option allows shipping rates to be calculated based on the space a package occupies (volumetric weight), rather than just its actual weight. Since carriers charge based on whichever is greater—actual or volumetric weight—enabling this ensures more accurate shipping costs for larger, lightweight items. 
  * **Do You Stack the Products in Boxes?:** Enable this if your products can be stacked vertically within a box (like books or flat packets). This helps optimize space during packing. If your items are better placed side by side or can’t be safely stacked, you can leave this option disabled. 

* * *

**Steps to Add a Custom Box:**

  1. Click **Add Box** and**** select **Add Custom Box**.
  2. In the **Add Package** section, enter a custom name for the box.
  3. Input the inner and outer dimensions **(length x width x height)**.
  4. Enter the **empty box weight** and the **maximum weight capacity** of the box.
  5. Review all details and click **Confirm**.

Your custom box will now be added.

**Steps to Add Carrier-Integrated Boxes (e.g., Stamps USPS Boxes):**

  1. Click **Add Box** and Select **Add Custom Box**
  2. Choose your preferred carrier boxes from the list
  3. Click on **Add** to add the box of your choice and **Close** to collapse the view.
  4. Click **Save** once you’ve added the desired boxes

You’ll find two important options to enable under **Box Packing** :

  1. **Enable “Use Volumetric Weight in Package Generation”****  
**Turn on this option if you want the system to consider**volumetric weight** (the space a package occupies) instead of just the actual weight.  

  2. **Enable “Do You Stack the Products in Boxes?”**  
Select this option if your products can be safely stacked vertically inside a box (like books, cartons, or packets). 

#### **How Does Box Packing Work?**

Suppose you’ve added a custom box with dimensions **10×10×10 cm** and a **maximum weight limit of 5 kg**. Now, you receive an order for a product weighing **3 kg** with dimensions **3×3×3 cm**. Here’s how the plugin processes it:

  * **Weight Check** : The product weighs less than the box’s 5 kg limit, so it passes the weight check.
  * **Volume Check** : The product’s volume is 27 cm³ (3×3×3), and the box volume is 1000 cm³, so it fits comfortably.
  * **Dimension Fit** : The plugin checks if the product’s longest side fits within the box dimensions; in this case, it does.
  * **Final Fit Check** : It ensures both the total weight and volume are within the box’s limits.
  * **Sorting** : The plugin sorts products and boxes by treating the longest side as the length for accurate packing.
  * **Box Selection** : Based on all checks, the plugin automatically selects the most suitable box for shipping.

**Refer to the**[**Box Packing Strategy for eCommerce platforms**](https://www.youtube.com/watch?v=Cdt2hqF6wRU)**for more information on Box Packing.**

### **3\. Stack Packing**

This method packs your products **vertically based on their height**. The plugin stacks products one over another inside the box using this configuration. You can configure:

  * Box dimensions.
  * Buffer Height (optional) – extra vertical space to prevent items from being compressed.

Example: If your product **height is 10 cm** , and you add a 2 cm **buffer height** , the **box should be****12 cm** tall to fit the item comfortably.

* * *

### **4\. Quantity-based packing**

This method relies solely on the **number of units** per box. It is not based on their size, weight, or shape.

For example, if you set **4 items per box** and someone **orders 10 items** , the system will pack them into **3 boxes: 4, 4, and 2 items**.

It is best used when:

  * You have a fixed number of items that fit in each box.
  * Products are lightweight or uniform in size.

* * *

### **5\. Weight- and Volume-based Packing**

This advanced method takes into account **both the product’s weight and volume**. It’s ideal for shipping items that are either:

  * Lightweight but bulky (e.g., cotton shirts)
  * Heavy but compact (e.g., ceramic mugs)

The plugin balances both factors to determine the most efficient packaging strategy.

Overall, choosing the right packing method in the **WooCommerce Shipping Services plugin** ensures **accurate rates, optimised packaging,** and**smoother shipping operations**.

* * *

## **How to Create Shipping Zones?**

Shipping zones allow you to customise shipping rates, delivery times, and carrier services based on where your customers are located. This helps you offer accurate and location-specific shipping options.

While WooCommerce lets you create shipping zones in its settings, **those zones do not carry over to the plugin**. If you want to set up shipping rules based on zones within the plugin, you’ll need to create them directly in the plugin settings.

* * *

**Note:**

  * The plugin does not rely on WooCommerce’s shipping zones. Shipping rates will still appear at checkout even if no zones are set up in WooCommerce.
  * Creating zones within the plugin is optional. It’s only recommended if you want more control over shipping to specific regions or markets.

* * *

The **WooCommerce Shipping Services plugin** offers you to**** optionally define custom zones based on:

  * Country
  * Country + State
  * Specific Postal Codes

These zones can then be used to map it with the shipping rules and customise it as needed.To set up the custom shipping zones, navigate to **☰ Menu > ****Plugin Settings > Shipping > Shipping Zones > Add Zone**.

Shipping zones can be defined based on one or a combination of the following criteria: **Country** , **State** , and **Postal Code** , as shown in the image below.

#### **Zone Fields Explained:**

  * **Zone Name** : Enter a meaningful name for your zone such as _Domestic_ , _US_ , or _Florida Zone_ based on your requirement.
  * **Activate** : Check this box to enable or disable the zone.
  * **Match All Conditions** : This setting controls how the selected zone criteria are evaluated.
    * **Enabled** : All specified conditions must be true for the zone to apply (AND logic).
    * **Disabled** : The zone will apply if **any one** of the selected conditions matches (_OR logic_).

#### **Choose Shipping Zone Criteria:**

You can define the zone using the following criteria, selecting the condition type as **“Equal To”** or **“Not Equal To”** based on your needs:

  * **Country** : Select from the list of available countries.
  * **Country – State** : Choose a specific state within a selected country.
  * **Postal Code:** You can enter one or more complete postal codes. To add multiple codes at once, separate them with commas in the input field (e.g., 90001,90002,90003) and press Enter. All the codes will be added automatically.

* * *

**Note:**

  * Wildcard entries such as **90*** or postal code ranges like **10001–90009** are not supported.

* * *

* * *

## **Set Up Shipping Carrier Rates & Services for Checkout and Fulfilment**

Setting up shipping carrier rates and services ensures that your customers see accurate shipping costs at checkout and that you can generate the right labels for order fulfilment. 

The **WooCommerce Shipping Services plugin** offers two sets of automation rules: 

  1. **Automating Label Generation:** Automatically applies shipping actions during label creation.
  2. **Customising Checkout Rates:** Automatically display tailored shipping rates during checkout using advanced rule sets.
     * **Request Log –** To view detailed records of rate calculations for each checkout transaction.
     * **Local Pickup Location Request Log –** To track and manage customer selections of Hold-at-Location services (e.g., for FedEx, PostNord).
     * **Shipping Classes –** Group similar products under one shipping category for better rate and carrier control.
     * **Rate Automation Enhancements –** Additional rule options that enhance how rates are displayed during checkout.
     * **Carrier Service Customisation –** To customise how carrier names appear to customers at checkout.
     * **Advanced Settings –** To exclude specific products from rate calculations or include landed cost in DHL Express quotes.

* * *

### **Shipping Rule Configuration for Label Generation**

The automation rules under this section are applied during the label generation process. Once a shipping carrier is integrated, **the plugin, by default, creates the required rules to streamline how shipping labels are generated.**

To set up the rules: Navigate to**Plugin Settings > Automation > Setup. **By default, there will be an automation rule created once you have integrated the shipping carrier.

  * Click on the**Edit** option to edit the rule
  * Click on the **Add New** option to add a new rule.

In the Setup Automation rules, there are two sections, based on which the rules can be created and used for label generation:

  1. **Automation Criteria**
  2. **Action Details**

* * *

**1\. Automation Criteria**

The following are the Criteria based on which the automation rule can be created.

  * **Any** – Applies rates to all orders, regardless of conditions.
  * **Zone** – Applies rules based on specific shipping zones.
  * **Quantity** – Applicable based on the product quantities in the order.
  * **Total Weight** – Applicable when the total order weight meets defined conditions.
  * **Price** – Applicable based on certain order price conditions.
  * **Vendor –** Select the vendor you want to set up with their shipping carrier account and shipping location to generate the shipping label.
  * **Time** – Applies rates based on the time the order was created.
  * **Total Weight Range** – Applicable based on the specific order weight range
  * **Total Price Range** – Applicable based on the specific order price range
  * **Shipping Method** – Used to map the custom shipping options, such as – flat rates, free shipping to the specific carrier services.

* * *

**2\. Action Details**

The following are the **Action Details** where the carrier services, special services and other necessary actions can be configured.

**Carrier & Package Configuration **

  * **Add Carrier Service** – Select preferred carrier and shipping services for label generation
  * **Set Carrier Service** – When a rule is configured with the **Set Carrier Service** option and the order matches the rule’s conditions, all other shipping rules are overridden by it.
  * **Set Package Dimensions** – Override any pre-selected package dimensions with the values configured here
  * **Set Package Weight** – Override any pre-selected package weight with the values configured here
  * **Adjust Package Weight** – Add a percentage to the actual weight; the adjusted weight will be used for label generation

**Address Configuration**

  * **Set Shipping From Address** – Set a default origin address when multiple addresses are configured
  * **Display Different From Address on Label** – Show a different address on the label instead of the actual ship-from address.
  * **Set Sold to Address** – Display a “Sold To” address on UPS labels
  * **Map Order Meta Fields to Shipping Address** – Map order meta fields to the shipping address using the Prefix and Meta Key.

**Shipping Preferences**

  * **Add Insurance/Extra Cover** – Providing Insurance to the label-generated orders
  * **Add Delivery Confirmation** – Providing Signature Confirmation (Normal or Adult Signature) for the label generated orders
  * **Enable Auto-Generate Label** – Automatically generate shipping labels when orders are imported
  * **Enable Saturday Delivery** – Automatically apply Saturday delivery for UPS orders
  * **Enable Auto Address Correction** – Automatically correct shipping addresses during label generation
  * **Not to Ship** – Automatically move unshippable orders to the “Not to Ship” section

**Carrier-Specific Special Services**

  * **Add DHL Special Services** – Enable options like Saturday Delivery, Direct Signature, No Signature Required, and Paperless Trade (PLT)
  * **Add DHL Freight Sweden Special Services** – Enable Doorstep Delivery
  * **Add Aramex MyFastway Special Services (Domestic)** – Enable Signature Required, Authority to Leave, and Standard Shipping (Domestic only)
  * **Add Aramex Special Services** – Enable services like First Delivery, First Domicile, Hold for Pickup, Noon Delivery, and Signature.
  * **Add Canada Post Special Services (Domestic)** – Enable services like Proof of Age (18/19), Card for Pickup, Do Not Safe Drop, and Leave at Door (Domestic only)
  * **Add Canpar Special Services** – Enable Saturday Delivery, Extra Care, No Signature, and other delivery options.
  * **Add New Zealand Post Special Services (Domestic)** – Enable specific services for domestic orders.
  * **Set Default Service Point for PostNord** – Choose one PostNord service point as the default shipping location. When a carrier service that supports service points is selected, this setting will automatically apply. This means all shipments will be sent there, no matter the customer’s address.
  * **Add XPO Logistics Special Services** – Enable applicable special services for XPO Logistics orders.

**Third-Party & Billing Options (UPS)**

  * **Third Party Shipment Charges Payer (UPS)** – Set a third-party payer by providing the account number and address.
  * **Duties and Taxes Payer (UPS)** – Define the payer for duties and taxes as either the sender or third party.

* * *

### **Shipping Rule Configuration for Checkout Rates**

This section in the plugin settings consists of the following options related to the checkout rates.

### **Request Log :**

The Request Log section helps you track all checkout rate transactions, where rate log IDs get created for each transaction. You can find the logs by navigating to **☰ Menu > ****Plugin Settings > Shipping Rates > Request Log.**

Click on one of the logs’ **Info icon (i)** to land on the **Request Summary** page.

On the **Request Summary** page, you’ll see key shipment details including the **Shipping To** and **Shipping From** addresses, a summary of the **Items and Packaging** , and an **Automation Summary** that confirms which carrier services were successfully displayed at checkout.

For more details, refer to the section on – [**Understanding the Request Log Summary**](https://docs.google.com/document/d/1rRBS9yL_JYDHjOc91xLBRseYisUC1bJqmu6nJc9FRPo/edit?tab=t.ld78jvd8xlfv#bookmark=id.q77cc56ye3l3)

* * *

### **Local Pickup Location Request Log:******

This section provides details of the transaction made at checkout by selecting a **Hold at Location/Service Point** , and is applicable only for **FedEx** and **PostNord** carriers.

Below are the images showing the path to view the transaction details of the **FedEx Hold at Location transaction**.

* * *

**Note:**

  * **USPS** does not support this feature.

* * *

**How “Hold at Location” Works:**

  * When a customer adds a product to the cart, a “**Hold at Location** ” section appears on the cart page.
  * The customer must enter their **country** and **postal code**.
  * Based on the input, the **nearest pickup location** will be displayed automatically.

After the order is placed, the transaction details can be found under **Local Pickup Location Request Log** in the plugin.

### **Shipping Class:**

A **product shipping class** is a category used to group products with similar shipping requirements, helping to apply specific shipping rates or rules more efficiently during checkout. It simplifies rate calculations based on size, weight, or shipping method.

**Example:** If you sell both mugs and furniture on your WooCommerce store, you can assign:

  * **“Fragile Items”** shipping class to mugs
  * **“Bulky Items”** shipping class for furniture

Using the **WooCommerce Shipping Services plugin** , different shipping rules can be configured:

  * Mugs (Fragile Items) shipped using **USPS** with protective packaging.
  * Furniture (Bulky Items) shipped using **FedEx Freight** with palletised handling.

This setup ensures accurate rate calculation and carrier selection tailored to the **product type**.

To Add a Shipping Class in the plugin –

**Configure the Shipping Class(s) in WooCommerce Settings:**

  * In the WordPress admin panel, navigate to **WooCommerce > Settings > Shipping > Classes**, click on **Add Shipping Class** and**** add all the required details about the shipping class you want to create.

**Add the Shipping Class created to the product:**

In the WordPress admin panel, navigate to **Products > All Products**, click on the product you want to add the shipping class to, go to **Product Data > Shipping** and add the Shipping Class that you created from the drop-down.

**Configure the Shipping Class(s) in the plugin:**

Navigate to **☰ Menu > Plugin Settings > Shipping Rates > Shipping Class > Sync Shipping Class, **and**** the shipping class assigned in your WooCommerce store directly gets imported.

### **Rate Automation:**

Shipping rules for displaying rates at checkout are added by default when a carrier is connected. In this section, you can add the shipping rate automation rules by navigating to**☰ Menu > Plugin Settings > Shipping Rates > Rate Automation.**

These rate automation rules ensure accurate shipping rates are shown to customers based on specific conditions during checkout:

  1. **Automation Criteria**
  2. **Action Details**

The configuration options are largely the same as those in the **Automating Label Generation** section, with a few additional features specific to **Rate Automation** , highlighted below.

**1\. Automation Criteria:**

**Product Shipping Class** – This helps in showing carrier service rates at checkout for a particular product type that is available in the shipping class created.

**2\. Action Details**

#### **Shipping Rate Configuration**

  * **Add Flat Rate –** This lets you add extra fees, give discounts, or offer free shipping on top of the regular shipping cost.
  * **Add Flat Rate Quantity –** This lets you add extra fees, give discounts, or offer free shipping on top of the regular shipping cost, based on how many products are in the order.
  * **Adjust Shipment Price** – Helps in adding a Handling Fee or providing a Discount to the actual Shipping Rate
  * **Adjust Shipment Price Based on Order Cost** – Helps in adding a Handling Fee or providing a Discount, based on the Order Cost, to the actual Shipping Rate

### **Carrier Services** : 

In this section, you have a provision to change the **display name of the carrier services** and show the updated name on the **checkout page**. To add a custom carrier service name, navigate to:

**☰ Menu > Plugin Settings > Shipping Rates > Carrier Services**

Add the **name** that you want to display in the checkout next to the service name you prefer.

You can see the customised service name for **USPS Ground Advantage** as **USPS Standard Shipping** displayed on the checkout page.

### **Advanced Settings**

This section includes the advanced settings of the plugin. To configure any advanced options available, navigate to: **☰ Menu > Plugin Settings > Shipping Rates > Advanced. **In this section, you have two main options:

  * **Skip Products from Rate Calculation** – Exclude specific products from the shipping rate display (specifically for the products available in different shipping classes).
  * **Multi-Vendor –** Lets you prevent orders from being split by vendor during shipping rate calculation. Enable this if you want to charge a single combined shipping rate for products from multiple vendors instead of calculating shipping separately for each.
  * **Add Landed Cost (DHL Express)** – Include customs and handling estimates in checkout quotes.

* * *

## **Optimise Shipping and Printing Configurations**

Use this section to set up your primary **shipping, label printing, tracking,** and**tax configurations**. It forms the foundation of your shipping workflow and helps streamline daily operations. To find the general settings, navigate to:**☰ Menu > Plugin Settings > General Settings**.

This portion contains the following:

  * Tax IDs
  * Print Settings 
  * Tax Invoice
  * Tracking 
  * Email 
  * Shipping

### **Add Tax IDs**

You can use this section to set up Tax IDs and add the **type of tax, its value, origin, and destination** based on your country’s rules. This feature is available only for PostNord, Sendle, and Amazon Shipping.

**Available Tax types:**

  1. **EORI Number** :  
A unique number required for importing/exporting goods to/from the UK or EU.
  2. **VAT on E-commerce** :  
Value Added Tax (VAT) that sellers must collect and pay for online sales, especially in cross-border sales.
  3. **Import One Stop Shop (IOSS)** :  
A system used in the EU that simplifies online sellers to report and pay VAT.
  4. **GST Registration Number** :  
Used in regions like India and Australia for Goods and Services Tax.
  5. **Importer Code** :  
A code assigned to businesses/ individuals who regularly import goods, for customs tracking.
  6. **Tax Code** :  
A set of numbers and letters used by governments to calculate how much tax a person/ business needs to pay.

* * *

### **Document – Print Settings**

In this section, you can set up what documents need to be printed. Choose which documents to print for each order and how many copies you want. If you turn on all the options here, then clicking “**Download All Documents** ” will print all the selected documents together.

### **1\. The documents that can be printed**

  * **Label:** A label is a document with shipping details that is attached to a package for delivery.
  * **Reference:** A reference is a custom note or identifier added to a shipment to help track or recognise the order.
  * **Commercial invoice:** A commercial invoice is a document that shows details of items being shipped internationally, used for customs clearance.
  * **T &C:** T&C stands for Terms and Conditions**,** which are the rules and guidelines that users must agree to follow when using a service or product.
  * **Picklist:** A picklist is a document or list used to identify and gather items from inventory for order fulfilment.
  * **COD Label:** A COD (Cash on Delivery) label is a shipping label that indicates the payment for the goods will be collected upon delivery.
  * **COD Reference:** A COD Reference is a unique identifier used to track and manage Cash on Delivery payments for a specific shipment.
  * **Tax Invoice:** A tax invoice is a document issued by a seller to a buyer, detailing the goods or services provided and the taxes charged on them.
  * **Packing Slip:** A packing slip is a document that lists the items included in a shipment, used to verify the contents of a package. 

**2\. Samples**  
The **Samples** option is to print sample labels by selecting the carrier and available format or sizes.

### **3\. Preview**

The **Print Preview** option lets you preview shipping documents for **2 selected orders** before printing. This helps you check the **layout** and**details** (like labels and invoices) to make sure everything looks right before you print or download them.

### **4\. Touchless Print Settings**

With **Touchless Printing** , you can print shipping labels automatically using your printer. Once set up, labels print instantly, no clicks needed, making order fulfilment faster and easier.  
You can reach out to the [**support team at PluginHive**](https://www.pluginhive.com/support/) for more details.

* * *

### Print Tax Invoice

A **tax invoice** is an official document that outlines the details of a sale, including product information, tax amounts, seller and buyer details. It helps customers claim tax credits and is essential for business records.

You can choose an **Order Invoice Template** that best fits your needs. You also have the option to include your **digital signature** , which will appear on the invoice.

#### Available Invoice Templates:

You can customise your tax invoice in the following formats:

  * **4×6** – Compact invoice, ideal for thermal printers and small packages.
  * **Large** – Full-sized invoice, suitable for detailed information and A4 printing.
  * **4×6 with Taxes** – Small invoice that includes tax details.
  * **International Invoice (India only)** – Meets FedEx and DHL international shipping requirements for Indian merchants.
  * **Custom Tax Invoice** – Fully customisable format that can be tailored to your brand and business needs.

**Customising a Tax Invoice**

Customising your tax invoice helps align it with your brand, enhances professionalism, and improves customer experience. It also supports compliance with legal requirements and makes it easier to manage sales and tax records.

#### How to Edit a Tax Invoice Template

To customise your tax invoice:

  1. Go to **Settings** in the plugin.
  2. Click **General > Tax Invoice**.
  3. Under **Order Invoice Template** , select **Custom Tax Invoice**.
  4. Click on **Edit Tax Invoice Template** to open the editable template.

You can modify or rearrange the fields like – Order details, Invoice details, Store address, Product information, Customer addresses, Additional notes or branding messages, Tax ID / Tax ID type, Digital signature or company logo. 

You can **preview your changes** before saving. Once you’re happy with the layout, click **Save**.

* * *

**Tip:**   
Adding your company logo to the invoice strengthens your brand identity and builds customer trust.

* * *

### Order Tracking 

The tracking feature keeps your customers informed about their order status in real-time. Once an order is shipped, the plugin automatically sends tracking emails with updates like **In Transit** , **Out for Delivery** , and **Delivered** , so customers always know where their order is.

**Customising the Tracking Email Template**

You can personalise the tracking email to match your brand and messaging style. The plugin lets you send tracking details, like the tracking number and shipping status, in the **Order Completion** email.

Here’s how the email template editor works:

  1. **Subject Line** : Set the subject line using placeholders like $order.orderNumber$ and $shop.name$ to include the order number and store name automatically.
  2. **HTML Email Template** : This is where you can customise the email’s content and design using HTML/CSS. Great for advanced users or developers.
  3. **Email Preview** : See a real-time preview of your email. It shows sample details like the tracking number, delivery status, shipping method, a thank-you message, and support contact info.
  4. **Buttons** :
     * **Reset Default** – Revert to the original default email format.
     * **Save** – Save any changes you’ve made.

The **information (i) icon** next to ‘Edit Email Template’ provides a list of variables you can use while customising the template. Simply click it to view all available variables.

In short, this feature helps you design and preview the shipping update emails sent to your customers when their order status changes.

* * *

### Order Confirmation Email

This feature lets you connect your email server (using **SMTP – Simple Mail Transfer Protocol**), so all order-related emails, like shipping updates and invoices, are sent from **your email address** instead of a generic one. This helps build trust and keeps your branding consistent.

**How to Enable**

  1. Tick the checkbox to enable the option.
  2. Once enabled, you’ll need to enter SMTP credentials, which you can get from popular email services like **Mailgun** or **SendGrid**.

**Required Details**

  * **SMTP Host** : The server used to send emails (e.g., smtp.gmail.com)
  * **SMTP Username** : Your email ID or login name
  * **SMTP Password** : Your login password or plugin-specific password
  * **Email From** : The email address shown as the sender
  * **Email Reply-To** : The email address where replies should go
  * **SMTP Port** : The port for sending emails (usually 465 or 587)

### Customise Shipping Options

This section lets you customise key shipping options to better suit your business needs. You can edit templates, set currency, manage customs values, and fine-tune delivery settings. Below is a quick breakdown of each option:

  1. **Packing Slip Template:** A format used to print the list of items in a shipment. It helps the customer and shipper know what’s inside the package. You can edit this template to match your branding and preferred layout by clicking on “**Edit Packing Slip Template** ”.
  2. **Picklist Template:** A layout used for the list of items that need to be picked from inventory before packing. Helps in organising the packing process. This template can be customised based on your workflow and team preferences. Click on “**Edit Picklist Template** ” to edit.
  3. **Preferred Shipment Currency:** Lets you choose which currency should be used for shipping costs (e.g., USD, INR, etc.).
  4. **Minimum Value for Customs/Insured Amount:** Sets the lowest value to declare for customs or insurance, even if the product price is lower. Useful for international shipping.
  5. **Custom Description To Be Displayed in Commercial Invoice:** Lets you decide what to show (like product name or category) in the invoice used for customs clearance in international shipments.
  6. **Estimated Delivery At Checkout:** When enabled, customers can see the expected delivery date before they place an order.
  7. **Convert Non-English Characters to English (Applicable only for UPS):** This feature changes any foreign language characters to English so that UPS can process shipping labels without errors.
  8. **Customs/Insured Amount To Be Used:** Allows you to pick what value (like product price or declared value) should be used for customs or insurance when generating labels.
  9. **Saturday Shipping:** When turned on, it allows your shipping carrier to deliver packages on Saturdays, too.
  10. **Include Shipping Charges in Declared Value:** Enable this option to include shipping charges in the declared value for insurance purposes (currently only works with BlueDart).

* * *

## **Set up Multi-Vendor Shipping**

### Multi-Vendor Shipping Made Simple with WooCommerce Shipping Services

Creating a multi-vendor marketplace on WooCommerce lets you offer a wide variety of products from different sellers, all under one roof. While this setup is great for customers, handling shipping from multiple vendors can get tricky, especially with different pickup addresses, rates, and delivery options.

That’s where **WooCommerce Shipping Services** steps in to make things easy.

Starting from the **$29 Popular plan** , the plugin supports multi-vendor functionality and takes care of everything from:

  * Showing live shipping rates based on each vendor’s location
  * Generating shipping labels separately for each vendor
  * Sending tracking details automatically to customers

**Need help setting this up?** Follow our full[ **Multi-Vendor Shipping Setup Guide**](https://www.pluginhive.com/knowledge-base/multi-vendor-shipping-using-woocommerce-shipping-services/), which includes all the steps you need to configure your store.

If you’re still building your marketplace, check out this guide on how to[ **convert your WooCommerce store into a multi-vendor marketplace in 6 easy steps**](https://www.pluginhive.com/woocommerce-store-to-multi-vendor-marketplace/?srsltid=AfmBOorpTbBY2J_3KcSCMOmkbzScrt2IWhEuaMvUOhjwACkYbcii2er_#online_multivendor-marketplace).

With the right tools, running a multi-vendor store with smooth shipping operations doesn’t have to be complicated.

* * *

## **Managing App Subscriptions**

To manage your app subscription, check out the two options below by navigating to **☰ Menu > Account**.

**1\. Billing Address**

  * The billing address is linked to your payment method (credit card, debit card, or payment account).
  * It’s used to verify payments, not for shipping orders.
  * By default, your store location is saved as the billing address.

To update the billing address or change the time zone, navigate to:  
**☰ Menu > Account > Billing Address**.

**2****.** **Manage plugin subscription:**

This page lets you manage your pluginHive plans, including viewing subscription details, label limits, and billing info. It also provides quick actions to view invoices, change your plan, or stop the subscription.

Here’s a brief on the main buttons:

  * **VIEW INVOICE(S)** : Allows you to view invoices related to your current or past subscriptions. Useful for keeping track of billing history or accounting.
  * **CHANGE SUBSCRIPTION** : Lets you upgrade or downgrade from your current plan to a different plan based on your shipping needs.
  * **STOP SUBSCRIPTION** : Cancels your current plan and disables related features after expiry.

To modify your subscription, navigate to:  
**☰****Menu > Account > Manage Subscription.**

These are the plans available in the WooCommerce Shipping Services plugin. You can select one of the options to **change the subscription**.

* * *

**Note:**

  * Due to RBI regulations, Indian merchants may not be able to subscribe using Indian cards directly on the platform. If you face this issue, please contact our support team, and we’ll provide you with a payment link.
  * You can choose to continue with either a **6-month** or **annual** plan after your trial ends.

* * *

* * *

## **Understand the Orders Grid**

The Orders Page serves as the central dashboard for managing all your **shipments, labels, pickups,** and**tracking activities**. With **robust filtering, sorting,** and**batch processing capabilities** , this page is designed to streamline your order fulfilment process and improve operational efficiency.

**Headers Available**

  * Orders
  * Labels
  * Pickup
  * Manifest
  * Tracking
  * Help

### **1\. Orders**

The Orders header allows you to view, filter, edit, and process all your imported orders. It acts as the control panel for managing shipping, packaging, fulfilment, and other logistics, offering a comprehensive set of tools.

### **Import Orders**

By default, orders will be automatically imported. However, if you see any delay or notice that an order hasn’t been imported, you can manually initiate the import using the **Import Orders** button.

### **Today’s Labels**

This view lets you see all the shipping labels that have been created today for quick access, allowing you to perform all post-label actions quickly and efficiently.

For example, if you generate labels for 20 orders in a day, you can:

  * View how many succeeded, failed, or are pending
  * Print all labels or download individual ones
  * Request a pickup or fulfil orders directly from here
  * Print a Pickup List for all orders.

This section is especially useful for reviewing all the labels you have processed that day.

### **View Options**

At the top of the Orders page, you’ll find four viewing tabs to help you quickly access orders based on their shipping lifecycle:

  * **All** – Displays all imported orders regardless of their status.
  * **Open** – Shows orders that have not yet been processed or labelled.
  * **Labelled** – Displays all orders for which shipping labels have already been generated.
  * **Fulfilled** – Displays orders that have been marked as fulfilled, either via the plugin or manually.

These tabs let you jump straight to relevant orders without manually applying filters each time.

### **Filters**

The “**Add Filter** ” button is available across all views, allowing precise control over which orders you want to view using the following criteria:

  * **Order ID** – Search and filter orders based on the order IDs, you can use the comma as a separator (ex: 1001,1002 or #1001, #1002)
  * **Name** – Filter by customer name.
  * **SKU** – Narrow down based on product SKU.
  * **Status** – Filter by order status, such as Open, Labelled, Fulfilled, etc.
  * **Country** – Filter based on the destination country.
  * **Date** – Choose from Today, Last Day, This Month, Last Month, or use a Custom Date Range.
  * **Phone** – Search by customer phone number.
  * **Carrier** – Filter based on the shipping carrier assigned to the order.
  * **Tags** – Use WooCommerce tags or custom tags to filter orders.

### **Custom Filter Options**

You can also create and reuse custom filters easily:

  * Use **“Save As”** to save your current filter view.
  * Click the **“+” (Plus)** icon next to the filter view dropdown to create a new saved view.
  * **Delete/Duplicate View:** If you want to duplicate a view to include additional filters while keeping the original, or if you decide to permanently remove a view, you can use the **Delete** or **Duplicate** options accordingly.

**For example,** if you have integrated two shipping carriers, say, **Stamps USPS** and **UPS** , and want to view orders based on the carrier, you can use the **_Carrier_** filter to create and save a filtered view. This allows you to quickly access and compare orders shipped via **Stamps USPS** and **UPS.**

### **Order Table Columns**

The grid layout displays a comprehensive view of every order with the following default columns:

  * **Order ID** – Clickable to view detailed Order Summary.
  * **Date** – Shows when the order was imported or created.
  * **Customer** – Customer’s name.
  * **Shipping Cost** – Calculated cost based on the selected package, carrier, and service.
  * **Packages** – Shows weight, dimensions, and number of boxes.
  * **Products** – Displays product names and their quantities.
  * **Carrier** – Shipping carrier and service assigned.
  * **Status** – Current order status in the plugin (Initial, Processing, Label Created, Fulfilled, Label Failed and Return Created).
  * **Total** – Total order value along with payment type (COD, Prepaid, or Manual).
  * **Outstanding** – Any pending payment value.
  * **Tags** – WooCommerce or plugin-specific tags.
  * **Ship To** – Shipping address of the customer.
  * **Errors** – Any order-level issues (e.g., failed address validation).
  * **Weight** – Total shipment weight.

### **Edit/Reorder the Tabular Columns:**

You can customise the table columns to suit your needs by enabling or disabling specific columns. Simply click the **Settings** icon, as shown below.

### **Order Rows and Pagination**

You can control how many orders appear on each page with the following pagination settings:  
**10, 20, 30, 40, 50, 60, 100****  
**This helps manage bulk orders efficiently and improves usability for large catalogues.

### **Sorting**

Sort orders by Order Date:

  * **Oldest to Newest**
  * **Newest to Oldest**

By default, the system displays orders from the last month, but this can be customised using filters.

### **Quick Actions (On Order Selection)**

When multiple orders are selected, additional tools become available.  
The available action buttons depend on:

  * The page view (**All, Open, Labelled, Fulfilled**)
  * The status of the selected orders

#### **Quick Actions** :

Depending on selected orders and their statuses, the following action buttons appear:

  * **Generate Label** – Creates a shipping label for orders that are in Processing Status and updates the order status to “**Label Created** ”.
  * **Quick Ship-** Allows you to process multiple single-package orders in one go. You can modify the From Address, Carrier, Service, Weight & Dimensions in this section. Once modified, you click on Generate Label to created label and fulfill orders automatically
  * **Edit Package –** Allows you to**** Add/remove boxes, modify box contents, adjust weight/dimensions and this is applicable only for one order at a time
  * **Request Pickup –** Schedules a carrier pickup for the order. The order then appears under the Pickup header.
  * **Print Documents** – Shows a dropdown of options to print all documents, which include – Label, Tax Invoice, Packing Slip, Pick List, or All options at once.

**Available Print Options:**

  * **Label** – Prints shipping label(s) for selected order(s) or batch.
  * **Packing Slips** – Lists shipment items; useful forthe warehouse and customers.
  * **Tax Invoice** – Official invoice with pricing and tax details.
  * **Pick List** – Consolidated product list for efficient picking.
  * **Commercial Invoice** – Required for international shipping; includes product, value, and origin details.
  * **All** – Prints all selected documents together in one click.

* * *

**Note:**

  * To use this option, ensure the desired document types (**Label** , **Packing Slip** , etc.) are enabled in **Plugin Settings → General Settings → Print Settings**.
  * Only the enabled documents will be printed when using the **All** option.

* * *

  * **Mark as Fulfilled –** Pushes the tracking number to your store (e.g., WooCommerce) and updates the order status to Fulfilled

**For Example:**

Selecting orders in **Processing** status on the All tab shows:

  * Generate Label
  * Quick Ship
  * Edit Package

Selecting an order in the **Label Created** state shows:

  * Request Pickup
  * Print Documents
  * Mark as Fulfilled

Here’s what the **Quick Ship** option looks like:

### **Order Status in the Plugin:**

  * **Initial** – This status appears when an order is unable to be processed due to unmatched rules or errors (e.g., carrier not offering any rate). If no rules applied or if a label is cancelled, the order resets to Initial. After changes are made, use **“Prepare shipment”** or **“Reprocess order”** to resume; this will then update the order status to Processing.
  * **Processing** – Orders that are ready to be processed.
  * **Label Created** – Orders for which a label has been generated.
  * **Fulfilled** – Orders fulfilled in the plugin.
  * **Label Failed** – Indicates a failure from the carrier during label generation.
  * **Returned Created** – Indicates that a return label is created.

**Note:**   
If you make any changes to plugin settings, make sure to “reprocess orders” using the **Reprocess** button available in **More actions**.

* * *

### **2\. Labels (Label Batches)**

This section displays the details of the shipping labels that have been created for various orders, including the status of label generation and shipment. It keeps track of the label batches you’ve created.

### **Filters**

  * Filter by Date Range to view relevant batches

### **Batch Columns**

  * **Date** – When labels were created
  * **Shipment Type** – Forward or Return
  * **Result** – Shows how many labels succeeded or failed
  * **Status** – Completed or Pending
  * **Print** – Print all labels in the batch or download individual ones

### **Advanced Options**

Selecting batches enables:

  * Print Documents (Labels, Packing Slip, Tax Invoice, Pick List individually or together)
  * Request Pickup
  * Mark as Fulfilled

**Ellipsis Menu (****⋮****) Allows**

  * Print the Pick List for the selected batch

This section is especially useful for reviewing large groups of orders processed together.

* * *

### **3\. Pickup**

This section helps you manage and monitor all pickup requests submitted through the system. Once you generate shipping labels, you can either request a pickup or mark orders as fulfilled.

### **Filters**

  * **Date Range** : Filter pickup requests based on a specific date range.
  * **More Actions** : Use the “More actions” menu to mark orders as fulfilled if needed.

### **Pickup Grid Columns**

  * **Date** : Shows when the pickup was requested
  * **Shipment Type** : Indicates whether the shipment is **Forward** or **Return**
  * **Carrier** : Displays the shipping carrier used
  * **Address** : Ship-from address selected for the pickup
  * **Order ID** : Linked order associated with the pickup request
  * **Status** : Indicates the status of the pickup – **Completed** or **Failed**.
  * **Pickup No.** : Unique identifier for the pickup request
  * **XML Data** : View pickup request data in XML format by clicking the ‘eye’ icon.

### **Pickup Management Options**

Based on the pickup request status, you’ll get the following available actions:

  * **Retry** : If the request fails, an error message will appear. You can retry the request after resolving the issue.
  * **Cancel** : Cancel the pickup request if you plan to drop off the packages yourself.
  * **Modify** : Make changes to the order details even after the pickup request has been scheduled.

This section ensures you can easily manage and monitor all your scheduled pickups.

* * *

### **4\. Manifest**

This section allows you to track and print shipping manifests for all fulfilled orders.  
A **Manifest** is a summary document generated after fulfilment, containing key shipment details such as order numbers, AWB (Air Waybill) numbers, and barcodes.

  * It consolidates shipping information for the carrier into one document.
  * The manifest barcode can be scanned to confirm or process all parcels together, saving time by avoiding individual scans.
  * Includes essential information like payment details, order numbers, and label barcodes for easy reference during parcel handover.

### **Filters**

  * **Date Range** : Filter manifests based on creation date.

### **Manifest Grid Columns**

  * **Date** : Shows when the manifest was generated
  * **Carrier** : Indicates the shipping carrier associated with the orders
  * **Address** : Displays the ship-from address used for the manifest
  * **Orders** : Number of orders included in the manifest
  * **Status** : Shows whether the manifest is **Pending** or **Completed**
  * **Print** : Print the generated manifest for physical handover
  * **Carrier Manifest** : Displays the carrier-specific version if available
  * **Debug** : Helps troubleshoot issues related to manifest generation

This is especially helpful when handing over multiple packages to the carrier.

* * *

### **5\. Tracking**

This section provides real-time shipment updates for all fulfilled orders.

The **Tracking tab** helps your fulfilment team or admin easily monitor delivery progress, investigate delays, and share status updates with customers.

  * Displays tracking statuses such as **Initial** (label generated, not scanned), **In Transit** , **Out for Delivery** , and **Delivered**
  * Clicking the tracking number opens a **timeline view** showing the shipment’s full history
  * Useful for customer support, quick verifications, and internal follow-ups

### **Filters**

  * **Date Range** : Filter tracking updates by shipment date
  * **Tracking Status** : View shipments based on their current status (e.g., In Transit, Delivered)

### **Tracking Grid Columns**

  * **Order** : Clickable link to view the order’s summary
  * **Store** : Name of the store associated with the order
  * **Carrier** : Displays the shipping carrier and service used
  * **Destination** : Country where the package is being delivered
  * **Expected Delivery** : Estimated delivery date provided by the carrier
  * **Status** : Real-time tracking update of the shipment
  * **Info** : Displays internal notes or any pending actions related to the shipment

* * *

**Tip:**   
Use the **Retrack** button to manually fetch the latest tracking status from the carrier.

* * *

This makes it easy to share updates with customers or investigate any delivery issues.

* * *

### **6\. Help**

This section offers quick access to setup guides, feature documentation, and customer support resources.If you need assistance or clarification while using features like **Orders, Labels, Pickup, Manifest** , or **Tracking** , this is your go-to tab. It’s designed to help you troubleshoot issues, understand functionalities, and make the most of the platform with ease.

* * *

### **Understanding the Menu View Section in the Plugin**

The **View** section in the WooCommerce Shipping Services plugin helps you monitor and manage your shipment workflow more efficiently.

Located under the **“Views”** tab in the plugin’s main menu, it includes 14 sections that track different shipping statuses, including **Orders, Labels, Pickup** and**Manifest** , which are covered above separately. The other set of options in the **Views tab** is:

  * Processing
  * Label Created
  * Store Fulfilment failed
  * Returs
  * Orders for Later
  * Labels Failed
  * Returns Failed
  * Order Cancelled
  * Not to Ship

Here are the sections within the View category:

### **Processing** :

This section displays all orders still in the processing stage, meaning labels have not yet been created. Here, you can:

  * Generate labels
  * Edit packaging
  * Add special services

### **Store Fulfilment Failed**

Sometimes, after a label is generated, the plugin may not be able to fulfil the order in WooCommerce. When that happens:

  * The Fulfilment Summary will show a clear error message explaining what went wrong (e.g., missing permissions or required info)
  * Once the issue is identified, you can fix it and reattempt fulfilment from the plugin

This section helps you resolve fulfilment failures quickly so customers receive tracking updates without delay.

### **Return**

Track all orders with return labels created.

  * Helps manage and monitor reverse shipments

### **Orders for Later**

You can set a future shipping date for specific orders. These orders will appear in this section:

  * Useful for scheduling shipments and monitoring upcoming fulfilment
  * Helps avoid accidental label generation before the intended ship date

### **Label Failed**

Orders for which forward shipping labels failed to generate due to missing or invalid information will be listed here:

  * Detailed error messages will help you understand why the label failed
  * You can correct the necessary information and retry the label generation

### **Return Failed**

This section shows orders where the return label generation failed. Common reasons include invalid return addresses or missing required data:

  * Use this section to troubleshoot and fix issues with reverse shipments

### **Order Canceled**

Shows orders that have been cancelled in WooCommerce.

  * Marked with a red line to avoid confusion
  * Prevents accidental label generation

### **Not to Ship**

Used for orders that don’t require shipping (e.g., local pickup or external fulfilment).

  * Mark as “Not to Ship” to hide them from the All Orders view
  * Can be re-enabled later for shipping if needed

* * *

## **Advanced/More Actions on the Order Grid**

### **Order Processing and Editing Options in the Order Grid of the Plugin**

Clicking the **ellipsis** (⋮) beside an order opens a full list of order-specific operations:

**1\. Generate Label****  
**Initiates the shipping label generation for the selected orders with the assigned carrier/service based on the package configuration.

**2\. Request Pickup****  
**Schedules a pickup request with the carrier using the pre-configured ship-from location.

**3\. Mark as Fulfilled****  
**Marks the order as fulfilled in the plugin, which in turn fulfils the WooCommerce Orders with the tracking number generated for the label(s).

**4\. Reprocess Orders****  
**Re-evaluates the shipping, packaging and automation rule data in case of changes, and assigns the updated data to the order, ensuring accurate rate/service selection and order processing.

**5\. Quick Ship**

The “Quick Ship” functionality enables users to rapidly generate shipping labels and fulfil all the selected orders directly from a single interface. This streamlines the shipping process by minimising data entry and allowing immediate label creation.

#### **Workflow Summary:**

  1. The user selects the shipping origin, carrier, and service level.
  2. Input weight and optionally dimensions.
  3. Clicks Generate Label to:
     * Produce a shipping label.
     * Mark the associated order(s) as fulfilled.

#### **Benefits:**

  * Simplifies and accelerates the shipping process.
  * Reduces manual effort by combining labelling and fulfilment in one step.
  * Offers flexibility through the carrier and service dropdowns.

**6\. Track Orders****  
**Allows tracking of the shipment using the carrier’s tracking number directly from the plugin.

**7\. Edit Packages****  
**Modify the package details (weight, dimensions, box type) associated with the order before generating the label.

**8\. Fulfil Manually****  
**Used when a label has been generated outside of the plugin and the order has to be manually fulfilled using the tracking number.

**9\. Change Carrier and Service****  
**Switch to a different carrier or service manually before generating the label.

**10\. Prepare Shipment****  
**Used when the Order is in**Initial** Status. This will initiate the backend process to prepare data for label generation or rate estimation.  
If the order details like shipping address, etc and matching shipping automation rules are present, then the Order will move to **Processing** Status.

**11\. Set Ship From Address****  
**Change the origin address (warehouse/sender address) from the pre-configured list of addresses configured in the plugin to use as Ship From Address for the order.

**12\. Cancel Shipment****  
**Void the label and cancel the shipment if already been generated.  
It can only be used if the Order is in **Label Created** Status.  
Some Carriers, like Australia Post MyPost Business and Canada Post Non-Contract Account users, will not be able to cancel the labels from the plugin due to carrier restrictions.

**13\. Change Status to Initial****  
**Resets the order status to Initial in the plugin to allow reprocessing from scratch.

**14\. Mark as Not to Ship****  
**Excludes the order from shipping workflows and moves them to the**Not To Ship** section in the plugin. Useful for cases like orders having digital products or for store pickups.

**15\. Change Shipping Date****  
**Adjust the scheduled shipping date for the order.

**16\. Create Return Label****  
**Generates a return shipping label for the**fulfilled** orders from the plugin.

**17\. Enable Saturday Delivery****  
**Activates the Saturday delivery option (if supported by the selected carrier/service).

**18\. Edit Special Features****  
**Add or edit additional shipment features like insurance, delivery signature confirmation, etc.

**19\. Validate Shipping Address****  
**Checks and corrects the recipient address using carrier address validation.

**20\. Confirm Address Changes****  
**Applies any address corrections identified during validation or manual edits.

**21\. Download Tax Invoice****  
**Downloads the tax invoice for the orders that have been processed using the plugin, reflecting charges and taxes.

**22\. Regenerate Tax Invoice and Packing Slip****  
**Regenerates a new copy of the tax invoice and packing slip with updated details.

**23\. Download Documents****  
**Downloads all shipment-related documents in a zip file (e.g., invoice, commercial invoice, shipping labels).

**24\. Edit Payment Type****  
**Change the payment method for the shipment, like switching between Prepaid and COD. Useful for Carriers like BlueDart, which support Cash on Delivery (COD) shipping.

**25\. Download the Packing Slip****  
**Download the generated packing slip to include with the shipment.

**26\. Print Picklist****  
**Opens the picklist of items in a PDF file in a new tab, which can be used for printing using the printer. Used in the order to assist with warehouse picking.

**27\. Download Labels****  
**Bulk download all labels associated with the order.

**28\. Print Return Label****  
**Prints the previously generated return label.

**29\. Print Labels****  
**Opens the Labels for the Order in a PDF file in a new tab, which can be used for printing using the printer.

**30\. Print Packing Slips****  
**Opens the Packing Slip for the Order in a PDF file in a new tab, which can be used for printing using the printer.

**31.** **Print Tax Invoice**

Opens the Tax Invoice for the Order in a PDF file in a new tab, which can be used for printing using the printer.  
  
**32\. Print Commercial Invoice**

Opens the Commercial Invoice (used for international shipments) for the Order in a PDF file in a new tab, which can be used for printing using the printer.

**33\. Print All Documents**

Prints all available documents at once for that order.

**34\. Edit Customer Reference in Label**

Allows you to edit the custom reference field printed on the shipping label.

**35\. Edit Mapped Order Meta**

Lets you edit custom metadata fields that are mapped to the order.

**36\. Add DHL Special Service**

This option allows the user to configure and submit DHL special shipment services. It includes:

  * Shipper’s reference number.
  * Selection of filing types for shipments (ITN number)
  * Specification of the unit of measure.
  * Selection of registration number type for the recipient.
  * Options to enable:
    * Saturday Delivery
    * Direct Signature
    * No Signature Required
    * Paperless Trade (PLT)

**37.** **Add PostNord Special Service**

This option enables users to add extra services to a PostNord shipment, including:

  * Selecting additional services from a dropdown list like Insurance, Indoor Delivery, Return to Sender, etc.
  * Choosing a category of item for CN22/CN23 documentation, like Gift, Returns, Sale of Goods, etc.
  * Adding CN23 document details like Sender Customs ReferenceId, Importer Reference, Postal Charges Amount and Currency, etc.

**38\. Set Service Point for PostNord**

Allows the user to set a specific service point for PostNord deliveries based on the shipping address. Used with a specific service that supports Service Points.

**39\. Add FedEx Special Services**

Provides options to configure additional FedEx shipment preferences:

  * Add Insurance.
  * Enable Delivery Signature.
  * Choose shipment charge payer (Sender, Recipient or Third Party)
  * Set the duties payment type (Sender, Recipient or Third Party)
  * Specify the purpose of shipment (e.g., Sold).
  * Define terms of sale (e.g., Delivered Duty Paid).
  * Select Freight Special Services (e.g., Liftgate Delivery, Liftgate Pickup, etc.)
  * Enable additional services:
    * Non-Standard Container
    * Saturday Pickup
    * Include Shipping in Commercial Invoice
    * Include Tax and Miscellaneous in Commercial Invoice
    * Enable Importer Of Record
    * Enter Recipient Customs ID.

**40\. Set Hold-At Location Point**

Allows the user to define a specific hold-at-location point for a FedEx shipment based on the shipping address.

**41\. Add DHL Freight Sweden Special Services**

Set Special Service like Doorstep Delivery for DHL Freight Sweden.

**42\. Set Service Point DHL Sweden**

Allows the user to define a specific service point for a DHL Freight Sweden shipment based on the shipping address. Used with a specific service that supports Service Points.

These options ensure granular control over order processing, allowing workflows to be tailored to your needs.

* * *

## **Display Live Rates at Checkout**

**Prerequisite:**

  * **Enabling Realtime Rates for Live Shipping Rates at Checkout**

To display live shipping rates at the checkout page, you must enable the **Realtime Rates** option in your WooCommerce store.

  * **What Happens If Realtime Rates Are Disabled?**
    * Live carrier-calculated rates won’t appear in the cart or checkout.
    * If you prefer to use flat rates, you’ll need to set them up manually in the WooCommerce Shipping Zone settings but this risks overcharging (which may cause cart abandonment) or undercharging (which can hurt your profit margins). If you don’t set any flat rates, no shipping options will appear at checkout.

  * **How to Enable Realtime Rates**  
Follow these steps to turn on Realtime Rates from your WordPress admin panel:

  1. Go to **WooCommerce > Settings > Shipping**
  2. Select **PluginHive WooCommerce Shipping Services > General**
  3. Enable the **Realtime Rates** checkbox

Once enabled, your customers will see accurate shipping rates from the carrier at checkout.

* * *

### **How to View Live Carrier Shipping Rates at Checkout**

To verify that live shipping rates are being displayed on your WooCommerce store, follow these steps:

  * In your WordPress Admin panel, hover over your store name located at the top-left corner and click on **‘Visit Store’** to access the storefront.

* * *

  * Add the desired product(s) to your cart.

* * *

  * Once you’ve added the products, navigate to the Cart page to review your order details. Enter the complete ‘Ship To’ address, Country, State, City/Town, and Pincode/Zipcode. Make sure all fields are filled in, as they are required to display the available shipping options. If everything looks accurate, proceed to the Checkout page to complete your order.

* * *

Your WooCommerce store will now display **live carrier shipping rates** at checkout (using **Stamps** **USPS** in this example), through the **WooCommerce Shipping Services** plugin.

Customers will be able to choose from real-time shipping services such as:

  * **USPS Priority Mail**
  * **USPS Priority Mail Express**

* * *

### **How to Verify Shipping Rates via Request Log**

To verify the rates shown at checkout:

  * Navigate to the **WooCommerce Shipping Services plugin.**
  * Go to **☰ Menu > Plugin Settings > Shipping Rates > Request Log.**

This section displays all real-time shipping rate requests sent from your checkout.

### **Accessing Specific Rate Logs**

In the **Request Log** page:

  * Logs are listed chronologically with a unique **Reference ID**
  * Click on the **“i” icon** under the “Info” column to open the detailed log related to the selected request.

This opens a complete breakdown of the shipping rate request used during checkout.

### **Understanding the Log Details**

Each rate log contains the following key sections:

### **Request Summary:**

**1\. Displays Shipping Address****(Recipient address)****:**

This is the address provided by the customer at checkout. Verify the shipping address and ensure that the address is within the serviceable area of the carrier that you have chosen so that there is no extra charge added.

**2\. Displays From Address (Shipper address)**

Verify the “from address” and ensure that the correct location is set as the default address if you have multiple “from addresses”, and make sure it is correct.

**3\. Items Summary**

  * Shows product details such as **SKU** , **quantity** , **cost** , **weight** , and **total**

**4\. Packing Summary**

The Packing Summary section provides detailed information about how the products in the order were packed based on the configured packing method. It shows:

  * **Date & Time** when the packing was done.
  * **Packaging Type** used (e.g., Box Packing, Weight-Based, etc.).
  * **Box Name** to identify the specific box used from the predefined packaging settings.
  * **Weight and Dimensions** of the packed box are critical for calculating accurate shipping rates.
  * **Status** indicating if the packing was successfully processed.

This section ensures transparency in how the shipment was prepared.

**5\. Automation Summary**

  * Shows Rate Automation rules applied (e.g., “Auto Rule for STAMPS USPS”)
  * Lists the **carrier** , **service** , **rate** , and **final rate. The** Final Rate is what is shown on checkout from the plugin.
  * Status and error indicators confirm successful rate retrieval

Multiple USPS service options are listed here, with actual rate calculations used during checkout.

* * *

## **Generate Labels One by One**

### **Generate Labels One by One with Quick Ship**

Efficient order fulfilment is key to running a successful eCommerce business. The **WooCommerce Shipping Services plugin** offers the **Single Label Generation Process (SLGP)** using the **Quick Ship** feature, making label creation fast and easy for individual orders.

With Quick Ship, you can:

  * Configure shipment details
  * Generate shipping labels
  * Fulfill orders  
All from a single screen, helping reduce errors and save time.

This streamlined approach reduces manual steps, minimises errors, and ensures that shipping operations remain fast and accurate.

### **How to Generate a Label – Using Quick Ship**

**Navigate to Orders View**

Click on the order number for which you need to generate a label.

**Order Page Overview**

After selecting an order, you’ll be directed to the **Order Page.** It has various sections, namely:

  1. Order Summary Details
  2. Recipient address
  3. Billing Address
  4. Packing Summary
  5. Rate Summary

#### **Order Summary Details**

This section captures the essential information needed to process and generate a shipping label. It includes:

  * **Fulfilled from:** The warehouse or shop location address fulfilling the order.
  * **Carrier:** Shipping service provider selected.
  * **Service:** Specific delivery method under the carrier.
  * **Package:** Type of packaging selected for the shipment.
  * **Weight (lbs):** Weight of the package.
  * **Dimensions (L×W×H in):** Box dimensions entered manually.
  * **Order Cost:** Total cost of the order.
  * **Balance:** Balance due.
  * **Paid:** The Amount paid by the customer.
  * **Signature Required:** A checkbox option for requiring delivery confirmation via signature.

Use this section to verify all shipping details before generating the label.

#### **Generate Label and Fulfil**

  * Click the **“Generate Label & Fulfil”** button.  

**Generate Label & Fulfil:** Once all details are verified, this button initiates label creation and order fulfilment.

#### **Printing Documents After Fulfilment**

Once an order is fulfilled, click on **Print Documents** to access and print various shipping-related documents.

Below is the label generated for the order above:

#### Available Print Options:

  * **Labels –** Prints the shipping label provided by the carrier.****
  * **Packing Slips –** Prints the packing slip generated by the plugin. 
  * **Tax Invoices –** Prints the tax invoice generated by the plugin. 
  * **Pick List –** Prints a pick list for order picking (generated by the plugin). 
  * **Commercial Invoice –** Prints the commercial invoice for international shipments (provided by the carrier). 
  * **All –** Prints all of the above documents in a single batch.

Once the order is fulfilled through the plugin, it will automatically be updated to **‘Completed’** status in the WooCommerce dashboard.

The **Single Label Generation (SLGP)** process using the**Quick Ship** interface in the **WooCommerce Shipping Services plugin** helps your team to:

  * Ship orders faster
  * Minimise errors
  * Improve customer satisfaction

* * *

**Tip:**   
Always double-check order details before generating labels, and use the available print options to keep your fulfilment process organised and efficient.

* * *

* * *

### **Generate Labels One by One without Quickship**

### **Overview**

In manual shipping workflows, businesses can verify and customise each shipment for accuracy and compliance. The **Single Label Generation Page (SLGP)** is ideal when automated Quickship isn’t suitable, especially for orders with special packaging, international rules, or personalisation.

### **Accessing the Order Page**

**Steps to begin the process of generating a label:**

  * Go to the **Orders View**.
  * Click on the **Order Number** to open the specific order’s detail page.

### **Order Information**

The order page includes the following order information sections:

  1. Fulfilment Location
  2. Rate Summary
  3. Recipient and Billing Information
  4. Order Cost Summary
  5. Packing Summary

#### **1\. Fulfilment Location**

Defines where the order ships from.**** Choosing the correct location ensures correct shipping calculations and expected delivery timelines.

#### **2\. Rate Summary**

  * **Customer Carrier Selection at Checkout** –**** Indicates if the customer chose a specific shipping carrier during checkout.
  * **Selected Carrier and Service** –**** Displays which carrier and service were selected, with editable options for updates.
  * **Shipping Options Table** –**** Provides a list of available carriers and services, showing cost and delivery time.  
Purpose: Helps choose the best value option for shipping.

#### **3\. Recipient & Billing Information**

  * **Recipient** –**** Shows the destination address. Can be updated if errors or changes are needed.
  * **Billing** –**** Displays the payment address for the order. Editable like the recipient info.

#### **4\. Order Cost Summary**

Displays the order subtotal (excluding shipping).**** This helps merchants confirm item totals before proceeding.

#### **5\. Packing Summary**

Details how the order is packed. Packaging affects shipping rates, safety, and delivery.

  * **Packaging Type –** Explains whether it’s a box, envelope, custom pack, etc.
  * **Box Name –** Refers to predefined packaging types used in fulfilment systems.
  * **Dimensions –** Length, width, and height of the package are vital for shipping calculations.
  * **Weight –** Shows the total package weight, including box and contents.

#### **Item Table Overview**

This section outlines what items are packed and their values:

  * **Item** – Product description or title
  * **SKU** – Stock Keeping Unit, helps with inventory tracking
  * **Cost** – Price assigned to the item
  * **Quantity** – How many units are packed
  * **Weight** – Weight of the item
  * **Total** – Price × Quantity

**Edit Option:** Use the pencil icon to make changes to quantities, box assignments, or weights before generating the label.

#### **Package Summary Table**

Gives a breakdown of all boxes used in the shipment:

  * **Sequence No.** – Order of the package if there are multiple
  * **Box Name** – The label of the box configuration
  * **Quantity** – Number of identical boxes in the shipment
  * **Weight (lbs)** – combined weight of box and contents
  * **Price (USD)** – Value or declared cost of the box contents

#### **Action Links:**

Quick tools to modify the package list:

  * **REMOVE** – Delete a box that was added by mistake.
  * **EDIT** – Change box contents or details.
  * **ADJUST** – Fine-tune parameters like weight or dimensions.

#### **Footer Actions:**

Used to manage changes made to the packing setup:

  * **ADD** – Add a new package or box row
  * **RESTORE** – Undo recent changes and revert to the last saved version
  * **CANCEL** – Discard changes without saving
  * **SAVE** – Confirm and apply your edits

### **Generating and Printing the Shipping Label**

Once you verify all order and packing details:Click **GENERATE LABEL** to create the shipping label using the selected carrier and service.

Use **PRINT DOCUMENTS** to access shipping papers.

Here’s a sample label printed:

#### **Available Print Options:**

  * **Labels –** Prints the shipping label provided by the carrier.****
  * **Packing Slips –** Prints the packing slip generated by the plugin. 
  * **Tax Invoices –** Prints the tax invoice generated by the plugin. 
  * **Pick List –** Prints a pick list for order picking (generated by the plugin). 
  * **Commercial Invoice –** Prints the commercial invoice for international shipments (provided by the carrier). 
  * **All –** Prints all of the above documents in a single batch.

### **Cancel Shipment**

**Need to make corrections?****  
**Use**CANCEL SHIPMENT** to void the current label and restart the process.

### **Fulfil the Order**

After printing the label:Click **MARK AS FULFILLED** to update the order as shipped in WooCommerce.

The system will record the tracking number and change the status to **FULFILLED**.

**Next Order Navigation feature** : Easily move to the next order using the arrow button on the Order page.

**Tracking  
Tracking** is automatically added once an order is marked as fulfilled using the plugin.

After fulfilment, the order status is updated to **“Completed”** in the WooCommerce dashboard.

To view the status and tracking details:

  * Go to **WooCommerce > Orders**
  * Click on the specific order
  * As shown in the image below, the order is marked as completed, and tracking information is automatically updated.

Merchants can also view the order status and tracking ID from the storefront.  
To check this, go to the **WooCommerce online store** and navigate to:**My Account > Orders. **Here, you can see the order status (e.g., _Completed_ , _Processing_ , etc.).

Click on the **View** button next to the order to see the full order details along with the tracking ID.

For customers, WooCommerce Shipping Services automatically includes the tracking details in the **Order Completion Email**.

Manual label generation via **SLGP** offers merchants full control over how packages are handled and shipped.  
This method is perfect for:

  * Customised orders
  * International shipments
  * Manual verification before fulfilment

It ensures accuracy, flexibility, and a better customer experience by allowing shipping to be handled on a case-by-case basis.

* * *

## **Generate Shipping Labels in Bulk**

Before proceeding with bulk label generation, we recommend reviewing the [**Understanding the Order Grid**](https://docs.google.com/document/d/1Q8Kn2e8lhcJkJq91TYSCui4o2DuAtjync1QaG97LyUg/edit?tab=t.wgxefnpqdbwb#bookmark=id.xmlemhssv16g) section to ensure you’re familiar with the order flow.

### **To Generate Labels in Bulk:**

  1. Navigate to the **Open** tab in the plugin.
  2. Verify the **package details** and **shipping cost** for each order.
  3. Select the checkboxes next to the order IDs you want to process.

Click to generate labels. You’ll be redirected to the **Label Batch** page to track the progress.

On the batch page, you’ll see the current status of the label generation process (e.g., _1 of 3_ means 1 label is created and 2 are in progress). Typically, each label takes just a second to be generated.

You can either wait for the batch to complete or return to the Order Grid to begin processing another set of orders. Previously created batches will continue in the background without affecting your workflow.

#### **Label Status Indicators:**

  * **Success** – Label has been successfully created.
  * **Processing** – Label is being generated.
  * **Initial** – Label generation is yet to start.
  * **Failure** – Label creation failed (if any issues occur).

### **To Print Labels & Other Documents:**

Once labels are generated:

  * Select the checkbox next to the batch.
  * Click **Print Documents**.
  * Choose to print shipping labels or other necessary documents based on your needs.

### **To Fulfil Orders & Request Pickup:**

To fulfil orders in WooCommerce:

  * Select the batch(es).
  * Click **Mark as Fulfilled**.

To request a pickup:

  * Select the relevant batch(es).

Click **Request Pickup**.

Once the orders are fulfilled through the plugin, they will automatically be updated to **‘Completed’** status in the WooCommerce dashboard as shown below.

* * *

**Note:**

  * The actions **Print Documents** , **Request Pickup** , and **Mark as Fulfilled** can be performed independently at any time.
  * There’s no required sequence or restriction for performing these actions.

* * *

* * *

The **WooCommerce Shipping Services plugin** transforms how you manage shipping within your WooCommerce store by offering a powerful**all-in-one** solution. From displaying accurate **real-time rates** at checkout to **printing shipping labels** , managing **carrier pickups** , easily **tracking shipments** and handling**international shipping** requirements, the plugin covers every step of the shipping process with precision and flexibility.

Whether you’re running a **small store or managing high-volume fulfilment** , the plugin adapts to your needs through customisable packing methods, advanced automation rules, and integration with over **30+ global carriers**. It simplifies shipping for both **domestic and international orders** , helping you save time, avoid costly errors, and deliver a seamless customer experience.

The plugin streamlines the shipping workflow within WooCommerce, helping merchants reduce manual effort, minimise errors, and deliver a faster, more reliable fulfilment experience for their customers.

[ Previous  Set up the Shipment Tracking & Notify app on your Shopify store.  ](https://www.pluginhive.com/knowledge-base/set-up-shopify-shipment-tracking-notify-app/)

[ Next  Multi-Vendor Shipping with WooCommerce Shipping Services  ](https://www.pluginhive.com/knowledge-base/multi-vendor-shipping-using-woocommerce-shipping-services/)
