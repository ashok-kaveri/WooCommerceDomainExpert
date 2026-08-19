# UPS and USPS – Display WooCommerce Shipping Rates with Price Adjustment

**Source:** https://www.pluginhive.com/knowledge-base/ups-usps-display-woocommerce-shipping-rates-with-price-adjustment/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# UPS and USPS – Display WooCommerce Shipping Rates with Price Adjustment

In this article, we will cover domestic and international shipping for two of the best shipping carriers in the US, UPS, and USPS, with the help of the WooCommerce Multi-Carrier Shipping plugin. This article will also cover shipping rates adjustment based on the cart subtotal, and how you can add it to the real-time shipping rates from the two shipping carriers.

* * *

## Business Case…

Shir owns a shop that receives customers from all over the world. Shir would like for the plugin to provide multiple rates based on the address keyed in on the cart page (based on whether it is a domestic or international shipment). She would also like to add extra shipping charges based on the amount the customer purchases from her website.

According to Shir,” _**…After the buyer has entered in their shipping address, the shipping options should populate based on domestic or international. The customers should be able to choose which option for shipping they would want to use depending on the shipping location. For domestic shipping, the options available should be,**_

  * _**First Class Mail (via Stamps)**_
  * _**Priority Mail (via stamps)**_
  * _**UPS Ground**_
  * _**UPS Express Saver**_

 _**And for international shipments,**_

  * _**USPS Priority international (via stamps)**_
  * _**UPS Worldwide**_

 _**Also, I require additional shipping cost $0.05 per unit amount in the cart subtotal. Is this possible with the Multi-Carrier plugin..?**_ ”

* * *

## Solution…

So Shir can easily achieve her business case with the help of the [**WooCommerce Multi-Carrier Shipping plugin**](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/). However, she will have to use the following features of the plugin in order to set it up to her specifications.

### Shipping Area Management

Shipping Area Management contains all the shipping zones, and destination address selection fields like the Country, States, Shipping Zones, and ZIP Codes. In the case of Shir, she will have to configure the Zone matrix in the Shipping Area Management tab as shown below.  

### Additional Cost Per Unit of the Cart Subtotal Price

Using the WooCommerce Multi-Carrier Shipping plugin, it becomes very easy to customize the shipping calculations and add an extra cost based on the cart value. The plugin supports flat-rate cost which can be added to the final shipping cost either for a price range, say 0 to $100, or per unit of the cart subtotal.

* * *

## How to Setup Domestic and International Shipping with UPS and USPS..?

  * After successfully [**installing and activating**](https://www.pluginhive.com/knowledge-base/how-to-download-install-update-woocommerce-plugin/) the WooCommerce multi-Carrier Shipping plugin, visit the plugin settings by clicking on the **Settings** option in the plugins page, or by visiting **WooCommerce = > Settings => Shipping => Shipping Area Management**
  * Create **2 Shipping Zones** ,
    * **United States – Targetting all states in the US**
    * **Everywhere**
  * Now set up 2 different areas in the **Shipping Area Management** for both these zones.
  * Once the Shipping Areas have been configured, proceed to the **Shipping Rules** and create the rules in the Multi-Carrier plugin based on your shipping requirements.
  * In the case of Shir, the shipping rules will be similar to the ones shown below.  

* * *

    * **Method Title** – The name of the service which will display on the cart/checkout page.
    * **Method Group** – The group classification of the services. When groups are enabled you will be able to view all the rates individually rather than just the one at the top.
    * **Area List** – Used to select the targeted area. For example – If a customer from Any Other Country apart from the US arrives on the cart page, they will receive USPS Priority Worldwide and UPS Worldwide which they will choose from.
    * **Shipping Class** – Used to pick the Shipping class which would be applicable for this method. We’ve chosen **Any Shipping Class** because Shir would like all the products to be available for domestic and international orders.
    * **Product Category** – Used to choose the particular product category that would be primarily used for that particular shipping method. Again, we’ve selected **Any Product Category** as all the categories will get applied to the Method chosen.
    * **Shipping Options** – Select the Shipping Option (Carriers names) from the drop-down
    * **Service** – Provides the list of services available with the Shipping Carrier. For Example, upon selecting UPS you will receive all UPS services listed in the drop-down, as shown below.  

* * *

    * Upon configuring the plugin in the above-mentioned manner, the UPS and USPS rates will populate on the cart and the checkout page for domestic as well as international shipments. 
    * ****For a D omestic Shipment to Bel Air (90210)  
****

* * *

**  
**

    * ****For an International Shipment to Calgary (T1Y 1A1)  
****

* * *

**  
**

  * Read more about [**how to set up the WooCommerce Multi-Carrier Shipping plugin**](https://www.pluginhive.com/knowledge-base/setting-multi-carrier-shipping-plugin-woocommerce/).

**NOTE: Kindly ensure your Credentials for all the carriers are correct and valid.**

* * *

## How to Add Additional Shipping Cost Based on the Cart Subtotal..?

Now we come to the second half of Shir’s requirement where she requires additional shipping cost based on the cart subtotal. In order to set up this scenario, just edit the shipping rules and fill the following settings in the shipping rule table.

  * **Based on** – This field defines the shipping rate calculation and will be based on either the weight, price, or quantity of the products on the cart page
  * **Min-Max** – Provide the range of the price/weight/quantity of the products in the cart page
  * **Cost Per Unit** – Set the cost adjustment based on the above factors.

In Shir’s case, she requires an additional $0.05 per unit cost, which can be set in the Cost Per Unit field, as shown in the image below.  

* * *

  * ****Domestic Shipping rates after the shipping rate adjustment  
****

* * *

**  
**

  * **International Shipping rates after the shipping rate adjustment  
**

* * *

## Final Thoughts…

In this case, we discussed the [**WooCommerce Multi-Carrier Shipping plugin**](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/) and how while using the plugin you can easily set up a complex shipping scenario where orders will be shipped domestically and internationally.

WooCommerce Multi-Carrier Shipping plugin supports free shipping and flat rate shipping along with real-time shipping rates from UPS, USPS, DHL, FedEx, and Stamps.com. This makes it the perfect option for store owners who are looking for a robust shipping solution to handle their complex shipping scenarios with multiple shipping carriers.

[ Previous  Setting up FedEx Account  ](https://www.pluginhive.com/knowledge-base/setting-fedex-account/)

[ Next  WooCommerce Shipping – Configure Shipping Area Management for Multiple Carriers  ](https://www.pluginhive.com/knowledge-base/woocommerce-shipping-configure-shipping-area-management-multiple-carriers/)
