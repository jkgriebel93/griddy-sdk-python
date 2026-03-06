from dataclasses import dataclass
from typing import Optional, Type, TypeVar, Union

from pydantic.fields import FieldInfo

T = TypeVar("T")


@dataclass
class SecurityMetadata:
    """Metadata describing a security field (API key, OAuth2, HTTP auth, etc.)."""

    option: bool = False
    scheme: bool = False
    scheme_type: Optional[str] = None
    sub_type: Optional[str] = None
    field_name: Optional[str] = None

    def get_field_name(self, default: str) -> str:
        """Return the field name, falling back to default if not set."""
        return self.field_name or default


@dataclass
class ParamMetadata:
    """Base metadata for request parameter serialization."""

    serialization: Optional[str] = None
    style: str = "simple"
    explode: bool = False


@dataclass
class PathParamMetadata(ParamMetadata):
    """Metadata for URL path parameters."""

    pass


@dataclass
class QueryParamMetadata(ParamMetadata):
    """Metadata for URL query parameters."""

    style: str = "form"
    explode: bool = True


@dataclass
class HeaderMetadata(ParamMetadata):
    """Metadata for HTTP header parameters."""

    pass


@dataclass
class RequestMetadata:
    """Metadata for request body media type."""

    media_type: str = "application/octet-stream"


@dataclass
class MultipartFormMetadata:
    """Metadata for multipart form fields."""

    file: bool = False
    content: bool = False
    json: bool = False


@dataclass
class FormMetadata:
    """Metadata for URL-encoded form fields."""

    json: bool = False
    style: str = "form"
    explode: bool = True


class FieldMetadata:
    """Aggregates all parameter metadata types for a single Pydantic field."""

    security: Optional[SecurityMetadata] = None
    path: Optional[PathParamMetadata] = None
    query: Optional[QueryParamMetadata] = None
    header: Optional[HeaderMetadata] = None
    request: Optional[RequestMetadata] = None
    form: Optional[FormMetadata] = None
    multipart: Optional[MultipartFormMetadata] = None

    def __init__(
        self,
        security: Optional[SecurityMetadata] = None,
        path: Optional[Union[PathParamMetadata, bool]] = None,
        query: Optional[Union[QueryParamMetadata, bool]] = None,
        header: Optional[Union[HeaderMetadata, bool]] = None,
        request: Optional[Union[RequestMetadata, bool]] = None,
        form: Optional[Union[FormMetadata, bool]] = None,
        multipart: Optional[Union[MultipartFormMetadata, bool]] = None,
    ) -> None:
        """Initialize field metadata, converting bool shortcuts to default instances."""
        self.security = security
        self.path = PathParamMetadata() if isinstance(path, bool) else path
        self.query = QueryParamMetadata() if isinstance(query, bool) else query
        self.header = HeaderMetadata() if isinstance(header, bool) else header
        self.request = RequestMetadata() if isinstance(request, bool) else request
        self.form = FormMetadata() if isinstance(form, bool) else form
        self.multipart = (
            MultipartFormMetadata() if isinstance(multipart, bool) else multipart
        )


def find_field_metadata(field_info: FieldInfo, metadata_type: Type[T]) -> Optional[T]:
    """Find metadata of the given type within a field's FieldMetadata annotation."""
    metadata = find_metadata(field_info, FieldMetadata)
    if not metadata:
        return None

    fields = metadata.__dict__

    for field in fields:
        if isinstance(fields[field], metadata_type):
            return fields[field]

    return None


def find_metadata(field_info: FieldInfo, metadata_type: Type[T]) -> Optional[T]:
    """Find the first metadata annotation of the given type on a field."""
    metadata = field_info.metadata
    if not metadata:
        return None

    for md in metadata:
        if isinstance(md, metadata_type):
            return md

    return None
