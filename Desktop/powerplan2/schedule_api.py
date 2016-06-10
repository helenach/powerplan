import json
import time
import requests

class ScheduleApiError(Exception):
    '''
    Raised if there is an error with the schedule API.
    '''
    pass

# The base API endpoint
base_url = 'http://umich-schedule-api.herokuapp.com'

# the amount of time to wait for the schedule API
timeout_duration = 25


def get_data(relative_path):
    '''
    Gets data from the schedule API at the specified path.
    Will raise a ScheduleApiError if unsuccessful.
    Assumes API will return JSON, returns as a dictionary.
    '''

    timeout_at = time.time() + timeout_duration

    while time.time() < timeout_at:
        r = requests.get(base_url + relative_path)
        if r.status_code == 200:
            return json.loads(r.text)
        if r.status_code == 400:
            break

    raise ScheduleApiError('error for url: {0} message: "{1}" code: {2}' \
        .format(relative_path, r.text, r.status_code))

def get_terms():
    '''
    Returns a list of valid terms.
    Each item in the list is a dictionary containing:
        ('TermCode', 'TermDescr', 'TermShortDescr')
    '''
    return get_data('/get_terms')

def get_schools(termCode): 
    return get_data('/get_schools?term_code='+str(termCode))

def get_subjects(termCode, schoolName): 
    return get_data('/get_subjects?term_code='+str(termCode)+'&school='+schoolName)

def get_catalog_numbers(termCode, schoolName, subjectName):
    return get_data('/get_catalog_numbers?term_code='+str(termCode)+
        '&school='+schoolName+'&subject='+subjectName)

def get_course_description (termCode, schoolName, subjectName, catalogNumber):
    return get_data('/get_course_description?term_code='+str(termCode)+
        '&school='+schoolName+'&subject='+subjectName+'&catalog_num='+str(catalogNumber))

def get_sections (termCode, schoolName, subjectName,catalogNumber):
    return get_data('/get_sections?term_code='+str(termCode)+'&school='+
        schoolName+'&subject='+subjectName+'&catalog_num='+str(catalogNumber))





def get_section_details(termCode, schoolName, subjectName, catalogNumber, sectionNumber): 
    return get_data('/get_section_details?term_code='+str(termCode)+'&school='+
        schoolName+'&subject='+subjectName+'&catalog_num='+str(catalogNumber)+
        '&section_num='+str(sectionNumber))

def get_meetings(termCode,schoolName,subjectName,catalogNumber,sectionNumber): 
    return get_data('/get_meetings?term_code='+str(termCode)+'&school='+
        schoolName+'&subject='+subjectName+'&catalog_num='+str(catalogNumber)+
        '&section_num='+str(sectionNumber))
def get_textbooks(termCode,schoolName,subjectName,catalogNumber,sectionNumber):
    return get_data('/get_textbooks?term_code='+str(termCode)+'&school='+
        schoolName+'&subject='+subjectName+'&catalog_num='+str(catalogNumber)+
        '&section_num='+str(sectionNumber))
def get_instructors(termCode,schoolName,subjectName,catalogNumber,sectionNumber):
    return get_data('/get_instructors?term_code='+str(termCode)+'&school='+
        schoolName+'&subject='+subjectName+'&catalog_num='+str(catalogNumber)+
        '&section_num='+str(sectionNumber))


