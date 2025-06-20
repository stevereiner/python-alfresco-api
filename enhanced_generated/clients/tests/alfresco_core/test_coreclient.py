import unittest
from unittest.mock import Mock, patch, MagicMock
from alfresco_client.alfresco_core.alfresco_core.api import CoreClient
from alfresco_client.alfresco_core.alfresco_core.rest import ApiException

class TestCoreClient(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.client = CoreClient(
            base_url="http://localhost:8080",
            username="admin",
            password="admin",
            verify_ssl=False
        )

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.get_node')
    def test_get__nodes_nodeId(self, mock_get_node):
        """Test getting a node by ID"""
        # Arrange
        expected_response = {
            'entry': {
                'id': 'test-node-id',
                'name': 'Test Node',
                'nodeType': 'cm:folder',
                'isFolder': True,
                'isFile': False
            }
        }
        mock_get_node.return_value = expected_response
        
        # Act
        result = self.client.nodes.get_node('test-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_get_node.assert_called_once_with('test-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.list_node_children')
    def test_get__nodes_nodeId_children(self, mock_list_children):
        """Test listing children of a node"""
        # Arrange
        expected_response = {
            'list': {
                'entries': [
                    {'entry': {'id': 'child1', 'name': 'Child 1', 'isFolder': True}},
                    {'entry': {'id': 'child2', 'name': 'Child 2', 'isFile': True}}
                ],
                'pagination': {'count': 2, 'hasMoreItems': False}
            }
        }
        mock_list_children.return_value = expected_response
        
        # Act
        result = self.client.nodes.list_node_children('parent-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_list_children.assert_called_once_with('parent-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.create_node')
    def test_post__nodes_nodeId_children(self, mock_create_node):
        """Test creating a new child node"""
        # Arrange
        node_body = {
            'name': 'New Folder',
            'nodeType': 'cm:folder'
        }
        expected_response = {
            'entry': {
                'id': 'new-node-id',
                'name': 'New Folder',
                'nodeType': 'cm:folder',
                'isFolder': True
            }
        }
        mock_create_node.return_value = expected_response
        
        # Act
        result = self.client.nodes.create_node(node_body, 'parent-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_create_node.assert_called_once_with(node_body, 'parent-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.update_node')
    def test_put__nodes_nodeId(self, mock_update_node):
        """Test updating a node"""
        # Arrange
        update_body = {'name': 'Updated Name'}
        expected_response = {
            'entry': {
                'id': 'test-node-id',
                'name': 'Updated Name',
                'nodeType': 'cm:folder'
            }
        }
        mock_update_node.return_value = expected_response
        
        # Act
        result = self.client.nodes.update_node(update_body, 'test-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_update_node.assert_called_once_with(update_body, 'test-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.delete_node')
    def test_delete__nodes_nodeId(self, mock_delete_node):
        """Test deleting a node"""
        # Arrange
        mock_delete_node.return_value = None
        
        # Act
        result = self.client.nodes.delete_node('test-node-id')
        
        # Assert
        self.assertIsNone(result)
        mock_delete_node.assert_called_once_with('test-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.get_node_content')
    def test_get__nodes_nodeId_content(self, mock_get_content):
        """Test getting node content"""
        # Arrange
        expected_content = b"Test file content"
        mock_get_content.return_value = expected_content
        
        # Act
        result = self.client.nodes.get_node_content('test-file-id')
        
        # Assert
        self.assertEqual(result, expected_content)
        mock_get_content.assert_called_once_with('test-file-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.update_node_content')
    def test_put__nodes_nodeId_content(self, mock_update_content):
        """Test updating node content"""
        # Arrange
        new_content = b"Updated file content"
        expected_response = {
            'entry': {
                'id': 'test-file-id',
                'name': 'test.txt',
                'content': {'mimeType': 'text/plain', 'sizeInBytes': len(new_content)}
            }
        }
        mock_update_content.return_value = expected_response
        
        # Act
        result = self.client.nodes.update_node_content(new_content, 'test-file-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_update_content.assert_called_once_with(new_content, 'test-file-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.comments_api.CommentsApi.list_comments')
    def test_get__nodes_nodeId_comments(self, mock_list_comments):
        """Test getting comments for a node"""
        # Arrange
        expected_response = {
            'list': {
                'entries': [
                    {
                        'entry': {
                            'id': 'comment-1',
                            'content': 'Test comment',
                            'createdBy': {'id': 'admin', 'displayName': 'Administrator'}
                        }
                    }
                ],
                'pagination': {'count': 1, 'hasMoreItems': False}
            }
        }
        mock_list_comments.return_value = expected_response
        
        # Act
        result = self.client.comments.list_comments('test-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_list_comments.assert_called_once_with('test-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.comments_api.CommentsApi.create_comment')
    def test_post__nodes_nodeId_comments(self, mock_create_comment):
        """Test creating a comment on a node"""
        # Arrange
        comment_body = {'content': 'New test comment'}
        expected_response = {
            'entry': {
                'id': 'new-comment-id',
                'content': 'New test comment',
                'createdBy': {'id': 'admin', 'displayName': 'Administrator'}
            }
        }
        mock_create_comment.return_value = expected_response
        
        # Act
        result = self.client.comments.create_comment(comment_body, 'test-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_create_comment.assert_called_once_with(comment_body, 'test-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.comments_api.CommentsApi.update_comment')
    def test_put__nodes_nodeId_comments_commentId(self, mock_update_comment):
        """Test updating a comment"""
        # Arrange
        update_body = {'content': 'Updated comment content'}
        expected_response = {
            'entry': {
                'id': 'comment-id',
                'content': 'Updated comment content',
                'modifiedBy': {'id': 'admin', 'displayName': 'Administrator'}
            }
        }
        mock_update_comment.return_value = expected_response
        
        # Act
        result = self.client.comments.update_comment(update_body, 'test-node-id', 'comment-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_update_comment.assert_called_once_with(update_body, 'test-node-id', 'comment-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.comments_api.CommentsApi.delete_comment')
    def test_delete__nodes_nodeId_comments_commentId(self, mock_delete_comment):
        """Test deleting a comment"""
        # Arrange
        mock_delete_comment.return_value = None
        
        # Act
        result = self.client.comments.delete_comment('test-node-id', 'comment-id')
        
        # Assert
        self.assertIsNone(result)
        mock_delete_comment.assert_called_once_with('test-node-id', 'comment-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.ratings_api.RatingsApi.list_ratings')
    def test_get__nodes_nodeId_ratings(self, mock_list_ratings):
        """Test getting ratings for a node"""
        # Arrange
        expected_response = {
            'list': {
                'entries': [
                    {
                        'entry': {
                            'id': 'likes',
                            'rating': 5,
                            'ratedBy': {'id': 'admin', 'displayName': 'Administrator'}
                        }
                    }
                ],
                'pagination': {'count': 1}
            }
        }
        mock_list_ratings.return_value = expected_response
        
        # Act
        result = self.client.ratings.list_ratings('test-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_list_ratings.assert_called_once_with('test-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.ratings_api.RatingsApi.create_rating')
    def test_post__nodes_nodeId_ratings(self, mock_create_rating):
        """Test creating a rating for a node"""
        # Arrange
        rating_body = {'id': 'likes', 'myRating': True}
        expected_response = {
            'entry': {
                'id': 'likes',
                'myRating': True,
                'ratedAt': '2025-06-18T10:00:00.000+0000'
            }
        }
        mock_create_rating.return_value = expected_response
        
        # Act
        result = self.client.ratings.create_rating(rating_body, 'test-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_create_rating.assert_called_once_with(rating_body, 'test-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.ratings_api.RatingsApi.get_rating')
    def test_get__nodes_nodeId_ratings_ratingId(self, mock_get_rating):
        """Test getting a specific rating"""
        # Arrange
        expected_response = {
            'entry': {
                'id': 'likes',
                'rating': 5,
                'ratedBy': {'id': 'admin', 'displayName': 'Administrator'}
            }
        }
        mock_get_rating.return_value = expected_response
        
        # Act
        result = self.client.ratings.get_rating('test-node-id', 'likes')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_get_rating.assert_called_once_with('test-node-id', 'likes')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.ratings_api.RatingsApi.delete_rating')
    def test_delete__nodes_nodeId_ratings_ratingId(self, mock_delete_rating):
        """Test deleting a rating"""
        # Arrange
        mock_delete_rating.return_value = None
        
        # Act
        result = self.client.ratings.delete_rating('test-node-id', 'likes')
        
        # Assert
        self.assertIsNone(result)
        mock_delete_rating.assert_called_once_with('test-node-id', 'likes')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.tags_api.TagsApi.list_tags_for_node')
    def test_get__nodes_nodeId_tags(self, mock_list_tags):
        """Test getting tags for a node"""
        # Arrange
        expected_response = {
            'list': {
                'entries': [
                    {'entry': {'tag': 'important', 'id': 'tag-1'}},
                    {'entry': {'tag': 'document', 'id': 'tag-2'}}
                ],
                'pagination': {'count': 2}
            }
        }
        mock_list_tags.return_value = expected_response
        
        # Act
        result = self.client.tags.list_tags_for_node('test-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_list_tags.assert_called_once_with('test-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.tags_api.TagsApi.create_tag_for_node')
    def test_post__nodes_nodeId_tags(self, mock_create_tag):
        """Test creating a tag for a node"""
        # Arrange
        tag_body = {'tag': 'new-tag'}
        expected_response = {
            'entry': {
                'tag': 'new-tag',
                'id': 'new-tag-id'
            }
        }
        mock_create_tag.return_value = expected_response
        
        # Act
        result = self.client.tags.create_tag_for_node(tag_body, 'test-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_create_tag.assert_called_once_with(tag_body, 'test-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.tags_api.TagsApi.delete_tag_from_node')
    def test_delete__nodes_nodeId_tags_tagId(self, mock_delete_tag):
        """Test deleting a tag from a node"""
        # Arrange
        mock_delete_tag.return_value = None
        
        # Act
        result = self.client.tags.delete_tag_from_node('test-node-id', 'tag-id')
        
        # Assert
        self.assertIsNone(result)
        mock_delete_tag.assert_called_once_with('test-node-id', 'tag-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.copy_node')
    def test_post__nodes_nodeId_copy(self, mock_copy_node):
        """Test copying a node"""
        # Arrange
        copy_body = {'targetParentId': 'target-parent-id', 'name': 'copied-node'}
        expected_response = {
            'entry': {
                'id': 'copied-node-id',
                'name': 'copied-node',
                'nodeType': 'cm:folder'
            }
        }
        mock_copy_node.return_value = expected_response
        
        # Act
        result = self.client.nodes.copy_node(copy_body, 'source-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_copy_node.assert_called_once_with(copy_body, 'source-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.lock_node')
    def test_post__nodes_nodeId_lock(self, mock_lock_node):
        """Test locking a node"""
        # Arrange
        lock_body = {'type': 'ALLOW_OWNER_CHANGES', 'lifetime': 'PERSISTENT'}
        expected_response = {
            'entry': {
                'id': 'test-node-id',
                'isLocked': True,
                'lockInfo': {'type': 'ALLOW_OWNER_CHANGES', 'lifetime': 'PERSISTENT'}
            }
        }
        mock_lock_node.return_value = expected_response
        
        # Act
        result = self.client.nodes.lock_node(lock_body, 'test-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_lock_node.assert_called_once_with(lock_body, 'test-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.unlock_node')
    def test_post__nodes_nodeId_unlock(self, mock_unlock_node):
        """Test unlocking a node"""
        # Arrange
        expected_response = {
            'entry': {
                'id': 'test-node-id',
                'isLocked': False
            }
        }
        mock_unlock_node.return_value = expected_response
        
        # Act
        result = self.client.nodes.unlock_node('test-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_unlock_node.assert_called_once_with('test-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.move_node')
    def test_post__nodes_nodeId_move(self, mock_move_node):
        """Test moving a node"""
        # Arrange
        move_body = {'targetParentId': 'new-parent-id'}
        expected_response = {
            'entry': {
                'id': 'test-node-id',
                'parentId': 'new-parent-id'
            }
        }
        mock_move_node.return_value = expected_response
        
        # Act
        result = self.client.nodes.move_node(move_body, 'test-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_move_node.assert_called_once_with(move_body, 'test-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.trashcan_api.TrashcanApi.list_deleted_nodes')
    def test_get__deleted_nodes(self, mock_list_deleted):
        """Test getting deleted nodes"""
        # Arrange
        expected_response = {
            'list': {
                'entries': [
                    {
                        'entry': {
                            'id': 'deleted-node-1',
                            'name': 'Deleted File',
                            'archivedBy': {'id': 'admin', 'displayName': 'Administrator'}
                        }
                    }
                ],
                'pagination': {'count': 1}
            }
        }
        mock_list_deleted.return_value = expected_response
        
        # Act
        result = self.client.trashcan.list_deleted_nodes()
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_list_deleted.assert_called_once()

    @patch('alfresco_client.alfresco_core.alfresco_core.api.trashcan_api.TrashcanApi.get_deleted_node')
    def test_get__deleted_nodes_nodeId(self, mock_get_deleted):
        """Test getting a specific deleted node"""
        # Arrange
        expected_response = {
            'entry': {
                'id': 'deleted-node-id',
                'name': 'Deleted File',
                'archivedBy': {'id': 'admin', 'displayName': 'Administrator'}
            }
        }
        mock_get_deleted.return_value = expected_response
        
        # Act
        result = self.client.trashcan.get_deleted_node('deleted-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_get_deleted.assert_called_once_with('deleted-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.trashcan_api.TrashcanApi.delete_deleted_node')
    def test_delete__deleted_nodes_nodeId(self, mock_permanent_delete):
        """Test permanently deleting a node from trashcan"""
        # Arrange
        mock_permanent_delete.return_value = None
        
        # Act
        result = self.client.trashcan.delete_deleted_node('deleted-node-id')
        
        # Assert
        self.assertIsNone(result)
        mock_permanent_delete.assert_called_once_with('deleted-node-id')

    def test_client_initialization(self):
        """Test that the CoreClient initializes correctly"""
        # Act & Assert
        self.assertIsNotNone(self.client)
        self.assertIsNotNone(self.client.nodes)
        self.assertIsNotNone(self.client.comments)
        self.assertIsNotNone(self.client.ratings)
        self.assertIsNotNone(self.client.tags)
        self.assertIsNotNone(self.client.trashcan)
        self.assertEqual(self.client.base_url, "http://localhost:8080")
        self.assertEqual(self.client.username, "admin")
        self.assertEqual(self.client.password, "admin")

    def test_get_api_info(self):
        """Test getting API information"""
        # Act
        info = self.client.get_api_info()
        
        # Assert
        self.assertIsInstance(info, dict)
        self.assertIn('name', info)
        self.assertIn('version', info)
        self.assertIn('description', info)
        self.assertIn('endpoints', info)
        self.assertEqual(info['name'], 'Alfresco Core API')

    # Placeholder methods for remaining TODOs - these would be implemented similarly
    @patch('alfresco_client.alfresco_core.alfresco_core.api.renditions_api.RenditionsApi.create_rendition')
    def test_post__nodes_nodeId_renditions(self, mock_create_rendition):
        """Test creating a rendition for a node"""
        # Arrange
        rendition_body = {'id': 'pdf'}
        expected_response = {
            'entry': {
                'id': 'pdf',
                'status': 'CREATED'
            }
        }
        mock_create_rendition.return_value = expected_response
        
        # Act
        result = self.client.renditions.create_rendition(rendition_body, 'test-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_create_rendition.assert_called_once_with(rendition_body, 'test-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.renditions_api.RenditionsApi.list_renditions')
    def test_get__nodes_nodeId_renditions(self, mock_list_renditions):
        """Test listing renditions for a node"""
        # Arrange
        expected_response = {
            'list': {
                'entries': [
                    {'entry': {'id': 'pdf', 'status': 'CREATED'}},
                    # Note: 'doclib' is a valid Alfresco rendition type (document library thumbnail)
                    {'entry': {'id': 'doclib', 'status': 'CREATED'}}
                ],
                'pagination': {'count': 2}
            }
        }
        mock_list_renditions.return_value = expected_response
        
        # Act
        result = self.client.renditions.list_renditions('test-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_list_renditions.assert_called_once_with('test-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.renditions_api.RenditionsApi.get_rendition')
    def test_get__nodes_nodeId_renditions_renditionId(self, mock_get_rendition):
        """Test getting a specific rendition"""
        # Arrange
        expected_response = {
            'entry': {
                'id': 'pdf',
                'status': 'CREATED',
                'content': {'mimeType': 'application/pdf'}
            }
        }
        mock_get_rendition.return_value = expected_response
        
        # Act
        result = self.client.renditions.get_rendition('test-node-id', 'pdf')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_get_rendition.assert_called_once_with('test-node-id', 'pdf')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.renditions_api.RenditionsApi.get_rendition_content')
    def test_get__nodes_nodeId_renditions_renditionId_content(self, mock_get_rendition_content):
        """Test getting rendition content"""
        # Arrange
        expected_content = b"PDF content binary data"
        mock_get_rendition_content.return_value = expected_content
        
        # Act
        result = self.client.renditions.get_rendition_content('test-node-id', 'pdf')
        
        # Assert
        self.assertEqual(result, expected_content)
        mock_get_rendition_content.assert_called_once_with('test-node-id', 'pdf')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.create_secondary_child_association')
    def test_post__nodes_nodeId_secondary_children(self, mock_create_secondary):
        """Test creating secondary child associations"""
        # Arrange
        association_body = {'childId': 'child-node-id', 'assocType': 'cm:contains'}
        expected_response = {
            'entry': {
                'childId': 'child-node-id',
                'assocType': 'cm:contains'
            }
        }
        mock_create_secondary.return_value = expected_response
        
        # Act
        result = self.client.nodes.create_secondary_child_association(association_body, 'parent-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_create_secondary.assert_called_once_with(association_body, 'parent-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.list_secondary_children')
    def test_get__nodes_nodeId_secondary_children(self, mock_list_secondary):
        """Test listing secondary children"""
        # Arrange
        expected_response = {
            'list': {
                'entries': [
                    {
                        'entry': {
                            'childId': 'child-node-id',
                            'assocType': 'cm:contains',
                            'isPrimary': False
                        }
                    }
                ],
                'pagination': {'count': 1}
            }
        }
        mock_list_secondary.return_value = expected_response
        
        # Act
        result = self.client.nodes.list_secondary_children('parent-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_list_secondary.assert_called_once_with('parent-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.delete_secondary_child_association')
    def test_delete__nodes_nodeId_secondary_children_childId(self, mock_delete_secondary):
        """Test deleting secondary child associations"""
        # Arrange
        mock_delete_secondary.return_value = None
        
        # Act
        result = self.client.nodes.delete_secondary_child_association('parent-node-id', 'child-node-id')
        
        # Assert
        self.assertIsNone(result)
        mock_delete_secondary.assert_called_once_with('parent-node-id', 'child-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.list_parents')
    def test_get__nodes_nodeId_parents(self, mock_list_parents):
        """Test getting node parents"""
        # Arrange
        expected_response = {
            'list': {
                'entries': [
                    {
                        'entry': {
                            'id': 'parent-node-id',
                            'name': 'Parent Folder',
                            'assocType': 'cm:contains',
                            'isPrimary': True
                        }
                    }
                ],
                'pagination': {'count': 1}
            }
        }
        mock_list_parents.return_value = expected_response
        
        # Act
        result = self.client.nodes.list_parents('child-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_list_parents.assert_called_once_with('child-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.create_association')
    def test_post__nodes_nodeId_targets(self, mock_create_association):
        """Test creating node associations"""
        # Arrange
        association_body = {'targetId': 'target-node-id', 'assocType': 'cm:references'}
        expected_response = {
            'entry': {
                'targetId': 'target-node-id',
                'assocType': 'cm:references'
            }
        }
        mock_create_association.return_value = expected_response
        
        # Act
        result = self.client.nodes.create_association(association_body, 'source-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_create_association.assert_called_once_with(association_body, 'source-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.list_target_associations')
    def test_get__nodes_nodeId_targets(self, mock_list_targets):
        """Test listing node target associations"""
        # Arrange
        expected_response = {
            'list': {
                'entries': [
                    {
                        'entry': {
                            'targetId': 'target-node-id',
                            'assocType': 'cm:references'
                        }
                    }
                ],
                'pagination': {'count': 1}
            }
        }
        mock_list_targets.return_value = expected_response
        
        # Act
        result = self.client.nodes.list_target_associations('source-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_list_targets.assert_called_once_with('source-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.delete_association')
    def test_delete__nodes_nodeId_targets_targetId(self, mock_delete_association):
        """Test deleting node associations"""
        # Arrange
        mock_delete_association.return_value = None
        
        # Act
        result = self.client.nodes.delete_association('source-node-id', 'target-node-id')
        
        # Assert
        self.assertIsNone(result)
        mock_delete_association.assert_called_once_with('source-node-id', 'target-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.nodes_api.NodesApi.list_source_associations')
    def test_get__nodes_nodeId_sources(self, mock_list_sources):
        """Test getting node source associations"""
        # Arrange
        expected_response = {
            'list': {
                'entries': [
                    {
                        'entry': {
                            'sourceId': 'source-node-id',
                            'assocType': 'cm:references'
                        }
                    }
                ],
                'pagination': {'count': 1}
            }
        }
        mock_list_sources.return_value = expected_response
        
        # Act
        result = self.client.nodes.list_source_associations('target-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_list_sources.assert_called_once_with('target-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.versions_api.VersionsApi.list_version_history')
    def test_get__nodes_nodeId_versions(self, mock_list_versions):
        """Test listing node versions"""
        # Arrange
        expected_response = {
            'list': {
                'entries': [
                    {
                        'entry': {
                            'id': '1.0',
                            'versionComment': 'Initial version',
                            'modifiedAt': '2025-06-18T10:00:00.000+0000',
                            'modifiedByUser': {'id': 'admin', 'displayName': 'Administrator'}
                        }
                    },
                    {
                        'entry': {
                            'id': '1.1',
                            'versionComment': 'Updated content',
                            'modifiedAt': '2025-06-18T11:00:00.000+0000',
                            'modifiedByUser': {'id': 'admin', 'displayName': 'Administrator'}
                        }
                    }
                ],
                'pagination': {'count': 2}
            }
        }
        mock_list_versions.return_value = expected_response
        
        # Act
        result = self.client.versions.list_version_history('test-node-id')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_list_versions.assert_called_once_with('test-node-id')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.versions_api.VersionsApi.get_version')
    def test_get__nodes_nodeId_versions_versionId(self, mock_get_version):
        """Test getting a specific version"""
        # Arrange
        expected_response = {
            'entry': {
                'id': '1.0',
                'versionComment': 'Initial version',
                'modifiedAt': '2025-06-18T10:00:00.000+0000',
                'modifiedByUser': {'id': 'admin', 'displayName': 'Administrator'},
                'content': {'mimeType': 'text/plain', 'sizeInBytes': 1024}
            }
        }
        mock_get_version.return_value = expected_response
        
        # Act
        result = self.client.versions.get_version('test-node-id', '1.0')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_get_version.assert_called_once_with('test-node-id', '1.0')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.versions_api.VersionsApi.delete_version')
    def test_delete__nodes_nodeId_versions_versionId(self, mock_delete_version):
        """Test deleting a version"""
        # Arrange
        mock_delete_version.return_value = None
        
        # Act
        result = self.client.versions.delete_version('test-node-id', '1.0')
        
        # Assert
        self.assertIsNone(result)
        mock_delete_version.assert_called_once_with('test-node-id', '1.0')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.versions_api.VersionsApi.get_version_content')
    def test_get__nodes_nodeId_versions_versionId_content(self, mock_get_version_content):
        """Test getting version content"""
        # Arrange
        expected_content = b"Version 1.0 content"
        mock_get_version_content.return_value = expected_content
        
        # Act
        result = self.client.versions.get_version_content('test-node-id', '1.0')
        
        # Assert
        self.assertEqual(result, expected_content)
        mock_get_version_content.assert_called_once_with('test-node-id', '1.0')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.versions_api.VersionsApi.revert_version')
    def test_post__nodes_nodeId_versions_versionId_revert(self, mock_revert_version):
        """Test reverting to a version"""
        # Arrange
        revert_body = {'comment': 'Reverting to version 1.0'}
        expected_response = {
            'entry': {
                'id': 'test-node-id',
                'versionComment': 'Reverting to version 1.0',
                'isLatestVersion': True
            }
        }
        mock_revert_version.return_value = expected_response
        
        # Act
        result = self.client.versions.revert_version(revert_body, 'test-node-id', '1.0')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_revert_version.assert_called_once_with(revert_body, 'test-node-id', '1.0')

    def test_post__nodes_nodeId_versions_versionId_renditions(self):
        # TODO: Implement test for creating version renditions
        pass

    def test_get__nodes_nodeId_versions_versionId_renditions(self):
        # TODO: Implement test for listing version renditions
        pass

    def test_get__nodes_nodeId_versions_versionId_renditions_renditionId(self):
        # TODO: Implement test for getting version rendition
        pass

    def test_get__nodes_nodeId_versions_versionId_renditions_renditionId_content(self):
        # TODO: Implement test for getting version rendition content
        pass

    def test_get__nodes_nodeId_action_definitions(self):
        # TODO: Implement test for getting action definitions
        pass

    def test_get__deleted_nodes_nodeId_content(self):
        # TODO: Implement test for getting deleted node content
        pass

    def test_post__deleted_nodes_nodeId_restore(self):
        # TODO: Implement test for restoring deleted nodes
        pass

    def test_get__deleted_nodes_nodeId_renditions(self):
        # TODO: Implement test for getting deleted node renditions
        pass

    def test_get__deleted_nodes_nodeId_renditions_renditionId(self):
        # TODO: Implement test for getting deleted node rendition
        pass

    def test_get__deleted_nodes_nodeId_renditions_renditionId_content(self):
        # TODO: Implement test for getting deleted node rendition content
        pass

    @patch('alfresco_client.alfresco_core.alfresco_core.api.downloads_api.DownloadsApi.create_download')
    def test_post__downloads(self, mock_create_download):
        """Test creating a download"""
        # Arrange
        download_body = {'nodeIds': ['node1', 'node2']}
        expected_response = {
            'entry': {
                'id': 'download-123',
                'status': 'PENDING',
                'filesAdded': 0,
                'bytesAdded': 0
            }
        }
        mock_create_download.return_value = expected_response
        
        # Act
        result = self.client.downloads.create_download(download_body)
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_create_download.assert_called_once_with(download_body)

    @patch('alfresco_client.alfresco_core.alfresco_core.api.downloads_api.DownloadsApi.get_download')
    def test_get__downloads_downloadId(self, mock_get_download):
        """Test getting download status"""
        # Arrange
        expected_response = {
            'entry': {
                'id': 'download-123',
                'status': 'DONE',
                'filesAdded': 2,
                'bytesAdded': 2048
            }
        }
        mock_get_download.return_value = expected_response
        
        # Act
        result = self.client.downloads.get_download('download-123')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_get_download.assert_called_once_with('download-123')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.downloads_api.DownloadsApi.cancel_download')
    def test_delete__downloads_downloadId(self, mock_cancel_download):
        """Test canceling a download"""
        # Arrange
        mock_cancel_download.return_value = None
        
        # Act
        result = self.client.downloads.cancel_download('download-123')
        
        # Assert
        self.assertIsNone(result)
        mock_cancel_download.assert_called_once_with('download-123')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.people_api.PeopleApi.create_person')
    def test_post__people(self, mock_create_person):
        """Test creating a person"""
        # Arrange
        person_body = {
            'id': 'testuser',
            'firstName': 'Test',
            'lastName': 'User',
            'email': 'test@example.com',
            'password': 'password123'
        }
        expected_response = {
            'entry': {
                'id': 'testuser',
                'firstName': 'Test',
                'lastName': 'User',
                'email': 'test@example.com',
                'enabled': True
            }
        }
        mock_create_person.return_value = expected_response
        
        # Act
        result = self.client.people.create_person(person_body)
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_create_person.assert_called_once_with(person_body)

    @patch('alfresco_client.alfresco_core.alfresco_core.api.people_api.PeopleApi.list_people')
    def test_get__people(self, mock_list_people):
        """Test listing people"""
        # Arrange
        expected_response = {
            'list': {
                'entries': [
                    {
                        'entry': {
                            'id': 'admin',
                            'firstName': 'Administrator',
                            'email': 'admin@example.com',
                            'enabled': True
                        }
                    },
                    {
                        'entry': {
                            'id': 'testuser',
                            'firstName': 'Test',
                            'lastName': 'User',
                            'email': 'test@example.com',
                            'enabled': True
                        }
                    }
                ],
                'pagination': {'count': 2}
            }
        }
        mock_list_people.return_value = expected_response
        
        # Act
        result = self.client.people.list_people()
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_list_people.assert_called_once()

    @patch('alfresco_client.alfresco_core.alfresco_core.api.people_api.PeopleApi.get_person')
    def test_get__people_personId(self, mock_get_person):
        """Test getting person details"""
        # Arrange
        expected_response = {
            'entry': {
                'id': 'testuser',
                'firstName': 'Test',
                'lastName': 'User',
                'email': 'test@example.com',
                'enabled': True,
                'company': {'organization': 'Test Corp'}
            }
        }
        mock_get_person.return_value = expected_response
        
        # Act
        result = self.client.people.get_person('testuser')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_get_person.assert_called_once_with('testuser')

    @patch('alfresco_client.alfresco_core.alfresco_core.api.people_api.PeopleApi.update_person')
    def test_put__people_personId(self, mock_update_person):
        """Test updating a person"""
        # Arrange
        update_body = {'firstName': 'Updated', 'company': {'organization': 'New Corp'}}
        expected_response = {
            'entry': {
                'id': 'testuser',
                'firstName': 'Updated',
                'lastName': 'User',
                'email': 'test@example.com',
                'company': {'organization': 'New Corp'}
            }
        }
        mock_update_person.return_value = expected_response
        
        # Act
        result = self.client.people.update_person(update_body, 'testuser')
        
        # Assert
        self.assertEqual(result, expected_response)
        mock_update_person.assert_called_once_with(update_body, 'testuser')

    def test_get__people_personId_activities(self):
        # TODO: Implement test for getting person activities
        pass

    def test_get__people_personId_favorite_sites(self):
        # TODO: Implement test for getting favorite sites
        pass

    def test_post__people_personId_favorite_sites(self):
        # TODO: Implement test for adding favorite sites
        pass

    def test_get__people_personId_favorite_sites_siteId(self):
        # TODO: Implement test for getting specific favorite site
        pass

    def test_delete__people_personId_favorite_sites_siteId(self):
        # TODO: Implement test for removing favorite sites
        pass

    def test_get__people_personId_favorites(self):
        # TODO: Implement test for getting favorites
        pass

    def test_post__people_personId_favorites(self):
        # TODO: Implement test for adding favorites
        pass

    def test_get__people_personId_favorites_favoriteId(self):
        # TODO: Implement test for getting specific favorite
        pass

    def test_delete__people_personId_favorites_favoriteId(self):
        # TODO: Implement test for removing favorites
        pass

    def test_get__people_personId_networks(self):
        # TODO: Implement test for getting person networks
        pass

    def test_get__people_personId_networks_networkId(self):
        # TODO: Implement test for getting specific network
        pass

    def test_get__people_personId_preferences(self):
        # TODO: Implement test for getting preferences
        pass

    def test_get__people_personId_preferences_preferenceName(self):
        # TODO: Implement test for getting specific preference
        pass


if __name__ == '__main__':
    unittest.main()

