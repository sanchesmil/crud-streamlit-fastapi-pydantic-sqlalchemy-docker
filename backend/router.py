from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductCreate, ProductUpdate, ProductResponse
from typing import List

from crud import (
     get_products,
     get_product,
     create_product,
     update_product,
     delete_product
)

router = APIRouter()

### Rota que busca todos os produtos
### sempre teremos 2 parametros obrigatorios, o PATH e o RESPONSE
@router.get("/products/", response_model=List[ProductResponse])
def read_all_products(db: Session = Depends(get_db)):
    products = get_products(db)
    return products

### Rota que busca 1 produto especifico
@router.get("/products/{product_id}", response_model=ProductResponse)
def read_one_product(product_id: int, db: Session=Depends(get_db)):
    product = get_product(product_id=product_id, db=db)

    if product is None:
        raise HTTPException(status_code=404, detail= 'Produto não encontrado.')

    return product

### Rota que insere um novo produto
@router.post("/products/", response_model=ProductResponse)
def create_one_product(product:ProductCreate,db: Session = Depends(get_db)):
    product = create_product(product=product, db=db)
    return product

### Rota que remove um produto
@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_one_product(product_id: int, db: Session=Depends(get_db)):
    product = delete_product(product_id, db)
    if product is None:
        raise HTTPException(status_code=404,detail="Produto não encontrado.")
    return product

### Rota que atualiza um produto
@router.put("/products/{product_id}/", response_model=ProductResponse)
def update_one_product(product_id:int, product: ProductUpdate, db: Session=Depends(get_db)):

    product = update_product(product=product, product_id=product_id, db=db)

    if product is None:
        raise HTTPException(status_code=404, detail= 'Produto não encontrado.')
   
    return product