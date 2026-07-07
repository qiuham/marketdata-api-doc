---
api_type: reference
source_type: vitepress
version: XTP Pro
scope: cn
asset_class: stock
domain: gateways
provider: zhongtai
provider_name: 中泰证券
product: xtppro
product_id: zhongtai-xtppro
id: zhongtai-xtppro-boostpython编译库说明
title: boost.python编译库说明
source_url: 'https://xtp.zts.com.cn/xtp-pro/API4/SDK%E7%BC%96%E8%AF%91%E5%BA%93%E8%AF%B4%E6%98%8E/Python%E7%89%88%E6%9C%ACSDK%E7%BC%96%E8%AF%91%E5%BA%93%E8%AF%B4%E6%98%8E.html'
page_url: 'https://xtp.zts.com.cn/xtp-pro/'
updated_at: 2026-05-21
---

# boost.python编译库说明

**boost.python编译库说明**  
  
目录

  * **1．Linux环境下编译说明**
    * 1.1. centos7参考环境
    * 1.2. 安装编译python3.9.13
    * 1.3. 安装编译boost_1_80_0
    * 1.4. 编译source
    * 1.5. 运行Demo
  * **2．windows环境下编译说明**
    * 2.1. win10参考环境
    * 2.2. 安装64位python3.9.13
    * 2.3. 安装64位boost_1_80_0
    * 2.4. 安装VS2015
    * 2.5. 编译boost.python库
    * 2.6. 使用CMake生成工程
    * 2.7. 编译source
    * 2.8. 运行Demo

  


## **1．Linux环境下编译说明** ​

### 1.1. centos7参考环境 ​

centos7.6   


gcc、g++(4.8.5版本)   


cmake-3.4.1(tar.gz)   


python3.9.13(tar.gz)   


boost_1_80_0(tar.gz)   


### 1.2. 安装编译python3.9.13 ​

**步骤一. 安装前的准备** Centos7默认安装了python2.7版本，我们需要编译安装python3.9.13。   


(1) 先看一下已安装的python在哪里。 [root@centos7 ~]# whereis python   


![avatar](/xtp-pro/assets/1.Bzu1-CcT.png)  


显示python在/usr/bin目录中。

(2) 进入/usr/bin查看python详情：

[root@centos7 ~]# cd /usr/bin   


[root@centos7 bin]# ll python*   


![avatar](/xtp-pro/assets/2.Fr5Z3AbB.png)  


如果没有安装python3.9.13，则需要按如下步骤安装。   


(3) 编译安装gcc、g++： 在安装CMake前，先要确认系统已经安装了gcc、g++，否则在安装CMake时会报错。  
centos下默认的gcc、g++版本是4.8.5。   


![avatar](/xtp-pro/assets/m_1.CS3nSXj5.png)  


但如果系统没有gcc、g++，则需要安装:   


[root@centos7 bin]# yum install gcc gcc-c++

(4) 编译安装CMake： 先检查是否已安装cmake：

[root@centos7 Downloads]# cmake -version

![avatar](/xtp-pro/assets/m_2.Dv7HHBKV.png)  


说明已安装cmake-3.4.1。

但如果没有安装CMake，则需要安装，这里是cmake-3.4.1，步骤如下：

  * 下载cmake包，解压到指定路径：



[root@centos7 Downloads]# wget <http://www.cmake.org/files/v3.4/cmake-3.4.1.tar.gz>

[root@centos7 Downloads]# tar -zxvf cmake-3.4.1.tar.gz -C /usr/local/   


  * 进入解压后的cmake目录配置：



[root@centos7 Downloads]# cd /usr/local/cmake-3.4.1   


[root@centos7 cmake-3.4.1]# ./configure   


![avatar](/xtp-pro/assets/m_3.DQfdh82B.png)  


  * 编译、安装cmake：



[root@centos7 cmake-3.4.1]# make

[root@centos7 cmake-3.4.1]# make install   


  * 查看cmake版本：



[root@centos7 cmake-3.4.1]# cmake -version

注意：在解压后的cmake-3.4.1目录下，编译源码及安装。  
  


**步骤二. 安装python3相关依赖包和编译环境**

在安装python3时，需要先安装依赖环境：

[root@centos7 bin]# yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gcc make   


![avatar](/xtp-pro/assets/3.eM9d9Q2i.png)  


如果不安装相关依赖包，在安装python3时会报找不到zlib、SSL等一连串错误！

如果本机安装了gcc、make，那么可以去掉这2项。  
  


**步骤三.下载、编译、安装**

(1) 下载python3.9.13安装包 可手动下载到Downloads文件夹，下载链接：<https://www.python.org/downloads/source/>  
  


![avatar](/xtp-pro/assets/4.DlwdHI8v.png)  


或者wget命令下载到Downloads文件夹：  
  


[root@centos7 Downloads]# wget <https://www.python.org/ftp/python/3.9.13/Python-3.9.13.tgz>    


(2) 解压安装包 解压到指定目录：/usr/local/   


[root@centos7 Downloads]# tar -xvf Python-3.9.13.tgz -C /usr/local/   


(3) 编译安装包

**因为下载的包未编译，所以我们需要编译一下，先创建编译安装目录/usr/local/python3，再到/usr/local/Python-3.9.13 编译。**  


[root@centos7 Downloads]# mkdir -p /usr/local/python3   


[root@centos7 Downloads]# cd /usr/local/Python-3.9.13   


[root@centos7 Python-3.9.13]# ./configure --prefix=/usr/local/python3   


![avatar](/xtp-pro/assets/5.Dn7KxzJ8.png)  


**注意** ：

（1）--prefix=是指定安装的目录，可以把所有资源文件放在/usr/local/python3路径下，这样不会杂乱，也便于卸载或移植软件。   


（2）如果编译报错，就先执行make clean，再重新执行 ./configure。   


[root@centos7 Python-3.9.13]# make clean   


[root@centos7 Python-3.9.13]# ./configure --prefix=/usr/local/python3   


（3）如果编译成功，则直接执行make ，再执行make install。   


[root@centos7 Python-3.9.13]# make   


[root@centos7 Python-3.9.13]# make install   


执行完毕，就可以切换到/usr/local/python3/bin目录去查看了。

![avatar](/xtp-pro/assets/6.S3zpr9wU.png)  


**步骤四. 创建软链接**

可通过软链接保留多个python版本，这个软链接决定了在命令行运行python的默认版本。  
  


(1) 先修改旧版本的软链接

[root@centos7 bin]# unlink python   


(2) 再创建新版本的软连接     [root@centos7 bin]# ln -s /usr/local/python3/bin/python3.9 /usr/bin/python

![avatar](/xtp-pro/assets/7.BRkHS6bR.png)  


(3) 检查python版本

[root@centos7 bin]# python -V

![avatar](data:image/png;base64,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)  


软链接创建成功。   


### 1.3. 安装编译boost_1_80_0 ​

**进入官网[http://www.boost.org/，选择较新的稳定版本，并且跟python版本相对应，这里是1.80.0版本。](http://www.boost.org/%EF%BC%8C%E9%80%89%E6%8B%A9%E8%BE%83%E6%96%B0%E7%9A%84%E7%A8%B3%E5%AE%9A%E7%89%88%E6%9C%AC%EF%BC%8C%E5%B9%B6%E4%B8%94%E8%B7%9Fpython%E7%89%88%E6%9C%AC%E7%9B%B8%E5%AF%B9%E5%BA%94%EF%BC%8C%E8%BF%99%E9%87%8C%E6%98%AF1.80.0%E7%89%88%E6%9C%AC%E3%80%82)**  


**步骤一. 下载boost_1_80_0安装包，解压缩**  
可手动下载到Downloads文件夹：  
  


下载链接：<https://www.boost.org/users/history/version_1_80_0.html>

![avatar](/xtp-pro/assets/9.D2hu8qC3.png)  


或者wget命令下载到Downloads文件夹：  
  


[root@centos7 Downloads]# wget <https://boostorg.jfrog.io/artifactory/main/release/1.80.0/source/boost_1_80_0.tar.gz>  


**步骤二. 解压安装包**

解压到指定目录：/usr/local/

[root@centos7 Downloads]# tar -xvf /home/sophie/Downloads/boost_1_80_0.tar.gz -C /usr/local/   


**步骤三. 编译**

进入/usr/local/boost_1_80_0目录编译   


[root@centos7 Downloads]# cd /usr/local/boost_1_80_0/   


执行bootstrap.sh   


[root@centos7 boost_1_80_0]# ./bootstrap.sh --with-python=/usr/local/python3   


![avatar](/xtp-pro/assets/10.B0zRrDgR.png)  


**步骤四. 安装**

**说明：--with-python 需要python3版本，通过include参数指定自定义版本的python包含路径**  


[root@centos7 boost_1_80_0]# ./b2 --toolset=gcc-4.8.5 --with-python include="/usr/local/python3/include/python3.9/" --with-system --with-thread --with-date_time --with-chrono   


![avatar](/xtp-pro/assets/11.oGTK5JMU.png)  


**boost目录下会生成stage文件夹，/stage/lib就是C++所需的python3的lib文件。至此boost.python3库编译完成。如下图所示：**  


![avatar](/xtp-pro/assets/12.BAy_9lHw.png)  


**编译生成的 /usr/local/boost_1_80_0/stage/lib文件，如下图所示：**  


![avatar](/xtp-pro/assets/13.B4uLyO9J.png)  


### 1.4. 编译source ​

**如果没有特殊的需求，建议使用python3.9.13版本，直接使用我们提供的库。**  


如果是其他python版本，则需要根据自己编译安装的python版本，及该python版本对应的编译后的boost库，自行编译所需的python封装库。   


xtp_api_python-master/source下有封装api的python源码。   


**步骤一. 查看CMakeList.txt中python和boost路径**

**路径：xtp_pro_api_python-master/source/Linux/xtpx_python_1.0.13/CMakeLists.txt**  


注意：设置python目录及boost库目录要正确，必须为解压缩后的路径。   


![avatar](/xtp-pro/assets/14.B9hsTw_M.png)  


**步骤二. 选择对应版本的行情库**

对于行情，在行情配置文件quote_config.ini设置启用enable_efvi=ON 且服务器是solarflare网卡的用户，要注意服务器安装的onload版本，XTP-Pro只提供了两种onload版本的库文件，路径分别是：

(1) xtp_pro_api_python-master/source/Linux/xtpx_api_python_1.0.13/onload-7.1.0.265/libxtpxquoteapi.so (2) xtp_pro_api_python-master/source/Linux/xtpx_api_python_1.0.13/onload-8.1.2.26/libxtpxquoteapi.so

如果服务器不是solarflare网卡的话，也就不能启用enable_efvi=ON的配置，对于这样的用户，建议使用路径onload-8.1.2.26/libxtpxquoteapi.so的库文件编译代码。

用户请将对应版本路径下的库文件libxtpxquoteapi.so复制到文件夹xtpxapi下编译源码。

**步骤三. 执行build.sh**

**路径：xtp_pro_api_python-master/source/Linux/xtpx_api_python_1.0.13/build.sh**  


进入：xtp_pro_api_python-master/source/Linux/xtpx_api_python_1.0.13/  
  


[root@centos7 xtpx_python_1.0.13]# ./build.sh  
  


![avatar](/xtp-pro/assets/15.DM1nRdOH.png)  


**执行完毕后，该目录会生成vnxtpxquote.so和vnxtpxtrader.so库文件。**  
  


![avatar](/xtp-pro/assets/16.BMNiJ44V.png)  


### 1.5. 运行Demo ​

**运行方式：把xtpxapi中两个.so文件、编译source生成的两个.so文件，以及/bin/test中的两个.py文件 拷贝到对应的平台下，并修改.py文件的账户信息，启动脚本运行。****运行平台路径如：xtp_pro_api_python-master/bin/Linux/centos7+python3.9/。**  
  


（1）先将xtpapi中原有的两个库文件 libxtpxquoteapi.so、libxtpxtraderapi.so 拷贝至 运行平台路径下。   


（2）再将编译source生成的两个库文件 vnxtpxquote.so、vnxtpxtrader.so 拷贝至 运行平台路径下。   


（3）最后将/bin/test中的两个脚本文件 quotetest.py 和 tradertest.py 拷贝至 运行平台路径下。   


![avatar](/xtp-pro/assets/17.B7MXQ_rp.png)  


（4）如果测试行情，则修改quotetest.py文件，改为实际使用的 ip、port、user、password、local_ip，然后运行quotetest.py。  
  


![avatar](/xtp-pro/assets/18.CPWTBvBj.png)  


**命令提示符方式如下：**  


[root@centos7 centos7+python3.9]# python quotetest.py  
（5）如果测试交易，则修改tradertest.py文件，改为实际使用的 ip、port、user、password、local_ip，然后运行tradertest.py。  
  


**命令提示符方式如下：**  


[root@centos7 centos7+python3.9]# python tradertest.py  
  


## **2．windows环境下编译说明** ​

### 2.1. win10参考环境 ​

Windows10 (64位)   


cmake-3.4.1(64位.zip)

VS2010 (V10.0版本) 或VS2015(V14.0版本)   


python3.9.13 (64位)   


boost_1_80_0 (64位.7z)   


### 2.2. 安装64位python3.9.13 ​

**步骤一. 下载python**

进入官网：[https://www.python.org/downloads/windows/，选择64位python3.9.13](https://www.python.org/downloads/windows/%EF%BC%8C%E9%80%89%E6%8B%A964%E4%BD%8Dpython3.9.13)  


说明：python3开始使用的是Anaconda3，但是在编译boost时提示错误，无法完成编译，所以最终选择的是64位python3.9.13。   


![avatar](/xtp-pro/assets/w_1.CTYqSpIl.png)  


**步骤二. 安装python**

![avatar](/xtp-pro/assets/w_2.fcnfCPC-.png)  


![avatar](/xtp-pro/assets/w_3.7acx8N_I.png)  


![avatar](/xtp-pro/assets/w_4.Di1yDfK6.png)  


**步骤三. 查看python版本**

安装成功后，打开cmd进入命令提示符，输入：python --version

![avatar](/xtp-pro/assets/w_5.8XaaVzLQ.png)  


### 2.3. 安装64位boost_1_80_0 ​

**步骤一. 下载boost**

进入官网：[http://www.boost.org/，选择较新的稳定版本，并且跟python版本相对应，这里是1.80.0版本](http://www.boost.org/%EF%BC%8C%E9%80%89%E6%8B%A9%E8%BE%83%E6%96%B0%E7%9A%84%E7%A8%B3%E5%AE%9A%E7%89%88%E6%9C%AC%EF%BC%8C%E5%B9%B6%E4%B8%94%E8%B7%9Fpython%E7%89%88%E6%9C%AC%E7%9B%B8%E5%AF%B9%E5%BA%94%EF%BC%8C%E8%BF%99%E9%87%8C%E6%98%AF1.80.0%E7%89%88%E6%9C%AC)  


(1) 官网选择历史版本

![avatar](/xtp-pro/assets/w_6.cQR9cNYs.png)  


或直接从官网链接下载

下载链接：[https://boostorg.jfrog.io/artifactory/main/release/1.80.0/source/，选择boost_1_80_0.7z](https://boostorg.jfrog.io/artifactory/main/release/1.80.0/source/%EF%BC%8C%E9%80%89%E6%8B%A9boost_1_80_0.7z)  
    **步骤二. 解压缩、安装** 下载完成之后，解压至 D:\MyThird\boost_1_80_0  
  


### 2.4. 安装VS2015 ​

下载并安装 VS2010 或 VS2015，或者 VSCode。   


### 2.5. 编译boost.python库 ​

以VS2015版本64位为例，打开64位的编译终端，注意：以“管理员身份运行”。   


![avatar](/xtp-pro/assets/w_7.D_g53SoW.png)  


**步骤一. 执行bootstrap.bat**

（1）切换到D盘，执行命令：   


C:\WINDOWS\system32>d:  
  


（2）进入boost源码目录，执行命令：

D:>cd MyThird\boost_1_80_0  
  


（3）运行bootstrap.bat，执行命令：   


D:\MyThird\boost_1_80_0>bootstrap.bat  
  


运行成功后，生成 b2.exe文件。

注意：较高版本的boost，运行成功只会生成b2.exe，不会生成bjam.exe。

  


![avatar](/xtp-pro/assets/w_8.BdT56-hb.png)  


![avatar](/xtp-pro/assets/w_9.9gkoxFHx.png)  


**步骤二. 编译，生成64位的静态库**

在命令行继续执行命令：   


D:\MyThird\boost_1_80_0>b2 --toolset=msvc-14.0 --with-python --with-thread --with-date_time \--build-type=complete address-model=64   


![avatar](/xtp-pro/assets/w_10.Cod_8VyU.png)  


说明：

（1）如果使用较高版本的boost没有生成bjam.exe，那么只能使用b2编译，而不能使用 bjam --toolset。   


（2） --toolset=msvc-14.0 表示VS2015的版本号为14.0，如果使用的VS2010则=msvc-10.0，请更改为实际使用的VS版本号。   


（3）address-model=64 表示生成的库为64位，如果=32就表示32位。   


（4） --with-python，系统要能找安装的python3版本，直接在cmd里面输入python能弹出python3的具体版本信息。  
  
![avatar](/xtp-pro/assets/w_11.CQ0pzqwG.png)  


**执行成功后，在boost_1_80_0/stage/lib/下就是C++所需python的lib文件。至此boost.python库编译完成。**

![avatar](/xtp-pro/assets/w_12.C2LvtqP8.png)  


### 2.6. 使用CMake生成工程 ​

**步骤一. 创建工程目录**

**python版本SDK的 source下包含 C++版本的api 和 封装api的python源码。** （1）python版本SDK下载地址：[https://github.com/ztsec/xtp_pro_api_python/，](https://github.com/ztsec/xtp_pro_api_python/%EF%BC%8C) 下载后解压缩 xtp_pro_api_python-master.zip。   


（2）将source/Windows/xtp_pro_api_python_1.0.13/ 下所有文件拷贝到 D:/XTPPythonDemo文件夹。   


（3）在XTPPythonDemo下创建build文件夹。   
  **步骤二. 修改CMakeLists.txt**

![avatar](/xtp-pro/assets/w_13.CWQCrMPG.png)  


**步骤三. Cmake配置**

（1）点击Browse Source按钮，指定XTPPythonDemo文件夹。   


（2）点击Browse Build按钮，指定XTPPythonDemo/build文件夹。   


（3）点击Configure按钮，选择VS版本，同编译boost.python库的vs版本一致。   


![avatar](/xtp-pro/assets/w_14.CgXaTuTV.png)  


**步骤四. Cmake生成工程**

点击Genertate按钮，执行成功后，可进入build文件夹查看生成的C++工程。   


![avatar](/xtp-pro/assets/w_15.BnryOkXp.png)  


### 2.7. 编译source ​

**将source下封装api的python源码，编译生成64位的release版本库文件：vnxtpxquote.dll、vnxtpxtrader.dll。**

（1）进入D:/XTPPythonDemo/build/，使用VS2015打开.sln工程，配置X64位、release版本。   


（2）点击菜单 生成->生成解决方案，编译成功后，可至 XTPPythonDemo/build/lib/Release/ 查看生成的 vnxtpxquote.dll、vnxtpxtrader.dll文件。   


（3）将生成的.dll文件后缀改名为.pyd，也可点击Cmake的Genertate按钮生成.pyd文件，修改成功后显示为 vnxtpxquote.pyd、vnxtpxtrader.pyd文件。  
  


### 2.8. 运行Demo ​

**运行方式：把xtpxapi中两个.dll文件、编译source生成的两个.pyd文件，以及/bin/test中的两个.py文件 拷贝到对应的平台下，并修改.py文件的账户信息，启动脚本运行。**

运行平台路径如：xtp_pro_api_python-master/bin/Windows/win64+python3.9/。  
  


（1）先将xtpapi中原有的库文件 xtpxquoteapi.dll、xtpxtraderapi.dll 拷贝至 运行平台路径下。  
  


（2）再将编译source生成的库文件 vnxtpxquote.pyd、vnxtpxtrader.pyd 拷贝至 运行平台路径下。   


（3）最后将/bin/test中的脚本文件 quotetest.py 和 tradertest.py 拷贝至 运行平台路径下。   


（4）如果测试行情，则修改quotetest.py文件，改为实际使用的 ip、port、user、password、local_ip，然后运行quotetest.py。  
  


**命令提示符方式如下：**  


C:WINDOWS\system32> python D:\xtp_pro_api_python-master\bin\Windows\win64+python3.9\quotetest.py  
  
如果测试交易，则修改tradertest.py文件，改为实际使用的 ip、port、user、password、local_ip，然后运行tradertest.py。  
  


**命令提示符方式如下：**  


C:WINDOWS\system32> python D:\xtp_pro_api_python-master\bin\Windows\win64+python3.9\tradertest.py
