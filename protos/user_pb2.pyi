from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("first_name", "last_name", "email", "password", "country_code", "phone", "user_id")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    email: str
    password: str
    country_code: str
    phone: str
    user_id: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., country_code: _Optional[str] = ..., phone: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class UserDetail(_message.Message):
    __slots__ = ("profile_picture_path",)
    PROFILE_PICTURE_PATH_FIELD_NUMBER: _ClassVar[int]
    profile_picture_path: str
    def __init__(self, profile_picture_path: _Optional[str] = ...) -> None: ...

class ViewProfileResponse(_message.Message):
    __slots__ = ("user", "user_detail")
    USER_FIELD_NUMBER: _ClassVar[int]
    USER_DETAIL_FIELD_NUMBER: _ClassVar[int]
    user: User
    user_detail: UserDetail
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., user_detail: _Optional[_Union[UserDetail, _Mapping]] = ...) -> None: ...

class SocialUser(_message.Message):
    __slots__ = ("first_name", "last_name", "email", "password", "country_code", "phone", "platform", "code")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    email: str
    password: str
    country_code: str
    phone: str
    platform: str
    code: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., country_code: _Optional[str] = ..., phone: _Optional[str] = ..., platform: _Optional[str] = ..., code: _Optional[str] = ...) -> None: ...

class Organization(_message.Message):
    __slots__ = ("name", "domain", "time_zone", "country", "id", "created_by", "status")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    name: str
    domain: str
    time_zone: str
    country: str
    id: str
    created_by: str
    status: str
    def __init__(self, name: _Optional[str] = ..., domain: _Optional[str] = ..., time_zone: _Optional[str] = ..., country: _Optional[str] = ..., id: _Optional[str] = ..., created_by: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class OrganizationDetails(_message.Message):
    __slots__ = ("profile_picture", "address", "state", "city", "postal_code", "website_url", "social_url", "org_id")
    PROFILE_PICTURE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_URL_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_URL_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    profile_picture: str
    address: str
    state: str
    city: str
    postal_code: str
    website_url: str
    social_url: _struct_pb2.Struct
    org_id: str
    def __init__(self, profile_picture: _Optional[str] = ..., address: _Optional[str] = ..., state: _Optional[str] = ..., city: _Optional[str] = ..., postal_code: _Optional[str] = ..., website_url: _Optional[str] = ..., social_url: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., org_id: _Optional[str] = ...) -> None: ...

class CreateOrganization(_message.Message):
    __slots__ = ("name", "domain", "time_zone", "country")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    name: str
    domain: str
    time_zone: str
    country: str
    def __init__(self, name: _Optional[str] = ..., domain: _Optional[str] = ..., time_zone: _Optional[str] = ..., country: _Optional[str] = ...) -> None: ...

class UpdateOrganization(_message.Message):
    __slots__ = ("name", "domain", "time_zone")
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    name: str
    domain: str
    time_zone: str
    def __init__(self, name: _Optional[str] = ..., domain: _Optional[str] = ..., time_zone: _Optional[str] = ...) -> None: ...

class UpdateOrganizationDetails(_message.Message):
    __slots__ = ("profile_picture", "address", "state", "city", "postal_code", "website_url", "social_url")
    class SocialUrlEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PROFILE_PICTURE_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_URL_FIELD_NUMBER: _ClassVar[int]
    SOCIAL_URL_FIELD_NUMBER: _ClassVar[int]
    profile_picture: bytes
    address: str
    state: str
    city: str
    postal_code: str
    website_url: str
    social_url: _containers.ScalarMap[str, str]
    def __init__(self, profile_picture: _Optional[bytes] = ..., address: _Optional[str] = ..., state: _Optional[str] = ..., city: _Optional[str] = ..., postal_code: _Optional[str] = ..., website_url: _Optional[str] = ..., social_url: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ViewOrganization(_message.Message):
    __slots__ = ("organization", "organization_details")
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    organization: Organization
    organization_details: OrganizationDetails
    def __init__(self, organization: _Optional[_Union[Organization, _Mapping]] = ..., organization_details: _Optional[_Union[OrganizationDetails, _Mapping]] = ...) -> None: ...

class CreateOrganizationRequest(_message.Message):
    __slots__ = ("organization",)
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    organization: CreateOrganization
    def __init__(self, organization: _Optional[_Union[CreateOrganization, _Mapping]] = ...) -> None: ...

class CreateOrganizationResponse(_message.Message):
    __slots__ = ("org_id", "message")
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    message: str
    def __init__(self, org_id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class UpdateOrganizationRequest(_message.Message):
    __slots__ = ("organization", "organization_details")
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    organization: UpdateOrganization
    organization_details: UpdateOrganizationDetails
    def __init__(self, organization: _Optional[_Union[UpdateOrganization, _Mapping]] = ..., organization_details: _Optional[_Union[UpdateOrganizationDetails, _Mapping]] = ...) -> None: ...

class ViewOrganizationRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ViewOrganizationResponse(_message.Message):
    __slots__ = ("view_organization",)
    VIEW_ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    view_organization: _containers.RepeatedCompositeFieldContainer[ViewOrganization]
    def __init__(self, view_organization: _Optional[_Iterable[_Union[ViewOrganization, _Mapping]]] = ...) -> None: ...

class DeleteOrganizationRequest(_message.Message):
    __slots__ = ("name", "password")
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    name: str
    password: str
    def __init__(self, name: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class UsersResponse(_message.Message):
    __slots__ = ("message", "user_id")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    message: str
    user_id: str
    def __init__(self, message: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class MessageResponse(_message.Message):
    __slots__ = ("message",)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class UpdateProfileRequest(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class UpdateEmailRequest(_message.Message):
    __slots__ = ("new_email",)
    NEW_EMAIL_FIELD_NUMBER: _ClassVar[int]
    new_email: str
    def __init__(self, new_email: _Optional[str] = ...) -> None: ...

class UpdatePasswordRequest(_message.Message):
    __slots__ = ("new_password", "current_password")
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    new_password: str
    current_password: str
    def __init__(self, new_password: _Optional[str] = ..., current_password: _Optional[str] = ...) -> None: ...

class DeleteUserRequest(_message.Message):
    __slots__ = ("password",)
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    password: str
    def __init__(self, password: _Optional[str] = ...) -> None: ...

class ChangeProfilePictureRequest(_message.Message):
    __slots__ = ("picture_data",)
    PICTURE_DATA_FIELD_NUMBER: _ClassVar[int]
    picture_data: bytes
    def __init__(self, picture_data: _Optional[bytes] = ...) -> None: ...

class ActionResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class VerifyInvitationReq(_message.Message):
    __slots__ = ("token", "first_name", "last_name", "password", "country_code", "phone")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    token: str
    first_name: str
    last_name: str
    password: str
    country_code: str
    phone: str
    def __init__(self, token: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., password: _Optional[str] = ..., country_code: _Optional[str] = ..., phone: _Optional[str] = ...) -> None: ...

class VerifyInvitationRes(_message.Message):
    __slots__ = ("invitation", "message", "domain")
    INVITATION_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    invitation: InvitationResponse
    message: str
    domain: str
    def __init__(self, invitation: _Optional[_Union[InvitationResponse, _Mapping]] = ..., message: _Optional[str] = ..., domain: _Optional[str] = ...) -> None: ...

class SignInReq(_message.Message):
    __slots__ = ("email", "password")
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    email: str
    password: str
    def __init__(self, email: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class CreateInvitationRequest(_message.Message):
    __slots__ = ("invitee_email_ids",)
    INVITEE_EMAIL_IDS_FIELD_NUMBER: _ClassVar[int]
    invitee_email_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, invitee_email_ids: _Optional[_Iterable[str]] = ...) -> None: ...

class InvitationResponse(_message.Message):
    __slots__ = ("id", "org_id", "invitee_email_id", "status", "created_by")
    ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    INVITEE_EMAIL_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATED_BY_FIELD_NUMBER: _ClassVar[int]
    id: str
    org_id: str
    invitee_email_id: str
    status: str
    created_by: str
    def __init__(self, id: _Optional[str] = ..., org_id: _Optional[str] = ..., invitee_email_id: _Optional[str] = ..., status: _Optional[str] = ..., created_by: _Optional[str] = ...) -> None: ...

class DisplayInvitationResponse(_message.Message):
    __slots__ = ("invitation_list",)
    INVITATION_LIST_FIELD_NUMBER: _ClassVar[int]
    invitation_list: _containers.RepeatedCompositeFieldContainer[InvitationResponse]
    def __init__(self, invitation_list: _Optional[_Iterable[_Union[InvitationResponse, _Mapping]]] = ...) -> None: ...

class DeleteInvitationRequest(_message.Message):
    __slots__ = ("invitee_email_id",)
    INVITEE_EMAIL_ID_FIELD_NUMBER: _ClassVar[int]
    invitee_email_id: str
    def __init__(self, invitee_email_id: _Optional[str] = ...) -> None: ...

class DisplayInvitationRequest(_message.Message):
    __slots__ = ("org_id",)
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class DisplayUser(_message.Message):
    __slots__ = ("user_id", "org_id", "role_name", "first_name", "last_name", "email_id", "status")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    role_name: str
    first_name: str
    last_name: str
    email_id: str
    status: str
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., role_name: _Optional[str] = ..., first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email_id: _Optional[str] = ..., status: _Optional[str] = ...) -> None: ...

class DisplayUserRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AssignServiceRequest(_message.Message):
    __slots__ = ("user_id", "service_id", "role_name")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    service_id: str
    role_name: str
    def __init__(self, user_id: _Optional[str] = ..., service_id: _Optional[str] = ..., role_name: _Optional[str] = ...) -> None: ...

class DisplayUserResponse(_message.Message):
    __slots__ = ("display_user",)
    DISPLAY_USER_FIELD_NUMBER: _ClassVar[int]
    display_user: _containers.RepeatedCompositeFieldContainer[DisplayUser]
    def __init__(self, display_user: _Optional[_Iterable[_Union[DisplayUser, _Mapping]]] = ...) -> None: ...

class RemoveUserRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class RemoveServiceRequest(_message.Message):
    __slots__ = ("service_id", "user_id")
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    service_id: str
    user_id: str
    def __init__(self, service_id: _Optional[str] = ..., user_id: _Optional[str] = ...) -> None: ...

class UpdateOrganizationRoleRequest(_message.Message):
    __slots__ = ("user_id", "role_name")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    role_name: str
    def __init__(self, user_id: _Optional[str] = ..., role_name: _Optional[str] = ...) -> None: ...

class UpdateServiceRoleRequest(_message.Message):
    __slots__ = ("user_id", "role_name", "service_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ROLE_NAME_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    role_name: str
    service_id: str
    def __init__(self, user_id: _Optional[str] = ..., role_name: _Optional[str] = ..., service_id: _Optional[str] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetPasswordReq(_message.Message):
    __slots__ = ("token", "new_password", "confirm_password")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    token: str
    new_password: str
    confirm_password: str
    def __init__(self, token: _Optional[str] = ..., new_password: _Optional[str] = ..., confirm_password: _Optional[str] = ...) -> None: ...

class ChangePasswordReq(_message.Message):
    __slots__ = ("current_password", "new_password", "confirm_password")
    CURRENT_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    NEW_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    current_password: str
    new_password: str
    confirm_password: str
    def __init__(self, current_password: _Optional[str] = ..., new_password: _Optional[str] = ..., confirm_password: _Optional[str] = ...) -> None: ...

class VerifyUserRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class ForgotPasswordReq(_message.Message):
    __slots__ = ("email",)
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class VerifyEmailRequest(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class SignupUser(_message.Message):
    __slots__ = ("first_name", "last_name", "email", "password", "country_code", "phone", "confirm_password")
    FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
    LAST_NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    CONFIRM_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    first_name: str
    last_name: str
    email: str
    password: str
    country_code: str
    phone: str
    confirm_password: str
    def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., email: _Optional[str] = ..., password: _Optional[str] = ..., country_code: _Optional[str] = ..., phone: _Optional[str] = ..., confirm_password: _Optional[str] = ...) -> None: ...

class EmptyRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ServicesResponse(_message.Message):
    __slots__ = ("services",)
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    services: _containers.RepeatedCompositeFieldContainer[Service]
    def __init__(self, services: _Optional[_Iterable[_Union[Service, _Mapping]]] = ...) -> None: ...

class Service(_message.Message):
    __slots__ = ("service_id", "service_name", "icon_url", "short_description", "features")
    SERVICE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_URL_FIELD_NUMBER: _ClassVar[int]
    SHORT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    service_id: str
    service_name: str
    icon_url: str
    short_description: str
    features: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, service_id: _Optional[str] = ..., service_name: _Optional[str] = ..., icon_url: _Optional[str] = ..., short_description: _Optional[str] = ..., features: _Optional[_Iterable[str]] = ...) -> None: ...
