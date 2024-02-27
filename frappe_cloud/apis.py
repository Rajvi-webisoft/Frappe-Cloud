import frappe
import json
from click import command
from kubernetes import client, config
from kubernetes.stream import stream
import yaml
import subprocess
from kubernetes import client, config
from kubernetes.client.rest import ApiException
import re
from datetime import datetime
import os


@frappe.whitelist()
def create_site():
    site_name = "aaa"

    query = """
        SELECT name, site_name, site_status, site_job_type 
        FROM `tabSite Creation Details` 
        WHERE site_name = %s 
            AND (site_status = 'Live' OR site_job_type = 'Create')
           
    """

    try:
        site_exists = frappe.db.sql(query, (site_name,), as_dict=True)
        if site_exists:
            # [site_job_name,site_job_status]=create_new_site(site_name, password)
            # return Response({'message': 'Site creation process initiated successfully','site_job_name':site_job_name,'site_job_status':site_job_status}, status=status.HTTP_200_OK)
            return "Error"        
        else:
            # return Response({'message': 'Site already exist in bench.','site_job_name':'','site_job_status':''}, status=status.HTTP_200_OK)
            return "Create New site"
    except Exception as e:
        # raise e
        print(e)
        # return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return "error"