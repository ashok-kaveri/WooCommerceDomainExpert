# Adjust WooCommerce FedEx Shipping Rates by Shipping Class

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-shipping-fedex-live-rate-adjustment-based-on-shipping-classes/
**Platform:** WooCommerce (WordPress)
**Plugin:** fedex
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Adjust WooCommerce FedEx Shipping Rates by Shipping Class

This article will cover an interesting shipping scenario involving WooCommerce Flat Rate Shipping along with adjusting the WooCommerce FedEx Shipping Rates with the help of the **[WooCommerce FedEx Shipping plugin](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)**.

* * *

## Why adjust WooCommerce FedEx shipping rates

Charles owns a WooCommerce store and has an interesting shipping scenario. According to Charles,

“** _I have 2 products in the cart. One with a flat rate shipping of $8 and the other which I generally ship via FedEx. The shipping cost is generally $30 for Standard Overnight delivery._****_What I want to display to the customer is a combined value of both the rates $8 and $30 on the cart/checkout page._****_So, $38 for Standard overnight must display instead of $30. Is this possible..?_** “

* * *

## How to do it

This scenario can be easily achieved using the following,

  * **[WooCommerce FedEx Shipping Plugin](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)**
  * [**Skip Shipping Class from Shipping Calculation Add-on plugin**](https://www.pluginhive.com/wp-content/uploads/2019/12/ph-skip-shipping-calculation.zip)
  * [**Hide WooCommerce Shipping Methods & Rate Adjustment**](https://www.pluginhive.com/product/hide-woocommerce-shipping-methods-and-rate-adjustment/)
  * [**Custom Code**](https://www.pluginhive.com/knowledge-base/add-additional-cost-shipping-service-based-shipping-class/)**to Add Flat Rate Shipping Cost to a WooCommerce Shipping Method based on Shipping Classes**

* * *

### Pre-Requisites

To set up this scenario, you would require the following

* * *

#### Create Shipping Classes

Based on the requirements, create two shipping classes and assign products to both of them

  * **Flat Rate Shipping Class**  
This shipping class will include all the products which you want to ship and charge a flat rate shipping fee
  * **Standard Shipping Class**  
This shipping class will include all the products which you want to ship via FedEx

* * *

#### Shipping Class Slug

Every WooCommerce Shipping Class has a unique slug which you can find by visiting,

**WooCommerce = > Settings => Shipping => Shipping Class.  
**

Copy the Shipping Class Slug for the Flat Rate Shipping Class.

* * *

#### Shipping Method Value on the Cart Page

You need to get the Shipping Method Value for all the shipping methods for which you want to add the Flat Rate Charge to the shipping cost. To find the value of a shipping method on the cart page, 

  * **Right Click** on the shipping method on the cart page and click on **Inspect**
  * Copy the **Value** as shown in the image below  

* * *

### How to Adjust WooCommerce FedEx shipping rates

To set up this scenario, you need to follow the steps below.

  * [**Install and activate**](https://www.pluginhive.com/knowledge-base/how-to-download-install-update-woocommerce-plugin/) the **WooCommerce Shipping Plugin for FedEx** on your WooCommerce store
  * [**Set up the plugin**](https://www.pluginhive.com/knowledge-base/setting-woocommerce-fedex-shipping-plugin/) based on your requirements and enable the **FedEx Shipping Services** which you want to offer on your website
  * Install the [**Skip Shipping Class from the Shipping Calculation Add-on plugin**](https://www.pluginhive.com/wp-content/uploads/2019/12/ph-skip-shipping-calculation.zip)
  * Click on Settings and visit the plugin settings  

  * Enable the **Skip Shipping Class** option.
  * Select the **Flat Rate Shipping Class** under the Shipping Class option. This will skip all the products in that shipping class from the FedEx shipping rates calculation  

  * Click on **Save Changes**
  * [**Download and Install**](https://www.pluginhive.com/product/hide-woocommerce-shipping-methods-and-rate-adjustment/) the PH Hide WooCommerce Shipping Methods and Rate Adjustments plugin
  * [**Set up**](https://www.pluginhive.com/hide-woocommerce-shipping-methods-complete-tutorial/) an add-on plugin
    * In this case, since products in the FedEx Shipping Class do not require Flat Rate Shipping
    * Choose the **FedEx Shipping Class** under the Shipping Class section
    * Enter the value of the Flat Rate shipping method under the Shipping Method option. This will hide the Flat Rate Shipping Method whenever the products having FedEx Shipping Class are there in the cart  

  * Add the [**custom code**](https://www.pluginhive.com/knowledge-base/add-additional-cost-shipping-service-based-shipping-class/) to the **Functions.php** file by visiting, **Appearance = > Editor => Functions.php**
    * Enter the shipping method values of all FedEx Shipping Services
    * Add the Flat Rate cost 8 in the code
    * Enter the Flat Rate Shipping Class Slug in the section shown below
    * Save the code  

* * *

## Shipping Scenario

  * **Case1: When FedEx Products are in the cart**  
  
  

  * **Case2: When Flat Rate Product is in the cart**  

  * **Case3: Both FedEx and Flat Rate Products are in the cart**  
  
Thus, when you have both FedEx and Flat Rate products in the cart, the flat rate of $8 will get added to the FedEx Ground.  
Hence, the final cost is **$23.74 + $8 = $31.74** as shown in the screenshot above.

* * *

## Final Thoughts

This article covers multiple shipping solutions developed to make life easier and handle complex shipping scenarios for WooCommerce store owners. Feel free to use the solutions provided in this article and let our [**shipping experts**](https://www.pluginhive.com/support/) know if you face any issues.

You can read more about our **[WooCommerce FedEx Shipping Plugin](https://www.pluginhive.com/product/woocommerce-fedex-shipping-plugin-with-print-label/)**. This plugin comes with a bunch of amazing features like real-time shipping rates, shipping labels, shipment tracking, FedEx pickup, and much more.

_**Happy selling!**_

[ Previous  How to Pack a Product into Multiple Packages on WooCommerce  ](https://www.pluginhive.com/knowledge-base/pack-multiple-packages-using-woocommerce-fedex-shipping-plugin/)

[ Next  How to Pack Items Based on Weight?  ](https://www.pluginhive.com/knowledge-base/pack-items-based-weight/)
