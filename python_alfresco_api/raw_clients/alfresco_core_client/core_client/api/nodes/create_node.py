from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.node_body_create import NodeBodyCreate
from ...models.node_entry import NodeEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    node_id: str,
    *,
    body: Union[
        NodeBodyCreate,
        NodeBodyCreate,
    ],
    auto_rename: Union[Unset, bool] = UNSET,
    major_version: Union[Unset, bool] = UNSET,
    versioning_enabled: Union[Unset, bool] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["autoRename"] = auto_rename

    params["majorVersion"] = major_version

    params["versioningEnabled"] = versioning_enabled

    json_include: Union[Unset, list[str]] = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/nodes/{node_id}/children",
        "params": params,
    }

    if isinstance(body, NodeBodyCreate):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, NodeBodyCreate):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, NodeEntry]]:
    if response.status_code == 201:
        response_201 = NodeEntry.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413
    if response.status_code == 415:
        response_415 = cast(Any, None)
        return response_415
    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422
    if response.status_code == 507:
        response_507 = cast(Any, None)
        return response_507
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, NodeEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NodeBodyCreate,
        NodeBodyCreate,
    ],
    auto_rename: Union[Unset, bool] = UNSET,
    major_version: Union[Unset, bool] = UNSET,
    versioning_enabled: Union[Unset, bool] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, NodeEntry]]:
    r"""Create a node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Create a node and add it as a primary child of node **nodeId**.

    This endpoint supports both JSON and multipart/form-data (file upload).

    **Using multipart/form-data**

    Use the **filedata** field to represent the content to upload, for example, the following curl
    command will
    create a node with the contents of test.txt in the test user's home folder.

    ```curl -utest:test -X POST
    host:port/alfresco/api/-default-/public/alfresco/versions/1/nodes/-my-/children -F
    filedata=@test.txt```

    You can use the **name** field to give an alternative name for the new file.

    You can use the **nodeType** field to create a specific type. The default is cm:content.

    You can use the **renditions** field to create renditions (e.g. doclib) asynchronously upon upload.
    Also, as requesting rendition is a background process,
    any rendition failure (e.g. No transformer is currently available) will not fail the whole upload
    and has the potential to silently fail.

    Use **overwrite** to overwrite an existing file, matched by name. If the file is versionable,
    the existing content is replaced.

    When you overwrite existing content, you can set the **majorVersion** boolean field to **true** to
    indicate a major version
    should be created. The default for **majorVersion** is **false**.
    Setting  **majorVersion** enables versioning of the node, if it is not already versioned.

    When you overwrite existing content, you can use the **comment** field to add a version comment that
    appears in the
    version history. This also enables versioning of this node, if it is not already versioned.

    You can set the **autoRename** boolean field to automatically resolve name clashes. If there is a
    name clash, then
    the API method tries to create a unique name using an integer suffix.

    You can use the **relativePath** field to specify the folder structure to create relative to the
    node **nodeId**.
    Folders in the **relativePath** that do not exist are created before the node is created.

    Any other field provided will be treated as a property to set on the newly created node.

    **Note:** setting properties of type d:content and d:category are not supported.

    **Note:** When creating a new node using multipart/form-data by default versioning is enabled and
    set to MAJOR Version.
    Since Alfresco 6.2.3 **versioningEnabled** flag was introduced offering better control over the new
    node Versioning.

    | **versioningEnabled** | **majorVersion** | **Version Type** |
    |-----------------------|------------------|------------------|
    |        unset          |        unset     |    MAJOR         |
    |        unset          |        true      |    MAJOR         |
    |        unset          |        false     |    MINOR         |
    |        true           |        unset     |    MAJOR         |
    |        true           |        true      |    MAJOR         |
    |        true           |        false     |    MINOR         |
    |        false          |        true      |    Unversioned   |
    |        false          |        false     |    Unversioned   |
    |        false          |        true      |    Unversioned   |
    <br>

    **Using JSON**

    You must specify at least a **name** and **nodeType**. For example, to create a folder:
    ```JSON
    {
      \"name\":\"My Folder\",
      \"nodeType\":\"cm:folder\"
    }
    ```

    You can create an empty file like this:
    ```JSON
    {
      \"name\":\"My text file.txt\",
      \"nodeType\":\"cm:content\"
    }
    ```
    You can update binary content using the ```PUT /nodes/{nodeId}``` API method.

    You can create a folder, or other node, inside a folder hierarchy:
    ```JSON
    {
      \"name\":\"My Special Folder\",
      \"nodeType\":\"cm:folder\",
      \"relativePath\":\"X/Y/Z\"
    }
    ```
    The **relativePath** specifies the folder structure to create relative to the node **nodeId**.
    Folders in the
    **relativePath** that do not exist are created before the node is created.

    You can set properties when you create a new node:
    ```JSON
    {
      \"name\":\"My Other Folder\",
      \"nodeType\":\"cm:folder\",
      \"properties\":
      {
        \"cm:title\":\"Folder title\",
        \"cm:description\":\"This is an important folder\"
      }
    }
    ```

    You can set multi-value properties when you create a new node which supports properties of type
    multiple.
     ```JSON
    {
      \"name\":\"My Other Folder\",
      \"nodeType\":\"custom:destination\",
      \"properties\":
      {
        \"cm:title\":\"Folder title\",
        \"cm:description\":\"This is an important folder\",
        \"custom:locations\": [
                             \"location X\",
                             \"location Y\"
                            ]
      }
    }
    ```

    Any missing aspects are applied automatically. For example, **cm:titled** in the JSON shown above.
    You can set aspects
    explicitly, if needed, using an **aspectNames** field.

    **Note:** setting properties of type d:content and d:category are not supported.

    You can also optionally disable (or enable) inherited permissions via *isInheritanceEnabled* flag:
    ```JSON
    {
      \"permissions\":
        {
          \"isInheritanceEnabled\": false,
          \"locallySet\":
            [
              {\"authorityId\": \"GROUP_special\", \"name\": \"Read\", \"accessStatus\":\"DENIED\"},
              {\"authorityId\": \"testuser\", \"name\": \"Contributor\", \"accessStatus\":\"ALLOWED\"}
            ]
        }
    }
    ```

    Typically, for files and folders, the primary children are created within the parent folder using
    the default \"cm:contains\" assocType.
    If the content model allows then it is also possible to create primary children with a different
    assoc type. For example:
    ```JSON
    {
      \"name\":\"My Node\",
      \"nodeType\":\"my:specialNodeType\",
      \"association\":
      {
        \"assocType\":\"my:specialAssocType\"
      }
    }
    ```

    Additional associations can be added after creating a node. You can also add associations at the
    time the node is created. This is
    required, for example, if the content model specifies that a node has mandatory associations to one
    or more existing nodes. You can optionally
    specify an array of **secondaryChildren** to create one or more secondary child associations, such
    that the newly created node acts as a parent node.
    You can optionally specify an array of **targets** to create one or more peer associations such that
    the newly created node acts as a source node.
    For example, to associate one or more secondary children at time of creation:
    ```JSON
    {
      \"name\":\"My Folder\",
      \"nodeType\":\"cm:folder\",
      \"secondaryChildren\":
        [ {\"childId\":\"abcde-01234-...\", \"assocType\":\"my:specialChildAssocType\"} ]
    }
    ```
    For example, to associate one or more targets at time of creation:
    ```JSON
    {
      \"name\":\"My Folder\",
      \"nodeType\":\"cm:folder\",
      \"targets\":
        [ {\"targetId\":\"abcde-01234-...\", \"assocType\":\"my:specialPeerAssocType\"} ]
    }
    ```

    **Note:** You can create more than one child by
    specifying a list of nodes in the JSON body. For example, the following JSON
    body creates two folders inside the specified **nodeId**, if the **nodeId** identifies
    a folder:

    ```JSON
    [
      {
        \"name\":\"My Folder 1\",
        \"nodeType\":\"cm:folder\"
      },
      {
        \"name\":\"My Folder 2\",
        \"nodeType\":\"cm:folder\"
      }
    ]
    ```
    If you specify a list as input, then a paginated list rather than an entry is returned in the
    response body. For example:

    ```JSON
    {
      \"list\": {
        \"pagination\": {
          \"count\": 2,
          \"hasMoreItems\": false,
          \"totalItems\": 2,
          \"skipCount\": 0,
          \"maxItems\": 100
        },
        \"entries\": [
          {
            \"entry\": {
              ...
            }
          },
          {
            \"entry\": {
              ...
            }
          }
        ]
      }
    }
    ```
    **Note:** When creating a new node using JSON by default versioning is disabled.
    Since Alfresco 6.2.3 **versioningEnabled** flag was introduced offering better control over the new
    node Versioning.

    | **versioningEnabled** | **majorVersion** | **Version Type** |
    |-----------------------|------------------|------------------|
    |        unset          |        unset     |    Unversioned   |
    |        unset          |        true      |    MAJOR         |
    |        unset          |        false     |    MINOR         |
    |        true           |        unset     |    MAJOR         |
    |        true           |        true      |    MAJOR         |
    |        true           |        false     |    MINOR         |
    |        false          |        true      |    Unversioned   |
    |        false          |        false     |    Unversioned   |
    |        false          |        true      |    Unversioned   |
    <br>

    Args:
        node_id (str):
        auto_rename (Union[Unset, bool]):
        major_version (Union[Unset, bool]):
        versioning_enabled (Union[Unset, bool]):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        body (NodeBodyCreate):
        body (NodeBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NodeEntry]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        body=body,
        auto_rename=auto_rename,
        major_version=major_version,
        versioning_enabled=versioning_enabled,
        include=include,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NodeBodyCreate,
        NodeBodyCreate,
    ],
    auto_rename: Union[Unset, bool] = UNSET,
    major_version: Union[Unset, bool] = UNSET,
    versioning_enabled: Union[Unset, bool] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, NodeEntry]]:
    r"""Create a node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Create a node and add it as a primary child of node **nodeId**.

    This endpoint supports both JSON and multipart/form-data (file upload).

    **Using multipart/form-data**

    Use the **filedata** field to represent the content to upload, for example, the following curl
    command will
    create a node with the contents of test.txt in the test user's home folder.

    ```curl -utest:test -X POST
    host:port/alfresco/api/-default-/public/alfresco/versions/1/nodes/-my-/children -F
    filedata=@test.txt```

    You can use the **name** field to give an alternative name for the new file.

    You can use the **nodeType** field to create a specific type. The default is cm:content.

    You can use the **renditions** field to create renditions (e.g. doclib) asynchronously upon upload.
    Also, as requesting rendition is a background process,
    any rendition failure (e.g. No transformer is currently available) will not fail the whole upload
    and has the potential to silently fail.

    Use **overwrite** to overwrite an existing file, matched by name. If the file is versionable,
    the existing content is replaced.

    When you overwrite existing content, you can set the **majorVersion** boolean field to **true** to
    indicate a major version
    should be created. The default for **majorVersion** is **false**.
    Setting  **majorVersion** enables versioning of the node, if it is not already versioned.

    When you overwrite existing content, you can use the **comment** field to add a version comment that
    appears in the
    version history. This also enables versioning of this node, if it is not already versioned.

    You can set the **autoRename** boolean field to automatically resolve name clashes. If there is a
    name clash, then
    the API method tries to create a unique name using an integer suffix.

    You can use the **relativePath** field to specify the folder structure to create relative to the
    node **nodeId**.
    Folders in the **relativePath** that do not exist are created before the node is created.

    Any other field provided will be treated as a property to set on the newly created node.

    **Note:** setting properties of type d:content and d:category are not supported.

    **Note:** When creating a new node using multipart/form-data by default versioning is enabled and
    set to MAJOR Version.
    Since Alfresco 6.2.3 **versioningEnabled** flag was introduced offering better control over the new
    node Versioning.

    | **versioningEnabled** | **majorVersion** | **Version Type** |
    |-----------------------|------------------|------------------|
    |        unset          |        unset     |    MAJOR         |
    |        unset          |        true      |    MAJOR         |
    |        unset          |        false     |    MINOR         |
    |        true           |        unset     |    MAJOR         |
    |        true           |        true      |    MAJOR         |
    |        true           |        false     |    MINOR         |
    |        false          |        true      |    Unversioned   |
    |        false          |        false     |    Unversioned   |
    |        false          |        true      |    Unversioned   |
    <br>

    **Using JSON**

    You must specify at least a **name** and **nodeType**. For example, to create a folder:
    ```JSON
    {
      \"name\":\"My Folder\",
      \"nodeType\":\"cm:folder\"
    }
    ```

    You can create an empty file like this:
    ```JSON
    {
      \"name\":\"My text file.txt\",
      \"nodeType\":\"cm:content\"
    }
    ```
    You can update binary content using the ```PUT /nodes/{nodeId}``` API method.

    You can create a folder, or other node, inside a folder hierarchy:
    ```JSON
    {
      \"name\":\"My Special Folder\",
      \"nodeType\":\"cm:folder\",
      \"relativePath\":\"X/Y/Z\"
    }
    ```
    The **relativePath** specifies the folder structure to create relative to the node **nodeId**.
    Folders in the
    **relativePath** that do not exist are created before the node is created.

    You can set properties when you create a new node:
    ```JSON
    {
      \"name\":\"My Other Folder\",
      \"nodeType\":\"cm:folder\",
      \"properties\":
      {
        \"cm:title\":\"Folder title\",
        \"cm:description\":\"This is an important folder\"
      }
    }
    ```

    You can set multi-value properties when you create a new node which supports properties of type
    multiple.
     ```JSON
    {
      \"name\":\"My Other Folder\",
      \"nodeType\":\"custom:destination\",
      \"properties\":
      {
        \"cm:title\":\"Folder title\",
        \"cm:description\":\"This is an important folder\",
        \"custom:locations\": [
                             \"location X\",
                             \"location Y\"
                            ]
      }
    }
    ```

    Any missing aspects are applied automatically. For example, **cm:titled** in the JSON shown above.
    You can set aspects
    explicitly, if needed, using an **aspectNames** field.

    **Note:** setting properties of type d:content and d:category are not supported.

    You can also optionally disable (or enable) inherited permissions via *isInheritanceEnabled* flag:
    ```JSON
    {
      \"permissions\":
        {
          \"isInheritanceEnabled\": false,
          \"locallySet\":
            [
              {\"authorityId\": \"GROUP_special\", \"name\": \"Read\", \"accessStatus\":\"DENIED\"},
              {\"authorityId\": \"testuser\", \"name\": \"Contributor\", \"accessStatus\":\"ALLOWED\"}
            ]
        }
    }
    ```

    Typically, for files and folders, the primary children are created within the parent folder using
    the default \"cm:contains\" assocType.
    If the content model allows then it is also possible to create primary children with a different
    assoc type. For example:
    ```JSON
    {
      \"name\":\"My Node\",
      \"nodeType\":\"my:specialNodeType\",
      \"association\":
      {
        \"assocType\":\"my:specialAssocType\"
      }
    }
    ```

    Additional associations can be added after creating a node. You can also add associations at the
    time the node is created. This is
    required, for example, if the content model specifies that a node has mandatory associations to one
    or more existing nodes. You can optionally
    specify an array of **secondaryChildren** to create one or more secondary child associations, such
    that the newly created node acts as a parent node.
    You can optionally specify an array of **targets** to create one or more peer associations such that
    the newly created node acts as a source node.
    For example, to associate one or more secondary children at time of creation:
    ```JSON
    {
      \"name\":\"My Folder\",
      \"nodeType\":\"cm:folder\",
      \"secondaryChildren\":
        [ {\"childId\":\"abcde-01234-...\", \"assocType\":\"my:specialChildAssocType\"} ]
    }
    ```
    For example, to associate one or more targets at time of creation:
    ```JSON
    {
      \"name\":\"My Folder\",
      \"nodeType\":\"cm:folder\",
      \"targets\":
        [ {\"targetId\":\"abcde-01234-...\", \"assocType\":\"my:specialPeerAssocType\"} ]
    }
    ```

    **Note:** You can create more than one child by
    specifying a list of nodes in the JSON body. For example, the following JSON
    body creates two folders inside the specified **nodeId**, if the **nodeId** identifies
    a folder:

    ```JSON
    [
      {
        \"name\":\"My Folder 1\",
        \"nodeType\":\"cm:folder\"
      },
      {
        \"name\":\"My Folder 2\",
        \"nodeType\":\"cm:folder\"
      }
    ]
    ```
    If you specify a list as input, then a paginated list rather than an entry is returned in the
    response body. For example:

    ```JSON
    {
      \"list\": {
        \"pagination\": {
          \"count\": 2,
          \"hasMoreItems\": false,
          \"totalItems\": 2,
          \"skipCount\": 0,
          \"maxItems\": 100
        },
        \"entries\": [
          {
            \"entry\": {
              ...
            }
          },
          {
            \"entry\": {
              ...
            }
          }
        ]
      }
    }
    ```
    **Note:** When creating a new node using JSON by default versioning is disabled.
    Since Alfresco 6.2.3 **versioningEnabled** flag was introduced offering better control over the new
    node Versioning.

    | **versioningEnabled** | **majorVersion** | **Version Type** |
    |-----------------------|------------------|------------------|
    |        unset          |        unset     |    Unversioned   |
    |        unset          |        true      |    MAJOR         |
    |        unset          |        false     |    MINOR         |
    |        true           |        unset     |    MAJOR         |
    |        true           |        true      |    MAJOR         |
    |        true           |        false     |    MINOR         |
    |        false          |        true      |    Unversioned   |
    |        false          |        false     |    Unversioned   |
    |        false          |        true      |    Unversioned   |
    <br>

    Args:
        node_id (str):
        auto_rename (Union[Unset, bool]):
        major_version (Union[Unset, bool]):
        versioning_enabled (Union[Unset, bool]):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        body (NodeBodyCreate):
        body (NodeBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NodeEntry]
    """

    return sync_detailed(
        node_id=node_id,
        client=client,
        body=body,
        auto_rename=auto_rename,
        major_version=major_version,
        versioning_enabled=versioning_enabled,
        include=include,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NodeBodyCreate,
        NodeBodyCreate,
    ],
    auto_rename: Union[Unset, bool] = UNSET,
    major_version: Union[Unset, bool] = UNSET,
    versioning_enabled: Union[Unset, bool] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, NodeEntry]]:
    r"""Create a node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Create a node and add it as a primary child of node **nodeId**.

    This endpoint supports both JSON and multipart/form-data (file upload).

    **Using multipart/form-data**

    Use the **filedata** field to represent the content to upload, for example, the following curl
    command will
    create a node with the contents of test.txt in the test user's home folder.

    ```curl -utest:test -X POST
    host:port/alfresco/api/-default-/public/alfresco/versions/1/nodes/-my-/children -F
    filedata=@test.txt```

    You can use the **name** field to give an alternative name for the new file.

    You can use the **nodeType** field to create a specific type. The default is cm:content.

    You can use the **renditions** field to create renditions (e.g. doclib) asynchronously upon upload.
    Also, as requesting rendition is a background process,
    any rendition failure (e.g. No transformer is currently available) will not fail the whole upload
    and has the potential to silently fail.

    Use **overwrite** to overwrite an existing file, matched by name. If the file is versionable,
    the existing content is replaced.

    When you overwrite existing content, you can set the **majorVersion** boolean field to **true** to
    indicate a major version
    should be created. The default for **majorVersion** is **false**.
    Setting  **majorVersion** enables versioning of the node, if it is not already versioned.

    When you overwrite existing content, you can use the **comment** field to add a version comment that
    appears in the
    version history. This also enables versioning of this node, if it is not already versioned.

    You can set the **autoRename** boolean field to automatically resolve name clashes. If there is a
    name clash, then
    the API method tries to create a unique name using an integer suffix.

    You can use the **relativePath** field to specify the folder structure to create relative to the
    node **nodeId**.
    Folders in the **relativePath** that do not exist are created before the node is created.

    Any other field provided will be treated as a property to set on the newly created node.

    **Note:** setting properties of type d:content and d:category are not supported.

    **Note:** When creating a new node using multipart/form-data by default versioning is enabled and
    set to MAJOR Version.
    Since Alfresco 6.2.3 **versioningEnabled** flag was introduced offering better control over the new
    node Versioning.

    | **versioningEnabled** | **majorVersion** | **Version Type** |
    |-----------------------|------------------|------------------|
    |        unset          |        unset     |    MAJOR         |
    |        unset          |        true      |    MAJOR         |
    |        unset          |        false     |    MINOR         |
    |        true           |        unset     |    MAJOR         |
    |        true           |        true      |    MAJOR         |
    |        true           |        false     |    MINOR         |
    |        false          |        true      |    Unversioned   |
    |        false          |        false     |    Unversioned   |
    |        false          |        true      |    Unversioned   |
    <br>

    **Using JSON**

    You must specify at least a **name** and **nodeType**. For example, to create a folder:
    ```JSON
    {
      \"name\":\"My Folder\",
      \"nodeType\":\"cm:folder\"
    }
    ```

    You can create an empty file like this:
    ```JSON
    {
      \"name\":\"My text file.txt\",
      \"nodeType\":\"cm:content\"
    }
    ```
    You can update binary content using the ```PUT /nodes/{nodeId}``` API method.

    You can create a folder, or other node, inside a folder hierarchy:
    ```JSON
    {
      \"name\":\"My Special Folder\",
      \"nodeType\":\"cm:folder\",
      \"relativePath\":\"X/Y/Z\"
    }
    ```
    The **relativePath** specifies the folder structure to create relative to the node **nodeId**.
    Folders in the
    **relativePath** that do not exist are created before the node is created.

    You can set properties when you create a new node:
    ```JSON
    {
      \"name\":\"My Other Folder\",
      \"nodeType\":\"cm:folder\",
      \"properties\":
      {
        \"cm:title\":\"Folder title\",
        \"cm:description\":\"This is an important folder\"
      }
    }
    ```

    You can set multi-value properties when you create a new node which supports properties of type
    multiple.
     ```JSON
    {
      \"name\":\"My Other Folder\",
      \"nodeType\":\"custom:destination\",
      \"properties\":
      {
        \"cm:title\":\"Folder title\",
        \"cm:description\":\"This is an important folder\",
        \"custom:locations\": [
                             \"location X\",
                             \"location Y\"
                            ]
      }
    }
    ```

    Any missing aspects are applied automatically. For example, **cm:titled** in the JSON shown above.
    You can set aspects
    explicitly, if needed, using an **aspectNames** field.

    **Note:** setting properties of type d:content and d:category are not supported.

    You can also optionally disable (or enable) inherited permissions via *isInheritanceEnabled* flag:
    ```JSON
    {
      \"permissions\":
        {
          \"isInheritanceEnabled\": false,
          \"locallySet\":
            [
              {\"authorityId\": \"GROUP_special\", \"name\": \"Read\", \"accessStatus\":\"DENIED\"},
              {\"authorityId\": \"testuser\", \"name\": \"Contributor\", \"accessStatus\":\"ALLOWED\"}
            ]
        }
    }
    ```

    Typically, for files and folders, the primary children are created within the parent folder using
    the default \"cm:contains\" assocType.
    If the content model allows then it is also possible to create primary children with a different
    assoc type. For example:
    ```JSON
    {
      \"name\":\"My Node\",
      \"nodeType\":\"my:specialNodeType\",
      \"association\":
      {
        \"assocType\":\"my:specialAssocType\"
      }
    }
    ```

    Additional associations can be added after creating a node. You can also add associations at the
    time the node is created. This is
    required, for example, if the content model specifies that a node has mandatory associations to one
    or more existing nodes. You can optionally
    specify an array of **secondaryChildren** to create one or more secondary child associations, such
    that the newly created node acts as a parent node.
    You can optionally specify an array of **targets** to create one or more peer associations such that
    the newly created node acts as a source node.
    For example, to associate one or more secondary children at time of creation:
    ```JSON
    {
      \"name\":\"My Folder\",
      \"nodeType\":\"cm:folder\",
      \"secondaryChildren\":
        [ {\"childId\":\"abcde-01234-...\", \"assocType\":\"my:specialChildAssocType\"} ]
    }
    ```
    For example, to associate one or more targets at time of creation:
    ```JSON
    {
      \"name\":\"My Folder\",
      \"nodeType\":\"cm:folder\",
      \"targets\":
        [ {\"targetId\":\"abcde-01234-...\", \"assocType\":\"my:specialPeerAssocType\"} ]
    }
    ```

    **Note:** You can create more than one child by
    specifying a list of nodes in the JSON body. For example, the following JSON
    body creates two folders inside the specified **nodeId**, if the **nodeId** identifies
    a folder:

    ```JSON
    [
      {
        \"name\":\"My Folder 1\",
        \"nodeType\":\"cm:folder\"
      },
      {
        \"name\":\"My Folder 2\",
        \"nodeType\":\"cm:folder\"
      }
    ]
    ```
    If you specify a list as input, then a paginated list rather than an entry is returned in the
    response body. For example:

    ```JSON
    {
      \"list\": {
        \"pagination\": {
          \"count\": 2,
          \"hasMoreItems\": false,
          \"totalItems\": 2,
          \"skipCount\": 0,
          \"maxItems\": 100
        },
        \"entries\": [
          {
            \"entry\": {
              ...
            }
          },
          {
            \"entry\": {
              ...
            }
          }
        ]
      }
    }
    ```
    **Note:** When creating a new node using JSON by default versioning is disabled.
    Since Alfresco 6.2.3 **versioningEnabled** flag was introduced offering better control over the new
    node Versioning.

    | **versioningEnabled** | **majorVersion** | **Version Type** |
    |-----------------------|------------------|------------------|
    |        unset          |        unset     |    Unversioned   |
    |        unset          |        true      |    MAJOR         |
    |        unset          |        false     |    MINOR         |
    |        true           |        unset     |    MAJOR         |
    |        true           |        true      |    MAJOR         |
    |        true           |        false     |    MINOR         |
    |        false          |        true      |    Unversioned   |
    |        false          |        false     |    Unversioned   |
    |        false          |        true      |    Unversioned   |
    <br>

    Args:
        node_id (str):
        auto_rename (Union[Unset, bool]):
        major_version (Union[Unset, bool]):
        versioning_enabled (Union[Unset, bool]):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        body (NodeBodyCreate):
        body (NodeBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NodeEntry]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        body=body,
        auto_rename=auto_rename,
        major_version=major_version,
        versioning_enabled=versioning_enabled,
        include=include,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        NodeBodyCreate,
        NodeBodyCreate,
    ],
    auto_rename: Union[Unset, bool] = UNSET,
    major_version: Union[Unset, bool] = UNSET,
    versioning_enabled: Union[Unset, bool] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, NodeEntry]]:
    r"""Create a node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Create a node and add it as a primary child of node **nodeId**.

    This endpoint supports both JSON and multipart/form-data (file upload).

    **Using multipart/form-data**

    Use the **filedata** field to represent the content to upload, for example, the following curl
    command will
    create a node with the contents of test.txt in the test user's home folder.

    ```curl -utest:test -X POST
    host:port/alfresco/api/-default-/public/alfresco/versions/1/nodes/-my-/children -F
    filedata=@test.txt```

    You can use the **name** field to give an alternative name for the new file.

    You can use the **nodeType** field to create a specific type. The default is cm:content.

    You can use the **renditions** field to create renditions (e.g. doclib) asynchronously upon upload.
    Also, as requesting rendition is a background process,
    any rendition failure (e.g. No transformer is currently available) will not fail the whole upload
    and has the potential to silently fail.

    Use **overwrite** to overwrite an existing file, matched by name. If the file is versionable,
    the existing content is replaced.

    When you overwrite existing content, you can set the **majorVersion** boolean field to **true** to
    indicate a major version
    should be created. The default for **majorVersion** is **false**.
    Setting  **majorVersion** enables versioning of the node, if it is not already versioned.

    When you overwrite existing content, you can use the **comment** field to add a version comment that
    appears in the
    version history. This also enables versioning of this node, if it is not already versioned.

    You can set the **autoRename** boolean field to automatically resolve name clashes. If there is a
    name clash, then
    the API method tries to create a unique name using an integer suffix.

    You can use the **relativePath** field to specify the folder structure to create relative to the
    node **nodeId**.
    Folders in the **relativePath** that do not exist are created before the node is created.

    Any other field provided will be treated as a property to set on the newly created node.

    **Note:** setting properties of type d:content and d:category are not supported.

    **Note:** When creating a new node using multipart/form-data by default versioning is enabled and
    set to MAJOR Version.
    Since Alfresco 6.2.3 **versioningEnabled** flag was introduced offering better control over the new
    node Versioning.

    | **versioningEnabled** | **majorVersion** | **Version Type** |
    |-----------------------|------------------|------------------|
    |        unset          |        unset     |    MAJOR         |
    |        unset          |        true      |    MAJOR         |
    |        unset          |        false     |    MINOR         |
    |        true           |        unset     |    MAJOR         |
    |        true           |        true      |    MAJOR         |
    |        true           |        false     |    MINOR         |
    |        false          |        true      |    Unversioned   |
    |        false          |        false     |    Unversioned   |
    |        false          |        true      |    Unversioned   |
    <br>

    **Using JSON**

    You must specify at least a **name** and **nodeType**. For example, to create a folder:
    ```JSON
    {
      \"name\":\"My Folder\",
      \"nodeType\":\"cm:folder\"
    }
    ```

    You can create an empty file like this:
    ```JSON
    {
      \"name\":\"My text file.txt\",
      \"nodeType\":\"cm:content\"
    }
    ```
    You can update binary content using the ```PUT /nodes/{nodeId}``` API method.

    You can create a folder, or other node, inside a folder hierarchy:
    ```JSON
    {
      \"name\":\"My Special Folder\",
      \"nodeType\":\"cm:folder\",
      \"relativePath\":\"X/Y/Z\"
    }
    ```
    The **relativePath** specifies the folder structure to create relative to the node **nodeId**.
    Folders in the
    **relativePath** that do not exist are created before the node is created.

    You can set properties when you create a new node:
    ```JSON
    {
      \"name\":\"My Other Folder\",
      \"nodeType\":\"cm:folder\",
      \"properties\":
      {
        \"cm:title\":\"Folder title\",
        \"cm:description\":\"This is an important folder\"
      }
    }
    ```

    You can set multi-value properties when you create a new node which supports properties of type
    multiple.
     ```JSON
    {
      \"name\":\"My Other Folder\",
      \"nodeType\":\"custom:destination\",
      \"properties\":
      {
        \"cm:title\":\"Folder title\",
        \"cm:description\":\"This is an important folder\",
        \"custom:locations\": [
                             \"location X\",
                             \"location Y\"
                            ]
      }
    }
    ```

    Any missing aspects are applied automatically. For example, **cm:titled** in the JSON shown above.
    You can set aspects
    explicitly, if needed, using an **aspectNames** field.

    **Note:** setting properties of type d:content and d:category are not supported.

    You can also optionally disable (or enable) inherited permissions via *isInheritanceEnabled* flag:
    ```JSON
    {
      \"permissions\":
        {
          \"isInheritanceEnabled\": false,
          \"locallySet\":
            [
              {\"authorityId\": \"GROUP_special\", \"name\": \"Read\", \"accessStatus\":\"DENIED\"},
              {\"authorityId\": \"testuser\", \"name\": \"Contributor\", \"accessStatus\":\"ALLOWED\"}
            ]
        }
    }
    ```

    Typically, for files and folders, the primary children are created within the parent folder using
    the default \"cm:contains\" assocType.
    If the content model allows then it is also possible to create primary children with a different
    assoc type. For example:
    ```JSON
    {
      \"name\":\"My Node\",
      \"nodeType\":\"my:specialNodeType\",
      \"association\":
      {
        \"assocType\":\"my:specialAssocType\"
      }
    }
    ```

    Additional associations can be added after creating a node. You can also add associations at the
    time the node is created. This is
    required, for example, if the content model specifies that a node has mandatory associations to one
    or more existing nodes. You can optionally
    specify an array of **secondaryChildren** to create one or more secondary child associations, such
    that the newly created node acts as a parent node.
    You can optionally specify an array of **targets** to create one or more peer associations such that
    the newly created node acts as a source node.
    For example, to associate one or more secondary children at time of creation:
    ```JSON
    {
      \"name\":\"My Folder\",
      \"nodeType\":\"cm:folder\",
      \"secondaryChildren\":
        [ {\"childId\":\"abcde-01234-...\", \"assocType\":\"my:specialChildAssocType\"} ]
    }
    ```
    For example, to associate one or more targets at time of creation:
    ```JSON
    {
      \"name\":\"My Folder\",
      \"nodeType\":\"cm:folder\",
      \"targets\":
        [ {\"targetId\":\"abcde-01234-...\", \"assocType\":\"my:specialPeerAssocType\"} ]
    }
    ```

    **Note:** You can create more than one child by
    specifying a list of nodes in the JSON body. For example, the following JSON
    body creates two folders inside the specified **nodeId**, if the **nodeId** identifies
    a folder:

    ```JSON
    [
      {
        \"name\":\"My Folder 1\",
        \"nodeType\":\"cm:folder\"
      },
      {
        \"name\":\"My Folder 2\",
        \"nodeType\":\"cm:folder\"
      }
    ]
    ```
    If you specify a list as input, then a paginated list rather than an entry is returned in the
    response body. For example:

    ```JSON
    {
      \"list\": {
        \"pagination\": {
          \"count\": 2,
          \"hasMoreItems\": false,
          \"totalItems\": 2,
          \"skipCount\": 0,
          \"maxItems\": 100
        },
        \"entries\": [
          {
            \"entry\": {
              ...
            }
          },
          {
            \"entry\": {
              ...
            }
          }
        ]
      }
    }
    ```
    **Note:** When creating a new node using JSON by default versioning is disabled.
    Since Alfresco 6.2.3 **versioningEnabled** flag was introduced offering better control over the new
    node Versioning.

    | **versioningEnabled** | **majorVersion** | **Version Type** |
    |-----------------------|------------------|------------------|
    |        unset          |        unset     |    Unversioned   |
    |        unset          |        true      |    MAJOR         |
    |        unset          |        false     |    MINOR         |
    |        true           |        unset     |    MAJOR         |
    |        true           |        true      |    MAJOR         |
    |        true           |        false     |    MINOR         |
    |        false          |        true      |    Unversioned   |
    |        false          |        false     |    Unversioned   |
    |        false          |        true      |    Unversioned   |
    <br>

    Args:
        node_id (str):
        auto_rename (Union[Unset, bool]):
        major_version (Union[Unset, bool]):
        versioning_enabled (Union[Unset, bool]):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        body (NodeBodyCreate):
        body (NodeBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NodeEntry]
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
            body=body,
            auto_rename=auto_rename,
            major_version=major_version,
            versioning_enabled=versioning_enabled,
            include=include,
            fields=fields,
        )
    ).parsed
