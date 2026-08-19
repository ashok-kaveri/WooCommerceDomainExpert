# How to resolve differences between rates returned by the plugin and the UPS shipping calculator

**Source:** https://www.pluginhive.com/knowledge-base/difference-rates-returned-plugin-ups-shipping-calculator/
**Platform:** WooCommerce (WordPress)
**Plugin:** ups
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# How to resolve differences between rates returned by the plugin and the UPS shipping calculator

Many of our customers complain about noticing differences in rates while using [**WooCommerce UPS Shipping plugin**](https://www.pluginhive.com/product/woocommerce-ups-shipping-plugin-with-print-label/) compared to the rates calculated on the UPS shipping calculator.

Here are some of the possible reasons for this:

  * The type of parcel packing you choose
  * Including tax on shipment
  * Customer Classification of rates
  * Negotiated Rates
  * Any price adjustment in services and packaging

Let’s look into each…

**The type of parcel packing you choose decides how UPS will charge you on the shipping.**

The UPS plugin has 3 types of packaging:

a) **Pack items Individually** – Here, since packaging happens individually, the rates come in  
multiples if more than one item is present in the cart.

Let’s take an example: An item with weight = 3lbs, dimensions = 15′ X 12′ X 4′ inch.

* * *

Let’s say the shipping rate for the above item is $35.52.

Shipping rate for 1 item in the cart

* * *

If we add one more item to the cart, the shipping rate also doubles; since there are two separate packages.

Two items packed individually

* * *

b) **Pack into boxes with weights and dimensions** – The rate is shown for a custom-defined box with items in  
it. Once you select the Box Packing option, settings for weight and dimensions are displayed. Click **Add Box** to set up the dimensions of the Box. Enter the following fields:

  * **Length** : Enter the required length of the box.
  * **Width** : Enter the required width of the box.
  * **Height** : Enter the required height of the box.
  * **Box Weight** : For heavy packing boxes, enter the weight of the box as well, so that it gets considered while packing items into the customized box.
  * **Max Weight** : Enter the maximum weight allowed per box.
  * **Enabled** : Select the checkbox to avail the box for packing.  
**Note** : Unit of Dimensions and weight are the same as in the General Settings.
  * Click **Remove Selected Box(es)** to delete the selected customized box from the Box Size settings.

All the cart items are packed into custom boxes defined in the Box Size settings. The best-fit box is auto-chosen from the customized boxes.

Since we have two units of the same item in the cart, stacking them together will be easy since they are of equal length and breadth. Only the height will increase. After stacking the two items, the new dimensions will be 15 x 12 x 8 and the weight will be 6 lbs. Now we need to define the custom box with weight and dimensions to fit these two items, as shown below.

* * *

The shipping cost will be charged based on the weight and box dimensions above. A screenshot of the shipping rates in the cart for the above box is shown below.

* * *

c) **Weight-based** – Here the rate is fetched completely based on the weight of the shipment. With two items on the cart, we have a total weight of 6 lbs. Based on weight, below is the screenshot of the shipping rates in the cart.

Thus can see the differences in shipping rates based on the type of parcel packing we choose. Again these differences depend totally on the source and destination, and also on the size and weight of the items.

**Including tax on shipment on the UPS, plugin will increase the shipment rate.**  
This criterion is applicable only to certain countries which charge extra tax on shipping. And the percentage of tax charged depends on the country’s tax laws.

**Rates are based on Customer Classification of rates.**

The rates may differ based on the customer classification that you choose on the UPS settings. The available options in the Customer Classification drop-down are as follows:

  * Rates Associated with Shipper Number
  * Daily Rates
  * Retail Rates
  * Standard List Rates

**Note:** You need to confirm your specific customer classification code with your UPS Account representative to set corresponding rates under this section.

The UPS price calculator shows different rates based on these selections. Below are the screenshots of the shipping rate differences based on Customer Classification.

Customer Classification- Rates associated with the shipper number

* * *

Customer classification – Daily Rates

* * *

Customer Classification – Retail Rates

* * *

Customer classification – Standard List Rates

* * *

Remember, these rates depend also on the shipment source and destination.

**Negotiated rates also affect the rates of shipping**.

Negotiated Rates are the contract rates established by UPS and your UPS Account Representative. Enabling Negotiated Rates within your shipping systems allows you to view the most current and accurate rates for your UPS account. In case you have a discount of 10% on your account, then you need to select the “Negotiated Rates” option on the plugin settings page to enable it for your customers, and then proceed with your shipment.

* * *

This will show the discounted rates on the cart/checkout page.

**Price adjustment in services and packaging.**

You can adjust the shipping price by adding/subtracting the required amount/from the actual shipping cost. Remember to use the minus sign (**–**) for subtracting the amount. You can mention the amount in % and $ for each service.  
For example, the shipping cost of Next Day Air (UPS) returned by UPS is $35.76

* * *

Price Adjustment for GROUND is kept as -5 % as shown below:

* * *

As a result, the Total Cost Displayed for Next Day Air (UPS) is $32.18 (the 5% of 3.58 is subtracted to 35.76 to get the actual shipping cost) as shown below.

* * *

You need to verify all these settings for understanding the reason for the price difference. If the rates differ even after checking all the above criteria, approach our support team with the debug details:

To get the debug details, enable the debug option in the plugin settings page and then place an order from the cart page. You will see a request and response info. Copy this info to a text file and send it to our support team. We will be happy to help you!

[ Previous  WooCommerce UPS Shipping Plugin [Error Code 10001] -The XML document is not well formed  ](https://www.pluginhive.com/knowledge-base/woocommerce-ups-shipping-plugin-print-label-xml-document-not-well-formed-error-code-10001/)

[ Next  How to resolve printing issue with Dymo label printer?  ](https://www.pluginhive.com/knowledge-base/resolve-printing-issue-dymo-label-printer/)
