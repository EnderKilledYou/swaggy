# coding: utf-8

"""
    NLD2 API

    The <b>NLD2 API</b> is a complete, programmable interface to all National Levee Database functionality. The NLD2 API is a RESTful web service, using standard technologies like HTTP verbs, headers, and status codes.<br/><br/>The <a href=\"/#/\" target=\"_blank\">National Levee Database website</a> is built on this API, and all of its services are available for integration into your application. To get started, we recommend exploring the website to learn about the functionality that is available and then using the OpenAPI specification below to try connecting to the test/hello endpoint.<br/><br/>Currently, you can develop your application with the public API. For more advanced features, you may need an NLD account and specific government clearance, depending on the nature of the data. If you need assistance, please email us at <a href=\"mailto:NLD@usace.army.mil\">NLD@usace.army.mil</a> or call us at <a href=\"tel:18775383387\">1-877-LEVEEUS</a> (1-877-538-3387).  # noqa: E501

    OpenAPI spec version: 3.26.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class EmbankmentSections(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'segment_id': 'float',
        'embankment_type': 'str',
        'project_name': 'str',
        'pump_station_count': 'float',
        'authorization_category_name': 'str',
        'usace_district': 'str',
        'river_system': 'str',
        'embankment_setting': 'str',
        'culvert_count': 'float',
        'non_culvert_closure_count': 'float',
        'protection_type': 'str',
        'embankment_material': 'str',
        'total_length_in_miles': 'float',
        'embankment_length_in_miles': 'float',
        'number_years_of_reliable_data': 'float',
        'past_seepage_performance': 'str',
        'past_sandboil_performance': 'str',
        'has_past_overtop_evaluation': 'bool',
        'breach_cause': 'str',
        'load_range': 'str',
        'duration_of_load_at_breach': 'str',
        'floodwall_type': 'str',
        'floodwall_configuration': 'str',
        'general_foundation': 'str',
        'exposed_wall_height_in_feet': 'float',
        'section_id': 'float',
        'last_edited_user_id': 'str',
        'last_edited_date': 'datetime'
    }

    attribute_map = {
        'segment_id': 'segmentId',
        'embankment_type': 'embankmentType',
        'project_name': 'projectName',
        'pump_station_count': 'pumpStationCount',
        'authorization_category_name': 'authorizationCategoryName',
        'usace_district': 'usaceDistrict',
        'river_system': 'riverSystem',
        'embankment_setting': 'embankmentSetting',
        'culvert_count': 'culvertCount',
        'non_culvert_closure_count': 'nonCulvertClosureCount',
        'protection_type': 'protectionType',
        'embankment_material': 'embankmentMaterial',
        'total_length_in_miles': 'totalLengthInMiles',
        'embankment_length_in_miles': 'embankmentLengthInMiles',
        'number_years_of_reliable_data': 'numberYearsOfReliableData',
        'past_seepage_performance': 'pastSeepagePerformance',
        'past_sandboil_performance': 'pastSandboilPerformance',
        'has_past_overtop_evaluation': 'hasPastOvertopEvaluation',
        'breach_cause': 'breachCause',
        'load_range': 'loadRange',
        'duration_of_load_at_breach': 'durationOfLoadAtBreach',
        'floodwall_type': 'floodwallType',
        'floodwall_configuration': 'floodwallConfiguration',
        'general_foundation': 'generalFoundation',
        'exposed_wall_height_in_feet': 'exposedWallHeightInFeet',
        'section_id': 'sectionId',
        'last_edited_user_id': 'lastEditedUserId',
        'last_edited_date': 'lastEditedDate'
    }

    def __init__(self, segment_id=None, embankment_type=None, project_name=None, pump_station_count=None, authorization_category_name=None, usace_district=None, river_system=None, embankment_setting=None, culvert_count=None, non_culvert_closure_count=None, protection_type=None, embankment_material=None, total_length_in_miles=None, embankment_length_in_miles=None, number_years_of_reliable_data=None, past_seepage_performance=None, past_sandboil_performance=None, has_past_overtop_evaluation=None, breach_cause=None, load_range=None, duration_of_load_at_breach=None, floodwall_type=None, floodwall_configuration=None, general_foundation=None, exposed_wall_height_in_feet=None, section_id=None, last_edited_user_id=None, last_edited_date=None, _configuration=None):  # noqa: E501
        """EmbankmentSections - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._segment_id = None
        self._embankment_type = None
        self._project_name = None
        self._pump_station_count = None
        self._authorization_category_name = None
        self._usace_district = None
        self._river_system = None
        self._embankment_setting = None
        self._culvert_count = None
        self._non_culvert_closure_count = None
        self._protection_type = None
        self._embankment_material = None
        self._total_length_in_miles = None
        self._embankment_length_in_miles = None
        self._number_years_of_reliable_data = None
        self._past_seepage_performance = None
        self._past_sandboil_performance = None
        self._has_past_overtop_evaluation = None
        self._breach_cause = None
        self._load_range = None
        self._duration_of_load_at_breach = None
        self._floodwall_type = None
        self._floodwall_configuration = None
        self._general_foundation = None
        self._exposed_wall_height_in_feet = None
        self._section_id = None
        self._last_edited_user_id = None
        self._last_edited_date = None
        self.discriminator = None

        if segment_id is not None:
            self.segment_id = segment_id
        if embankment_type is not None:
            self.embankment_type = embankment_type
        if project_name is not None:
            self.project_name = project_name
        if pump_station_count is not None:
            self.pump_station_count = pump_station_count
        if authorization_category_name is not None:
            self.authorization_category_name = authorization_category_name
        if usace_district is not None:
            self.usace_district = usace_district
        if river_system is not None:
            self.river_system = river_system
        if embankment_setting is not None:
            self.embankment_setting = embankment_setting
        if culvert_count is not None:
            self.culvert_count = culvert_count
        if non_culvert_closure_count is not None:
            self.non_culvert_closure_count = non_culvert_closure_count
        if protection_type is not None:
            self.protection_type = protection_type
        if embankment_material is not None:
            self.embankment_material = embankment_material
        if total_length_in_miles is not None:
            self.total_length_in_miles = total_length_in_miles
        if embankment_length_in_miles is not None:
            self.embankment_length_in_miles = embankment_length_in_miles
        if number_years_of_reliable_data is not None:
            self.number_years_of_reliable_data = number_years_of_reliable_data
        if past_seepage_performance is not None:
            self.past_seepage_performance = past_seepage_performance
        if past_sandboil_performance is not None:
            self.past_sandboil_performance = past_sandboil_performance
        if has_past_overtop_evaluation is not None:
            self.has_past_overtop_evaluation = has_past_overtop_evaluation
        if breach_cause is not None:
            self.breach_cause = breach_cause
        if load_range is not None:
            self.load_range = load_range
        if duration_of_load_at_breach is not None:
            self.duration_of_load_at_breach = duration_of_load_at_breach
        if floodwall_type is not None:
            self.floodwall_type = floodwall_type
        if floodwall_configuration is not None:
            self.floodwall_configuration = floodwall_configuration
        if general_foundation is not None:
            self.general_foundation = general_foundation
        if exposed_wall_height_in_feet is not None:
            self.exposed_wall_height_in_feet = exposed_wall_height_in_feet
        if section_id is not None:
            self.section_id = section_id
        if last_edited_user_id is not None:
            self.last_edited_user_id = last_edited_user_id
        if last_edited_date is not None:
            self.last_edited_date = last_edited_date

    @property
    def segment_id(self):
        """Gets the segment_id of this EmbankmentSections.  # noqa: E501


        :return: The segment_id of this EmbankmentSections.  # noqa: E501
        :rtype: float
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id):
        """Sets the segment_id of this EmbankmentSections.


        :param segment_id: The segment_id of this EmbankmentSections.  # noqa: E501
        :type: float
        """

        self._segment_id = segment_id

    @property
    def embankment_type(self):
        """Gets the embankment_type of this EmbankmentSections.  # noqa: E501


        :return: The embankment_type of this EmbankmentSections.  # noqa: E501
        :rtype: str
        """
        return self._embankment_type

    @embankment_type.setter
    def embankment_type(self, embankment_type):
        """Sets the embankment_type of this EmbankmentSections.


        :param embankment_type: The embankment_type of this EmbankmentSections.  # noqa: E501
        :type: str
        """

        self._embankment_type = embankment_type

    @property
    def project_name(self):
        """Gets the project_name of this EmbankmentSections.  # noqa: E501


        :return: The project_name of this EmbankmentSections.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this EmbankmentSections.


        :param project_name: The project_name of this EmbankmentSections.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def pump_station_count(self):
        """Gets the pump_station_count of this EmbankmentSections.  # noqa: E501


        :return: The pump_station_count of this EmbankmentSections.  # noqa: E501
        :rtype: float
        """
        return self._pump_station_count

    @pump_station_count.setter
    def pump_station_count(self, pump_station_count):
        """Sets the pump_station_count of this EmbankmentSections.


        :param pump_station_count: The pump_station_count of this EmbankmentSections.  # noqa: E501
        :type: float
        """

        self._pump_station_count = pump_station_count

    @property
    def authorization_category_name(self):
        """Gets the authorization_category_name of this EmbankmentSections.  # noqa: E501


        :return: The authorization_category_name of this EmbankmentSections.  # noqa: E501
        :rtype: str
        """
        return self._authorization_category_name

    @authorization_category_name.setter
    def authorization_category_name(self, authorization_category_name):
        """Sets the authorization_category_name of this EmbankmentSections.


        :param authorization_category_name: The authorization_category_name of this EmbankmentSections.  # noqa: E501
        :type: str
        """

        self._authorization_category_name = authorization_category_name

    @property
    def usace_district(self):
        """Gets the usace_district of this EmbankmentSections.  # noqa: E501


        :return: The usace_district of this EmbankmentSections.  # noqa: E501
        :rtype: str
        """
        return self._usace_district

    @usace_district.setter
    def usace_district(self, usace_district):
        """Sets the usace_district of this EmbankmentSections.


        :param usace_district: The usace_district of this EmbankmentSections.  # noqa: E501
        :type: str
        """

        self._usace_district = usace_district

    @property
    def river_system(self):
        """Gets the river_system of this EmbankmentSections.  # noqa: E501


        :return: The river_system of this EmbankmentSections.  # noqa: E501
        :rtype: str
        """
        return self._river_system

    @river_system.setter
    def river_system(self, river_system):
        """Sets the river_system of this EmbankmentSections.


        :param river_system: The river_system of this EmbankmentSections.  # noqa: E501
        :type: str
        """

        self._river_system = river_system

    @property
    def embankment_setting(self):
        """Gets the embankment_setting of this EmbankmentSections.  # noqa: E501


        :return: The embankment_setting of this EmbankmentSections.  # noqa: E501
        :rtype: str
        """
        return self._embankment_setting

    @embankment_setting.setter
    def embankment_setting(self, embankment_setting):
        """Sets the embankment_setting of this EmbankmentSections.


        :param embankment_setting: The embankment_setting of this EmbankmentSections.  # noqa: E501
        :type: str
        """

        self._embankment_setting = embankment_setting

    @property
    def culvert_count(self):
        """Gets the culvert_count of this EmbankmentSections.  # noqa: E501


        :return: The culvert_count of this EmbankmentSections.  # noqa: E501
        :rtype: float
        """
        return self._culvert_count

    @culvert_count.setter
    def culvert_count(self, culvert_count):
        """Sets the culvert_count of this EmbankmentSections.


        :param culvert_count: The culvert_count of this EmbankmentSections.  # noqa: E501
        :type: float
        """

        self._culvert_count = culvert_count

    @property
    def non_culvert_closure_count(self):
        """Gets the non_culvert_closure_count of this EmbankmentSections.  # noqa: E501


        :return: The non_culvert_closure_count of this EmbankmentSections.  # noqa: E501
        :rtype: float
        """
        return self._non_culvert_closure_count

    @non_culvert_closure_count.setter
    def non_culvert_closure_count(self, non_culvert_closure_count):
        """Sets the non_culvert_closure_count of this EmbankmentSections.


        :param non_culvert_closure_count: The non_culvert_closure_count of this EmbankmentSections.  # noqa: E501
        :type: float
        """

        self._non_culvert_closure_count = non_culvert_closure_count

    @property
    def protection_type(self):
        """Gets the protection_type of this EmbankmentSections.  # noqa: E501


        :return: The protection_type of this EmbankmentSections.  # noqa: E501
        :rtype: str
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type):
        """Sets the protection_type of this EmbankmentSections.


        :param protection_type: The protection_type of this EmbankmentSections.  # noqa: E501
        :type: str
        """

        self._protection_type = protection_type

    @property
    def embankment_material(self):
        """Gets the embankment_material of this EmbankmentSections.  # noqa: E501


        :return: The embankment_material of this EmbankmentSections.  # noqa: E501
        :rtype: str
        """
        return self._embankment_material

    @embankment_material.setter
    def embankment_material(self, embankment_material):
        """Sets the embankment_material of this EmbankmentSections.


        :param embankment_material: The embankment_material of this EmbankmentSections.  # noqa: E501
        :type: str
        """

        self._embankment_material = embankment_material

    @property
    def total_length_in_miles(self):
        """Gets the total_length_in_miles of this EmbankmentSections.  # noqa: E501


        :return: The total_length_in_miles of this EmbankmentSections.  # noqa: E501
        :rtype: float
        """
        return self._total_length_in_miles

    @total_length_in_miles.setter
    def total_length_in_miles(self, total_length_in_miles):
        """Sets the total_length_in_miles of this EmbankmentSections.


        :param total_length_in_miles: The total_length_in_miles of this EmbankmentSections.  # noqa: E501
        :type: float
        """

        self._total_length_in_miles = total_length_in_miles

    @property
    def embankment_length_in_miles(self):
        """Gets the embankment_length_in_miles of this EmbankmentSections.  # noqa: E501


        :return: The embankment_length_in_miles of this EmbankmentSections.  # noqa: E501
        :rtype: float
        """
        return self._embankment_length_in_miles

    @embankment_length_in_miles.setter
    def embankment_length_in_miles(self, embankment_length_in_miles):
        """Sets the embankment_length_in_miles of this EmbankmentSections.


        :param embankment_length_in_miles: The embankment_length_in_miles of this EmbankmentSections.  # noqa: E501
        :type: float
        """

        self._embankment_length_in_miles = embankment_length_in_miles

    @property
    def number_years_of_reliable_data(self):
        """Gets the number_years_of_reliable_data of this EmbankmentSections.  # noqa: E501


        :return: The number_years_of_reliable_data of this EmbankmentSections.  # noqa: E501
        :rtype: float
        """
        return self._number_years_of_reliable_data

    @number_years_of_reliable_data.setter
    def number_years_of_reliable_data(self, number_years_of_reliable_data):
        """Sets the number_years_of_reliable_data of this EmbankmentSections.


        :param number_years_of_reliable_data: The number_years_of_reliable_data of this EmbankmentSections.  # noqa: E501
        :type: float
        """

        self._number_years_of_reliable_data = number_years_of_reliable_data

    @property
    def past_seepage_performance(self):
        """Gets the past_seepage_performance of this EmbankmentSections.  # noqa: E501


        :return: The past_seepage_performance of this EmbankmentSections.  # noqa: E501
        :rtype: str
        """
        return self._past_seepage_performance

    @past_seepage_performance.setter
    def past_seepage_performance(self, past_seepage_performance):
        """Sets the past_seepage_performance of this EmbankmentSections.


        :param past_seepage_performance: The past_seepage_performance of this EmbankmentSections.  # noqa: E501
        :type: str
        """

        self._past_seepage_performance = past_seepage_performance

    @property
    def past_sandboil_performance(self):
        """Gets the past_sandboil_performance of this EmbankmentSections.  # noqa: E501


        :return: The past_sandboil_performance of this EmbankmentSections.  # noqa: E501
        :rtype: str
        """
        return self._past_sandboil_performance

    @past_sandboil_performance.setter
    def past_sandboil_performance(self, past_sandboil_performance):
        """Sets the past_sandboil_performance of this EmbankmentSections.


        :param past_sandboil_performance: The past_sandboil_performance of this EmbankmentSections.  # noqa: E501
        :type: str
        """

        self._past_sandboil_performance = past_sandboil_performance

    @property
    def has_past_overtop_evaluation(self):
        """Gets the has_past_overtop_evaluation of this EmbankmentSections.  # noqa: E501


        :return: The has_past_overtop_evaluation of this EmbankmentSections.  # noqa: E501
        :rtype: bool
        """
        return self._has_past_overtop_evaluation

    @has_past_overtop_evaluation.setter
    def has_past_overtop_evaluation(self, has_past_overtop_evaluation):
        """Sets the has_past_overtop_evaluation of this EmbankmentSections.


        :param has_past_overtop_evaluation: The has_past_overtop_evaluation of this EmbankmentSections.  # noqa: E501
        :type: bool
        """

        self._has_past_overtop_evaluation = has_past_overtop_evaluation

    @property
    def breach_cause(self):
        """Gets the breach_cause of this EmbankmentSections.  # noqa: E501


        :return: The breach_cause of this EmbankmentSections.  # noqa: E501
        :rtype: str
        """
        return self._breach_cause

    @breach_cause.setter
    def breach_cause(self, breach_cause):
        """Sets the breach_cause of this EmbankmentSections.


        :param breach_cause: The breach_cause of this EmbankmentSections.  # noqa: E501
        :type: str
        """

        self._breach_cause = breach_cause

    @property
    def load_range(self):
        """Gets the load_range of this EmbankmentSections.  # noqa: E501


        :return: The load_range of this EmbankmentSections.  # noqa: E501
        :rtype: str
        """
        return self._load_range

    @load_range.setter
    def load_range(self, load_range):
        """Sets the load_range of this EmbankmentSections.


        :param load_range: The load_range of this EmbankmentSections.  # noqa: E501
        :type: str
        """

        self._load_range = load_range

    @property
    def duration_of_load_at_breach(self):
        """Gets the duration_of_load_at_breach of this EmbankmentSections.  # noqa: E501


        :return: The duration_of_load_at_breach of this EmbankmentSections.  # noqa: E501
        :rtype: str
        """
        return self._duration_of_load_at_breach

    @duration_of_load_at_breach.setter
    def duration_of_load_at_breach(self, duration_of_load_at_breach):
        """Sets the duration_of_load_at_breach of this EmbankmentSections.


        :param duration_of_load_at_breach: The duration_of_load_at_breach of this EmbankmentSections.  # noqa: E501
        :type: str
        """

        self._duration_of_load_at_breach = duration_of_load_at_breach

    @property
    def floodwall_type(self):
        """Gets the floodwall_type of this EmbankmentSections.  # noqa: E501


        :return: The floodwall_type of this EmbankmentSections.  # noqa: E501
        :rtype: str
        """
        return self._floodwall_type

    @floodwall_type.setter
    def floodwall_type(self, floodwall_type):
        """Sets the floodwall_type of this EmbankmentSections.


        :param floodwall_type: The floodwall_type of this EmbankmentSections.  # noqa: E501
        :type: str
        """

        self._floodwall_type = floodwall_type

    @property
    def floodwall_configuration(self):
        """Gets the floodwall_configuration of this EmbankmentSections.  # noqa: E501


        :return: The floodwall_configuration of this EmbankmentSections.  # noqa: E501
        :rtype: str
        """
        return self._floodwall_configuration

    @floodwall_configuration.setter
    def floodwall_configuration(self, floodwall_configuration):
        """Sets the floodwall_configuration of this EmbankmentSections.


        :param floodwall_configuration: The floodwall_configuration of this EmbankmentSections.  # noqa: E501
        :type: str
        """

        self._floodwall_configuration = floodwall_configuration

    @property
    def general_foundation(self):
        """Gets the general_foundation of this EmbankmentSections.  # noqa: E501


        :return: The general_foundation of this EmbankmentSections.  # noqa: E501
        :rtype: str
        """
        return self._general_foundation

    @general_foundation.setter
    def general_foundation(self, general_foundation):
        """Sets the general_foundation of this EmbankmentSections.


        :param general_foundation: The general_foundation of this EmbankmentSections.  # noqa: E501
        :type: str
        """

        self._general_foundation = general_foundation

    @property
    def exposed_wall_height_in_feet(self):
        """Gets the exposed_wall_height_in_feet of this EmbankmentSections.  # noqa: E501


        :return: The exposed_wall_height_in_feet of this EmbankmentSections.  # noqa: E501
        :rtype: float
        """
        return self._exposed_wall_height_in_feet

    @exposed_wall_height_in_feet.setter
    def exposed_wall_height_in_feet(self, exposed_wall_height_in_feet):
        """Sets the exposed_wall_height_in_feet of this EmbankmentSections.


        :param exposed_wall_height_in_feet: The exposed_wall_height_in_feet of this EmbankmentSections.  # noqa: E501
        :type: float
        """

        self._exposed_wall_height_in_feet = exposed_wall_height_in_feet

    @property
    def section_id(self):
        """Gets the section_id of this EmbankmentSections.  # noqa: E501


        :return: The section_id of this EmbankmentSections.  # noqa: E501
        :rtype: float
        """
        return self._section_id

    @section_id.setter
    def section_id(self, section_id):
        """Sets the section_id of this EmbankmentSections.


        :param section_id: The section_id of this EmbankmentSections.  # noqa: E501
        :type: float
        """

        self._section_id = section_id

    @property
    def last_edited_user_id(self):
        """Gets the last_edited_user_id of this EmbankmentSections.  # noqa: E501


        :return: The last_edited_user_id of this EmbankmentSections.  # noqa: E501
        :rtype: str
        """
        return self._last_edited_user_id

    @last_edited_user_id.setter
    def last_edited_user_id(self, last_edited_user_id):
        """Sets the last_edited_user_id of this EmbankmentSections.


        :param last_edited_user_id: The last_edited_user_id of this EmbankmentSections.  # noqa: E501
        :type: str
        """

        self._last_edited_user_id = last_edited_user_id

    @property
    def last_edited_date(self):
        """Gets the last_edited_date of this EmbankmentSections.  # noqa: E501


        :return: The last_edited_date of this EmbankmentSections.  # noqa: E501
        :rtype: datetime
        """
        return self._last_edited_date

    @last_edited_date.setter
    def last_edited_date(self, last_edited_date):
        """Sets the last_edited_date of this EmbankmentSections.


        :param last_edited_date: The last_edited_date of this EmbankmentSections.  # noqa: E501
        :type: datetime
        """

        self._last_edited_date = last_edited_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(EmbankmentSections, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EmbankmentSections):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EmbankmentSections):
            return True

        return self.to_dict() != other.to_dict()
