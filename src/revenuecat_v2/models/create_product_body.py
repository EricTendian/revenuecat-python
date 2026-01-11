from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.product_type import ProductType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.product_subscription_input_type_0 import ProductSubscriptionInputType0


T = TypeVar("T", bound="CreateProductBody")


@_attrs_define
class CreateProductBody:
    """
    Attributes:
        store_identifier (str): The store identifier of the product.
            - For Apple App Store products this is the product ID of the subscription or in-app product.
            - For Google's Play Store, it should follow the format 'productId:basePlanId' for subscription products and SKU
            for one-time purchase products.
            - For Stripe, the product identifier that always starts with "prod_"
            - For Amazon, if it's a subscription, the term SKU of the subscription. If it's a one-time purchase, the SKU of
            the product.
            - For Roku, this is the product identifier of the subscription or one-time purchase product.
             Example: com.revenuecat.magicweather.monthly.
        app_id (str): The ID of the app Example: app1a2b3c4.
        type_ (ProductType):
        display_name (None | str | Unset): The display name of the product Example: Premium Monthly 2023.
        subscription (None | ProductSubscriptionInputType0 | Unset): Subscription parameters for product creation. Only
            supported for simulated store products.
        title (None | str | Unset): The user-facing title of the product. This field is required for Test Store
            products. Example: Premium Monthly 2023.
    """

    store_identifier: str
    app_id: str
    type_: ProductType
    display_name: None | str | Unset = UNSET
    subscription: None | ProductSubscriptionInputType0 | Unset = UNSET
    title: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.product_subscription_input_type_0 import ProductSubscriptionInputType0

        store_identifier = self.store_identifier

        app_id = self.app_id

        type_ = self.type_.value

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        subscription: dict[str, Any] | None | Unset
        if isinstance(self.subscription, Unset):
            subscription = UNSET
        elif isinstance(self.subscription, ProductSubscriptionInputType0):
            subscription = self.subscription.to_dict()
        else:
            subscription = self.subscription

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "store_identifier": store_identifier,
                "app_id": app_id,
                "type": type_,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if subscription is not UNSET:
            field_dict["subscription"] = subscription
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.product_subscription_input_type_0 import ProductSubscriptionInputType0

        d = dict(src_dict)
        store_identifier = d.pop("store_identifier")

        app_id = d.pop("app_id")

        type_ = ProductType(d.pop("type"))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_subscription(data: object) -> None | ProductSubscriptionInputType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_product_subscription_input_type_0 = ProductSubscriptionInputType0.from_dict(data)

                return componentsschemas_product_subscription_input_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProductSubscriptionInputType0 | Unset, data)

        subscription = _parse_subscription(d.pop("subscription", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        create_product_body = cls(
            store_identifier=store_identifier,
            app_id=app_id,
            type_=type_,
            display_name=display_name,
            subscription=subscription,
            title=title,
        )

        return create_product_body
