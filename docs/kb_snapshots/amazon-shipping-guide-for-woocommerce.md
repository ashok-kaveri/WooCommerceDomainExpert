# WooCommerce Amazon Shipping Guide

**Source:** https://www.pluginhive.com/knowledge-base/amazon-shipping-guide-for-woocommerce/
**Platform:** WooCommerce (WordPress)
**Plugin:** amazon-shipping
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce Amazon Shipping Guide

> This guide will help you integrate your Amazon Shipping account with your WooCommerce store using the [WooCommerce Shipping Services Plugin](https://www.pluginhive.com/woocommerce-shipping-services/) by PluginHive. Once you have successfully integrated Amazon Shipping with WooCommerce, you will be able to automatically display Amazon Shipping rates at checkout, print shipping labels, and easily track your shipments.

* * *

## **Add, Install, and Activate WooCommerce Shipping Services Plugin**

Install the [WooCommerce Shipping Services](https://www.pluginhive.com/woocommerce-shipping-services/) Plugin.

**Reference** : [How to install and activate the WooCommerce Shipping Services Plugin](https://www.pluginhive.com/knowledge-base/setting-up-woocommerce-shipping-services/#download_install_activate_plugin)

* * *

## Add your Amazon Shipping Account 

Go to the **Plugin** **Settings** → **Carrier (+) icon** as shown below:

* * *

Select the carrier **“Amazon Shipping”** & Click on **“Add Account”** as shown below.

* * *

In the Account Details, select the **“Country of Origin”** from the drop-down menu and click on the **Connect** button to connect your Amazon Shipping account with the WooCommerce Shipping Services Plugin.

* * *

You will be redirected to the Amazon Shipping Sign-in page. Enter your Amazon Shipping registered email ID or phone number below and click on **‘Continue’.**

* * *

Enter the password and click on **‘Sign in’.**

* * *

**_Note_**  
  

If you don’t have Amazon Seller Central login credentials, then you need to register for Shipper Central:

  * For India: [**Register here**](https://shipping.amazon.in/?ref_tag=SWA_IN_Referral_plugnhive_24)
  * For the US: [**Register here**](https://shipping.amazon.com/)
  * For the UK: [**Register here**](https://shipping.amazon.co.uk/)
  * For France: [**Register here**](https://shipping.amazon.fr/)
  * For Italy: [**Register here**](https://shipping.amazon.it/)
  * For Spain: [**Register here**](https://shipping.amazon.es/)

* * *

Click the checkbox to allow WooCommerce Multi Carrier Shipping Label to access your Amazon Shipping account, then click ‘**Authorize** ‘

* * *

Upon successful registration, you will see the **Registration successful** message displayed below.

* * *

Once the registration is successful, the carrier account number automatically gets added to the carrier account details.

* * *

**Now you can access Amazon Shipping services using the plugin.** The plugin allows you to display Amazon Shipping rates, generate and print shipping labels in bulk, and track Amazon Shipping in real time.

* * *

## Verify the Shipper or Warehouse Address

Once you add the Amazon Shipping account, verify the shipper address details. Ensure your warehouse address matches the one you set up in your Amazon Shipping Shipper Central account.

* * *

**_Note_**  
  

The address must be within the respective country to where you’re shipping. Amazon Shipping currently doesn’t support cross-border shipments

* * *

Click on the **(≡)** icon and visit **Settings > Address** and your store name will be listed there.

* * *

Click on the store name and you can see the shipper address and other details as shown below.

* * *

Review the shipper details. If changes are needed, make them and click “**Save.** “

* * *

** _Note_**  
  

Please ensure the address entered is accurate, as it will be used to calculate shipping rates at the checkout page. Additionally, make sure to include the “Company Name” field, as Amazon Shipping uses this information to display your company name on the tracking portal and in any email communication related to your shipments.

* * *

## Configure Weight & Dimensions for Your Products and Choose the Right Packaging Method

To calculate the accurate shipping rate for an order, you must configure the product’s weight correctly.

**Reference** : [How to Configure the weight & dimensions for products and choose the right packaging method](https://www.pluginhive.com/knowledge-base/setting-up-woocommerce-shipping-services/#configure_product_weight_dimensions)

* * *

## Opt for the Preferred Amazon Shipping Services to be Displayed at the WooCommerce Checkout

The plugin automatically displays all the available Amazon Shipping rates on the WooCommerce checkout page. However, if you want to display shipping rates for a particular Amazon Shipping service on your WooCommerce checkout, you can do so using the Rate Automation functionality.

Click on the **(≡)** icon and visit **Settings > Shipping Rates > Rate Automation**, as shown below.

* * *

The plugin automatically creates rules for the shipping carriers that you add to help you choose the services that will be displayed on the WooCommerce store. Click on **Edit** to customize the shipping automation rules based on your preferences.

* * *

By default, the **“Any”** condition is selected in the automation criteria, which applies to all cases. Under the Action Details tab, the respective carrier, along with **“All”** services, will be selected by default.

* * *

However, if you want to select your preferred Amazon Shipping service(s) that you want to display to your customers, then you may do as shown below:

* * *

However, you can always choose to calculate and display shipping rates for the above-selected shipping service(s) based on various conditions, such as,

  * WooCommerce Shipping Zones
  * The product quantity that the customer chooses
  * Total weight of all the products
  * Cart sub-total amount
  * Shipping Classes
  * Time of order placement
  * Total weight range
  * Total price range

Based on your preference, you can select any conditions and the plugin will calculate the shipping rates only if the conditions are matched.

* * *

Click on the “**Update Rule** ” once the required changes are made, as shown below.

* * *

## Display Amazon Shipping rates on the WooCommerce checkout

Visit the store and add a product to the cart. Enter a shipping address and calculate the shipping cost. The Plugin will display the shipping cost for all the available Amazon Shipping services or the shipping services that you have selected based on your preference at WooCommerce checkout.

* * *

**_Note_**  
  

  * Shipping rates are calculated based on product weight, dimensions, shipping origin and destination, packaging type, and selected special services (if any).
  * Here’s a summary of the Amazon Shipping services available in different countries:

Country| Service ID| Service Name| Carrier ID| Carrier Name  
---|---|---|---|---  
United States| std-us-swa-mfn| Amazon Shipping Ground| AMZN_US| Amazon Shipping  
United Kingdom| SWA-UK-PREM| Amazon Shipping One Day| AMZN_UK| Amazon Shipping  
United Kingdom| SWA-UK-2D| Amazon Shipping Two Day| AMZN_UK| Amazon Shipping  
Spain| SWA-ES-PRIME-PREM| Amazon Shipping Express| AMZN_ES| Amazon Shipping  
Italy| SWA-IT-PRIME-PREM| Spedizione nazionale express| AMZN_IT| Amazon Shipping  
France| SWA-FR-PRIME-PREM| Amazon Shipping One Day| AMZN_FR| Amazon Shipping  
India| SWA-IN-OA| Amazon Shipping Standard| ATS| Amazon Shipping  
  
* * *

## Verify the Shipping Cost Displayed on the WooCommerce Checkout Page

If you encounter any issues, review the logs for more information. If a deeper investigation is needed, you can share the logs with Amazon Shipping support. You can check the logs by going to**Settings > Shipping Rates > Request Log.**

* * *

Click on the **(i) icon** in front of the most recent Shipping Rate Request, as shown below.

* * *

After viewing the request log, you can verify the**Items,** **Package Details** & **Shipping Methods** under this section:

* * *

## Print the Amazon Shipping Labels for your WooCommerce Orders

Visit the **Orders** tab and select the order(s) for which you want to generate and print a shipping label, and click on **Generate Labels** , as shown below.

* * *

Select the order(s) again and click on **Print Labels to** get the shipping labels for your orders, as shown below.

* * *

The plugin will automatically redirect you to another page to print the shipping labels along with other documents like the tax invoice as shown below.

* * *

**_Note_**  
  

Pickup window should be pre-scheduled before attempting to generating a shipping label. In case of any issues in setting up the pickup window in Amazon Shipping Shipper Central, please contact Amazon Shipping support using your Shipper Central help pages.

* * *

## Mark Orders as Fulfilled and Automatically Send Amazon Shipping Tracking Details to your Customers via Email

After generating and printing the label(s), you can visit the **Orders** tab & select all the orders that are ready to be shipped, and click on **Mark As Fulfilled** to fulfill these orders.

* * *

Once you mark the orders as fulfilled in the plugin, your WooCommerce orders will be automatically marked as completed. You can visit the **WooCommerce** **> Orders** page to check the order status and click on the order. In the image below, you can see the order is automatically marked as completed. Also, the shipment tracking details are automatically updated for the WooCommerce orders.

* * *

For the customers: The WooCommerce Shipping Services plugin automatically sends the tracking details to the customer via the WooCommerce Order Shipped Email, as shown in the image below.

* * *

## Track your Amazon Shipping Orders 

To track your orders, select the orders that are shipped and click on **Track Your Orders**. Or, you can track all the orders by visiting the **Tracking** tab, where the plugin will display the live tracking status of all the shipments, as shown below.

* * *

If you face any issues or have any queries on setting up the plugin, feel free to [**contact our support**](https://www.pluginhive.com/support/).

[ Previous  Setting Up WooCommerce Shipping Services For FedEx  ](https://www.pluginhive.com/knowledge-base/set-up-woocommerce-fedex-shipping-services/)

[ Next  Troubleshooting WooCommerce Shipping Services  ](https://www.pluginhive.com/knowledge-base/troubleshooting-woocommerce-shipping-services/)
