---
exchange: binance
source_url: https://developers.binance.com/en/docs/products/mini-program/openservice/preparation
api_type: Guide
updated_at: 2026-11-20 18:38:39.932889
---

# Preparation

## <a name="preparation"></a>Preparation

### <a name="create-account"></a>Create a Developer Account on the Merchant Workspace

Merchants can apply for a developer account on the Merchant Workspace after completing the Know Your
Business (KYB) process.

### <a name="create-ak-sk"></a>Create AK and SK on the Merchant Workspace

Navigate to the Development Page in the Merchant Workspace.
![Development Page](/img/mp-management/mp-open-service-002.png)

<a name="create"></a>Click the 'Create' button.
![Create](/img/mp-management/mp-open-service-003.png) Please note, the Secret Key (SK) will only be
displayed once. Ensure to record the SK safely, as it will be required for accessing the OpenService
API. ![SK](/img/mp-management/mp-open-service-004.png)

### <a name="upload-rsa-key"></a>Upload RSA Public Key

Navigate to the Settings Page within the Merchant Workspace.
![Settings](/img/mp-management/mp-open-service-005.png)

**Generating an RSA Key Pair** Several tools are available for generating an RSA key pair. The steps
below detail how to generate this key pair using OpenSSL.

**1. Install OpenSSL.**

- For Linux systems, use the following command:

```shell
\>> sudo apt-get install openssl
```

- For Windows systems, download and install OpenSSL from the official website.

**2. Generate RSA Key Pair.**

- For Linux systems, use the following commands:

```shell
\>> $ openssl

OpenSSL> genrsa -out rsa\_private\_key.pem 2048 ##generate private key

OpenSSL> rsa -in rsa\_private\_key.pem -pubout -out rsa\_public\_key.pem
```

**Upload the RSA Public Key**

![Upload Key](/img/mp-management/mp-open-service-006.png)

---

# Preparation

## <a name="preparation"></a>Preparation

### <a name="create-account"></a>Create a Developer Account on the Merchant Workspace

Merchants can apply for a developer account on the Merchant Workspace after completing the Know Your
Business (KYB) process.

### <a name="create-ak-sk"></a>Create AK and SK on the Merchant Workspace

Navigate to the Development Page in the Merchant Workspace.
![Development Page](/img/mp-management/mp-open-service-002.png)

<a name="create"></a>Click the 'Create' button.
![Create](/img/mp-management/mp-open-service-003.png) Please note, the Secret Key (SK) will only be
displayed once. Ensure to record the SK safely, as it will be required for accessing the OpenService
API. ![SK](/img/mp-management/mp-open-service-004.png)

### <a name="upload-rsa-key"></a>Upload RSA Public Key

Navigate to the Settings Page within the Merchant Workspace.
![Settings](/img/mp-management/mp-open-service-005.png)

**Generating an RSA Key Pair** Several tools are available for generating an RSA key pair. The steps
below detail how to generate this key pair using OpenSSL.

**1. Install OpenSSL.**

- For Linux systems, use the following command:

```shell
\>> sudo apt-get install openssl
```

- For Windows systems, download and install OpenSSL from the official website.

**2. Generate RSA Key Pair.**

- For Linux systems, use the following commands:

```shell
\>> $ openssl

OpenSSL> genrsa -out rsa\_private\_key.pem 2048 ##generate private key

OpenSSL> rsa -in rsa\_private\_key.pem -pubout -out rsa\_public\_key.pem
```

**Upload the RSA Public Key**

![Upload Key](/img/mp-management/mp-open-service-006.png)