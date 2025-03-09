from pydantic import BaseModel, PositiveFloat, PositiveInt, EmailStr
from datetime import datetime
from typing import Optional

# O SCHEMA define as validações quando interajo com o usuário
# Para cada model posso ter 1 ou + schemas de validação, conforme as operações que necessitar

class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    categoria: str
    email_fornecedor: EmailStr

# VALIDAÇÃO DE CRIACAO  de um PRODUTO  
# na criação, os dados informados são os mesmos do ProductBase
class ProductCreate(ProductBase):
    pass

# VALIDAÇÃO DE ATUALIZAÇÃO  de um PRODUTO
# na atualização, permito que o usuário altere 1 ou + campos
class ProductUpdate(ProductBase):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    categoria: Optional[str] = None
    email_fornecedor: Optional[EmailStr] = None

# VALIDAÇÃO DE LEITURA de um PRODUTO (SELECT)
# Representa o retorno do produto ao cliente
# ProductResponse é a única classe que se comunica com o ORM
class ProductResponse(ProductBase):
    id: PositiveInt
    created_at: datetime

    # é o que permite converter PYDANTIC em ORM nas funções de CRUD
    class Config:
        from_attributes = True