from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_order_service
from app.schemas.orders import CreateOrderRequest, CreateOrderResponse
from app.domain.entities import CustomerId
from app.services.order_service import OrderService

router = APIRouter(prefix="/orders")


@router.post(
    "",
    response_model=CreateOrderResponse,
    status_code=201,
)
def create(
    request: CreateOrderRequest,
    service: OrderService = Depends(get_order_service),
):
    try:
        result = service.create_order(
            customer_id=CustomerId(request.customer_id),
            shipping_address=request.shipping_address.to_domain(),
            items=[item.to_domain() for item in request.items],
        )

        return CreateOrderResponse(order_id=result.id.value, status=result.status)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
