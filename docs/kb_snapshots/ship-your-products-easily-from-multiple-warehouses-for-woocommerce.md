# Ship your Products from Multiple Warehouses in WooCommerce

**Source:** https://www.pluginhive.com/knowledge-base/ship-your-products-easily-from-multiple-warehouses-for-woocommerce/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Ship your Products from Multiple Warehouses in WooCommerce

Store owners often provide shipping from more than one warehouse. The reason is the large volume of orders and the various shipping destinations that they have to cover. In addition, shipping items from multiple warehouses results in lower shipping costs as the distance is decreased significantly.

However, the option to accommodate multiple warehouses is not provided by WooCommerce by default. As a result, it is not very easy to handle such cases where the store owners have more than one warehouse. Here we’ll discuss the setup of the Add-On that enables the Ship From Address to be changed solely based on the Destination Zip entered in the cart.

* * *

### Changing Ship From Address for Warehouses based on the Destination Address in WooCommerce

#### Business Case:

_**I have two warehouses that are located in New York and California. I have noticed that the shipping rates are higher and more expensive when I’m shipping from California to New York or vice versa. I would like to have my customers receive lower shipping rates by having the ‘Ship From’ address change to my secondary warehouse based on the ‘Ship To’ address and Zipcode mentioned while checking out.**_

_**Is there any way to do this?**_

####  Solution:

This business case requires a change of the ‘Ship From’ address based on the ‘Ship To’ address that is entered in the Cart page.

Using the [WooCommerce UPS Shipping plugin](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) and a **WooCommerce UPS Multi-Warehouse Shipping Add-On** , you can provide the ship from address of your warehouse based on the destination address entered. You can easily [**download**](https://www.pluginhive.com/tailor-made-woocommerce-shipping-solutions/#woocommerce_multi_warehouse_shipping) the addon.

To configure the **Add-On** so that the Ship From address changes based on a particular Ship To address, you will have to follow the steps listed below:

  * Make sure the [WooCommerce UPS Shipping plugin](https://www.pluginhive.com/knowledge-base/setting-woocommerce-ups-shipping-plugin/) is configured accordingly.
  * Next, proceed to the Plugin page and navigate to **Add a New Plugin > Upload Plugin > (**_select the add-on from the downloads folder_**) > Install & Activate**
  * Now, head to the Add-on and configure it in the following manner.
    * Begin by entering the Destination Zip code (ex., **Zip code 90202**) that is to bring around the change in the Ship From address.
    * Make sure the **Address** , **City** , **Country** , **State Code,** and **Postal Code** for the secondary **Ship From** address are filled in.
    * Save the page and proceed to the store and add an item to the cart, and enter the shipping address (a zip code that has not been specified in the add-on). By doing so, the request that is sent to UPS will be with the primary Store Ship From address.
    * Now, enter the zip code that has been saved in the **Add-o,n** and the complete **Ship From** address changes based on the **Destination Zip** entered in the cart.

* * *

  * This add-on permits multiple zip codes to be set and saved so that when customers from those zip codes start purchasing items from the store, the Add-On will automatically change the Ship From address and thus resulting in slightly lower rates and easier shipping methods for that customer.

***An example of this solution is where we’ve entered the Ship To address as California 90211, and the Ship From address remains as the primary store address. However, when the Ship To Zip code is changed to 90202, the Ship From address changes to the one configured in the Add-On (_shown below_)

***Another piece of information to remember is that this add-on accepts wildcard entries, you need to use star (*) for a wildcard entry and a comma (,) as a separator

Other Zip Code – 90211 that is not configured in the Add-OnZip code 90202 results in the Ship From address changing to the address configured in the Add-On

The UPS shipping rates will be displayed on the Checkout page based on the location. Other than that, the WooCommerce UPS Shipping plugin has a ton of other amazing features. You have features like generating shipping labels in bulk, order tracking, and much more…

* * *

## Summary…

In this article, we discussed the [**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) and how you can handle the shipping of your products from multiple warehouses.

With increasing volumes of orders, it is very common to see store owners shipping from multiple warehouses. Upon using the **WooCommerce UPS Shipping plugin** along with the **Change Shipping From Address based on Postcode** , online store owners can easily make sure their shipments will be delivered successfully from a dedicated warehouse based on the **Destination address**.

If you have any suggestions regarding the article, feel free to share your views in the comment section below. And if you have any queries regarding the plugin or the App, feel free to**[contact our customer support](https://www.pluginhive.com/support/)**.

[ Previous  WooCommerce UPS COD for Europe – Automatically convert the currency into Euro  ](https://www.pluginhive.com/knowledge-base/woocommerce-ups-cod-for-europe-automatically-convert-the-currency-into-euro/)

[ Next  How to allow Customers to Download UPS labels from an Online Repair Shop  ](https://www.pluginhive.com/knowledge-base/how-to-allow-customers-to-download-ups-labels-repair-shop/)
