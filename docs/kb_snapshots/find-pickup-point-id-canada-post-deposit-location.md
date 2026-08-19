# Find Pickup Point ID for Canada Post Deposits on WooCommerce

**Source:** https://www.pluginhive.com/knowledge-base/find-pickup-point-id-canada-post-deposit-location/
**Platform:** WooCommerce (WordPress)
**Plugin:** canada-post
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# Find Pickup Point ID for Canada Post Deposits on WooCommerce

In this article, we will tell you how you can find your Pickup Point ID for the Canada Post deposit location when using the WooCommerce Canada Post Shipping Plugin with Print Label.

If you wish to deposit your items at a post office or a Canada Post facility, our WooCommerce Canada Post Shipping Plugin with Print Label provides an option called **Pickup Point Id** to do so. This Id specifies the deposit location where you can leave your package to be shipped.

#### Following are the steps to find Pickup Point Id of your deposit location:

  * To use _Pickup Point Id_ option, you have to first disable the _Pickup_ option in the plugin. You can only use either of the options for pickup facility.

  * To find Pickup Point Id, visit Canada Post website [here](https://www.canadapost.ca/cpotools/apps/fdl/business/findDepositLocation?execution=e1s1).  
You can see a screenshot of the website below:

There are three fields that you need to fill in to find your deposit location:

_**1) Type of Mailing:** _Select the type of mailing option provided by Canada Post. When you broadly classify the mailing options of Canada Post, it includes letter mail (send in regular-sized envelopes) as well as the parcel shipping services (with varying rates based on distance, weight, and size).

The below screenshot shows the choice of Canada Post mailing options available to you in the **Find a Deposit Location** Tool:

For example, here let us select _NEIGHBOURHOOD MAIL – STANDARD_ mailing type.__ Each mailing type is explained later in this article here

 _**2) Number of Pieces:**_ Allows you to enter the quantity of the items that you will be depositing.  
Let’s assume we are sending five different mails or packages here.

_**3) Postal Code:**_ Allows you to enter the postal code of the deposit location. Remember to enter the complete postal code. Let us enter  _T1A 7L4_ here _._

These settings are configured as shown below:

  * Once you fill in all three fields, click **Find** to get the available deposit location.

You can see the results displayed in tabular form. These results are the addresses of the available deposit locations based on the information you entered.

The table consists of six columns as described below:

  1. **Site#:** This site number is the shipping point Id, and is a unique four-character alphanumeric value for each pickup location.
  2. **Name:** The name of the post office or Canada Post pickup facility.
  3. **Address:** The address of the respective post office or Canada Post pickup facility.
  4. **City:** The name of the city where the post office or the pickup facility is located.
  5. **Prov:** The name of the province in which the city is located.
  6. **Postal Code:** Postal code of the respective post office or pickup facility.

The **Site#** is the **Pickup Point Id** in context of our Canada Post plugin. Copy the site number of your desired deposit location and paste it in the _Pickup Point Id_ option of our Canada Post plugin, and save the settings.

That’s it. You have now configured the pickup point id and thereby the deposit location for your **[WooCommerce Canada Post Shipping Plugin with Print Label](https://www.pluginhive.com/product/woocommerce-canada-post-shipping-plugin-with-print-label/).**

### Types of Mailing provided by Canada Post

The following mailing options are provided by Canada Post:

  * **Incentive Lettermail:** Incentive Lettermail is a category of Lettermail service that consists of large volumes of mail items. It is available for customers with a Canada Post Agreement who prepare their mail according to specific requirements.  
These can include:
    * Letters, cards (including [postcards](https://www.postalytics.com/blog/canada-post-rates/)) or similar communications, self-mailer.
    * An annual, semi-annual or quarterly report.
    * Receipts or invoices (or similar document containing financial information).
    * A notice of voting for federal, provincial or municipal events.
    * A CD or DVD (must be submitted to Canada Post for testing and approval).
    * A flexible magnet.
    * or any other mail the customer chooses to send at the applicable Incentive Lettermail price and which meets the applicable qualifications.

It has two variations:

  1. INCENTIVE LETTERMAIL MACHINEABLE STANDARD
  2. INCENTIVE LETTERMAIL MACHINEABLE OVERSIZE

For more information on Incentive Lettermail, read [this](https://www.canadapost.ca/tools/pg/Amalgamated/Amalgamated_ILM-e.pdf) article.

  * **L****ettermail:** Lettermail is the most convenient and cost-effective way in Canada to send personal messages, business correspondence, invoices, and billing statements within Canada.  
Lettermail can include everything as an incentive letter mail, in addition to dry biological specimens, or any other mail the customer chooses to send which meets the applicable qualifications.

It has two variations:

  1. LETTERMAIL OTHER O/S (FULL RATE OS)
  2. LETTERMAIL OTHER STANDARD (FULL RATE STD)

For more information on Lettermail, read [this](https://www.canadapost.ca/tools/pg/manual/PGletterml-e.pdf) article.

  * **Personalized Mail:** The Personalized Mail service is a proven and effective direct marketing and advertising medium that offers customers the ability to personalize their mailing and tailor their promotional messages to specific consumers or prospects.  
Mini-catalogs are acceptable as Personalized Mail. A Mini-catalogue is defined as printed matter with a list of items for sale containing item description, item numbers and/or prices. It must contain a minimum of 8 pages or panels and meet Machineable Standard Personalized Mail service requirements.

It comes in four variations:

  1. PERSONALIZED MAIL SPECIAL HNDL (STD) – Special handling standard mail items.
  2. PERSONALIZED MAIL SPECIAL HNDL (OS, DIM) – Special handling oversize and dimensional mail items.
  3. PERSONALIZED MAIL MAC STD, MINI-CAT – Machineable standard mini-catalogs mail items
  4. PERSONALIZED MAIL MACHINEABLE (OS) – Machineable oversize mail items.

For more information on Personalized Mail, read [this](https://www.canadapost.ca/tools/pg/Amalgamated/Amalgamated_CPPM-e.pdf) article.

  * **Publication Mail:** Publication Mail is defined as mailable items, which includes the following –
    * Magazines and newspapers in print form containing news and miscellaneous information, such as articles, features, and advertising.
    * Newsletters in print form, non-promotional in nature, containing news or information to a membership, special interest group or association and are usually in the form of printed sheets, pamphlets or small newspapers.
    * Contains a maximum ratio of 70% advertising to 30% news/editorial (including editorial content sponsored by an advertiser) in no more than 50% of the issues in any 12-month period (enclosures and samples are not included in the 70/30 ratio).

It comes in three variations:

  1. PUBLICATIONS MAIL SPECIAL HNDL, DF – Special handling delivery facility presort.
  2. PUBLICATIONS MAIL MACHINEABLE – STD – Machineable standard mail items.
  3. PUBLICATIONS MAIL MACHINEABLE OS – Machineable oversize mail items.

For more information on Publications Mail, read [this](https://www.canadapost.ca/tools/pg/Amalgamated/Amalgamated_PM-e.pdf) article.

  * **Neighborhood Mail:** Neighbourhood Mail is one of Canada Post’s targeted direct mail services. It consists of printed and non-printed matter such as product samples that are not addressed to specific delivery addresses in Canada. It provides geographic, demographic and lifestyle information to target mailings to neighborhoods or localities that have the highest potential audience – without a customer database.  
Neighbourhood Mail can be accepted if it includes:
    * Flyers
    * Newspapers
    * Community newspapers
    * Cards
    * Coupons
    * Co-op mailings
    * Envelopes
    * Catalogs
    * Inserts and enclosures
    * Brochures
    * Single sheets
    * CDs and DVDs
    * Magazines

It comes in two variations:

  1. NEIGHBOURHOOD MAIL – STANDARD
  2. NEIGHBOURHOOD MAIL – OS

For more information on Neighbourhood Mail, read [this](https://www.canadapost.ca/tools/pg/Amalgamated/Amalgamated_CPNM-e.pdf) article.

  * **LetterPost:** Letter-post is the most economical method of sending personal and business correspondence to the United States and international destinations. Letter-post items are composed of paper or other material with the general characteristics of paper (e.g., tickets, photographs, etc.). These items must meet the requirements for Letter-post, including size and weight.  
It can include:
    * Letters
    * Self-mailers
    * Cards
    * Postcards
    * Other paper that meets these specifications which the Customer chooses to deposit.

It comes in two variations:

  1. LETTERPOST -USA
  2. LETTERPOST -INTERNATIONAL

For more information on Neighbourhood Mail, read [this](https://www.canadapost.ca/tools/pg/manual/PGletpost-e.pdf) article.

  * **Postal Code Targeting:** Postal Code Targeting service provides customers the ability to target a specific geographic/demographic at the Postal Code level. It is a Standard Machineable mail item with a unique 2D barcode printed on each mail item. During processing, Canada Post’s automated equipment will spray the address found within the 2D barcode on the item. The mail item will then be sequenced for delivery.

For more information on Postal Code Targeting, read [this](https://www.canadapost.ca/tools/pg/Amalgamated/Amalgamated_PCT-e.pdf) article.

  * **Parcels – Any combination of products:** Parcel services in Canada Post are available in two ways:
    1. **Canada –** Parcel service within Canada is for people who need to ship documents, packets, and parcels for delivery inside Canada. For more information on Parcel service within Canada, read [this](https://www.canadapost.ca/tools/pg/manual/PGpscanada-e.asp) article.
    2. **U.S.A and International –** Parcel services to the U.S.A. and to international destinations are subject to the size and weight restrictions.  
For more information on Parcel services to U.S.A and international destination, read [this](https://www.canadapost.ca/tools/pg/manual/PGpsus_int-e.asp) article.

  * **Packets (US/INT’L) or Prepaid (Any Dest.):** Canada Post provides tracked packets and small packets services to U.S.A as well as other international destinations. The tracked packet services give you the opportunity to ship small items economically and with visibility, which includes delivery confirmation. Whereas the small packet service is specially designed with minimal features to keep the price low and the shipping simple, for small and lightweight packages.  
Prepaid products are flat-prices, postage-included envelopes, and labels. They are purchased in advance and used as required. They are available for _Xpresspost – U.S.A_ and _Xpresspost – International_ services.

For more information on TrackedPacket, read [this](https://www.canadapost.ca/cpo/mc/assets/pdf/business/trackedpacket_en.pdf) article, and for SmallPacket, read [this](https://www.canadapost.ca/cpo/mc/assets/pdf/business/smallpacketusaintlair_en.pdf) article.

  * **Delivered Tonight:** With this service, you can offer your customers an option to receive the items to be delivered on the same day or within hours of placing the order.  
To know how this service works, read [this](https://www.canadapost.ca/web/en/blogs/business/details.page?article=2015/06/25/how_to_add_delivered&cat=shipping&cattype=business) article.

To know more about PluginHive Canada Post plugin, read features on the [product page](https://www.pluginhive.com/product/woocommerce-canada-post-shipping-plugin-with-print-label/).

[ Previous  Setting Up WooCommerce Canada Post Shipping Plugin  ](https://www.pluginhive.com/knowledge-base/setting-woocommerce-canada-post-shipping-plugin/)

[ Next  Troubleshooting WooCommerce Canada Post Plugin  ](https://www.pluginhive.com/knowledge-base/troubleshooting-woocommerce-canada-post-plugin/)
