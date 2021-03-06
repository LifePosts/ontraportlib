# -*- coding: utf-8 -*-

"""
    ontraportlib.controllers.messages_controller

    This file was automatically generated by APIMATIC BETA v2.0 on 11/14/2017
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..models.response import Response
from ..exceptions.api_exception import APIException

class MessagesController(BaseController):

    """A Controller to access Endpoints in the ontraportlib API."""
    

    def get_message(self,
                    id):
        """Does a GET request to /message.

        This will fetch data from an existing Message.

        Args:
            id (int): ID of Object.

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
        _query_builder += '/message'
        _query_url = APIHelper.clean_url(_query_builder)
        _query_parameters = {
            'id': id
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.http_client.get(_query_url, headers=_headers, query_parameters=_query_parameters)
        _context = self.execute_request(_request)        

        # Endpoint and global error handling using HTTP status codes.
        if _context.response.status_code == 404:
            raise APIException('Message not found', _context)
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Response.from_dictionary)

    def update_message(self,
                       alias,
                       due_date,
                       email_title,
                       mfrom,
                       id,
                       message_body,
                       name,
                       plaintext,
                       reply_to_email,
                       resource,
                       send_from,
                       send_out_name,
                       send_to,
                       subject,
                       task_data,
                       task_form,
                       task_owner):
        """Does a PUT request to /message.

        TODO: type endpoint description here.

        Args:
            alias (string): Message alias.
            due_date (int): Use this only for Task Messages. This is the
                number of days after assignment this Task is due.
            email_title (string): Short title that will appear as the first
                line in email clients.
            mfrom (string): Who will this Message come from? If not
                <b>owner</b> or <b>custom</b>, this field can contain the
                Staff user ID to send the Message from.
            id (int): ID of the Message to be updated.
            message_body (string): Use this for Legacy Email Messages only.
                This is the HTML content of the Message.
            name (string): Name of your Message.
            plaintext (string): The plain text version of your Message (for
                Email messages). For SMS Messages, this is the content that
                will be sent.
            reply_to_email (string): The email address to use as the reply-to
                in the Message.
            resource (string): For ONTRAmail Messages only; this is the
                content of the message. Note that this can be extremely
                complex, so you should start by inspecting the resource that
                is sent when saving a Message from inside the App. For SMS
                Messages, use the plaintext field for content.
            send_from (string): Custom Send-from email address. Leave this
                empty to use your default email address. Otherwise, this must
                be a validated send-from email address.
            send_out_name (string): Name to be used in the 'Message From'
                field when the <b>from</b> field is set to <b>custom</b>.
            send_to (string): Only used with SMS Messages or Custom Objects.
                Select the field to use when there may be a parent or child
                relationship to the Object type given in
                <b>object_type_id</b>. The default for SMS Message is
                <b>sms_number.</b>
            subject (string): Subject to be sent with the Message.
            task_data (string): Use this only for Task Messages. This is the
                content of the Message.
            task_form (int): Use this only for Task Messages. This is the
                optional Form ID to be filled when the Task is completed. This
                form must already exist.
            task_owner (int): Use this only for Task Messages. This is the
                Staff user ID of the Task owner.

        Returns:
            Response: Response from the API. Message successfully updated

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/message'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'alias': alias,
            'due_date': due_date,
            'email_title': email_title,
            'from': mfrom,
            'id': id,
            'message_body': message_body,
            'name': name,
            'objectID': 7,
            'plaintext': plaintext,
            'reply_to_email': reply_to_email,
            'resource': resource,
            'send_from': send_from,
            'send_out_name': send_out_name,
            'send_to': send_to,
            'subject': subject,
            'task_data': task_data,
            'task_form': task_form,
            'task_owner': task_owner
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.put(_query_url, headers=_headers, parameters=_form_parameters)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Response.from_dictionary)

    def create_save_message(self,
                            alias,
                            due_date,
                            email_title,
                            mfrom,
                            message_body,
                            name,
                            object_type_id,
                            plaintext,
                            reply_to_email,
                            resource,
                            send_from,
                            send_out_name,
                            send_to,
                            subject,
                            task_data,
                            task_form,
                            task_owner,
                            mtype):
        """Does a POST request to /message.

        TODO: type endpoint description here.

        Args:
            alias (string): Message alias.
            due_date (int): Use this only for Task Messages. This is the
                number of days after assignment this Task is due.
            email_title (string): Short title that will appear as the first
                line in email clients.
            mfrom (string): Who will this Message come from? If not
                <b>owner</b> or <b>custom</b>, this field can contain the
                Staff user ID to send the Message from.
            message_body (string): Use this for Legacy Email Messages only.
                This is the HTML content of the Message.
            name (string): Name of your Message.
            object_type_id (int): Object type to associate with this Message.
                This will be zero (0) for Contacts. You should only change
                this if you are using Custom Objects.
            plaintext (string): The plain text version of your Message (for
                Email messages). For SMS Messages, this is the content that
                will be sent.
            reply_to_email (string): The email address to use as the reply-to
                in the Message.
            resource (string): For ONTRAmail Messages only; this is the
                content of the message. Note that this can be extremely
                complex, so you should start by inspecting the resource that
                is sent when saving a Message from inside the App. For SMS
                Messages, use the plaintext field for content.
            send_from (string): Custom Send-from email address. Leave this
                empty to use your default email address. Otherwise, this must
                be a validated send-from email address.
            send_out_name (string): Name to be used in the 'Message From'
                field when the <b>from</b> field is set to <b>custom</b>.
            send_to (string): Only used with SMS Messages or Custom Objects.
                Select the field to use when there may be a parent or child
                relationship to the Object type given in
                <b>object_type_id</b>. The default for SMS Message is
                <b>sms_number.</b>
            subject (string): Subject to be sent with the Message.
            task_data (string): Use this only for Task Messages. This is the
                content of the Message.
            task_form (int): Use this only for Task Messages. This is the
                optional Form ID to be filled when the Task is completed. This
                form must already exist.
            task_owner (int): Use this only for Task Messages. This is the
                Staff user ID of the Task owner.
            mtype (string): Message type: use <b>template</b> for ONTRAmail,
                <b>e-mail</b> for Legacy Email, <b>sms</b> for SMS Messages,
                <b>task</b> for Task Messages.

        Returns:
            Response: Response from the API. Message successfully created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/message'
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare form parameters
        _form_parameters = {
            'alias': alias,
            'due_date': due_date,
            'email_title': email_title,
            'from': mfrom,
            'message_body': message_body,
            'name': name,
            'object_type_id': object_type_id,
            'objectID': 7,
            'plaintext': plaintext,
            'reply_to_email': reply_to_email,
            'resource': resource,
            'send_from': send_from,
            'send_out_name': send_out_name,
            'send_to': send_to,
            'subject': subject,
            'task_data': task_data,
            'task_form': task_form,
            'task_owner': task_owner,
            'type': mtype
        }
        _form_parameters = APIHelper.form_encode_parameters(_form_parameters)

        # Prepare and execute request
        _request = self.http_client.post(_query_url, headers=_headers, parameters=_form_parameters)
        _context = self.execute_request(_request)        
        self.validate_response(_context)    

        # Return appropriate type
        return APIHelper.json_deserialize(_context.response.raw_body, Response.from_dictionary)
