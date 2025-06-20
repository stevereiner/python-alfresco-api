# Import using alternative method due to hyphen in package name
import importlib
SearchSQLClient = getattr(importlib.import_module('alfresco_client.alfresco_search-sql.alfresco_search-sql.api'), 'SearchSQLClient')
__all__ = ['SearchSQLClient']
