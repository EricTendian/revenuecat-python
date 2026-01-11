from enum import Enum


class WebhookEventType(str, Enum):
    BILLING_ISSUE = "billing_issue"
    CANCELLATION = "cancellation"
    EXPIRATION = "expiration"
    INITIAL_PURCHASE = "initial_purchase"
    INVOICE_ISSUANCE = "invoice_issuance"
    NON_RENEWING_PURCHASE = "non_renewing_purchase"
    PRODUCT_CHANGE = "product_change"
    REFUND_REVERSED = "refund_reversed"
    RENEWAL = "renewal"
    SUBSCRIPTION_EXTENDED = "subscription_extended"
    SUBSCRIPTION_PAUSED = "subscription_paused"
    TEMPORARY_ENTITLEMENT_GRANT = "temporary_entitlement_grant"
    TRANSFER = "transfer"
    UNCANCELLATION = "uncancellation"
    VIRTUAL_CURRENCY_TRANSACTION = "virtual_currency_transaction"

    def __str__(self) -> str:
        return str(self.value)
