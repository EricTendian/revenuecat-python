from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.product_object import ProductObject
from ..models.product_type import ProductType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.app import App
    from ..models.one_time_product_type_0 import OneTimeProductType0
    from ..models.subscription_product_type_0 import SubscriptionProductType0


T = TypeVar("T", bound="Product")


@_attrs_define
class Product:
    """
    Attributes:
        object_ (ProductObject): String representing the object's type. Objects of the same type share the same value.
            Always has the value `list`.
        id (str): The id of the product Example: prod1a2b3c4d5e.
        store_identifier (str): The store product identifier Example: rc_1w_199.
        type_ (ProductType):
        created_at (int): The date when the product was created in ms since epoch Example: 1658399423658.
        app_id (str): The id of the app Example: app1a2b3c4.
        display_name (None | str): The display name of the product Example: Premium Monthly 2023.
        subscription (None | SubscriptionProductType0 | Unset):
        one_time (None | OneTimeProductType0 | Unset):
        app (App | Unset):
    """

    object_: ProductObject
    id: str
    store_identifier: str
    type_: ProductType
    created_at: int
    app_id: str
    display_name: None | str
    subscription: None | SubscriptionProductType0 | Unset = UNSET
    one_time: None | OneTimeProductType0 | Unset = UNSET
    app: App | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.one_time_product_type_0 import OneTimeProductType0
        from ..models.subscription_product_type_0 import SubscriptionProductType0

        object_ = self.object_.value

        id = self.id

        store_identifier = self.store_identifier

        type_ = self.type_.value

        created_at = self.created_at

        app_id = self.app_id

        display_name: None | str
        display_name = self.display_name

        subscription: dict[str, Any] | None | Unset
        if isinstance(self.subscription, Unset):
            subscription = UNSET
        elif isinstance(self.subscription, SubscriptionProductType0):
            subscription = self.subscription.to_dict()
        else:
            subscription = self.subscription

        one_time: dict[str, Any] | None | Unset
        if isinstance(self.one_time, Unset):
            one_time = UNSET
        elif isinstance(self.one_time, OneTimeProductType0):
            one_time = self.one_time.to_dict()
        else:
            one_time = self.one_time

        app: dict[str, Any] | Unset = UNSET
        if not isinstance(self.app, Unset):
            app = self.app.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "object": object_,
                "id": id,
                "store_identifier": store_identifier,
                "type": type_,
                "created_at": created_at,
                "app_id": app_id,
                "display_name": display_name,
            }
        )
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if one_time is not UNSET:
            field_dict["one_time"] = one_time
        if app is not UNSET:
            field_dict["app"] = app

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app import App
        from ..models.one_time_product_type_0 import OneTimeProductType0
        from ..models.subscription_product_type_0 import SubscriptionProductType0

        d = dict(src_dict)
        object_ = ProductObject(d.pop("object"))

        id = d.pop("id")

        store_identifier = d.pop("store_identifier")

        type_ = ProductType(d.pop("type"))

        created_at = d.pop("created_at")

        app_id = d.pop("app_id")

        def _parse_display_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        display_name = _parse_display_name(d.pop("display_name"))

        def _parse_subscription(data: object) -> None | SubscriptionProductType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_subscription_product_type_0 = SubscriptionProductType0.from_dict(data)

                return componentsschemas_subscription_product_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SubscriptionProductType0 | Unset, data)

        subscription = _parse_subscription(d.pop("subscription", UNSET))

        def _parse_one_time(data: object) -> None | OneTimeProductType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_one_time_product_type_0 = OneTimeProductType0.from_dict(data)

                return componentsschemas_one_time_product_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OneTimeProductType0 | Unset, data)

        one_time = _parse_one_time(d.pop("one_time", UNSET))

        _app = d.pop("app", UNSET)
        app: App | Unset
        if isinstance(_app, Unset):
            app = UNSET
        else:
            app = App.from_dict(_app)

        product = cls(
            object_=object_,
            id=id,
            store_identifier=store_identifier,
            type_=type_,
            created_at=created_at,
            app_id=app_id,
            display_name=display_name,
            subscription=subscription,
            one_time=one_time,
            app=app,
        )

        return product
