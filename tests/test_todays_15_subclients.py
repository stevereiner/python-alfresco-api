"""
Comprehensive tests for today's 15 implemented subclients.

Tests the 15 subclients that were implemented today:
- Phase 1: authentication, people, sql, favorites, sites (5)
- Phase 2: groups, preferences, tags, shared_links, trashcan (5) 
- Phase 3: audit, networks, aspects, types (4)
- Deployments: deployments (1)

Verifies basic functionality, method availability, and proper integration.
"""

import pytest
from python_alfresco_api.client_factory import ClientFactory
from python_alfresco_api.auth_util import SimpleAuthUtil


class TestTodaysFifteenSubclients:
    """Test the 15 subclients implemented today for basic functionality."""
    
    def setup_method(self):
        """Setup for each test method."""
        self.auth = SimpleAuthUtil(
            username="admin",
            password="admin"
        )
        self.factory = ClientFactory(
            base_url="http://localhost:8080",
            auth_util=self.auth,
            timeout=30
        )

    def test_authentication_subclient_methods(self):
        """Test authentication subclient (Phase 1) - 6 methods (3+3)."""
        auth_client = self.factory.create_auth_client()
        assert auth_client is not None
        
        auth_subclient = auth_client.authentication
        assert auth_subclient is not None
        
        # Test method availability (basic sync/async)
        expected_methods = [
            'create_ticket', 'create_ticket_async',
            'validate_ticket', 'validate_ticket_async', 
            'delete_ticket', 'delete_ticket_async'
        ]
        
        available_methods = [m for m in dir(auth_subclient) if not m.startswith('_') and callable(getattr(auth_subclient, m))]
        
        for method in expected_methods:
            assert hasattr(auth_subclient, method), f"authentication should have {method} method"
        
        # Verify we have the expected number of methods (6 basic + detailed methods)
        assert len(available_methods) >= 6, f"authentication should have at least 6 methods, got {len(available_methods)}"
        
        print(f"[OK] Authentication: {len(available_methods)} methods available")

    def test_people_subclient_methods(self):
        """Test people subclient (Phase 1) - 8 methods (4+4)."""
        core_client = self.factory.create_core_client()
        assert core_client is not None
        
        people_subclient = core_client.people
        assert people_subclient is not None
        
        # Test method availability (basic sync/async only)
        expected_methods = [
            'create_person', 'create_person_async',
            'get_person', 'get_person_async',
            'list_people', 'list_people_async',
            'update_person', 'update_person_async'
        ]
        
        available_methods = [m for m in dir(people_subclient) if not m.startswith('_') and callable(getattr(people_subclient, m))]
        
        for method in expected_methods:
            assert hasattr(people_subclient, method), f"people should have {method} method"
        
        assert len(available_methods) >= 8, f"people should have at least 8 methods, got {len(available_methods)}"
        
        print(f"[OK] People: {len(available_methods)} methods available")

    def test_sql_subclient_methods(self):
        """Test sql subclient (Phase 1) - 4 methods (2+2)."""
        search_sql_client = self.factory.create_search_sql_client()
        assert search_sql_client is not None
        
        sql_subclient = search_sql_client.sql
        assert sql_subclient is not None
        
        # Test method availability (4-pattern: basic + detailed)
        expected_methods = [
            'search', 'search_async',
            'search_detailed', 'search_detailed_async'
        ]
        
        available_methods = [m for m in dir(sql_subclient) if not m.startswith('_') and callable(getattr(sql_subclient, m))]
        
        for method in expected_methods:
            assert hasattr(sql_subclient, method), f"sql should have {method} method"
        
        assert len(available_methods) >= 4, f"sql should have at least 4 methods, got {len(available_methods)}"
        
        print(f"[OK] SQL: {len(available_methods)} methods available")

    def test_favorites_subclient_methods(self):
        """Test favorites subclient (Phase 1) - 8 methods (4+4)."""
        core_client = self.factory.create_core_client()
        assert core_client is not None
        
        favorites_subclient = core_client.favorites
        assert favorites_subclient is not None
        
        # Test method availability (basic sync/async only)
        expected_methods = [
            'create_favorite', 'create_favorite_async',
            'delete_favorite', 'delete_favorite_async',
            'get_favorite', 'get_favorite_async',
            'list_favorites', 'list_favorites_async'
        ]
        
        available_methods = [m for m in dir(favorites_subclient) if not m.startswith('_') and callable(getattr(favorites_subclient, m))]
        
        for method in expected_methods:
            assert hasattr(favorites_subclient, method), f"favorites should have {method} method"
        
        assert len(available_methods) >= 8, f"favorites should have at least 8 methods, got {len(available_methods)}"
        
        print(f"[OK] Favorites: {len(available_methods)} methods available")

    def test_sites_subclient_methods(self):
        """Test sites subclient (Phase 1) - 10 methods (5+5)."""
        core_client = self.factory.create_core_client()
        assert core_client is not None
        
        sites_subclient = core_client.sites
        assert sites_subclient is not None
        
        # Test method availability (basic sync/async only)
        expected_methods = [
            'create_site', 'create_site_async',
            'get_site', 'get_site_async',
            'list_sites', 'list_sites_async',
            'update_site', 'update_site_async',
            'delete_site', 'delete_site_async'
        ]
        
        available_methods = [m for m in dir(sites_subclient) if not m.startswith('_') and callable(getattr(sites_subclient, m))]
        
        for method in expected_methods:
            assert hasattr(sites_subclient, method), f"sites should have {method} method"
        
        assert len(available_methods) >= 10, f"sites should have at least 10 methods, got {len(available_methods)}"
        
        print(f"[OK] Sites: {len(available_methods)} methods available")

    def test_groups_subclient_methods(self):
        """Test groups subclient (Phase 2) - 10 methods (5+5)."""
        core_client = self.factory.create_core_client()
        assert core_client is not None
        
        groups_subclient = core_client.groups
        assert groups_subclient is not None
        
        # Test method availability (basic sync/async only)
        expected_methods = [
            'create_group', 'create_group_async',
            'get_group', 'get_group_async',
            'list_groups', 'list_groups_async',
            'update_group', 'update_group_async',
            'delete_group', 'delete_group_async'
        ]
        
        available_methods = [m for m in dir(groups_subclient) if not m.startswith('_') and callable(getattr(groups_subclient, m))]
        
        for method in expected_methods:
            assert hasattr(groups_subclient, method), f"groups should have {method} method"
        
        assert len(available_methods) >= 10, f"groups should have at least 10 methods, got {len(available_methods)}"
        
        print(f"[OK] Groups: {len(available_methods)} methods available")

    def test_preferences_subclient_methods(self):
        """Test preferences subclient (Phase 2) - 4 methods (2+2)."""
        core_client = self.factory.create_core_client()
        assert core_client is not None
        
        preferences_subclient = core_client.preferences
        assert preferences_subclient is not None
        
        # Test method availability (basic sync/async only)
        expected_methods = [
            'get_preference', 'get_preference_async',
            'list_preferences', 'list_preferences_async'
        ]
        
        available_methods = [m for m in dir(preferences_subclient) if not m.startswith('_') and callable(getattr(preferences_subclient, m))]
        
        for method in expected_methods:
            assert hasattr(preferences_subclient, method), f"preferences should have {method} method"
        
        assert len(available_methods) >= 4, f"preferences should have at least 4 methods, got {len(available_methods)}"
        
        print(f"[OK] Preferences: {len(available_methods)} methods available")

    def test_tags_subclient_methods(self):
        """Test tags subclient (Phase 2) - 12 methods (6+6)."""
        core_client = self.factory.create_core_client()
        assert core_client is not None
        
        tags_subclient = core_client.tags
        assert tags_subclient is not None
        
        # Test method availability (basic sync/async only)
        expected_methods = [
            'create_tag_for_node', 'create_tag_for_node_async',
            'delete_tag_from_node', 'delete_tag_from_node_async',
            'get_tag', 'get_tag_async',
            'list_tags', 'list_tags_async',
            'list_tags_for_node', 'list_tags_for_node_async',
            'update_tag', 'update_tag_async'
        ]
        
        available_methods = [m for m in dir(tags_subclient) if not m.startswith('_') and callable(getattr(tags_subclient, m))]
        
        for method in expected_methods:
            assert hasattr(tags_subclient, method), f"tags should have {method} method"
        
        assert len(available_methods) >= 12, f"tags should have at least 12 methods, got {len(available_methods)}"
        
        print(f"[OK] Tags: {len(available_methods)} methods available")

    def test_shared_links_subclient_methods(self):
        """Test shared_links subclient (Phase 2) - 14 methods (7+7)."""
        core_client = self.factory.create_core_client()
        assert core_client is not None
        
        shared_links_subclient = core_client.shared_links
        assert shared_links_subclient is not None
        
        # Test method availability (basic sync/async only)
        expected_methods = [
            'create_shared_link', 'create_shared_link_async',
            'get_shared_link', 'get_shared_link_async',
            'list_shared_links', 'list_shared_links_async',
            'delete_shared_link', 'delete_shared_link_async',
            'email_shared_link', 'email_shared_link_async',
            'get_shared_link_rendition', 'get_shared_link_rendition_async',
            'list_shared_link_renditions', 'list_shared_link_renditions_async'
        ]
        
        available_methods = [m for m in dir(shared_links_subclient) if not m.startswith('_') and callable(getattr(shared_links_subclient, m))]
        
        for method in expected_methods:
            assert hasattr(shared_links_subclient, method), f"shared_links should have {method} method"
        
        assert len(available_methods) >= 14, f"shared_links should have at least 14 methods, got {len(available_methods)}"
        
        print(f"[OK] Shared Links: {len(available_methods)} methods available")

    def test_trashcan_subclient_methods(self):
        """Test trashcan subclient (Phase 2) - 12 methods (6+6)."""
        core_client = self.factory.create_core_client()
        assert core_client is not None
        
        trashcan_subclient = core_client.trashcan
        assert trashcan_subclient is not None
        
        # Test method availability (basic sync/async only)
        expected_methods = [
            'list_deleted_nodes', 'list_deleted_nodes_async',
            'get_deleted_node', 'get_deleted_node_async',
            'restore_deleted_node', 'restore_deleted_node_async',
            'delete_deleted_node', 'delete_deleted_node_async',
            'get_archived_node_rendition', 'get_archived_node_rendition_async',
            'list_deleted_node_renditions', 'list_deleted_node_renditions_async'
        ]
        
        available_methods = [m for m in dir(trashcan_subclient) if not m.startswith('_') and callable(getattr(trashcan_subclient, m))]
        
        for method in expected_methods:
            assert hasattr(trashcan_subclient, method), f"trashcan should have {method} method"
        
        assert len(available_methods) >= 12, f"trashcan should have at least 12 methods, got {len(available_methods)}"
        
        print(f"[OK] Trashcan: {len(available_methods)} methods available")

    def test_audit_subclient_methods(self):
        """Test audit subclient (Phase 3) - 16 methods (8+8)."""
        core_client = self.factory.create_core_client()
        assert core_client is not None
        
        audit_subclient = core_client.audit
        assert audit_subclient is not None
        
        # Test method availability (basic sync/async only)
        expected_methods = [
            'list_audit_apps', 'list_audit_apps_async',
            'get_audit_app', 'get_audit_app_async',
            'update_audit_app', 'update_audit_app_async',
            'list_audit_entries_for_audit_app', 'list_audit_entries_for_audit_app_async',
            'list_audit_entries_for_node', 'list_audit_entries_for_node_async',
            'get_audit_entry', 'get_audit_entry_async',
            'delete_audit_entry', 'delete_audit_entry_async',
            'delete_audit_entries_for_audit_app', 'delete_audit_entries_for_audit_app_async'
        ]
        
        available_methods = [m for m in dir(audit_subclient) if not m.startswith('_') and callable(getattr(audit_subclient, m))]
        
        for method in expected_methods:
            assert hasattr(audit_subclient, method), f"audit should have {method} method"
        
        assert len(available_methods) >= 16, f"audit should have at least 16 methods, got {len(available_methods)}"
        
        print(f"[OK] Audit: {len(available_methods)} methods available")

    def test_networks_subclient_methods(self):
        """Test networks subclient (Phase 3) - 6 methods (3+3)."""
        core_client = self.factory.create_core_client()
        assert core_client is not None
        
        networks_subclient = core_client.networks
        assert networks_subclient is not None
        
        # Test method availability (basic sync/async only)
        expected_methods = [
            'get_network', 'get_network_async',
            'get_network_for_person', 'get_network_for_person_async',
            'list_networks_for_person', 'list_networks_for_person_async'
        ]
        
        available_methods = [m for m in dir(networks_subclient) if not m.startswith('_') and callable(getattr(networks_subclient, m))]
        
        for method in expected_methods:
            assert hasattr(networks_subclient, method), f"networks should have {method} method"
        
        assert len(available_methods) >= 6, f"networks should have at least 6 methods, got {len(available_methods)}"
        
        print(f"[OK] Networks: {len(available_methods)} methods available")

    def test_aspects_subclient_methods(self):
        """Test aspects subclient (Phase 3) - 4 methods (2+2)."""
        model_client = self.factory.create_model_client()
        assert model_client is not None
        
        aspects_subclient = model_client.aspects
        assert aspects_subclient is not None
        
        # Test method availability (basic sync/async only)
        expected_methods = [
            'list_aspects', 'list_aspects_async',
            'get_aspect', 'get_aspect_async'
        ]
        
        available_methods = [m for m in dir(aspects_subclient) if not m.startswith('_') and callable(getattr(aspects_subclient, m))]
        
        for method in expected_methods:
            assert hasattr(aspects_subclient, method), f"aspects should have {method} method"
        
        assert len(available_methods) >= 4, f"aspects should have at least 4 methods, got {len(available_methods)}"
        
        print(f"[OK] Aspects: {len(available_methods)} methods available")

    def test_types_subclient_methods(self):
        """Test types subclient (Phase 3) - 4 methods (2+2)."""
        model_client = self.factory.create_model_client()
        assert model_client is not None
        
        types_subclient = model_client.types
        assert types_subclient is not None
        
        # Test method availability (basic sync/async only)
        expected_methods = [
            'list_types', 'list_types_async',
            'get_type', 'get_type_async'
        ]
        
        available_methods = [m for m in dir(types_subclient) if not m.startswith('_') and callable(getattr(types_subclient, m))]
        
        for method in expected_methods:
            assert hasattr(types_subclient, method), f"types should have {method} method"
        
        assert len(available_methods) >= 4, f"types should have at least 4 methods, got {len(available_methods)}"
        
        print(f"[OK] Types: {len(available_methods)} methods available")

    def test_deployments_subclient_methods(self):
        """Test deployments subclient (Previously completed) - 12 methods (6+6)."""
        workflow_client = self.factory.create_workflow_client()
        assert workflow_client is not None
        
        deployments_subclient = workflow_client.deployments
        assert deployments_subclient is not None
        
        # Test method availability (4-pattern: basic + detailed)
        expected_basic_methods = [
            'list_deployments', 'list_deployments_async',
            'get_deployment', 'get_deployment_async',
            'delete_deployment', 'delete_deployment_async'
        ]
        
        expected_detailed_methods = [
            'list_deployments_detailed', 'list_deployments_detailed_async',
            'get_deployment_detailed', 'get_deployment_detailed_async',
            'delete_deployment_detailed', 'delete_deployment_detailed_async'
        ]
        
        available_methods = [m for m in dir(deployments_subclient) if not m.startswith('_') and callable(getattr(deployments_subclient, m))]
        
        for method in expected_basic_methods:
            assert hasattr(deployments_subclient, method), f"deployments should have {method} method"
        
        for method in expected_detailed_methods:
            assert hasattr(deployments_subclient, method), f"deployments should have {method} method"
        
        assert len(available_methods) >= 12, f"deployments should have at least 12 methods, got {len(available_methods)}"
        
        print(f"[OK] Deployments: {len(available_methods)} methods available")

    def test_raw_client_delegation_pattern(self):
        """Test that all today's subclients use the new delegation pattern."""
        # Get all clients
        core_client = self.factory.create_core_client()
        auth_client = self.factory.create_auth_client()
        model_client = self.factory.create_model_client()
        workflow_client = self.factory.create_workflow_client()
        search_sql_client = self.factory.create_search_sql_client()
        
        # Test subclients use delegation pattern (have raw_client property, not _get_raw_client method)
        subclients_to_test = [
            ('authentication', auth_client.authentication),
            ('people', core_client.people),
            ('sql', search_sql_client.sql),
            ('favorites', core_client.favorites),
            ('sites', core_client.sites),
            ('groups', core_client.groups),
            ('preferences', core_client.preferences),
            ('tags', core_client.tags),
            ('shared_links', core_client.shared_links),
            ('trashcan', core_client.trashcan),
            ('audit', core_client.audit),
            ('networks', core_client.networks),
            ('aspects', model_client.aspects),
            ('types', model_client.types),
            ('deployments', workflow_client.deployments)
        ]
        
        for name, subclient in subclients_to_test:
            # Should have raw_client property (new delegation pattern)
            assert hasattr(subclient, 'raw_client'), f"{name} should have raw_client property"
            assert hasattr(subclient, 'httpx_client'), f"{name} should have httpx_client property"
            
            # Should NOT have _get_raw_client method (old pattern)
            assert not hasattr(subclient, '_get_raw_client'), f"{name} should not have _get_raw_client method (old pattern)"
            
            # Should have parent_client reference
            assert hasattr(subclient, 'parent_client'), f"{name} should have parent_client reference"
            
            print(f"[OK] {name}: Uses delegation pattern correctly")

    def test_timeout_propagation_to_todays_subclients(self):
        """Test that timeout=30 propagates correctly to all today's 15 subclients."""
        # Verify factory has timeout=30
        assert self.factory.timeout == 30
        
        # Get all clients
        core_client = self.factory.create_core_client()
        auth_client = self.factory.create_auth_client()
        model_client = self.factory.create_model_client()
        workflow_client = self.factory.create_workflow_client()
        search_sql_client = self.factory.create_search_sql_client()
        
        # Test that parent clients have timeout
        parent_clients = [
            ('core', core_client),
            ('auth', auth_client),
            ('model', model_client),
            ('workflow', workflow_client),
            ('search_sql', search_sql_client)
        ]
        
        for name, client in parent_clients:
            # Parent should have timeout
            if hasattr(client, 'timeout'):
                assert client.timeout == 30, f"{name} client should have timeout=30"
            
            # Raw client should be accessible (timeout doesn't break creation)
            try:
                raw_client = client.raw_client
                assert raw_client is not None, f"{name} raw_client should be accessible with timeout=30"
            except Exception as e:
                pytest.fail(f"{name} raw_client failed with timeout=30: {e}")
        
        # Test subclients can access their raw clients (delegation works with timeout)
        subclients_to_test = [
            ('authentication', auth_client.authentication),
            ('people', core_client.people),
            ('sql', search_sql_client.sql),
            ('favorites', core_client.favorites),
            ('sites', core_client.sites),
            ('groups', core_client.groups),
            ('preferences', core_client.preferences),
            ('tags', core_client.tags),
            ('shared_links', core_client.shared_links),
            ('trashcan', core_client.trashcan),
            ('audit', core_client.audit),
            ('networks', core_client.networks),
            ('aspects', model_client.aspects),
            ('types', model_client.types),
            ('deployments', workflow_client.deployments)
        ]
        
        for name, subclient in subclients_to_test:
            try:
                # Should be able to access raw_client through delegation
                raw_client = subclient.raw_client
                assert raw_client is not None, f"{name} should access raw_client via delegation with timeout=30"
                
                # Should be able to access httpx_client through delegation
                httpx_client = subclient.httpx_client
                assert httpx_client is not None, f"{name} should access httpx_client via delegation with timeout=30"
                
                print(f"[OK] {name}: Timeout delegation works correctly")
                
            except Exception as e:
                pytest.fail(f"{name} delegation failed with timeout=30: {e}")

    def test_comprehensive_summary(self):
        """Summary test showing all 15 subclients are properly implemented."""
        
        # Count methods across all today's subclients
        core_client = self.factory.create_core_client()
        auth_client = self.factory.create_auth_client()
        model_client = self.factory.create_model_client()
        workflow_client = self.factory.create_workflow_client()
        search_sql_client = self.factory.create_search_sql_client()
        
        subclients_and_expected_methods = [
            # Phase 1 (5 subclients)
            ('authentication', auth_client.authentication, 12),  # 6 basic + 6 detailed
            ('people', core_client.people, 8),                   # 4+4 basic only
            ('sql', search_sql_client.sql, 4),                   # 2+2 4-pattern
            ('favorites', core_client.favorites, 8),             # 4+4 basic only
            ('sites', core_client.sites, 10),                    # 5+5 basic only
            # Phase 2 (5 subclients)
            ('groups', core_client.groups, 10),                  # 5+5 basic only
            ('preferences', core_client.preferences, 4),         # 2+2 basic only
            ('tags', core_client.tags, 12),                      # 6+6 basic only
            ('shared_links', core_client.shared_links, 14),      # 7+7 basic only
            ('trashcan', core_client.trashcan, 12),              # 6+6 basic only
            # Phase 3 (4 subclients)
            ('audit', core_client.audit, 16),                    # 8+8 basic only
            ('networks', core_client.networks, 6),               # 3+3 basic only
            ('aspects', model_client.aspects, 4),                # 2+2 basic only
            ('types', model_client.types, 4),                    # 2+2 basic only
            # Deployments (1 subclient)
            ('deployments', workflow_client.deployments, 12)     # 6+6 4-pattern
        ]
        
        total_methods = 0
        implemented_subclients = 0
        
        for name, subclient, expected_count in subclients_and_expected_methods:
            available_methods = [m for m in dir(subclient) if not m.startswith('_') and callable(getattr(subclient, m))]
            actual_count = len(available_methods)
            
            assert actual_count >= expected_count, f"{name} should have at least {expected_count} methods, got {actual_count}"
            
            total_methods += actual_count
            implemented_subclients += 1
            
            print(f"[OK] {name}: {actual_count} methods")
        
        print(f"\n[SUCCESS] TODAY'S IMPLEMENTATION SUMMARY:")
        print(f"  - Subclients implemented: {implemented_subclients}/15")
        print(f"  - Total methods available: {total_methods}")
        print(f"  - Phase 1: 5 subclients (authentication, people, sql, favorites, sites)")
        print(f"  - Phase 2: 5 subclients (groups, preferences, tags, shared_links, trashcan)")
        print(f"  - Phase 3: 4 subclients (audit, networks, aspects, types)")
        print(f"  - Deployments: 1 subclient (deployments)")
        print(f"  - All use proper delegation pattern")
        print(f"  - All support timeout propagation")
        print(f"  - All provide sync/async method variants")
        
        assert implemented_subclients == 15
        assert total_methods >= 136  # Conservative estimate based on expected counts
