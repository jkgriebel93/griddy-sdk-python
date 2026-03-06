from typing import TYPE_CHECKING, Literal, Optional, TypeVar, Union

from pydantic import BaseModel as PydanticBaseModel
from pydantic import ConfigDict, model_serializer
from typing_extensions import TypeAlias, TypeAliasType

UNSET_SENTINEL = "~?~unset~?~sentinel~?~"


class BaseModel(PydanticBaseModel):
    model_config = ConfigDict(
        populate_by_name=True, arbitrary_types_allowed=True, protected_namespaces=()
    )

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(n)
            serialized.pop(n, None)

            is_optional = not f.is_required()
            is_nullable = isinstance(f.default, Unset)
            optional_nullable = is_optional and is_nullable
            is_set = self.__pydantic_fields_set__.intersection({n})  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not is_optional or (optional_nullable and is_set)
            ):
                m[k] = val

        return m


class Unset(BaseModel):
    @model_serializer(mode="plain")
    def serialize_model(self):
        return UNSET_SENTINEL

    def __bool__(self) -> Literal[False]:
        return False


UNSET = Unset()


T = TypeVar("T")
if TYPE_CHECKING:
    Nullable: TypeAlias = Union[T, None]
    OptionalNullable: TypeAlias = Union[Optional[Nullable[T]], Unset]
else:
    Nullable = TypeAliasType("Nullable", Union[T, None], type_params=(T,))
    OptionalNullable = TypeAliasType(
        "OptionalNullable", Union[Optional[Nullable[T]], Unset], type_params=(T,)
    )

UnrecognizedInt: TypeAlias = int
UnrecognizedStr: TypeAlias = str
