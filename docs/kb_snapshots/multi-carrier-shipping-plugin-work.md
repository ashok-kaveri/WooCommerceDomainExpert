# How does Multi-Carrier Shipping Plugin for WooCommerce work?

**Source:** https://www.pluginhive.com/knowledge-base/multi-carrier-shipping-plugin-work/
**Platform:** WooCommerce (WordPress)
**Plugin:** multi-carrier
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# How does Multi-Carrier Shipping Plugin for WooCommerce work?

Considering you have successfully purchased and activated the **[Multi-Carrier Shipping Plugin for WooCommerce](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/) **and registered with FedEx, UPS, USPS, Stamps, and DHL, let’s look at a simple use case to understand how this plugin works.

Consider you have set three shipping zones **United States** , **Canada** , and the default **Rest of the World** as defined below:

We also create two shipping classes **Class A** and **Class B** as defined below. These classes are applied on two products of **Category A** and **Category B** respectively.

### Get started with configuring Shipping Area Management:

There are four types of area list that can be created –  _Zone List, Country List, State List,_ and  _Postal Code List._ You can create areas for all four as follows:

  * **Area List** : Let’s create a new zone area and name it as _Canada Zone List_ and select _Canada Zone_ from available shipping zones in the _List_ options.

  * **Country List** : Let’s add another area of countries titled  _List of 3 Asian Countries_ and select _China, India_ and  _Japan_ for our list.

  * **State List** : We also add a state list titled _United States_ to list few states of United States (U.S) and select _California, Washington_ and _Texas._

  * **Postal Code List:** Let’s add a new area of Postal codes for two areas in New York City titled  _NewYork Postal Code._ Let’s enter two postal codes _10001_ and _10002._

### Move on to configure the Multi-Carrier Shipping Plugin for WooCommerce Rule Table section.

#### Case 1: **Set FedEx shipping option for Canada region**

  * Create a new rule with a method titled  _MCS Canada_(Indicating Multi-Carrier Shipping Canada).
  * Select the Area List option as  _Canada Zone List_ from our created list of areas in Shipping Area Management.
  * Select a shipping class _Class A_ and both product categories _CategoryA_ and _CategoryB_ for this case.
  * Select _Weight_ option to calculate shipping rates based on the weight of the products and set minimum and maximum weight as _1_ and _10_ pounds respectively.
  * Select the Shipping Option as _FedEx_ to get FedEx shipping rates.
  * Select any shipping service provided by FedEx. For our case, let us select _INTERNATIONAL ECONOMY_ service.

Below is a screenshot of how FedEx shipping rates are calculated on the Cart page. If the weight of the product is beyond the range, the Fallback rate is applied.

#### Case 2: **Set UPS shipping option for Asia region**

  * Add a new rule with a method titled  _MCS Asian Countries_(Indicating Multi-Carrier Shipping Asian Countries).
  * Select the Area List option as _List of 3 Asian Countries._
  * Select the product category  _CategoryA_.
  * Select _Item Qty_ option to calculate shipping rates based on the quantity of the Category A products. Set the range for item quantity as 1 to 3.
  * We also set a flat rate as handling charges of _$10_.
  * Select the Shipping Option as _UPS_ to get UPS shipping rates.
  * For international shipping service, let’s select _UPS Worldwide Express_ service.

Following screenshot shows you how UPS shipping services are calculated on the Cart page. A flat rate of $10 is added to the shipping cost. Once the quantity of the products increases to four or more, the fallback rate is applied.

#### Case 3: **Set USPS shipping option for the United States region**

  * Add a new rule with a method titled  _MCS United States_(Indicating Multi-Carrier Shipping United States).
  * Select the Area List option as _the United States_.
  * Select a shipping class _Class B_ and product category  _CategoryB_ for this use case.
  * Select _the Price_ option to calculate shipping rates based on the price of the products. Set the price range of $_100_ to _$400_.
  * Select the Shipping Option as _USPS_ to get USPS shipping rates.
  * For shipping the United States, let’s select _Standard Post_ service.

Following screenshot shows how USPS shipping rates are calculated in the Cart page. If the price of the product is beyond the defined range, the fallback rate is applied.

#### Case 4: **Set Stamps USPS shipping option for Asia region**

  * Add a new rule with a method titled  _MCS Asian Countries 2_(Indicating Multi-Carrier Shipping Asian Countries 2).
  * Select the Area List option as _List of 3 Asian Countries._
  * Select the product category  _CategoryB_.
  * Select _Item Qty_ option to calculate shipping rates based on the quantity of the CategoryB products. Set the range for item quantity as 2 to 5.
  * Select the Shipping Option as _Stamps_  _USPS_ to get Stamps USPS shipping rates.
  * For international shipping service, let’s select _Priority Mail: Package_ service.

Below is a screenshot of how Stamps USPS shipping rates are calculated on the Cart page. If the quantity of the product is beyond the range, Fallback rate is applied.

#### Case 5: **Set DHL Express shipping option for United States region**

  * Add a new rule with a method titled  _MCS United States 2_(Indicating Multi-Carrier Shipping United States 2).
  * Select the Area List option as _United States_.
  * Select a shipping class _Class A_ for this use case.
  * Select _Price_ option to calculate shipping rates based on price of the products. Set the price range as $5 _0_ to _$300_.
  * Select the Shipping Option as _DHL Express_ to get DHL Express shipping rates.
  * For shipping United States, let’s select _Express Worldwide_ service.

Following screenshot shows how DHL Express shipping rates are calculated in the Cart page. If the price of the product is beyond the defined range, the fallback rate is applied.

#### 

#### Case 6: **Set Flat Rate shipping option for few postal codes region of New York.**

  * Add a new rule with a method titled  _MCS New York_(Indicating Multi-Carrier Shipping New York).
  * Select the Area List option as _N_ _ew York Postal Codes_.
  * Select a shipping class as _Any Shipping Class_. This will disable the _Product Category, Based on_ and _Min-Max_ attribute, as the flat rate will be now be applied to all the products which are shipped to specific postal codes.
  * Set cost for the flat rate option as $20.
  * Select the Shipping Option as _Flat Rate_.

Following is a screenshot of how Flat rate is calculated for products that are shipped to New York City. As the quantity of products increase, the shipping cost gets multiplied.

We have now set the rule matrix. Further, we can set a **Fallback Rate** if some shipping service or rule metric is not applicable in a region.

The following is a screenshot of how Fallback Rate is affected on the Cart page.

  

### How does Method Group work?

**Method Groups** option allows you to group methods to display multiple shipping methods, one for each group, on the cart and checkout page.  

Once you enable this option, a new column appears in the rule table as shown below:

Let us consider the following two cases to understand how _Method Groups_ work:

**Case 1:** Consider there are three method rules –  _Rule1, Rule2_ &_Rule3,_ with three different shipping options  _FedEx_ , _UPS_ & _DHL Express_.  
_Rule1_ and Rule2 and grouped together using the method group name _Group1 and Rule3_ belongs to the method group  _Group2_ as defined in the screenshot below.__

Once a product belonging to a particular product category (in this case, Toys or any product category) or shipping class (in this case, Small Items) is added to the cart, the shipping methods appear in the cart as shown below:

The shipping method  _Multi Carrier Shipping(Group1)_ represents the first rule,  _Rule1_ of G _roup1,_ whereas  _Rule3_ represents the third rule in the rule table which belongs to _G_ _roup2.  
_An important factor to notice here is that, all the rules of a particular group are not listed in the cart. In this case,  _Rule2_ of _Group1_ is not listed. This is because, the first applicable rule of a group will only be displayed on the cart/checkout page.

**Case 2:** Consider the same method rules (_Rule1_ , _Rule2_ and _Rule3_) with the same shipping options (_FedEx, UPS_ &  _DHL_ Express).  
In this case, _Rule1_ is grouped under  _Group1, Rule2 is grouped under Group2 and Rule3_ belongs to the method group  _Group3_ as defined in the screenshot below:

Once a product belonging to a particular product category (in this case, Toys or any product category) or shipping class (in this case, Small Items) is added to the cart, the shipping methods appear in the cart as shown below:

Since each rule belongs to unique method groups, all the rules are displayed on the cart page.

Check out the features of [**Multi-Carrier Shipping Plugin for WooCommerce** here](https://www.pluginhive.com/product/multiple-carrier-shipping-plugin-woocommerce/).

[ Previous  Shipping Prohibited Items in WooCommerce  ](https://www.pluginhive.com/knowledge-base/hassle-free-shipping-flammable-goods-using-woocommerce/)

[ Next  Does WooCommerce Multi Carrier Shipping support DHL & FedEx in Mexico?  ](https://www.pluginhive.com/knowledge-base/woocommerce-multi-carrier-shipping-plugin-supports-dhl-fedex-mexico/)
