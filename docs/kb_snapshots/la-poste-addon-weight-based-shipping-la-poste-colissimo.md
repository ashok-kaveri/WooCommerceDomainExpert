# La Poste Add-on: Weight-Based Shipping for La Poste Colissimo

**Source:** https://www.pluginhive.com/knowledge-base/la-poste-addon-weight-based-shipping-la-poste-colissimo/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# La Poste Add-on: Weight-Based Shipping for La Poste Colissimo

In this article, I will explain how to set up WooCommerce weight-based shipping for Colissimo (Colissimo is the package delivery service to individuals of La Poste). Read below to know more.

**Shipping cost for Colissimo Belgique (Belgium)**

* * *

**Shipping cost for Colissimo France métropolitaine et Monaco (France and Monaco)**

* * *

Different shipping costs are based on various weights, and after a certain weight cost, calculates based on a per kg basis. France & Monaco has the same shipping cost and Belgium has a different cost based on the table listed above. As per the requirement, we need to consider only the “Domicile has signature” value.  
Analyzed various plugin options to implement these shipping calculations but was not very convinced due to the following issues.

  * WooCommerce doesn’t have weight-based shipping calculations.
  * few plugins need many rows to calculate costs based on a per kg basis.
  * few plugins are complex to set up. Need to go through a lot of documentation to understand the concepts.
  * few plugins take a long time due to multiple submissions to a server.
  * A few plugins remind me of the olden days of DOS programming with a lot of text formatting.

* * *

Decided to write a plugin to address these issues and was quite happy with the result [Weight and Country-based WooCommerce Shipping Plugin](https://wordpress.org/plugins/weight-country-woocommerce-shipping/ "Weight and Country based WooCommerce Shipping Plugin").

  * super simple & fast to set up shipping costs in a matrix format.
  * quick help in the column itself doesn’t need to go through the documentation.
  * can set up fixed cost or cost per kg.
  * possible to calculate the shipping cost by rounding the weight to the nearest 1kg, .5kg, etc. or the shipping cost calculates based on the exact weight.
  * different shipping costs for different countries.

* * *

Sorry, let’s come back and set up Colissimo 🙂  
I can assure you that setup will not take more than 5 minutes, It’s simple & fast. Let’s GO!

* * *

Select the country, configure minimum & maximum weight, fixed cost & cost per kg and finally set up the weight rounding that’s all you are done.  
In a few rows cost per weight column is blank, the shipping cost will be fixed for these rules. Similarly, when base cost and cost per weight are entered shipping will be the fixed cost for the minimum weight and the remaining weight will be calculated per kg basis. Also, did you notice the value in column “weight round” is 1, in this case, Colissimo round the weight to the nearest kg. If the weight is 4.5kg Colissimo charges you 5kg.  
Did you notice the small question mark icon near the title that’s your quick help.

* * *

Before winding up let’s have a look at the WooCommerce shopping cart and see how the calculated price display.

Shipping cost for France for 1kg weight. The base Rate for 1kg is 7.95 and no weight-based cost is defined. So the total shipping cost, in this case, is 7.95.

Shipping cost for France for 10kg weight. In this case, the Base rate is 7.95 and the cost per weight is .77. For the first 1kg 7.95, and for the remaining 9kg 7.95. Total 7.95+9*.77 which is 14.88 in total.

That’s all you are ready to ship with Colissimo and WooCommerce!! I will try to come up with a similar article to explain how to set up Chronopost International(a member of the La Poste group). Also, we will be soon releasing a WooCommerce plugin to integrate La Poste web services to have real-time rates and shipping label printing.

[ Previous  Universal Shipping Calculator for La Poste Colissimo on WooCommerce  ](https://www.pluginhive.com/knowledge-base/steps-migrate-universal-shipping-calculator-la-poste-colissimo/)

[ Next  Shipping Pro – Case based on weight and price  ](https://www.pluginhive.com/knowledge-base/shipping-pro-case-based-weight-price/)
