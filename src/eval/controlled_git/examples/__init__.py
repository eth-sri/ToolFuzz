def get_all_examples(classdef):
    comments_on_issues = []
    for coi in classdef.__subclasses__():
        comments_on_issues.append(coi())
    
    return comments_on_issues
