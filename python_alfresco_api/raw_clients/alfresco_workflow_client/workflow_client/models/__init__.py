"""Contains all the data models used in inputs/outputs"""

from .candidate import Candidate
from .candidate_candidate_type import CandidateCandidateType
from .candidate_entry import CandidateEntry
from .candidate_paging import CandidatePaging
from .candidate_paging_list import CandidatePagingList
from .company import Company
from .deployment import Deployment
from .deployment_entry import DeploymentEntry
from .deployment_paging import DeploymentPaging
from .deployment_paging_list import DeploymentPagingList
from .error import Error
from .error_error import ErrorError
from .item import Item
from .item_body import ItemBody
from .item_entry import ItemEntry
from .item_paging import ItemPaging
from .item_paging_list import ItemPagingList
from .pagination import Pagination
from .person import Person
from .process import Process
from .process_body import ProcessBody
from .process_body_variable import ProcessBodyVariable
from .process_definition import ProcessDefinition
from .process_definition_entry import ProcessDefinitionEntry
from .process_definition_paging import ProcessDefinitionPaging
from .process_definition_paging_list import ProcessDefinitionPagingList
from .process_entry import ProcessEntry
from .process_paging import ProcessPaging
from .process_paging_list import ProcessPagingList
from .task import Task
from .task_body import TaskBody
from .task_body_state import TaskBodyState
from .task_entry import TaskEntry
from .task_form_model import TaskFormModel
from .task_form_model_entry import TaskFormModelEntry
from .task_form_model_paging import TaskFormModelPaging
from .task_form_model_paging_list import TaskFormModelPagingList
from .task_paging import TaskPaging
from .task_paging_list import TaskPagingList
from .task_state import TaskState
from .variable import Variable
from .variable_body import VariableBody
from .variable_entry import VariableEntry
from .variable_paging import VariablePaging
from .variable_paging_list import VariablePagingList

__all__ = (
    "Candidate",
    "CandidateCandidateType",
    "CandidateEntry",
    "CandidatePaging",
    "CandidatePagingList",
    "Company",
    "Deployment",
    "DeploymentEntry",
    "DeploymentPaging",
    "DeploymentPagingList",
    "Error",
    "ErrorError",
    "Item",
    "ItemBody",
    "ItemEntry",
    "ItemPaging",
    "ItemPagingList",
    "Pagination",
    "Person",
    "Process",
    "ProcessBody",
    "ProcessBodyVariable",
    "ProcessDefinition",
    "ProcessDefinitionEntry",
    "ProcessDefinitionPaging",
    "ProcessDefinitionPagingList",
    "ProcessEntry",
    "ProcessPaging",
    "ProcessPagingList",
    "Task",
    "TaskBody",
    "TaskBodyState",
    "TaskEntry",
    "TaskFormModel",
    "TaskFormModelEntry",
    "TaskFormModelPaging",
    "TaskFormModelPagingList",
    "TaskPaging",
    "TaskPagingList",
    "TaskState",
    "Variable",
    "VariableBody",
    "VariableEntry",
    "VariablePaging",
    "VariablePagingList",
)
