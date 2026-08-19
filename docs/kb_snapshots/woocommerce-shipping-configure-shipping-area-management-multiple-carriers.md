# WooCommerce Shipping – Configure Shipping Area Management for Multiple Carriers

**Source:** https://www.pluginhive.com/knowledge-base/woocommerce-shipping-configure-shipping-area-management-multiple-carriers/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# WooCommerce Shipping – Configure Shipping Area Management for Multiple Carriers

This article explains how to set up Shipping Area Management within the **WooCommerce Multi-Carrier Shipping plugin** to get real-time shipping rates from **UPS, USPS, FedEx, Stamps.com, and DHL**. It is a complete guide to using multiple shipping areas in your WooCommerce store based on factors like **WooCommerce Shipping Zones, Countries, States & Postal codes.**

## Content

  * **What is Shipping Area Management and why would you use it?**
  * **Set up Shipping Area Management based on Zones**
  * **Set up Shipping Area Management based on Countries**
  * **Set up Shipping Area Management based on States**
  * **Set up Shipping Area Management based on Postal Codes**

* * *

### What is Shipping Area Management and why would you use it?

**Shipping Area Management** provides store owners with the ability to use WooCommerce Shipping Zones with [**WooCommerce Multi-Carrier Shipping Plugin**](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/). Apart from this, the user is also able to manage Country Names, City Names, and Postcodes without the use/help of **Shipping Zones.**

With the help of Shipping Area Management store owners are permitted to define the areas where they will target a specific shipping carrier. In this way, only that Shipping method will apply to the defined area under **Shipping Area Management.**

  * In order to locate **Shipping Area Management** you will have to navigate to **WooCommerce > Settings > Shipping > Shipping Area Management**.

Now we will cover 4 scenarios regarding the available areas in **Shipping Area Management.**

### Set up and Configure the Shipping Area Management based on Shipping Zones

First, in order to have the shipping areas setup based on **Zones,** you will have to add **Shipping Zones** based on the region your shipping services are offered.

  * To locate **Shipping Zones,** navigate to **WooCommerce > Settings > Shipping > Shipping Zones**.How to add a Shipping Zone
  * While adding the Shipping zone make sure to specify the Zone name as well as the region you are targeting. If the region is not set for any country/location then that zone will consider all countries and locations.Creating Zone names and regions within the Zone
  * When the settings are stored two Shipping Zones are created. One for the US (_**United States**_) and the second targeting Everywhere (**_Rest of the world_**) (shown below).The final zone list displaying (the United States & Everywhere)
  * While setting up **Shipping Area Management** click on **Add** to set up the area based on the zones as shown in the image below.Add shipping area management
  * While setting up **Zones** under **Shipping Area Management** you will be given an option in a drop-down to choose the types of areas you will be targeting.Creating a new Area based on Zone list
  * Select the **Zones** option from the drop-down. Now the Zone matrix will accept the values that are stored in **Shipping Zones.** So as shown in the image below, both the United States and Everywhere are populated under **Area Name** and **List**.The configuration of the Zone Matrix based on two zones
  * Now that the **Zones** have been configured both in **Shipping Zones** as well as **Shipping Area Management** , proceed to set up the rule table which will determine the services or shipping options that will be applied to these particular **Zones**.Adding rules to the rule table (Multi-Carrier Shipping plugin)
  * Enable **Method Group**.Method Group

Method groups are required when there are multiple Shipping Methods in the Rule Table. This field is used mainly to distinguish the various Shipping Methods from one another while calculating Shipping Rates within the cart/checkout page.

Multiple Shipping Methods with Method Groups

****If there are multiple rules with no Method Group Setup the Shipping calculator will not be able to pull in all the services which have been configured in the WooCommerce Multi-Carrier Shipping plugin**

While creating a new rule, it’s a good practice to have the service name listed under **Method Title** to reduce confusion.

  * As you can see from the image below, the **Area List** has been populated with the Zones that were setup earlier in **Shipping Area Management.  
*This is a manual setting and does not get auto populated**
  * The **Shipping Option** field is a drop-down which will provide you with a list of services/carriers (UPS, USPS, FedEx, Stamps USPS) and so on…
  * The **Service** option is a list of services provided by that Carrier (UPS, USPS, FedEx, Stamps USPS).  
*** It is important to remember to select the correct Service from the drop down and not get confused between Domestic services & International services**.  
Setting up the Rule Table based on Zones
  * Upon completing the setup, as shown above, retrieve the shipping rates and services by entering the **Shipping Address** in the cart page.
  * The services will populate based on the destination address configured in the rule table, as shown in the images below.

#### **Shipping Rates calculated for the US Zone:**

Rates based on a domestic address (NYC) UPS and USPS populate in the Shipping Calculator

#### **Shipping Rates calculated for the Everywhere Zone (International Shipment):**

Rates based on an International address (CA) FedEx rates appear in the Shipping Calculator

* * *

### Steps to setup and configure the Shipping Area Management based on countries.

  * Start by accessing the **Shipping Area Management setting** and configure the Area List based on **Country List** (shown below)  

  * Set the areas by providing the **Area Name** followed by the list of countries for each area.Zone Matrix configuration based on Countries
  * Once the Zone Matrix has been set up, proceed to the **Rule Table** and configure the Methods accordingly, based on countries to be targeted for each Shipping Method listed.Rule table with Area list based on Countries
  * Proceed to the store and add items to the cart, followed by the Shipping address.**  
Below are three examples of rates getting calculated on the basis of the destination address.**

Rates for International orders – EuropeRates for International orders – AsiaRates for Domestic orders – North America

* * *

### Steps to setup and configure the Shipping Area Management based on States

  * Start by accessing the **Shipping Area Management setting** and configure the Area List based on State List (shown below)  

  * Set the areas by providing the **Area Name** followed by the States for each area.Zone Matrix configuration based on States
  * Once the Zone Matrix has been setup, proceed to the rule table and configure the Methods accordingly, based on the states to be targeted for each Shipping Method listed.Rule table with Area list based on States

  * Proceed to the store and add items to the cart, followed by the Shipping address.  
**Below are two examples of rates getting calculated on the basis of the destination address.**

Rates based on States – HawaiiRates based on States – California

* * *

### Steps to setup and configure the Shipping Area Management based on Postal Codes

  * Start by accessing the **Shipping Area Management setting** and configure the Area List based on Postal code List (shown below)  

  * Set the areas by providing the **Area Name** followed by the list of Postal codes for each area.Zone Matrix configuration – Postal codes
  * Once the Zone Matrix has been set up, proceed to the rule table and configure the Methods accordingly, based on the Postal Codes to be targeted for each Shipping Method listed.Rule table with Area list based on Postal codes
  * Proceed to the store and add items to the cart, followed by the Shipping address.  
**Below are two examples of rates getting calculated on the basis of the destination address.**

Rates based on ZIP codes – 10001Rates based on ZIP codes – 90210

* * *

## Summary…

The Shipping Area Management is a section within the [**WooCommerce Multi-Carrier Shipping plugin**](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/) that enables store owners to determine the service they would like to provide users with solely based on one of the four categories: WooCommerce Shipping Zones, Countries, States and Postal codes.

This article was all about the Shipping Area Management and how you can set it up in a seamless fashion. The Shipping Area Management determines the services to be used for both domestic as well as International orders & shipments.

If you have any queries regarding customizing the Shipping Area Management or setting up the shipping rules for WooCommerce Multi-Carrier Shipping plugin in order to achieve the optimized working of your online store, based on your business case, feel free to [**write to us** ](https://www.pluginhive.com/support/)or share your views in the comment section below.

[ Previous  UPS and USPS – Display WooCommerce Shipping Rates with Price Adjustment  ](https://www.pluginhive.com/knowledge-base/ups-usps-display-woocommerce-shipping-rates-with-price-adjustment/)

[ Next  How to troubleshoot Multi-Carrier Shipping Plugin for WooCommerce?  ](https://www.pluginhive.com/knowledge-base/troubleshoot-multi-carrier-shipping-plugin-woocommerce/)
