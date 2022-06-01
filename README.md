[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# lojack-clients
A collection of client libraries and OpenAPI documentation files for accessing Spireon LoJack's APIs.

## Description
This package first and foremost contains unofficial OpenAPI documentation for the APIs that are used for the Spireon LoJack's application. There are four different services that have been identified, each with an API that has its own subdomain. These include `identity`, `automotive`, `maintenance`, and `services`.

The OpenAPI documentation files can be found under the `openapi` directory. Each service has their own subdirectory which contains only a single `openapi.yaml` file documenting the services' API.

Additionally, this package contains Python client libraries that have been generated from the OpenAPI documentation using the [openapi-generators/openapi-python-client](https://github.com/openapi-generators/openapi-python-client). Everything inside the `lojack_clients` directory has been generated using the client generator. There are however some minor customizations made to the templates that the generator uses to generate the client classes. These customizations were necessary to make the client work with the APIs' authentication schemes.

### Services
Each different service has its own purpose with separate endpoints. You will likely primarily be interacting with the `identity` and `services` services. It is likely that there are more services and endpoints that exist, however these ones listed are only the ones that have been discovered so far.

#### identity
This service contains a single endpoint which is used for authenticating and generating an access token that can be used with other services.

#### automotive
This service contains a single endpoint used to get information about the dealership that your account is associated with.

#### maintenance
This service contains two endpoints that relate to maintenance of your car, one for getting repair orders and another for getting a vehicle's suggested maintenance schedule.

#### services
This service contains several endpoints which are responsible for the vast majority of the functionality within the LoJack application.

## Usage
Each service acts as its own library with its own client class.

First, you will need to instantiate the identity client which you will use to generate an access token. You should use the `from_login` class factory method to instantiate the identity client.

```python
from lojack_clients.identity import AuthenticatedClient as IdentityClient

identity_client = IdentityClient.from_login(username, password)
```
Here the `AuthenticatedClient` import is aliased as `IdentityClient` to avoid conflicts with `AuthenticatedClient` classes from the other services' client libraries.

All endpoints require authentication so you will only use the `AuthenticatedClient`. 

Next, you will need to call the get_identity_token endpoint to retrieve an access token:

```python
from lojack_clients.identity.models import GetIdentityTokenResponse200
from lojack_clients.identity.api.default import get_identity_token
from lojack_clients.identity.types import Response as IdentityResponse

token_response: GetIdentityTokenResponse200 = get_identity_token.sync(client=identity_client)
# or if you need more info (e.g. status_code)
token_response: Response[GetIdentityTokenResponse200] = get_identity_token.sync_detailed(client=identity_client)
```

Or do the same thing with an async version:

```python
from lojack_clients.identity.models import GetIdentityTokenResponse200
from lojack_clients.identity.api.default import get_identity_token
from lojack_clients.identity.types import Response as IdentityResponse

token_response: GetIdentityTokenResponse200 = await get_identity_token.asyncio(client=identity_client)
# or if you need more info (e.g. status_code)
token_response: Response[GetIdentityTokenResponse200] = await get_identity_token.asyncio_detailed(client=identity_client)
```

Here the `Response` import is aliased as `IdentityResponse` to avoid conflicts with `Response` classes from the other services' client libraries.

*Because each of the client libraries are automatically generated, the `Response` classes for each library are all the same and interchangeable.*

You can then instantiate any of the other three clients using the access token found in the identity response. You should use the `from_token` class factory method to instantiate any of the other three clients.

```python
from lojack_clients.services import AuthenticatedClient as ServicesClient

# if you used the sync or asyncio methods
services_client = ServicesClient.from_token(token_response.token)

# or if you used sync_detailed or asyncio_detailed methods
services_client = ServicesClient.from_token(token_response.parsed.token)
```

You can now use this client to call any of the other endpoints from within the service, similar to how the identity client was used to call the get_identity_token endpoint.

```python
from lojack_clients.services.models import GetAllUserAssetsResponse200
from lojack_clients.services.api.default import get_all_user_assets
from lojack_clients.services.types import Response as ServicesResponse

assets_response: GetAllUserAssetsResponse200 = get_all_user_assets.sync(client=services_client)
```

Just as the endpoint before, you can use `sync_detailed` if you need more information about the response, and `asyncio` / `asyncio_detailed` to do the same with async calls.

Putting all the steps together, this is what it would look like to authenticate and make a call to retrieve all user assets.

```python
from lojack_clients.identity import AuthenticatedClient as IdentityClient
from lojack_clients.identity.models import GetIdentityTokenResponse200
from lojack_clients.identity.api.default import get_identity_token
from lojack_clients.identity.types import Response as IdentityResponse
from lojack_clients.services import AuthenticatedClient as ServicesClient
from lojack_clients.services.models import GetAllUserAssetsResponse200
from lojack_clients.services.api.default import get_all_user_assets
from lojack_clients.services.types import Response as ServicesResponse

identity_client = IdentityClient.from_login(username, password)
token_response: GetIdentityTokenResponse200 = get_identity_token.sync(client=identity_client)

services_client = ServicesClient.from_token(token_response.token)
assets_response: GetAllUserAssetsResponse200 = get_all_user_assets.sync(client=services_client)
```

Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but the async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` by async instead of blocking

1. All path/query params, and bodies become method arguments.
1. All endpoints can be found under `lojack_clients/{service}/api/default/{endpoint}.py`.
1. Endpoint file names are generated using the request's `operationId` key in the OpenAPI documentation (converted to snake_case).

## Development
All code inside the `lojack_clients` directory is automatically generated. If any changes are made to any of the services' openapi.yaml file, you can update the service's client library by running `./scripts/build_api_clients`. You can pass in specific services that you want to build libraries for, or you can call it without any arguments to build client libraries for all four services. For eg. `./scripts/build_api_clients services identity` would build the libraries for only the `services` and `identity` clients.

Customized template files for the client libraries exist under `./client-generator/templates/{service}`. If you need to customize some of the generated code you can add or modify Jinja template files there.

Other information about how the code is generated and how it can be configured can be found within the [openapi-generators/openapi-python-client](https://github.com/openapi-generators/openapi-python-client) project on GitHub.

## Contributing
If you know of any endpoints or services that aren't disclosed here you're welcome to open up a pull request to add them to the OpenAPI documentation. If there are any other improvements or suggestions, feel free to open a pull request or an issue.

## Disclaimer
This project is not affiliated, associated, authorized, endorsed by, or in any way officially connected with Spireon, Inc. The names Spireon and LoJack are trademarks or registered trademarks of Spireon and its subsidiaries. Any related names, marks, emblems and images are registered trademarks of their respective owners. This project has been developed entirely through the use and observation of publicly available information. Use of this project or information within this project comes with no guarantees or warranties. Whenever using or interacting with any services from Spireon, Inc. you must ensure that you are following the Spireon, Inc. terms of service agreement as well as any other agreements that may apply. If you are associated with Spireon, inc and have any questions or concerns, please [submit an issue](https://github.com/scorgn/lojack-clients/issues/new) on the GitHub repository.
