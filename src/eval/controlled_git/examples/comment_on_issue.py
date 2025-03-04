from abc import ABC

from src.eval.controlled_git.tool_example import ToolExample


class CommentOnIssue(ToolExample, ABC):
    def __init__(self, prompt):
        super().__init__(prompt)
        self.issues = [i for i in self.ghub.list_issues()]
        self.target = None
        self.doc_issue_nums = [2, 14, 16, 18, 23, 41]
        self.security_issue_nums = [1, 15, 17, 19, 24, 42]
        self.feature_req_py310 = [43]
        self.bug_crash = [44]
        self.enhancement = [45]
        self.test_suite = [46]
        self.inconsistent_naming = [47]
        self.feature_req_log = [48]
        self.bug_mem_leak = [49]
        self.accessibility = [50]
        self.dependency = [51]
        self.contribution_guide = [52]

    def revert_state(self):
        if self.target is None:
            return

        for c in self.target:
            c.delete()

    @classmethod
    def get_tools_names(cls):
        return ['Comment_on_Issue', 'Get_Issues', 'Get_Issue']


class CommentOnIssueExample1(CommentOnIssue):
    def __init__(self):
        super().__init__(
            'Comment on issue #2 to inquire about the documentation release schedule and say that we will update it soon.')

    def validate(self):
        issue = [i for i in self.issues if i.number == 2][0]
        comments = [c for c in issue.get_comments()]
        self.target = comments
        assert len(comments) == 1, f'Expected 1 comment on issue but got {len(comments)}'


class CommentOnIssueExample2(CommentOnIssue):

    def __init__(self):
        super().__init__(
            'Add a comment to GitHub issue #2 regarding the roadmap for documentation release: "We are working on it and will update it soon."')

    def validate(self):
        issue = [i for i in self.issues if i.number == 2][0]
        comments = [c for c in issue.get_comments()]
        self.target = comments
        assert len(comments) == 1, f'Expected 1 comment on issue but got {len(comments)}'


class CommentOnIssueExample3(CommentOnIssue):
    def __init__(self):
        super().__init__(
            'Add a comment to the GitHub issue requesting documentation release details. Tell the user that we will do it ASAP.')

    def validate(self):
        comment_found = False
        issues = [i for i in self.issues if i.number in self.doc_issue_nums]
        for issue in issues:
            for _ in issue.get_comments():
                comment_found = True
                break
            if comment_found:
                self.target = issue.get_comments()
                break
        assert comment_found, f'Expected a comment on one of the issues but none found'


class CommentOnIssueExample4(CommentOnIssue):
    def __init__(self):
        super().__init__(
            'Comment on the GitHub issue regarding the security breach found in dependencies. The comment should be that we\'ve added the problem on our roadmap.')

    def validate(self):
        comment_found = False

        issues = [i for i in self.issues if i.number in self.security_issue_nums]
        for issue in issues:
            for _ in issue.get_comments():
                comment_found = True
                break
            if comment_found:
                self.target = issue.get_comments()
                break
        assert comment_found, f'Expected a comment on one of the issues but none found'


class CommentOnIssueExample5(CommentOnIssue):

    def __init__(self):
        super().__init__(
            'Comment on GitHub issue to inquire what deadline do they expect for the roadmap on releasing documentation for the library.')

    def validate(self):
        comment_found = False
        issues = [i for i in self.issues if i.number in self.doc_issue_nums]
        for issue in issues:
            for _ in issue.get_comments():
                comment_found = True
                break
            if comment_found:
                self.target = issue.get_comments()
                break
        assert comment_found, f'Expected a comment on one of the issues but none found'


class CommentOnIssueExample6(CommentOnIssue):

    def __init__(self):
        super().__init__(
            'Comment on GitHub issue regarding documentation request that this is priority for us and will be done in the next quarter')

    def validate(self):
        comment_found = False
        issues = [i for i in self.issues if i.number in self.doc_issue_nums]
        for issue in issues:
            for _ in issue.get_comments():
                comment_found = True
                break
            if comment_found:
                self.target = issue.get_comments()
                break
        assert comment_found, f'Expected a comment on one of the issues but none found'


class CommentOnIssueExample7(CommentOnIssue):
    def __init__(self):
        super().__init__(
            'Add a comment to issue #2 requesting an update on the documentation roadmap by telling them that it will soon be out.')

    def validate(self):
        comment_found = False
        issues = [i for i in self.issues if i.number in self.doc_issue_nums]
        for issue in issues:
            for _ in issue.get_comments():
                comment_found = True
                break
            if comment_found:
                self.target = issue.get_comments()
                break
        assert comment_found, f'Expected a comment on one of the issues but none found'


class CommentOnIssueExample8(CommentOnIssue):
    def __init__(self):
        super().__init__(
            'Add a comment to a GitHub issue about the documentation request saying that it will be resolved as soon as possible.')

    def validate(self):
        comment_found = False
        issues = [i for i in self.issues if i.number in self.doc_issue_nums]
        for issue in issues:
            for _ in issue.get_comments():
                comment_found = True
                break
            if comment_found:
                self.target = issue.get_comments()
                break
        assert comment_found, f'Expected a comment on one of the issues but none found'


class CommentOnIssueExample9(CommentOnIssue):
    def __init__(self):
        super().__init__(
            'Comment on the GitHub issue requesting documentation release information and let them know that we are working on it.')

    def validate(self):
        comment_found = False
        issues = [i for i in self.issues if i.number in self.doc_issue_nums]
        for issue in issues:
            for _ in issue.get_comments():
                comment_found = True
                break
            if comment_found:
                self.target = issue.get_comments()
                break
        assert comment_found, f'Expected a comment on one of the issues but none found'


class CommentOnIssueExample10(CommentOnIssue):
    def __init__(self):
        super().__init__(
            'Answer to the contribution guide issue with a comment that we will add this and thanks for the suggestion.')

    def validate(self):
        comment_found = False
        issues = [i for i in self.issues if i.number in self.contribution_guide]
        for issue in issues:
            for _ in issue.get_comments():
                comment_found = True
                break
            if comment_found:
                self.target = issue.get_comments()
                break
        assert comment_found, f'Expected a comment on one of the issues but none found'


class CommentOnIssueExample11(CommentOnIssue):
    def __init__(self):
        super().__init__(
            'Can you please answer to the outdated library version request, that as of now we cannot update due to compatibility issues.')

    def validate(self):
        comment_found = False
        issues = [i for i in self.issues if i.number in self.dependency]
        for issue in issues:
            for _ in issue.get_comments():
                comment_found = True
                break
            if comment_found:
                self.target = issue.get_comments()
                break
        assert comment_found, f'Expected a comment on one of the issues but none found'


class CommentOnIssueExample12(CommentOnIssue):
    def __init__(self):
        super().__init__(
            'There is an issue on accessibility improvements, please comment that we are working on it and will be fixed soon.')

    def validate(self):
        comment_found = False
        issues = [i for i in self.issues if i.number in self.accessibility]
        for issue in issues:
            for _ in issue.get_comments():
                comment_found = True
                break
            if comment_found:
                self.target = issue.get_comments()
                break
        assert comment_found, f'Expected a comment on one of the issues but none found'


class CommentOnIssueExample13(CommentOnIssue):
    def __init__(self):
        super().__init__(
            'Let know the person who reported the memory leak bug, that it has been fixed and will be released in the next version.')

    def validate(self):
        comment_found = False
        issues = [i for i in self.issues if i.number in self.bug_mem_leak]
        for issue in issues:
            for _ in issue.get_comments():
                comment_found = True
                break
            if comment_found:
                self.target = issue.get_comments()
                break
        assert comment_found, f'Expected a comment on one of the issues but none found'


class CommentOnIssueExample14(CommentOnIssue):
    def __init__(self):
        super().__init__(
            'Comment on the issue regarding the feature request for adding logging support that we already have this feature.')

    def validate(self):
        comment_found = False
        issues = [i for i in self.issues if i.number in self.feature_req_log]
        for issue in issues:
            for _ in issue.get_comments():
                comment_found = True
                break
            if comment_found:
                self.target = issue.get_comments()
                break
        assert comment_found, f'Expected a comment on one of the issues but none found'


class CommentOnIssueExample15(CommentOnIssue):
    def __init__(self):
        super().__init__(
            'Let the person who reported the inconsistency in our naming conventions that is already being worked on and we are introducing style guides next month.')

    def validate(self):
        comment_found = False
        issues = [i for i in self.issues if i.number in self.inconsistent_naming]
        for issue in issues:
            for _ in issue.get_comments():
                comment_found = True
                break
            if comment_found:
                self.target = issue.get_comments()
                break
        assert comment_found, f'Expected a comment on one of the issues but none found'


class CommentOnIssueExample16(CommentOnIssue):
    def __init__(self):
        super().__init__(
            'Please ask on the "Test suite missing for core functionalities" what core functionalities are missing tests and so that we can add them')

    def validate(self):
        comment_found = False
        issues = [i for i in self.issues if i.number in self.test_suite]
        for issue in issues:
            for _ in issue.get_comments():
                comment_found = True
                break
            if comment_found:
                self.target = issue.get_comments()
                break
        assert comment_found, f'Expected a comment on one of the issues but none found'


class CommentOnIssueExample18(CommentOnIssue):
    def __init__(self):
        super().__init__(
            'Please let the person who reported the unexpected crash, that this is very serious and we would need further logs to investigate and fix it.')

    def validate(self):
        comment_found = False
        issues = [i for i in self.issues if i.number in self.bug_crash]
        for issue in issues:
            for _ in issue.get_comments():
                comment_found = True
                break
            if comment_found:
                self.target = issue.get_comments()
                break
        assert comment_found, f'Expected a comment on one of the issues but none found'


class CommentOnIssueExample19(CommentOnIssue):
    def __init__(self):
        super().__init__(
            'Answer to the request for python 3.10 that we are not ready to make this jump as of now but will put it on our roadmap for next year.')

    def validate(self):
        comment_found = False
        issues = [i for i in self.issues if i.number in self.feature_req_py310]
        for issue in issues:
            for _ in issue.get_comments():
                comment_found = True
                break
            if comment_found:
                self.target = issue.get_comments()
                break
        assert comment_found, f'Expected a comment on one of the issues but none found'
