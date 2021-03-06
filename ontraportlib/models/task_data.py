# -*- coding: utf-8 -*-

"""
    ontraportlib.models.task_data
 
    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ) on 11/14/2017
"""
import  ontraportlib.models.task_followup
import  ontraportlib.models.base_model

class TaskData(ontraportlib.models.base_model.BaseModel):

    """Implementation of the 'TaskData' model.

    TODO: type model description here.

    Attributes:
        followup (TaskFollowup): TODO: type description here.
        outcome (string): Task outcome name. This must start with ":=" For
            example, <strong>":=signed"</strong>.
        task_form_data (string): These fields can be used to update associated
            Object data when completing a task. For example, set
            <strong>task_form_title</strong> to "New title" to change the
            Contact's title.

    """

    def __init__(self, 
                 followup = None,
                 outcome = None,
                 task_form_data = None):
        """Constructor for the TaskData class"""
        
        # Initialize members of the class
        self.followup = followup
        self.outcome = outcome
        self.task_form_data = task_form_data

        # Create a mapping from Model property names to API property names
        self.names = {
            "followup" : "followup",
            "outcome" : "outcome",
            "task_form_data" : "task_form_data",
        }


    @classmethod
    def from_dictionary(cls, 
                        dictionary):
        """Creates an instance of this model from a dictionary
       
        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.
            
        Returns:
            object: An instance of this structure class.
            
        """
        if dictionary == None:
            return None
        else:
            # Extract variables from the dictionary
            followup = ontraportlib.models.task_followup.TaskFollowup.from_dictionary(dictionary.get("followup")) if dictionary.get("followup") else None
            outcome = dictionary.get("outcome")
            task_form_data = dictionary.get("task_form_data")
            # Return an object of this model
            return cls(followup,
                       outcome,
                       task_form_data)
