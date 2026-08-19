# Set Up Purolator with WooCommerce Shipping Services

**Source:** https://www.pluginhive.com/knowledge-base/purolator-setup-with-woocommerce-shipping-services/
**Platform:** WooCommerce (WordPress)
**Plugin:** purolator
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Set Up Purolator with WooCommerce Shipping Services

This guide will help you integrate your Purolator shipping account with your WooCommerce store using **[WooCommerce Shipping Services](https://www.pluginhive.com/woocommerce-shipping-services/)** by PluginHive. Once you have successfully integrated you will be able to automatically display Purolator shipping rates at checkout, print shipping labels, and easily track your shipments.

* * *

## On This Page

  * Download, install & activate the plugin
  * Add Purolator shipping carrier account
  * Verify the shipper or warehouse address
  * Display a preferred Purolator shipping service on WooCommerce cart & checkout
  * Configure weight and dimensions for your WooCommerce Products
  * Configure the shipping boxes and select the parcel packing method
  * Display Purolator shipping rates on the WooCommerce cart & checkout page
  * Place test orders choosing different Purolator shipping methods
  * Review the Purolator shipping services selected automatically for the orders 
  * Make the correction and reprocess the order if the order status is stuck as Initial with errors
  * Verify the payment method & the shipping cost for the order
  * Print the shipping labels for your WooCommerce order(s)
  * Request Purolator pickup from within WooCommerce 
  * Fulfill orders and send WooCommerce Order Completion Email to customers along with the tracking details
  * Print order manifest for the carrier pick up personnel
  * Monitor the shipment tracking status of your orders
  * [WooCommerce Multi-Vendor setup with PluginHive WSS](https://www.pluginhive.com/knowledge-base/multi-vendor-shipping-using-woocommerce-shipping-services/)
  * Frequently Asked Questions

* * *

### Download, Install and Activate WooCommerce Shipping Services

* * *

The plugin is available for download at the **PluginHive’s[WooCommerce Purolator Shipping Plugin with Print Label](https://www.pluginhive.com/woocommerce-shipping-services/)** page.

Install the plugin and activate it from the WordPress plugins page.

* * *

* * *

Visit the plugin settings by clicking on the Settings option, and click on **Register**.

After the registration, click on the **Let’s Start Fulfilling** , as shown below, to access the plugin setup wizard.

* * *

* * *

### Add Purolator shipping carrier account

[WooCommerce Shiping Services](https://www.pluginhive.com/woocommerce-shipping-services/) allows you to use Purolator along with other top shipping carriers simultaneously to display live shipping rates, generate & print shipping labels, and track Purolator shipments in real-time.

Within the setup wizard, click on **Start** to integrate Purolator to your WooCommerce store.

* * *

* * *

Click on Purolator.

* * *

* * *

Add the shipping carrier account credentials to integrate Purolator into WooCommerce.

You need to get the following details from Purolator and add them to the plugin.

  * Carrier Name
  * Web Service Key
  * Web Service Password
  * Account Number

* * *

* * *

After adding the details shown above, click on **Add** , and the plugin will add your preferred shipping carrier successfully.

Click on **Next** and now you can start fulfilling your orders by clicking on the **Start Shipping** button as shown below.

* * *

* * *

**_Note_**  
If you don’t have Purolator shipping account credentials, you can create one using a simple process. To get the credentials, please read – [**Create Purolator Account & Get Credentials**](https://www.pluginhive.com/purolator-account-setup/)

* * *

### Verify the shipper or warehouse address

Once the Purolator setup is complete, verify the shipper or the warehouse details. This will ensure the correct shipper address (shipper address must be within Canada in the case of Purolator) to be used while getting shipping rates and shipping labels for your order.

Click on the **(≡)** icon and visit **Settings > Address** and your store name will be listed there.

* * *

Click on the store name and you can see the shipper or warehouse address, along with the telephone number as shown below.

* * *

* * *

Review the shipper details and click on **Save** once the modifications are made.

* * *

### Display the preferred Purolator shipping services on WooCommerce cart & checkout

The plugin automatically displays all the available Purolator shipping rates on the WooCommerce cart and checkout page. However, if you want to display shipping rates for a particular Purolator shipping service on your WooCommerce store, you can do so without any hassle.

Click on the **(≡)** icon and visit **Settings > Shipping Rates > Rate Automation**, as shown below.

* * *

* * *

The plugin automatically creates rules for the shipping carriers that you add to help you choose the services that will be displayed on the WooCommerce store. Click on **Edit** to customize the shipping automation rules based on your preferences.

Under the **Action Details** tab, select your preferred shipping service that you want to display to your customers, as shown below.

* * *

* * *

You can also choose to calculate and display shipping rates for the above-selected shipping services based on various conditions, such as,

  * WooCommerce Shipping Zones
  * Product quantity in the cart
  * Total weight of all the products in the cart
  * Cart sub-total amount
  * WooCommerce Shipping Classes
  * Particular vendor
  * Time of order placement
  * Total weight range

Based on your preference, you can select any of the conditions and the plugin will calculate the shipping rates only if the conditions are matched.

If you do not want to set any particular condition, you can select **Any** option as shown below.

* * *

* * *

Click on**Save** once the modifications are done.

* * *

### Configure weight and dimensions for your WooCommerce Products

* * *

** _Reference_**  
For More Details on Configuring Weight & Dimensions Read – [WooCommerce Product Weight & Dimensions](https://www.pluginhive.com/knowledge-base/setting-up-woocommerce-shipping-services/#configure_product_weight_dimensions).   

* * *

### Configure the shipping boxes and select the parcel packing method

The plugin allows you to choose from some of the most advanced packaging methods to efficiently pack your products into the boxes. These packing methods include,

  * **Weight Based Packing (recommended)  
** A packing method purely based on the weight of the product, where you can set a maximum weight **(max.** **weight)** as your box capacity and the plugin will automatically determine the number of boxes to ship your products
  * **Box Packing**  
A packing method based on both the Weight as well as Dimensions, where you can create your own boxes with custom weight and dimensions. The plugin will automatically calculate the correct box size that fits your products and save you a lot of hassle.
  * **Stack Packing**  
An advanced packing method based on the total height of the products, where the plugin calculates the correct box suitable for your products by stacking up all the products to a certain height.
  * **Quantity Based Packing**

* * *

** _Reference_**  
For More Details on Configuring Shipping Boxes Read – [WooCommerce Parcel Packing Methods](https://www.pluginhive.com/knowledge-base/setting-up-woocommerce-shipping-services/#configure_shipping_boxes_select_parcel_packing_method).   

* * *

### Display Purolator shipping rates on the WooCommerce cart & checkout page

Visit the WooCommerce shop page and add a product to the cart. Enter the shipping address and calculate the shipping cost. The plugin will display the shipping cost for all the available Purolator shipping services or the shipping services that you have selected based on your preference.

* * *

* * *

#### a. Verify the shipping cost displayed on the WooCommerce cart page

After displaying the shipping rates on the WooCommerce cart page, verify whether the shipping cost is accurate by visiting the **Settings > Shipping Rates > Request Log**

* * *

* * *

Click on the **(i) icon** in front of the most recent Shipping Rate Request, as shown below.

* * *

* * *

After viewing the request log, you can verify the following under this section,

**Package Details** – includes the product name, quantity, weight, cost, type of packaging method as shown below.

* * *

* * *

**Shipping Methods** – includes the shipping carrier(s), all the enabled shipping services, shipping cost for the available services, and estimated transit days for the shipment, as shown below.

* * *

* * *

Once you have verified both the package details and the shipping methods, you can proceed to place the order.

* * *

**_Note_**  
In case you do not see your preferred shipping service at the WooCommerce cart page, or get this message, **“No shipping options were found”**  
* Verify the package details  
* Verify the shipping methods  
* Click on the error dislayed for the preferred shipping services  

* * *

### Place test orders choosing different Purolator shipping methods

After complete verification of the packages, shipping services as well as shipping cost, place a few orders using different Purolator shipping services of your preference.

Now visit the **Shipping** tab from your WordPress Dashboard. Under the orders section, the plugin will automatically import all the WooCommerce orders that are marked as Processing and display it as shown below.

* * *

* * *

  * WooCommerce order ID
  * Date of purchase
  * Customer Name
  * Customer’s shipping address
  * Shipping carrier & shipping service
  * Order status
  * Order subtotal and the mode of payment
  * Shipping cost
  * Number of packages or boxes required for the shipment
  * Shipping date
  * Order summary displaying all the details like product list, total weight, all available shipping services, etc. 

* * *

**_Note_**  
The plugin will automatically import all the **PROCESSING** orders. In case the WooCommerce order status is not **PROCESSING** , you will be required to change the order status to **PROCESSING** manually from the WooCommerce Orders page.  

* * *

### Review the Purolator shipping services selected automatically for the orders

* * *

By default, the orders are assigned those shipping services which are selected by the customers while placing the orders.

However, if the order has been placed using another shipping method like **Free Shipping, Flat Rate Shipping, or any third-party shipping method** , the plugin **automatically assigns the cheapest available shipping service** across all the shipping carriers that you have configured within the plugin.

In the image below, you can see that Purolator is the shipping carrier and Purolator Ground is the shipping service assigned to the order.

* * *

* * *

In order to verify the shipping carrier and the service assigned to the order, click on the **(i) icon** under the **Order Summary** for that order.

Under the **Rate Summary** section, you can see the same Purolator Ground being marked as **Customer Selected** , and hence assigned to the order for fulfillment, as shown in the image below.

* * *

* * *

### Make the correction and reprocess the order if the order status is stuck as “Initial” with errors

** _Reference_**  
For More Details on Correcting Errors & Reprocessing Orders Read – [Reprocessing WooCommerce Orders](https://www.pluginhive.com/knowledge-base/setting-up-woocommerce-shipping-services/#make_corrections_reprocess_orders_on_initial_with_error).   

* * *

### Verify the payment method & the Purolator shipping cost for the order

Once the orders are in Processing status and are ready for fulfillment, verify the payment method of the WooCommerce orders, as the shipping cost varies for different payment methods.

You can check the payment method of the order by clicking the (i) icon in the **Order Summary** and visiting the **Order Details** section, as shown below.

* * *

* * *

Once the payment method is verified, you can visit the **Rate Summary** to review the shipping cost for every Purolator shipping service that you will pay based on the payment method, as shown below.

* * *

* * *

### Print the Purolator shipping labels for your WooCommerce order(s)

Visit the **Orders** tab and select the order(s) for which you want to generate and print a shipping label, and click on **Generate Labels** , as shown below.

* * *

* * *

Select the order(s) again and click on **Print Labels to** get the shipping labels for your orders, as shown below.

* * *

* * *

The plugin will automatically redirect you to print the shipping labels along with other documents like the tax invoice, as shown below.

* * *

* * *

### Request Purolator pickup from within WooCommerce

Once your orders are ready for shipping, WooCommerce Shipping Services allow you to request the **[Purolator pick up](https://www.pluginhive.com/purolator-pickup-woocommerce-shopify/)** from within your WooCommerce store.

Visit the **Orders** tab and select all the orders for which you want to request the carrier pickup. Now click on the **Request Pickup** option, as shown below.

* * *

* * *

Once the pickup is requested successfully, you can visit the **Pickup** tab to view the status of the pickup, as shown below.

* * *

As you can see, you can view the pickup status as well as cancel the pickup based on your requirements.

* * *

### Fulfill orders and send WooCommerce Order Completion Email to customers along with the Purolator tracking details

After requesting the pickup, you can visit the **Orders** tab and select all the orders which are ready to be shipped, and click on **Mark As Shipped** to fulfill these orders.

* * *

* * *

Once you mark the orders as shipped, your WooCommerce orders will be automatically marked as **Completed**. Visit the **WooCommerce > Orders **page to check the order status and click on the order.

In the image below, you can see the order is automatically marked as completed. Also, the shipment tracking details are automatically updated to the WooCommerce orders.

* * *

* * *

As for the customers, WooCommerce Shipping Services automatically sends the tracking details to the customer via the WooCommerce Order Completion Email, as shown in the image below.

* * *

* * *

### Print order manifest for the carrier pick up personnel

WooCommerce Shipping Services also allows you to print the shipping manifest for your shipping carrier pickup personnel, which you can print directly from your WooCommerce store.

Visit the Manifest tab and click on the Print icon to get the shipping manifest, as shown below.

* * *

* * *

As you can see in the image below, the manifest generated will have the following details.

  * Airwaybill Number
  * WooCommerce Order Number
  * Payment Method
  * Attention (customer) Name and Contact Number
  * Customer’s City
  * Product Name and Quantity
  * Package Weight and Dimensions
  * Barcode Airwaybill

* * *

* * *

### Monitor the shipment tracking status of your orders

To track your orders, select the orders that are shipped and click on **Track Your Shipments**. Or, you can track all the orders by visiting the **Tracking** tab, where the plugin will display the live tracking status of all the shipments, as shown below.

* * *

* * *

### Frequently Asked Questions

Here are the answers to some of the frequently asked questions to help you understand this plugin better.

#### a. I see there is a mismatch in rates while comparing the rates shown in the app and my account rates with the carrier. What can be the reason?

The rates mismatch could happen due to incorrect or missing configurations in the Ship From Address, Ship To Address, Weight, Dimensions, Package Type, or the Carrier Services & Rates.

* * *

**_Reference_**  
For More Details on How to Fix Rates Mismatch Read – [Inaccurate Shipping Rates at WooCommerce Checkout](https://www.pluginhive.com/knowledge-base/troubleshooting-woocommerce-shipping-services/#inaccurate_shipping_rates_on_woocommerce_cart_checkout_page).   

* * *

#### b. I ship around 50-100 orders per day. Generating labels one by one is not feasible for my business. Does this plugin help automate the process for me in any way?

Absolutely!

The plugin can automate the process of generating shipping labels as soon as your orders come in. Based on the shipping services selected by the customers, the plugin will generate the labels automatically.

All you need to do is select the orders in bulk and print 100s of labels in a single click.

* * *

#### c. We ship from multiple warehouses. Will this plugin help me set up my shipping from multiple warehouses?

Yes! The plugin allows you to set up multiple addresses for your warehouses. Based on your business requirements, the plugin allows you to create different automation rules, as shown below.

* * *

* * *

You can see in the image the plugin will ship the products from the US warehouse and use the US-based Purolator shipping services to display rates and generate shipping labels.

* * *

#### d. Does this plugin allow me to configure my print label settings and will I be able to change the shipping document printing preference?

While printing shipping documents like Purolator shipping labels, Commercial Invoices, Tax Invoices, Return Labels, etc. the plugin allows you to customize the print layout as well as choose the number of copies that you want to print.

All you need to do is visit the**Settings > General Settings > Print Settings** and modify the document print layout and the number of copies, as shown below.

You can also view the printing layout by clicking the “Preview” button as shown below.

* * *

**[WooCommerce Shipping Services](https://www.pluginhive.com/woocommerce-shipping-services/)** by PluginHive automates Purolator shipping for your WooCommerce store and helps you fulfill your orders from within your online store, without any hassle.

Feel free to contact the **[PluginHive customer support](https://www.pluginhive.com/support/)** team if you require further assistance with the plugin.

[ Previous  Multi-Vendor Shipping with WooCommerce Shipping Services  ](https://www.pluginhive.com/knowledge-base/multi-vendor-shipping-using-woocommerce-shipping-services/)

[ Next  Setting Up WooCommerce Shipping Services For FedEx  ](https://www.pluginhive.com/knowledge-base/set-up-woocommerce-fedex-shipping-services/)
