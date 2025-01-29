from typing import Annotated
from fastapi import APIRouter, Depends

from app.models.collection import CollectionCreate, CollectionPublic
from app.dependencies import SessionDep
from app.services.collections import CollectionService

router = APIRouter(
    prefix="/collections",
    tags=["collections"],
)


def get_collection_service(session: SessionDep):
    return CollectionService(session)


@router.get("/", response_model=list[CollectionPublic])
async def get_all_collections(
    collectionService: Annotated[CollectionService, Depends(get_collection_service)],
) -> list[CollectionPublic]:
    return collectionService.get_all_collections()


@router.get("/{collection_id}", response_model=CollectionPublic)
async def get_collection(
    collection_id: int,
    collectionService: Annotated[CollectionService, Depends(get_collection_service)],
) -> CollectionPublic:
    return collectionService.get_collection(collection_id)


@router.post("/", response_model=CollectionPublic)
async def create_collection(
    collection_request: CollectionCreate,
    collectionService: Annotated[CollectionService, Depends(get_collection_service)],
) -> CollectionPublic:
    return collectionService.create_collection(collection_request)


@router.delete("/{collection_id}")
async def delete_collection(
    collection_id: int,
    collectionService: Annotated[CollectionService, Depends(get_collection_service)],
) -> dict[str, str]:
    return collectionService.delete_collection(collection_id)
