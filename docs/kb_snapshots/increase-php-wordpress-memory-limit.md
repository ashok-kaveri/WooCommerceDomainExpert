# How to Increase PHP WordPress Memory Limit?

**Source:** https://www.pluginhive.com/knowledge-base/increase-php-wordpress-memory-limit/
**Platform:** WooCommerce (WordPress)
**Plugin:** general
**Note:** Screenshots may show an older plugin UI — text content is current.

---

# How to Increase PHP WordPress Memory Limit?

In this guide, we would help you solve the WordPress Memory Limit error by increasing the memory size from within your WordPress. Read along to learn more.

## What is WordPress Memory Limit Error?

WordPress is a pretty stable platform to build websites but may give you some errors on occasion. By default, WordPress provides very little memory size( usually 32 or 64 MB) to its users. Depending on your hosting provider and server, this value may differ. 

Since most sites nowadays require way more size than the default value, you may get a memory error like this.
    
    
    Fatal error: Allowed memory size of xx bytes exhausted

## How to increase the PHP Memory Limit of your WordPress?

There are two possible ways to increase the WordPress Memory limit of your website. 

  1. Define the new memory size all by yourself
  2. Let your hosting provider change it from the server

Let’s see how to increase memory in both ways. We would take a small example to show you how to do it. 

### Changing the memory limit yourself

The very first step is to go into your wp-config.php file found in your WordPress’s root folder. You would need a file manager or an FTP Client to find this folder. 

Once you’re in, you need to copy and paste the following code into your wp-config.php file. 
    
    
    define( 'WP_MEMORY_LIMIT', '512M' );

This particular code line is to tell WordPress to increase the PHP memory limit to 512MB. 

**Please Note:** You must paste this code just before the line ‘That’s all, stop editing! Happy blogging.’ You can refer to the following sample image.

After that, you must save the changes and upload the file back to your server to see if the error message is gone or not. 

If that doesn’t remove the error message, you may have to go to the PHP.ini file. If you have access to your PHP.ini file, you can go there and look for ‘memory_limit’ as shown below. 

Now, you need to replace the pre-defined size with the new one. So, for instance, if your line shows 256M, then try entering 512M:
    
    
    memory_limit = 512M; Maximum amount of memory a script may consume (64MB)

However, if you don’t have access to your PHP.ini file, then you would have to do a workaround. You can try adding the following code to your .htaccess file. 
    
    
    php_value memory_limit 512M

Have a look at the image below for your reference:

### Contacting your hosting provider

WordPress memory size can vary from server to server. Depending on your current hosting plan, you may be limited to a specific memory size(256MB, 512MB, 1GB, or more). 

That’s because each hosting plan would provide different sets of resources to customers. Should you feel the need to increase the size of your PHP Memory, then feel free to contact your hosting plan and change the plan. Specialized [WordPress VPS](https://www.scalahosting.com/wordpress-hosting.html) providers implement custom settings that tailor the platform to your requirements and ensure impeccable performance. In addition, you can always contact your host’s support agents, who will help you configure the server and make the most of it.

* * *

## Conclusion

We understand that it can be troublesome to encounter such an error while working on your website. Luckily, you’re safe as there are a ton of options and help available to keep you going. 

In the case of the WordPress Memory Limit issue, you have two safe ways to solve the issue permanently. We discussed, 

  1. How to increase the limit manually using any client software.
  2. If nothing works, contact your hosting provider to increase it at the server level. 

If you have any doubts regarding this or need help with any of the PluginHive plugins, feel free to **[Contact PluginHive Customer Support](https://www.pluginhive.com/support/)**. 

Check out our **[WooCommerce Shipping plugins](https://www.pluginhive.com/product-tag/woocommerce-shipping/)** if you are in the need of some outstanding online shipping solutions.

**_Good luck_** 🙂

[ Previous  Setting Up Magento 2.0 Default USPS Shipping Extension  ](https://www.pluginhive.com/knowledge-base/setting-up-magento-2-0-usps-shipping-plugin/)

[ Next  Increase the Maximum Input Variables Limit(Max Input Vars) on your WordPress.  ](https://www.pluginhive.com/knowledge-base/increase-max-input-vars-limit-on-your-wordpress/)
