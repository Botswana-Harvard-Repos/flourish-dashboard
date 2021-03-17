from django.conf import settings
from edc_model_wrapper import ModelWrapper

from .child_assent_model_wrapper_mixin import ChildAssentModelWrapperMixin
from .consent_model_wrapper_mixin import ConsentModelWrapperMixin


class ChildDummyConsentModelWrapper(ChildAssentModelWrapperMixin,
                                    ConsentModelWrapperMixin,
                                    ModelWrapper):

    model = 'flourish_child.childdummysubjectconsent'
    next_url_name = settings.DASHBOARD_URL_NAMES.get(
        'child_listboard_url')
    next_url_attrs = ['subject_identifier', 'screening_identifier']
    querystring_attrs = ['subject_identifier', 'screening_identifier']

    @property
    def screening_identifier(self):
        subject_consent = self.subject_consent_cls.objects.get(
            subject_identifier=self.subject_identifier)
        return subject_consent.screening_identifier


    @property
    def assent_options(self):
        """Returns a dictionary of options to get an existing
         child assent model instance.
        """
        options = dict(
            subject_identifier=self.object.subject_identifier)
        return options

    @property
    def consent_options(self):
        """Returns a dictionary of options to get an existing
        consent model instance.
        """
        options = dict(
            subject_identifier=self.subject_identifier,
            version=self.consent_version)
        return options

    @property
    def subject_identifier(self):
        subject_identifier = self.object.subject_identifier.split('-')
        subject_identifier.pop()
        caregiver_subject_identifier = '-'.join(subject_identifier)
        return caregiver_subject_identifier
