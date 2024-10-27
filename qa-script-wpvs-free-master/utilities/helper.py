import time

from utilities.testrail import *
from datetime import datetime


url = "https://zennode.testrail.io/"
email = "anu@zennode.com"
password = "Zennode@123"


def get_client():
    client = APIClient(url)
    client.user = email
    client.password = password
    return client


def get_id_property(case_id, property_name):
    case_property = get_client().send_get('get_case/%s' % case_id)['%s' % property_name]
    # time.sleep(2)
    return case_property


def get_project_id(project_name):
    global project_id
    client = get_client()
    projects = client.send_get('get_projects')
    for project in projects['projects']:
        if project['name'] == project_name:
            project_id = project['id']
            # project_found_flag=True
            break
    return project_id


def get_test_run_id(project_name):
    client = get_client()
    project_id = get_project_id(project_name)
    date_and_time = datetime.today().strftime('%d-%m-%Y %H:%M:%S')
    test_run = client.send_post('add_run/%s' % project_id,
                                {'name': 'Automation Run %s' % date_and_time})
    return test_run['id']


def update_test_run(case_id, run_id, result_flag):
    client = get_client()
    status_id = 1 if result_flag is True else 5  # status_id is 1 for Passed, 2 For Blocked, 4 for Retest and 5 for Failed

    if run_id is not None:
        try:
            result = client.send_post('add_result_for_case/%s/%s' % (run_id, case_id),
                                      {'status_id': status_id})
        except Exception as e:
            print('Exception in update_testrail() updating TestRail.')
            print('PYTHON SAYS: ')
            print(e)
        else:
            print('\n', 'Updated test result for case: %s in test run: %s' % (case_id, run_id))


def get_section_cases(project_id, section_id):
    client = get_client()
    section = client.send_get('get_cases/%s&section_id=%s' % (project_id, section_id))

    return section['cases']


def get_case(case_id):
    client = get_client()
    case_details = client.send_get('get_case/%s' % case_id)
    print(case_details)
# update_test_run(1010977, 9909, True, "The test run is completed")
