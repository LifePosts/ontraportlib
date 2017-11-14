# -*- coding: utf-8 -*-

"""
    ontraportlib.controllers.objects_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 11/14/2017
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..models.response import Response
from ..exceptions.api_exception import APIException
from ..models.format_enum import FormatEnum


class ObjectsController(BaseController):

    """A Controller to access Endpoints in the ontraportlib API."""
    

    def get_object(self,
                   id,
                   object_id):
        """Does a GET request to /object.

        This will fetch data for a given Object type and ID.

        Args:
            id (int): ID of Object.
            object_id (int): Object Type ID.

        Returns:
            Response: Response from the API. Successful object query

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/object'
        _query_url = APIHelper.clean_url(_query_builder)
        _query_parameters = {
            'id': id,
            'objectID': object_id
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)
        _context = self.execute_request(_request)        

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Invalid objectID', _context)
        elif _context.response.status_code == 404:
            raise APIException('Object not found', _context)
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Response.from_dictionary)

    def delete_object(self,
                      id,
                      object_id):
        """Does a DELETE request to /object.

        This will delete an Object with the given Object type and ID.

        Args:
            id (int): ID of Object.
            object_id (int): Object Type ID.

        Returns:
            Response: Response from the API. Successful object query

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/object'
        _query_url = APIHelper.clean_url(_query_builder)
        _query_parameters = {
            'id': id,
            'objectID': object_id
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers, query_parameters=_query_parameters)
        _context = self.execute_request(_request)        

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Invalid objectID', _context)
        elif _context.response.status_code == 404:
            raise APIException('Object not found', _context)
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Response.from_dictionary)

    def get_objects(self,
                    condition,
                    date_range,
                    externs,
                    group_ids,
                    ids,
                    list_fields,
                    object_id,
                    perform_all,
                    range,
                    search,
                    search_notes,
                    sort,
                    sort_dir,
                    start):
        """Does a GET request to /objects.

        TODO: type endpoint description here.

        Args:
            condition (string): Apply this condition to the collection query.
                This is essentially like a SQL WHERE clause, e.g.
                firstname='Ben'
            date_range (list of int): Start and End dates to search, in
                seconds since Jan 1, 1970, as a comma-separated list. Start
                (index 0 in the array) is inclusive, End (index 1) is
                exclusive. Either or both can be empty.
            externs (string): External fields to include in results
            group_ids (list of int): Array of Group ID for Object type as
                comma-delimited list
            ids (list of int): Array of Object IDs as comma-delimited list.
            list_fields (list of string): Array of fields to return in
                response as comma-delimited list.
            object_id (int): Object Type ID.
            perform_all (bool): Perform request on all Objects that match
                criteria.
            range (int): Number of results to return (maximum=50)
            search (string): Search Objects for this string
            search_notes (bool): Boolean flag to additionally search Object
                Notes for the Search term given in Search parameter
            sort (string): Field used to sort results
            sort_dir (SortDirEnum): Sort direction, must be used in
                conjunction with <b>sort</b> parameter.
            start (int): Return results starting at this offset

        Returns:
            Response: Response from the API. Successful object query

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/objects'
        _query_url = APIHelper.clean_url(_query_builder)
        _query_parameters = {
            'condition': condition,
            'date_range': date_range,
            'externs': externs,
            'group_ids': group_ids,
            'ids': ids,
            'listFields': list_fields,
            'objectID': object_id,
            'performAll': perform_all,
            'range': range,
            'search': search,
            'searchNotes': search_notes,
            'sort': sort,
            'sortDir': sort_dir,
            'start': start
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)
        _context = self.execute_request(_request)        

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Invalid objectID', _context)
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Response.from_dictionary)

    def update_objects(self,
                       id,
                       object_id,
                       data=None):
        """Does a PUT request to /objects.

        This will update an Object's data. The Object type and ID and required
        parameters, but other parameters are dependent upon the object type.
        We have provided optional parameters as examples for updating a
        Contact. When using this in your application, all invalid parameters
        will be ignored.

        Args:
            id (int): ID of Object.
            object_id (int): Object Type ID.
            data (dict): Optional, attributes of object to be updated.

        Returns:
            Response: Response from the API. Successfully updated object

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        if data is None:
            data = {}

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/objects'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'id': id,
            'objectID': object_id
        }
        _form_parameters.update(data)
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=_form_parameters)
        _context = self.execute_request(_request)        

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 404:
            raise APIException('Object not found', _context)
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Response.from_dictionary)

    def create_object(self,
                      object_id,
                      data=None):
        """Does a POST request to /object.

        This will create an Object with the given data. Object type is a
        required parameters, but other parameters are optional and dependent
        upon the object type. We have provided optional parameters as examples
        for updating a Contact. When using this in your application, all
        invalid parameters will be ignored.

        Args:
            object_id (int): Object Type ID.
            data (dict): Data for object.

        Returns:
            Response: Response from the API. Successful object query

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        if data is None:
            data = {}

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/objects'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'objectID': object_id
        }
        _form_parameters.update(data)
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        _context = self.execute_request(_request)        

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Invalid objectID', _context)
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Response.from_dictionary)

    def delete_objects(self,
                       condition,
                       date_range,
                       externs,
                       group_ids,
                       ids,
                       list_fields,
                       object_id,
                       perform_all,
                       range,
                       search,
                       search_notes,
                       sort,
                       sort_dir,
                       start):
        """Does a DELETE request to /objects.

        TODO: type endpoint description here.

        Args:
            condition (string): Apply this condition to the collection query.
                This is essentially like a SQL WHERE clause, e.g.
                firstname='Ben'
            date_range (list of int): Start and End dates to search, in
                seconds since Jan 1, 1970, as a comma-separated list. Start
                (index 0 in the array) is inclusive, End (index 1) is
                exclusive. Either or both can be empty.
            externs (string): External fields to include in results
            group_ids (list of int): Array of Group ID for Object type as
                comma-delimited list
            ids (list of int): Array of Object IDs as comma-delimited list.
            list_fields (list of string): Array of fields to return in
                response as comma-delimited list.
            object_id (int): Object Type ID.
            perform_all (bool): Perform request on all Objects that match
                criteria.
            range (int): Number of results to return (maximum=50)
            search (string): Search Objects for this string
            search_notes (bool): Boolean flag to additionally search Object
                Notes for the Search term given in Search parameter
            sort (string): Field used to sort results
            sort_dir (SortDirEnum): Sort direction, must be used in
                conjunction with <b>sort</b> parameter.
            start (int): Return results starting at this offset

        Returns:
            Response: Response from the API. Successful object query

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/objects'
        _query_url = APIHelper.clean_url(_query_builder)
        _query_parameters = {
            'condition': condition,
            'date_range': date_range,
            'externs': externs,
            'group_ids': group_ids,
            'ids': ids,
            'listFields': list_fields,
            'objectID': object_id,
            'performAll': perform_all,
            'range': range,
            'search': search,
            'searchNotes': search_notes,
            'sort': sort,
            'sortDir': sort_dir,
            'start': start
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers, query_parameters=_query_parameters)
        _context = self.execute_request(_request)        

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Invalid objectID', _context)
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Response.from_dictionary)

    def get_objects_info(self,
                         condition,
                         date_range,
                         group_ids,
                         object_id,
                         search,
                         search_notes):
        """Does a GET request to /objects/getInfo.

        Get information about an Objects Collection, such as the number of
        Objects that match the given criteria.

        Args:
            condition (string): Apply this condition to the collection query.
                This is essentially like a SQL WHERE clause, e.g.
                firstname='Ben'
            date_range (list of int): Start and End dates to search, in
                seconds since Jan 1, 1970, as a comma-separated list. Start
                (index 0 in the array) is inclusive, End (index 1) is
                exclusive. Either or both can be empty.
            group_ids (list of int): Array of Group ID for Object type as
                comma-delimited list
            object_id (int): Object Type ID.
            search (string): Search Objects for this string
            search_notes (bool): Boolean flag to additionally search Object
                Notes for the Search term given in Search parameter

        Returns:
            Response: Response from the API. Successful object query

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/objects/getInfo'
        _query_url = APIHelper.clean_url(_query_builder)
        _query_parameters = {
            'condition': condition,
            'date_range': date_range,
            'group_ids': group_ids,
            'objectID': object_id,
            'search': search,
            'searchNotes': search_notes
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)
        _context = self.execute_request(_request)        

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Invalid objectID', _context)
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Response.from_dictionary)

    def get_meta(self,
                 object_id,
                 format=FormatEnum.BYID):
        """Does a GET request to /objects/meta.

        This will get a list of existing Object types and their corresponding
        field names. Use the <b>objectID</b> parameter to This will get a
        single Object type.

        Args:
            format (FormatEnum): Choose to get the list indexed by Object
                class name or integer ID.
            object_id (int): Object Type ID.
        Kwargs:
            format (FormatEnum): Choose to get the list indexed by Object
                class name or integer ID. Default `FormatEnum.BYID`.

        Returns:
            Response: Response from the API. Successful object query

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/objects/meta'
        _query_url = APIHelper.clean_url(_query_builder)
        _query_parameters = {
            'format': format,
            'objectID': object_id
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Response.from_dictionary)

    def create_saveorupdate_object(self,
                                   object_id,
                                   data=None):
        """Does a POST request to /objects/saveorupdate.

        This will create an Object with the given data or will merge with an
        Object in the database if the unique field matches another Object’s.
        Object type is a required parameter, but other parameters are optional
        and depend on the Object type. We have provided optional parameters as
        examples for updating a Contact. When using this in your application,
        all invalid parameters will be ignored.

        Args:
            object_id (int): Object Type ID.
            data (dict): Data for object.

        Returns:
            Response: Response from the API. Successful object query

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """
        if data is None:
            data = {}

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/objects/saveorupdate'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'objectID': object_id
        }
        _form_parameters.update(data)
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        _context = self.execute_request(_request)        

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 400:
            raise APIException('Invalid objectID', _context)
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Response.from_dictionary)

    def add_tag(self,
                add_list,
                condition,
                date_range,
                externs,
                group_ids,
                ids,
                list_fields,
                object_id,
                perform_all,
                range,
                search,
                search_notes,
                sort,
                sort_dir,
                start):
        """Does a PUT request to /objects/tag.

        This will add a Tag to an Object. when adding or removing Tags, either
        <b>ids</b> or <b>group_ids</b> must be given.

        Args:
            add_list (list of int): Array of Tag IDs as comma-delimited list.
            condition (string): Apply this condition to the collection query.
                This is essentially like a SQL WHERE clause, e.g.
                firstname='Ben'
            date_range (list of int): Start and End dates to search, in
                seconds since Jan 1, 1970, as a comma-separated list. Start
                (index 0 in the array) is inclusive, End (index 1) is
                exclusive. Either or both can be empty.
            externs (string): External fields to include in results
            group_ids (list of int): Array of Group ID for Object type as
                comma-delimited list
            ids (list of int): Array of Object IDs as comma-delimited list.
            list_fields (list of string): Array of fields to return in
                response as comma-delimited list.
            object_id (int): Object Type ID.
            perform_all (bool): Perform request on all Objects that match
                criteria.
            range (int): Number of results to return (maximum=50)
            search (string): Search objects for this string
            search_notes (bool): Boolean flag to additionally search Object
                Notes for the Search term given in Search parameter
            sort (string): Field used to sort results
            sort_dir (SortDirEnum): Sort direction, must be used in
                conjunction with <b>sort</b> parameter.
            start (int): Return results starting at this offset

        Returns:
            Response: Response from the API. Successfully added Tag(s)

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/objects/tag'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'add_list': add_list,
            'condition': condition,
            'date_range': date_range,
            'externs': externs,
            'group_ids': group_ids,
            'ids': ids,
            'listFields': list_fields,
            'objectID': object_id,
            'performAll': perform_all,
            'range': range,
            'search': search,
            'searchNotes': search_notes,
            'sort': sort,
            'sortDir': sort_dir,
            'start': start
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=_form_parameters)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Response.from_dictionary)

    def remove_tag(self,
                   condition,
                   date_range,
                   externs,
                   group_ids,
                   ids,
                   list_fields,
                   object_id,
                   perform_all,
                   range,
                   remove_list,
                   search,
                   search_notes,
                   sort,
                   sort_dir,
                   start):
        """Does a DELETE request to /objects/tag.

        This will remove a Tag from an Object using a Tag ID. When adding or
        removing Tags, either <b>ids</b> or <b>group_ids</b> must be given.

        Args:
            condition (string): Apply this condition to the collection query.
                This is essentially like a SQL WHERE clause, e.g.
                firstname='Ben'
            date_range (list of int): Start and End dates to search, in
                seconds since Jan 1, 1970, as a comma-separated list. Start
                (index 0 in the array) is inclusive, End (index 1) is
                exclusive. Either or both can be empty.
            externs (string): External fields to include in results
            group_ids (list of int): Array of Group ID for Object type as
                comma-delimited list
            ids (list of int): Array of Object IDs as comma-delimited list.
            list_fields (list of string): Array of fields to return in
                response as comma-delimited list.
            object_id (int): Object Type ID.
            perform_all (bool): Perform request on all Objects that match
                criteria.
            range (int): Number of results to return (maximum=50)
            remove_list (list of int): Array of Tag IDs as comma-delimited
                list.
            search (string): Search objects for this string
            search_notes (bool): Boolean flag to additionally search Object
                Notes for the Search term given in Search parameter
            sort (string): Field used to sort results
            sort_dir (SortDirEnum): Sort direction, must be used in
                conjunction with <b>sort</b> parameter.
            start (int): Return results starting at this offset

        Returns:
            Response: Response from the API. Successfully removed Tag(s)

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/objects/tag'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'condition': condition,
            'date_range': date_range,
            'externs': externs,
            'group_ids': group_ids,
            'ids': ids,
            'listFields': list_fields,
            'objectID': object_id,
            'performAll': perform_all,
            'range': range,
            'remove_list': remove_list,
            'search': search,
            'searchNotes': search_notes,
            'sort': sort,
            'sortDir': sort_dir,
            'start': start
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.delete(_query_url, headers=_headers, parameters=_form_parameters)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Response.from_dictionary)
