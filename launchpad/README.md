Launchpad
=========

以下代码需要安装python库`launchpadlib`


## buglist.py ##
List all bugs marked as 'Fix Released' on a given series
找出所给项目的所有标记为"Fix Released"的bugs。
 
用法：
  python buglist.py glance     essex


## map-email-to-lp-name.py ##

Attempt to find a launchpad name for every email address supplied:
根据邮箱名称，获取其在launchpad上的用户名称。

用法：
  python map-email-to-lp-name.py foo@bar.com blaa@foo.com

## email-to-name-and-date.py ##

根据邮箱名称，获取用户在launchapd中详细信息

用法：

  python email-to-name-and-date.py foo@bar.com blaa@foo.com
