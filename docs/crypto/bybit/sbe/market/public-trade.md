---
exchange: bybit
source_url: https://bybit-exchange.github.io/docs/v5/sbe/market/public-trade
api_type: Market Data
updated_at: 2026-10-17 18:44:04.244192
---

# Self Match Prevention

## What is SMP?

With the Self Match Prevention function users can choose the execution method when placing an order. When the counterparty is the same UID or belongs to the same specified SMP group, the execution can be effected accordingly:

  1. Cancel maker: Cancel the maker order when executed; taker order remains.
  2. Cancel taker: Cancel the taker order when executed; maker order remains.
  3. Cancel both: Cancel both taker and maker orders when executed.



Once an order is placed in the orderbook, its smpType becomes invalid. This means that, for example, if you place a taker order without an smpType (`smpType=None`) that matches against your existing maker order set with `smpType=CancelMaker`, the taker will execute. This is because the maker order's `smpType=CancelMaker` became invalid once it placed in the orderbook.

## How to set SMP?

Check request params of [Place Order](/docs/v5/order/create-order). Specify parameter `smpType` when placing the order

## What is SMP Trade Group?

  * SMP is available for any user by UID level.
  * SMP Trade Group Management is only available for institutions at present.



**SMP Trade Group** : refers to a group of UIDs. When any of the UIDs in this group places an order and the SMP execution policy is selected, it will be triggered when the maker order under any of the UIDs in this group is matched.

**More details** :

  1. Each UID can only join one SMP Trade Group.

  2. SMP Trade Group is a UID-level management group, so when a main-account joins an SMP Trade Group, all the subaccounts under this main-account will automatically join the Trade Group as well.



  * If the main-account has already joined an SMP Trade Group, and a subaccount is created after it, this new subaccount will automatically join the same SMP Trade Group by default.
  * A subaccount does not have to be tied to the same SMP Trading Group as the main-account. It is only the default behaviour. It can be reset into different groups manually if needed.


  3. The relationship between SMP Trade Group and UIDs can be changed: when a UID joins a new SMP Trade Group or is removed from an SMP Trade Group. This operation will not affect the pre-existing orders, it will only affect the newly placed orders after the relationship has changed.



**Notes** : Based on this, we strongly suggest that when there will be an SMP Trade Group change, you should cancel all pre-existing orders to avoid an unexpected execution.

  4. The SMP Trade Group has a higher priority on SMP execution, so an individual UID is only taken into account when there is no SMP Trade Group on either side.

  5. Once the order is standing in the orderbook, its SMP flag doesn't matter any more. The system always follows the tag on the latter order.




**Examples** :  
1st of Jan: UID1 joins SMP Trade Group A, and places Order1;  
2nd of Jan: UID1 is removed from SMP Trade Group A, but Order1 is still active and "New"

  * case1: If UID1 joined SMP Trade Group B, and placed Order2, if Order2 meets Order1, it will be executed since they belong to two different groups.
  * case2: If UID1 did not join any other groups after being removed from SMP Trade Group A, and placed Order2, if Order2 meets Order1, the SMP will be triggered because UID1 did not have a group when it placed Order2, so SMP was triggered at the UID level (the same UID1).



## How to manage my UIDs & SMP Trade Group?

You can contact your institutional business manager or email Bybit via: [institutional_services@bybit.com](mailto:institutional_services@bybit.com)

## SMP across Bybit Global vs. Bybit compliant sites

  * **Bybit Global:** Institutional clients can choose whether to enable SMP.
  * **Bybit compliant sites:** SMP is **enabled by default for all users**.
    * **Note:** Most compliant sites currently support **spot trading only**.



**Rollout schedule** :  


The first site to go live will be **Bybit Turkey** , followed by:

  * **Turkey:** 2026/01/27
  * **Kazakhstan:** 2026/02/24
  * **Georgia:** 2026/03/10
  * **Other compliant sites (in development):** SMP will be enabled **immediately upon launch**.



**Site-specific SMP behavior** (effective 2026-08-04):

Site| Product| Behavior  
---|---|---  
Kazakhstan (KAZ)| Derivatives| SMP is **mandatory**. All derivative orders have SMP force-enabled.  
Turkey (TUR), Kazakhstan (KAZ), Georgia (GEO)| Spot| If `smpType` is `None`, an invalid value, or not provided, it is automatically set to `CancelMaker`.

---

# 自成交攔截

## 什麼是自成交？

提供自成交攔截(Self Match Prevention)功能，用戶在下單時可以選擇執行方式。當交易對手為相同的UID或屬於相同指定的SMP群組時，可按照以下方式進行執行：

  1. 取消maker單：當執行時取消maker訂單，但taker訂單仍保留。
  2. 取消taker單：當執行時取消taker訂單，但maker訂單仍保留。
  3. 兩者皆取消：當執行時取消taker單和maker單。



## 如何設置自成交類型?

[創建訂單](/docs/zh-TW/v5/order/create-order)接口, 可以通過`smpType`參數來設定smp類型

## 什麼是SMP交易群組?

  * 任何用戶都可使用SMP功能，僅單UID維度。
  * SMP交易群組管理功能目前僅適用於機構。



**SMP交易群組** ：指一組UID。當此群組中的任何UID下單並選擇SMP執行政策時，只要該群組中任何UID的限價單被匹配，就會觸發SMP執行政策。

**更多細節** ：

  1. 每個UID只能加入一個SMP交易群組。

  2. SMP交易群組是UID級別的管理群組，因此當主帳戶加入SMP交易群組時，所有屬於該主帳戶的子帳戶也會自動加入該交易群組。



  * 如果主帳戶已經加入某個SMP交易群組，則在其之後創建子帳戶，這個新的子帳戶將自動默認加入相同的SMP交易群組。
  * 子帳戶不必與主帳戶綁定到相同的SMP交易群組。這只是自動加入相同群組的默認機制。如果真的需要，可以手動重置為不同的群組。


  3. SMP交易群組和UID之間的關聯可以更改，例如UID加入新的SMP交易群組或從SMP交易群組中刪除，這將不會影響現有的訂單，而僅會影響關係更改後新下的訂單



**注意** : 基於這點，我們強烈建議在SMP交易群組發生變更時，最好取消所有現有訂單，以避免意外執行。

  4. SMP交易群組在SMP執行中具有較高優先級，當任何一方沒有群組時，UID才會生效。

  5. 一旦訂單進入訂單簿，其 smp 標誌就不再重要。系統始終遵循後一個訂單的smp標籤。




**示例** ：  
1月1日：UID1加入SMP交易群組A，並下訂單1；  
1月2日：UID1被從SMP交易群組A中移除，但訂單1仍然處於活躍狀態且為“新”狀態。

  * 情況1：如果UID1加入了SMP交易群組B並下了訂單2，如果訂單2與訂單1相符，它將被執行，因為它們屬於兩個不同的群組。
  * 情況2：如果UID1在被從SMP交易群組A中移除後沒有加入任何其他群組並下了訂單2，如果訂單2與訂單1相符，SMP將被觸發，因為UID1在下訂單2時沒有群組，所以SMP在UID級別（同一個UID1）被觸發。



## 如何管理我的UID及SMP交易群組?

您可以聯繫您的機構業務經理或通過電子郵件聯繫Bybit，電子郵件地址為: [institutional_services@bybit.com](mailto:institutional_services@bybit.com)

## Bybit Global 與 Bybit 合規站點之間的 SMP

  * **Bybit Global:** 機構客戶可自行選擇是否啟用 SMP
  * **Bybit 合規站點:** SMP 將 **預設為所有用戶啟用**
    * **注意:** 多數合規站點目前僅支援 **現貨交易**



**上線排期** :   


首個上線站點為 **Bybit 土耳其站** , 其後依序為:

  * **土耳其站:** 2026/01/27
  * **哈薩克斯坦站:** 2026/02/24
  * **格魯吉亞站:** 2026/03/10
  * **其他合規站點 (開發中):** 將於站點上線時 **立即啟用 SMP** 。



**各站點 SMP 特殊規則** （2026-08-04 起生效）：

站點| 產品| 行為  
---|---|---  
哈薩克斯坦（KAZ）| 衍生品| SMP **強制開啟** 。所有衍生品訂單均強制啟用 SMP。  
土耳其（TUR）、哈薩克斯坦（KAZ）、格魯吉亞（GEO）| 現貨| 若 `smpType` 為 `None`、非法值或未傳值，系統將自動設為 `CancelMaker`。