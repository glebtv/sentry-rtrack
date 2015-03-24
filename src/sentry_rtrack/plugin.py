"""
sentry_rtrack.plugin
~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2012 by the Sentry Team, see AUTHORS for more details.
:copyright: (c) 2015 RocketScience, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from django import forms
from sentry.plugins.bases.issue import IssuePlugin
from django.utils.translation import ugettext_lazy as _
import json
import requests
import sentry_rtrack

class RtrackOptionsForm(forms.Form):
    rtrack_token = forms.CharField(
        label=_('API Token'),
        widget=forms.TextInput(attrs={'placeholder': ''}),
        help_text=_('Enter your project API token.'),
        required=True)
    rtrack_project = forms.CharField(
        label=_('Project Name'),
        widget=forms.TextInput(attrs={'placeholder': 'e.g. rtrack'}),
        help_text=_('Enter your project name.'),
        required=True)

class RtrackPlugin(IssuePlugin):
    author = 'rocketscience.pro'
    author_url = 'https://github.com/glebtv/sentry-rtrack'
    version = sentry_rtrack.VERSION
    description = "Integrate Rtrack issues by linking a repository to a project"
    resource_links = [
        ('Bug Tracker', 'https://github.com/glebtv/sentry-rtrack/issues'),
        ('Source', 'https://github.com/glebtv/sentry-rtrack'),
    ]

    slug = 'rtrack'
    title = _('Rtrack')
    conf_title = title
    conf_key = 'rtrack'
    project_conf_form = RtrackOptionsForm

    def is_configured(self, request, project, **kwargs):
        return bool(self.get_option('rtrack_project', project))

    def get_new_issue_title(self, **kwargs):
        return 'Create RT Issue'

    def create_issue(self, request, group, form_data, **kwargs):
        project = self.get_option('rtrack_project', group.project)
        token = self.get_option('rtrack_token', group.project)

        payload = {'title': form_data['title'], 'description': form_data['description'], 'project': project, 'token': token}
        headers = {'content-type': 'application/json'}
        r = requests.post("http://rtrack.ru/webhooks/sentry", data=json.dumps(payload), headers=headers)
        return r.json()['intid']



    def get_issue_label(self, group, issue_id, **kwargs):
        return 'GL-%s' % issue_id

    def get_issue_url(self, group, issue_id, **kwargs):
        project = self.get_option('rtrack_project', group.project)

        return 'http://rtrack.ru/%s/issues/%s' % (project, issue_id)
